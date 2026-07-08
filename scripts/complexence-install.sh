#!/usr/bin/env bash
# complexence-install.sh — scaffold a .complexence/ lab into a target repository.
#
# Turns a project into a Complexence "lab" (spec/complexence-labs.md §4): copies the
# blank templates from install/ into <target>/.complexence/, wiring the repo into the
# research loop WITHOUT embedding any domain knowledge.
#
#   ./scripts/complexence-install.sh                 # install into the current dir
#   ./scripts/complexence-install.sh /path/to/repo   # install into another repo
#   ./scripts/complexence-install.sh --role chief-risk-officer /path/to/repo
#
# The generated .complexence/ is PRIVATE lab data. Never commit it into the public
# Complexence repo — this script refuses to install into its own source repo. Keep
# your lab in a private repository (or a gitignored area). See GUARDRAILS.md.
#
# Portable to the bash 3.2 that ships with macOS. Copies only; never overwrites an
# existing .complexence/.
set -euo pipefail

# --- locate the runtime source (this repo) ---------------------------------------
script_dir="$(cd "$(dirname "$0")" && pwd -P)"
runtime_root="$(cd "$script_dir/.." && pwd -P)"
install_src="$runtime_root/install"
agents_src="$runtime_root/agents"

# --- parse args ------------------------------------------------------------------
role="chief-of-staff"   # universal default (ADR-0001 principle 3)
target="$(pwd)"
while [ "$#" -gt 0 ]; do
  case "$1" in
    --role) role="${2:-}"; shift 2 ;;
    -h|--help)
      grep '^#' "$0" | sed 's/^# \{0,1\}//'; exit 0 ;;
    *) target="$1"; shift ;;
  esac
done
target="$(cd "$target" && pwd -P)"

# --- guard: do not install into the public runtime itself ------------------------
if [ "$target" = "$runtime_root" ]; then
  echo "refusing: '$target' is the public Complexence runtime itself." >&2
  echo "A .complexence/ lab is PRIVATE data. Install into a separate (private) repo." >&2
  exit 1
fi

dest="$target/.complexence"
if [ -e "$dest" ]; then
  echo "exists: $dest already present — leaving it untouched." >&2
  exit 1
fi

# --- scaffold --------------------------------------------------------------------
mkdir -p "$dest"/roles "$dest"/experiments "$dest"/metrics "$dest"/schemas \
         "$dest"/prompts "$dest"/summaries

cp "$install_src/charter.template.md"              "$dest/charter.md"
cp "$install_src/operating-principles.template.md" "$dest/operating-principles.md"
cp "$install_src/experiments/EXP-000.template.md"  "$dest/experiments/EXP-000.template.md"
cp "$install_src/metrics/orientation-log.template.md" "$dest/metrics/orientation-log.md"
cp "$install_src/schemas/experiment.schema.json"   "$dest/schemas/experiment.schema.json"

# install the universal role plus any requested domain role, if the contract exists
installed_roles="chief-of-staff"
cp "$agents_src/chief-of-staff.prompt.md" "$dest/roles/chief-of-staff.prompt.md"
if [ "$role" != "chief-of-staff" ]; then
  if [ -f "$agents_src/$role.prompt.md" ]; then
    cp "$agents_src/$role.prompt.md" "$dest/roles/$role.prompt.md"
    installed_roles="$installed_roles, $role"
  else
    echo "note: role '$role' has no public contract in agents/ yet — installing" >&2
    echo "      chief-of-staff only. Add the role prompt to your lab by hand." >&2
  fi
fi

# a placeholder gitignore: in a PRIVATE lab you commit the whole scaffold
cat > "$dest/.gitignore" <<'EOF'
# .complexence/ is PRIVATE lab data. In a private lab repo, commit all of it.
# If any of it must stay untracked even within the lab, ignore it here.
# NEVER let this directory reach the public Complexence repo. See GUARDRAILS.md.
EOF

echo "installed Complexence lab → $dest"
echo "  roles:     $installed_roles"
echo "  next:      edit charter.md, then run the chief-of-staff role over your inbox"
echo "  reminder:  this is PRIVATE — keep it out of the public repo (GUARDRAILS.md)"
