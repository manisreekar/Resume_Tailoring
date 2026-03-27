# Multi-Job Resume Tailoring Workflow

## Overview

Handles 3-5 similar jobs efficiently. Shared gap analysis + per-job tailoring.

**When to use:** User provides 2+ JDs at once, or says "batch" / "multiple jobs".

## Phase 0: Job Intake

**Goal:** Collect all JDs, initialize batch.

For each job, collect:
- JD text or URL
- Company name + role title (extract from JD if possible)
- Priority: high/medium/low (default: medium)

Initialize batch state:
```bash
python3 scripts/batch_manager.py init "batch-{YYYY-MM-DD}-{slug}"
```

For each job collected:
```bash
python3 scripts/batch_manager.py add-job "{batch_id}" \
  --company "{Company}" --role "{Role}" --priority "{priority}"
```

Quick-scan each JD for tech keywords (lightweight — NOT full analysis):
```bash
python3 scripts/jd_analyzer.py "{jd_text}"
```

Present batch summary and get user confirmation before proceeding.

## Phase 1: Aggregate Gap Analysis

**Goal:** Build unified gap list across all jobs to avoid redundant work.

**Process:**

1. For each job, extract requirements from JD (must-have vs nice-to-have)
2. Compare requirements against base resume — flag gaps (skills not on resume)
3. Deduplicate gaps across jobs and prioritize:
   - **Critical** (3+ jobs): address first
   - **Important** (2 jobs): address second
   - **Job-specific** (1 job): address last or skip

4. Present gap summary to user:

```
COVERAGE SUMMARY:
- Job 1 ({Company}): {N} gaps
- Job 2 ({Company}): {N} gaps

AGGREGATE GAPS ({N} unique after dedup):
- {N} critical (appear in 3+ jobs)
- {N} important (appear in 2 jobs)
- {N} job-specific
```

Ask user:
1. PROCEED — address gaps via skill injection during per-job processing
2. REVIEW GAPS — see detailed breakdown first

Update batch state:
```bash
python3 scripts/batch_manager.py update-phase "{batch_id}" "gap_analysis"
```

**Checkpoint:** User approves before per-job processing begins.

## Phase 2: Per-Job Processing

**Goal:** Process each job through the standard single-job workflow (Phase 0-5 from SKILL.md).

**Processing Modes — ask user before starting:**
- **INTERACTIVE** (default) — checkpoints per job (tailoring plan approval)
- **EXPRESS** — auto-approve using best judgment, review all at end

**Per-Job Loop:**

For each pending job:

1. Update status:
   ```bash
   python3 scripts/batch_manager.py update-job "{batch_id}" "job-{N}" "in_progress"
   ```

2. Run standard single-job flow from SKILL.md:
   - Read `phase-0-analysis.md` → full JD analysis (cache check first)
   - Read `phase-1-2-tailoring.md` + `framework-switching.md` → switch + inject
   - Read `phase-3-5-output.md` → generate LaTeX, compile PDF, write recruiter email
   - Update `resume_index.md` via cache_check.py

3. Output to `resumes/{Company}_{Framework1}_{Framework2}/`:
   - `jd.md`, `resume.tex`, `Mani_Resume.pdf`, `Mani_Resume.log`, `recruiter_mail.md`, `run_log.md`

4. Mark complete:
   ```bash
   python3 scripts/batch_manager.py update-job "{batch_id}" "job-{N}" "completed"
   ```

5. Show progress:
   ```
   ✓ Job {N}/{total}: {Company} - {Role}
   Jobs remaining: {remaining}
   Continue? (Y/N/pause)
   ```

**Pause/Resume:** If user says "pause", state is saved in `_batch_state.json`. Resume with `python3 scripts/batch_manager.py status "{batch_id}"`.

## Phase 3: Batch Finalization

After all jobs complete:

1. Generate summary:
   ```bash
   python3 scripts/batch_manager.py summary "{batch_id}"
   ```

2. Present to user:
   ```
   All {N} resumes generated!

   JOB RESULTS:
   - Job 1: {Company} | Folder: resumes/{folder}/
   - Job 2: {Company} | Folder: resumes/{folder}/
   ...

   Each folder contains: jd.md, resume.tex, .pdf, .log, recruiter_mail.md

   REVIEW OPTIONS:
   1. APPROVE ALL
   2. REVIEW INDIVIDUALLY
   3. REVISE SPECIFIC JOB — make changes, regenerate
   ```

3. Handle revisions: apply changes → regenerate LaTeX → recompile → verify 2 pages.

4. Finalize batch:
   ```bash
   python3 scripts/batch_manager.py complete "{batch_id}"
   ```

## Incremental Batch Support

To add jobs to a completed batch:

```bash
# Check existing batch
python3 scripts/batch_manager.py status "{batch_id}"

# Add new job
python3 scripts/batch_manager.py add-job "{batch_id}" \
  --company "{Company}" --role "{Role}"
```

Only run gap analysis on NEW gaps (skills not covered by previous jobs).
Process new jobs through standard per-job loop. Existing jobs are untouched.

## Edge Cases

1. **Jobs too diverse** (<40% overlap): suggest splitting into separate batches or process as individual single-job runs
2. **One job fails** (e.g., pdflatex error): continue with others, revisit failed job after
3. **Add/remove jobs mid-batch**: use `batch_manager.py add-job` or `update-job "{batch_id}" "job-N" "skipped"`
4. **Batch interrupted**: state auto-saved after each job. Resume with `batch_manager.py status`
