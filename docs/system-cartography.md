# System Cartography

**How to map an unknown system you are responsible for.**

Status: public method doc

---

## What this is

A method for walking into a system you did not fully build, and coming out with a
map: compact, legible, categorized, and ending in decisions.

It was derived from walking an AWS account, but AWS is the worked example, not the
subject. The subject is the general move. The same eight categories and the same
seven rules apply to a Linux host, a Kubernetes cluster, a codebase you inherited,
a household's paperwork, or a business you are being handed.

The test of a map is not completeness. It is whether a person can hold the whole
thing at once and then act.

---

## Part 1 — The problem that makes mapping necessary

**Complex systems do not enumerate themselves.**

A Linux box has `ls /`. You can walk the filesystem and eventually see everything,
because there is one root and one tree. That is a rare property, and it is why
Linux feels knowable.

AWS has no `ls /`. There are ~200 services, each with its own API, most scoped to
one of 17 regions, and nothing anywhere returns "here is what exists." A forgotten
resource in `ap-southeast-2` bills forever and never appears on any screen you
happen to be looking at.

Most real systems are the AWS case, not the Linux case. Your household finances,
your obligations, your codebase's true dependency set. There is no root, no tree,
and no call that returns everything.

So the work is not *reading* an inventory. The work is *reconstructing* one.

---

## Part 2 — The eight categories

Every system decomposes into the same eight slots. This is the frame you carry in,
before you know anything about the specific system. It is what makes the map
comparable across systems and repeatable across time.

| # | Category | The question | Linux | AWS | Kubernetes |
|---|---|---|---|---|---|
| 1 | **Identity** | Who is acting, and with what authority? | `whoami`, `id`, `/etc/passwd` | `sts get-caller-identity`, IAM | `auth can-i --list`, RBAC |
| 2 | **Running** | What is executing right now? | `ps aux`, `top` | EC2, Lambda, ECS, RDS | pods, deployments, daemonsets |
| 3 | **Exposed** | What is reachable from outside? | `ss -tulpn` | security groups, load balancers, public IPs | services, ingress, network policies |
| 4 | **Stored** | What persists, and what is orphaned? | `df -h`, `du -sh *` | S3, EBS, snapshots | PVs, PVCs, configmaps, secrets |
| 5 | **Scheduled** | What regenerates on its own? | `crontab`, `systemctl list-timers` | auto scaling, EventBridge rules | replica counts, cronjobs, HPAs |
| 6 | **Owned** | What belongs to a deployment unit? | `dpkg -l`, `rpm -qa` | CloudFormation stacks, Terraform state | `ownerReferences`, Helm releases |
| 7 | **Recorded** | What does the system remember? | `auth.log`, `~/.bash_history` | CloudTrail | Events, audit log |
| 8 | **Enabled** | What was ever switched on, including things now unused? | leftover `/etc` config | service-linked IAM roles | CRDs, admission webhooks |

Three systems, one frame. The Kubernetes column was added after the frame was already
fixed, against a system with a very different shape — no regions, a real API root,
ownership as a first-class field — and no category had to move to accommodate it.

That is the claim this frame makes, and it is falsifiable. If you meet a system where
one of the eight has no answer, the frame is wrong and should be revised, not
stretched to fit.

Categories 1–4 are the **static** picture: what is there.
Category 5 is the **dynamic** picture: what puts it back when you remove it.
Categories 6–8 are the **historical** picture: how it got this way.

Most people map only 1–4, which is why their maps go stale and their cleanups get
undone. The last four are where the leverage is.

---

## Part 3 — The seven rules

### 1. Stand somewhere known before you look at anything

Establish the vantage point first: which system, acting as whom, with what
permissions. A map without a "you are here" is decoration.

In AWS this is `sts get-caller-identity` — the one call that requires no
permissions and cannot lie. The equivalent exists everywhere. Find it and run it
first, every time, even when you are sure.

### 2. Triangulate from independent indexes, and name each one's blind spot

No single index is complete. Build the picture from several partial ones, and
state explicitly what each cannot see. The gaps between indexes are where forgotten
things live.

For an AWS account, three independent indexes:

