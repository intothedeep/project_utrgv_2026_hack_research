#!/bin/bash
### Smallest circle: closed form vs SOCP. CPU only, one core. Template: skills/cradle-cluster/templates/job.slurm
### Usage on login001 (main session only):  cd ~/smallest_circle && sbatch jobs/run.slurm <RUN> [--n N]
### Node gpu011 is set by the owner (repo CLAUDE.md, 2026-11-07). The skill lists gpu[011-012] as
### partition gpul40q (SKILL.md section 3, other group's equipment, submit permission separate).
### No --gres: this job needs no GPU. If sbatch rejects that, report; do not add a GPU on a guess.
#SBATCH --job-name=smallest_circle
#SBATCH --output=logs/%x.out.%j
#SBATCH --error=logs/%x.err.%j
#SBATCH -N 1
#SBATCH -p gpul40q
#SBATCH --nodelist=gpu011
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=4G
#SBATCH --time=02:00:00         # UNMEASURED guess: ~19 cases x 1000 SOCP solves; fix after the first run

set -euo pipefail
RUN="${1:?give the run name, e.g. sbatch jobs/run.slurm v1_n1000}"; shift || true

PROJ=~/smallest_circle
ENV=~/myEnvs/smallest_circle
CODE="$PROJ/code"
RUN_DIR="$PROJ/runs/${SLURM_JOB_ID}_${RUN}"
mkdir -p "$RUN_DIR" "$PROJ/logs"
[ -f "$CODE/CODE_COMMIT" ] || { echo "no $CODE/CODE_COMMIT: write it before upload (README step 1)" >&2; exit 1; }
cd "$RUN_DIR"

source "$ENV/bin/activate"
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 PYTHONPATH="$CODE/src"
# sacct is disabled on Cradle: these lines ARE the run record.
echo "=== run $RUN job $SLURM_JOB_ID host $(hostname) dir $RUN_DIR start $(date -Is) ==="
echo "code_commit $(cat "$CODE/CODE_COMMIT")"
python -c "import platform, numpy, cvxpy, clarabel; print('python', platform.python_version(), 'numpy', numpy.__version__, 'cvxpy', cvxpy.__version__, 'clarabel', clarabel.__version__)"

# Snapshot of the exact code this run used (rules/measurement.md section 2).
cp -R "$CODE/src" "$RUN_DIR/code_snapshot"
cp "$CODE/CODE_COMMIT" "$CODE/pyproject.toml" "$RUN_DIR/"
(cd "$RUN_DIR/code_snapshot" && find . -name '*.py' | sort | xargs sha256sum) > "$RUN_DIR/code.sha256"

python -m smallest_circle.run --run "$RUN" --job "$SLURM_JOB_ID" --out "$RUN_DIR" "$@"

# Give the output files this run's name so files from different jobs never mix once fetched.
for f in manifest.json results/rows.csv results/summary.json; do
  [ -f "$f" ] && cp "$f" "${f%.*}_${SLURM_JOB_ID}_${RUN}.${f##*.}" || echo "MISSING $f"
done
ls -laR "$RUN_DIR" | head -40
echo "=== done $(date -Is) ==="
