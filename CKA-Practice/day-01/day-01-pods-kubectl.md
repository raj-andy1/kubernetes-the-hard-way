## Important Links needed

Kubernetes Docs
https://kubernetes.io/docs/

kubectl Cheat Sheet
https://kubernetes.io/docs/reference/kubectl/cheatsheet/

Kubernetes API Reference (v1.32)
https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/


## Exam Setup (Run at Session Start)

> Run these commands at the start of **every practice session**  
> and **immediately after the CKA exam terminal opens**.

### kubectl Alias
```bash
alias k=kubectl

source <(kubectl completion bash)
complete -F __start_kubectl k



# CKA Day 1 — Pods & kubectl Speed

## Learning Objectives

By the end of Day 1, you should be able to:

- Create a Pod using an **imperative command** and convert it to YAML
- Edit Pod YAML correctly **from memory**
- Understand where `labels`, `env`, and `ports` belong in Pod specs
- Verify a running Pod by exec’ing into it
- Work confidently inside a **non-default namespace**
- Complete the full Pod lifecycle in **under 7 minutes**

This day builds the foundation for **every other CKA task**.

---

## Tasks to Complete (Required)

### Task 1 — Namespace Setup
Create a namespace named `cka-practice`.

**Success criteria**
- Namespace exists
- All subsequent resources are created in this namespace

---

### Task 2 — Imperative Pod → YAML
Create a Pod with the following requirements:

- Name: `web-pod`
- Namespace: `cka-practice`
- Image: `nginx:1.25`
- Label: `app=web`
- Expose container port `80`
- Environment variable: `ENV=prod`

**Rules**
- Start with an imperative command
- Generate YAML using `--dry-run=client -o yaml`
- Apply the Pod from the YAML file (not directly)

**Success criteria**
- Pod reaches `Running`
- YAML is syntactically correct
- No docs used

---

### Task 3 — Verify Pod Internals
From inside the Pod:
- Verify nginx is responding on port 80

**Success criteria**
- You see the nginx welcome page via `curl localhost`

---

### Task 4 — Inspect & Clean Up
- View Pod labels
- Describe the Pod
- Delete the Pod
- Confirm it is fully removed

**Success criteria**
- No Pods left in `cka-practice`

---

## Challenge Tasks (Drill It In)

> These are optional but **highly recommended**.  
> Do them only after completing the required tasks.

### Challenge 1 — Speed Run
Redo Tasks 2–4 with a **hard time limit**:

- Target time: **≤ 7 minutes**
- No notes
- No docs

If you miss the time, repeat once.

---

### Challenge 2 — YAML Recall
Without looking anything up, recreate this structure from memory:

```yaml
metadata:
  labels:
spec:
  containers:
    - name:
      image:
      ports:
      env:

## Additional Practice Tasks (Day 1 Reinforcement)

> These tasks reinforce Pod fundamentals and kubectl speed.
> Do not use documentation unless explicitly stated.

---

### Task 5 — Imperative Creation (No YAML File)

Create a Pod named `web-pod-imp` with the following:

- Namespace: `cka-practice`
- Image: `nginx:1.25`
- Label: `app=web`
- Expose container port `80`

**Rules**
- Use a single imperative command
- Do not create or edit a YAML file

**Success criteria**
- Pod is `Running`
- Correct label is present

**Cleanup**
- Delete the Pod when finished

---

### Task 6 — Label Mutation

1. Recreate `web-pod` (YAML or imperative — your choice)
2. Add a new label:
   - `tier=frontend`
3. Verify the label using:
   ```bash
   kubectl get pods --show-labels

##Debugging
`kubectl get events -n <ns> --sort-by=.metadata.creationTimestamp | tail`