| Index | Shows | Blind to |
|---|---|---|
| **The bill** | everything that costs money | anything free or still in a free tier |
| **Fingerprints** (service-linked roles) | every service ever switched on, with dates | services that create no role |
| **History** (CloudTrail) | every change actually made | anything older than 90 days |

Any one of them alone produces a confident, wrong map. Together they cover each
other's holes.

### 3. Start from the ranking the system already computes

Do not enumerate alphabetically and hope to stumble on what matters. Every system
is already sorting its components by importance along some axis, and that sort is
free to read.

In AWS the axis is the bill. On a host it is `du -sh *` or CPU time. In a codebase
it is change frequency. Read the existing ranking first, then investigate the top
of it. This is the difference between a survey and an investigation.

### 4. Sweep exhaustively, display sparsely

These are not in tension. Probe all 17 regions; print only the rows that are not
empty. Coverage is a property of the *scan*. Compactness is a property of the
*render*.

The one requirement: **say what you suppressed.** A legend that reads
"regions with nothing are omitted" turns silence into information. Without it,
absence is indistinguishable from failure, and the map lies by omission.

### 5. Find what regenerates before you change anything

A static inventory is a photograph. The map has to show the control loops, because
those determine whether any change you make survives.

On Linux you kill a process, it comes back, and you go find the systemd unit. Same
move everywhere. An auto scaling group with `DesiredCapacity: 2` will replace what
you delete, forever, and bill you for each replacement.

**Scheduler first, resource second.** Always. This is the single rule that
separates a cleanup from a fight with the system.

Its sibling: **do not hand-delete what a deployment unit owns.** Removing a
CloudFormation-managed resource by hand is `rm`-ing a file that `dpkg` installed.
The system now disagrees with reality and will re-assert itself later. Delete the
stack, not its members.

### 6. Put it on a time axis

Sorted by creation time, an inventory becomes a narrative: your own decisions, in
order, with the gaps visible. Patterns and trends do not exist in a snapshot. They
only appear against time.

`ls -lrt` is the canonical form and the reason it is the right default: **newest
last**, so the most recent thing is where the eye already is when the output stops
scrolling.

The same logic gives the rule for rankings: `du -sh * | sort -h` puts the biggest
last. **Put the answer where the eye lands.** Sort direction is not cosmetic; it
decides what the reader walks away with.

### 7. Treat contradictions between indexes as the highest-value finding

When two indexes disagree, that is not noise to reconcile away. That is the
investigation. Two from a single AWS walk:

- Config's recorder existed and was set to record *everything*, but its status said
  `recording: false`. Two calls, opposite impressions. The one that answers the
  question is `describe-configuration-recorder-status`, not
  `describe-configuration-recorders`. **Existence is not operation.**
- The recorder was stopped, yet `PutEvaluations` events were firing every few
  minutes. Resolution: Security Hub had created ~375 Config *rules*, and periodic
  rules evaluate and bill independently of the recorder. **A dependency can outlive
  the thing it appears to depend on.**

Both findings came from noticing that two readings did not fit. Neither would have
surfaced from any single index. Where the map contradicts itself, dig.

---

## Part 4 — Rendering rules

The map is not the data. Legibility is a design act, and these are the constraints
that produced a readable one.

- **One screen.** If it does not fit, it is not a map, it is a dump. Sections can
  scroll; the shape must not.
- **Fixed columns, aligned by visible width.** Pad by rendered length, not byte
  length. ANSI colour codes and UTF-8 characters both break naive padding.
- **`-` for zero.** Absence must be visible and quiet. A column of dashes with one
  number in it is instantly readable; a column of zeros is not.
- **Units on the value, not the header.** `$12.40/mo` in the cell beats a header
  that says "monthly cost in USD".
- **Every number carries its command.** The map cites its sources. Any cell must be
  re-derivable by copying one printed line and running it. This is what makes a map
  trustworthy rather than authoritative, and it is what makes it teachable.
- **Three periods minimum, never one number.** `$40.00 → $28.50 → $22.10 → $14.75`
  says something a single "$26.34/mo" cannot. Direction is the finding.
