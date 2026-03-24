#!/usr/bin/env python3
"""
Batch state manager for multi-job resume tailoring.

Usage:
  Init batch:      python3 scripts/batch_manager.py init "batch-2025-03-24-search"
  Add job:         python3 scripts/batch_manager.py add-job "batch-id" --company "Google" --role "SWE" --priority "high"
  Update job:      python3 scripts/batch_manager.py update-job "batch-id" "job-1" "completed"
  Update phase:    python3 scripts/batch_manager.py update-phase "batch-id" "per_job_processing"
  Status:          python3 scripts/batch_manager.py status "batch-id"
  Summary:         python3 scripts/batch_manager.py summary "batch-id"
  Complete batch:  python3 scripts/batch_manager.py complete "batch-id"
  List batches:    python3 scripts/batch_manager.py list

Output: Single-line deterministic responses (easy for LLM to parse).
"""

import sys
import os
import json
from datetime import datetime, timezone

BATCHES_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "resumes", "batches")


def _state_path(batch_id: str) -> str:
    return os.path.join(BATCHES_DIR, batch_id, "_batch_state.json")


def _load(batch_id: str) -> dict:
    path = _state_path(batch_id)
    if not os.path.exists(path):
        print(f"ERROR|Batch not found: {batch_id}")
        sys.exit(1)
    with open(path) as f:
        return json.load(f)


def _save(batch_id: str, state: dict) -> None:
    path = _state_path(batch_id)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        json.dump(state, f, indent=2)


def init_batch(batch_id: str) -> None:
    path = _state_path(batch_id)
    if os.path.exists(path):
        print(f"EXISTS|{batch_id}")
        return

    state = {
        "batch_id": batch_id,
        "created": datetime.now(timezone.utc).isoformat(),
        "current_phase": "intake",
        "jobs": [],
    }
    _save(batch_id, state)
    print(f"CREATED|{batch_id}")


def add_job(batch_id: str, company: str, role: str, priority: str = "medium") -> None:
    state = _load(batch_id)
    job_num = len(state["jobs"]) + 1
    job_id = f"job-{job_num}"

    # Check for duplicate company+role
    for j in state["jobs"]:
        if j["company"] == company and j["role"] == role:
            print(f"DUPLICATE|{j['job_id']}|{company}|{role}")
            return

    state["jobs"].append({
        "job_id": job_id,
        "company": company,
        "role": role,
        "priority": priority,
        "status": "pending",
        "added": datetime.now(timezone.utc).isoformat(),
    })
    _save(batch_id, state)
    print(f"ADDED|{job_id}|{company}|{role}|{priority}")


def update_job(batch_id: str, job_id: str, new_status: str) -> None:
    valid = {"pending", "in_progress", "completed", "failed", "skipped"}
    if new_status not in valid:
        print(f"ERROR|Invalid status: {new_status}. Must be one of: {', '.join(sorted(valid))}")
        sys.exit(1)

    state = _load(batch_id)
    for job in state["jobs"]:
        if job["job_id"] == job_id:
            job["status"] = new_status
            if new_status == "completed":
                job["completed_at"] = datetime.now(timezone.utc).isoformat()
            _save(batch_id, state)
            print(f"UPDATED|{job_id}|{new_status}")
            return
    print(f"ERROR|Job not found: {job_id}")
    sys.exit(1)


def update_phase(batch_id: str, phase: str) -> None:
    state = _load(batch_id)
    state["current_phase"] = phase
    _save(batch_id, state)
    print(f"PHASE|{batch_id}|{phase}")


def show_status(batch_id: str) -> None:
    state = _load(batch_id)
    total = len(state["jobs"])
    completed = sum(1 for j in state["jobs"] if j["status"] == "completed")
    pending = sum(1 for j in state["jobs"] if j["status"] == "pending")
    in_progress = sum(1 for j in state["jobs"] if j["status"] == "in_progress")

    print(f"BATCH|{batch_id}|phase:{state['current_phase']}|total:{total}|completed:{completed}|pending:{pending}|in_progress:{in_progress}")
    for job in state["jobs"]:
        print(f"  JOB|{job['job_id']}|{job['company']}|{job['role']}|{job['status']}|{job['priority']}")


