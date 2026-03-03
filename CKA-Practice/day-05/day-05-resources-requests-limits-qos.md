# CKA Day 5 — Resources (Requests, Limits, OOMKilled, QoS)

## Exam Setup (Run at Session Start)

> Run these commands at the start of **every practice session**
> and **immediately after the CKA exam terminal opens**.

### kubectl Alias
```bash
alias k=kubectl
```

### kubectl Autocomplete (Bash – Exam Environment)
```bash
source <(kubectl completion bash)
complete -F __start_kubectl k
```

---

## Allowed Documentation (Bookmark These)

- Kubernetes Docs  
  https://kubernetes.io/docs/

- kubectl Cheat Sheet  
  https://kubernetes.io/docs/reference/kubectl/cheatsheet/

- Kubernetes API Reference (v1.32)  
  https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/

---

## Learning Objectives

By the end of Day 5, you should be able to:

- Set CPU and memory **requests** and **limits**
- Predict common failure modes: **OOMKilled** and throttling
- Explain Kubernetes **QoS classes**: BestEffort, Burstable, Guaranteed
- Use `describe` and `events` to diagnose resource-related failures
- Fix resource issues quickly during the exam

---

## Tasks to Complete (Required)

### Task 1 — Create a Pod with Requests & Limits

Create a Pod named `res-pod` with:
- Namespace: `cka-practice`
- Image: `busybox`
- Command: `sleep 3600`
- Requests: cpu `50m`, memory `64Mi`
- Limits: cpu `100m`, memory `128Mi`

**Success criteria**
- Pod is Running
- `kubectl describe` shows requests/limits

---

### Task 2 — Force an OOMKilled

Create a Pod named `oom-pod` with:
- Image: `busybox`
- Memory limit: `32Mi`
- Command that allocates more than 32Mi of memory

**Hint**
- Use a shell loop to fill memory (e.g., write to a variable or /dev/shm)

**Success criteria**
- Pod is terminated with reason `OOMKilled`
- Restart count increases (if restart policy applies)

---

### Task 3 — Fix the OOM

Fix `oom-pod` so it stays running by:
- Increasing memory limit, or
- Reducing memory usage

**Success criteria**
- Pod stays Running
- No OOMKilled events

---

### Task 4 — Identify QoS Class

For each of these pods, determine QoS class using `describe`:

- BestEffort: no requests/limits
- Burstable: requests != limits or only requests/limits set
- Guaranteed: requests == limits for all resources

**Success criteria**
- You can identify QoS within 30 seconds per pod

---

## Challenge Tasks (Drill It In)

### Challenge 1 — CPU Throttling Awareness

Create a Pod with:
- CPU limit `10m`
- A CPU-intensive loop

Observe:
- Pod remains Running but is slow

Explain:
- Why it isn't killed
- What CPU throttling means

---

### Challenge 2 — Resource Debug from Events Only

Break a Pod due to insufficient resources or OOM and debug using only:
```bash
kubectl get events -n cka-practice --sort-by=.metadata.creationTimestamp | tail
```

---

### Challenge 3 — Speed Drill

Given a Pod that is OOMKilled:
- Identify root cause within 2 minutes
- Apply the smallest fix

---

## Common Exam Traps

- Confusing requests vs limits
- Thinking CPU throttling kills Pods (it doesn't)
- Not checking `Last State` in `describe`
- Forgetting QoS class impacts eviction priority

---

## Solutions (Only If Stuck)

<details>
<summary>Show solutions</summary>

### Example resources block
```yaml
resources:
  requests:
    cpu: 50m
    memory: 64Mi
  limits:
    cpu: 100m
    memory: 128Mi
```

---

### OOM Pod command (one option)
```yaml
command: ["sh", "-c"]
args:
  - |
    x=""
    while true; do
      x="${x}0123456789"
    done
```

---

### Check QoS
```bash
kubectl describe pod <pod> -n cka-practice | grep -i "qos"
```

</details>

---

## Speed Targets

| Task | Target |
|---|---|
Set resources | ≤ 5 min |
Identify OOM cause | ≤ 2 min |
Fix | ≤ 3 min |
QoS identify | ≤ 30 sec each |
Total | ≤ 45 min |

---

## Pass Criteria for Day 5

You can move on if:

- You can set requests/limits without docs
- You can produce and identify OOMKilled quickly
- You can classify QoS reliably
- You can apply a minimal fix under time pressure

---

## Mental Model (Memorize)

> Requests = scheduling + guaranteed minimum  
> Limits = max usage enforced (OOM or throttling)  
> Memory limit breach = kill  
> CPU limit breach = throttle

---

## Notes

- One thing I confused:
- One command that helped:
- One pattern I’ll remember:

---