- **Mark age.** `<- today`, `<- this week`. Recency is the cheapest signal available
  and it usually points at the live problem.
- **End in a flag list.** Ranked, actionable, short. A map that does not terminate
  in decisions is a report.

---

## Part 5 — The walk, in order

The categories say *what* to look for. The order says *when*, and the order is not
arbitrary: each step constrains the next.

```
0  identity      stand somewhere known
1  cost          read the ranking the system already computed
2  resources     what is running                          [sweep all regions]
3  security      what is always-on and always-billing
4  network       what is exposed
5  storage       what persists, what is orphaned
6  schedulers    what regenerates   <- READ BEFORE DELETING ANYTHING
7  packages      what a deployment owns
8  auth          who can get in
9  history       what was actually done here
10 fingerprints  what was ever switched on
11 flags         the decision surface
```

Identity first because everything after is scoped to it. Cost second because it
tells you where to spend attention. Schedulers before any action. Flags last,
because they are a *conclusion*, and a conclusion presented before its evidence is
just an assertion.

---

## Part 6 — Before you change anything: image the disk

Standard forensic discipline, and it transfers exactly. Dump every `describe-*`
response to a timestamped directory before the first deletion.

On Linux you image the disk because evidence is volatile. In AWS nothing vanishes
on its own, but deletion is irreversible and there is no undo. Same habit,
different reason: **capture before you kill it.**

Once captured, every later question is answered from disk with `jq`, against a
system you have not yet modified.

```bash
SNAP=~/aws-forensics/$(date +%Y-%m-%d) && mkdir -p "$SNAP"
aws_walk.sh --json > "$SNAP/walk.json"
aws_walk.sh --deep > "$SNAP/walk.txt"
```

---

## Part 7 — The instrument

Once the walk is stable, it is worth building an instrument that runs it the same
way every time — so today's map diffs against last month's. `aws_walk.sh` is this
playbook's AWS implementation; what matters here is its *shape*, which ports.

Give the instrument four entry points, because they are the four questions you
actually ask, pointed at a system with no filesystem:

| Command | Analogue | What it answers |
|---|---|---|
| `aws_walk.sh` | the full walk | all eight categories, in order |
| `aws_walk.sh -t` | `ls -lrt` | everything by creation time, newest last |
| `aws_walk.sh --du` | `du -sh * \| sort -h` | what costs and what stores, biggest last |
| `aws_walk.sh --top` | `top` | live view, refreshing |

Every step prints the `aws` command it ran, so the script is also the tutorial:
lift any line, run it standalone, learn the API. `-e` adds the reasoning for each
step. `--tsv` and `--json` make it a pipe. It never writes.

---

## Part 8 — Porting this to another system

The eight categories are the portable part. To map something new, answer these
in order and the map writes itself:

1. What is the `get-caller-identity` here — the call that establishes vantage
   without needing permission?
2. Is there an `ls /`? If not, what are the three partial indexes, and what is each
   one blind to?
3. What ranking does this system already compute for free?
4. What is the enumeration space that must be swept exhaustively (regions, hosts,
   namespaces, accounts, folders)?
5. What are the schedulers — the things that put state back?
6. What is the package manager — the thing that owns resources and will re-assert?
7. Where is the history, and how far back does it go?
8. What are the fingerprints of past decisions that outlive their cause?

Answer those eight and you have the map's skeleton before you have run a single
command. The commands are then just filling in cells.

**The systems worth this treatment are rarely the technical ones.** A codebase you
inherited, yes — but also a household's paperwork, a business being handed to you,
a scheduled-job tree nobody has audited in two years. The AWS and Kubernetes walks
are worked examples because they are legible enough to publish, not because they are
where the method pays best. It pays best where nobody has ever drawn a map at all.

---

## Related

- [`spec/complexence-capability.md`](../spec/complexence-capability.md) — the
  orientation map this method serves. Cartography is what L0–L2 looks like when the
  system is one you did not build.
- [`GUARDRAILS.md`](../GUARDRAILS.md) — method in public, data in private. A map of
  a real system is data; the method that produced it is not.

Worked examples for AWS and Kubernetes exist as separate walks and are not part of
this repo — this repo holds the general move.