def show_summary(batch_id: str) -> None:
    state = _load(batch_id)
    total = len(state["jobs"])
    completed = sum(1 for j in state["jobs"] if j["status"] == "completed")

    print(f"SUMMARY|{batch_id}|{completed}/{total} completed|phase:{state['current_phase']}")
    for job in state["jobs"]:
        folder = f"{job['company']}_{job.get('folder_suffix', 'Unknown')}" if job.get("folder_suffix") else job["company"]
        print(f"  {job['job_id']}|{job['company']}|{job['role']}|{job['status']}|resumes/{folder}/")


def complete_batch(batch_id: str) -> None:
    state = _load(batch_id)
    state["current_phase"] = "completed"
    state["completed_at"] = datetime.now(timezone.utc).isoformat()
    _save(batch_id, state)

    total = len(state["jobs"])
    completed = sum(1 for j in state["jobs"] if j["status"] == "completed")
    print(f"COMPLETED|{batch_id}|{completed}/{total} jobs")


def list_batches() -> None:
    if not os.path.exists(BATCHES_DIR):
        print("NO_BATCHES")
        return

    batches = [d for d in os.listdir(BATCHES_DIR)
               if os.path.isfile(os.path.join(BATCHES_DIR, d, "_batch_state.json"))]

    if not batches:
        print("NO_BATCHES")
        return

    for b in sorted(batches):
        state = _load(b)
        total = len(state["jobs"])
        completed = sum(1 for j in state["jobs"] if j["status"] == "completed")
        print(f"BATCH|{b}|{state['current_phase']}|{completed}/{total}")


def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print('  python3 scripts/batch_manager.py init "batch-id"')
        print('  python3 scripts/batch_manager.py add-job "batch-id" --company "X" --role "Y"')
        print('  python3 scripts/batch_manager.py update-job "batch-id" "job-1" "completed"')
        print('  python3 scripts/batch_manager.py update-phase "batch-id" "phase-name"')
        print('  python3 scripts/batch_manager.py status "batch-id"')
        print('  python3 scripts/batch_manager.py summary "batch-id"')
        print('  python3 scripts/batch_manager.py complete "batch-id"')
        print('  python3 scripts/batch_manager.py list')
        sys.exit(1)

    cmd = sys.argv[1]

    if cmd == "init":
        init_batch(sys.argv[2])
    elif cmd == "add-job":
        # Parse --company, --role, --priority from args
        batch_id = sys.argv[2]
        company = role = ""
        priority = "medium"
        i = 3
        while i < len(sys.argv):
            if sys.argv[i] == "--company" and i + 1 < len(sys.argv):
                company = sys.argv[i + 1]
                i += 2
            elif sys.argv[i] == "--role" and i + 1 < len(sys.argv):
                role = sys.argv[i + 1]
                i += 2
            elif sys.argv[i] == "--priority" and i + 1 < len(sys.argv):
                priority = sys.argv[i + 1]
                i += 2
            else:
                i += 1
        if not company or not role:
            print("ERROR|--company and --role are required")
            sys.exit(1)
        add_job(batch_id, company, role, priority)
    elif cmd == "update-job":
        update_job(sys.argv[2], sys.argv[3], sys.argv[4])
    elif cmd == "update-phase":
        update_phase(sys.argv[2], sys.argv[3])
    elif cmd == "status":
        show_status(sys.argv[2])
    elif cmd == "summary":
        show_summary(sys.argv[2])
    elif cmd == "complete":
        complete_batch(sys.argv[2])
    elif cmd == "list":
        list_batches()
    else:
        print(f"ERROR|Unknown command: {cmd}")
        sys.exit(1)


if __name__ == "__main__":
    main()
