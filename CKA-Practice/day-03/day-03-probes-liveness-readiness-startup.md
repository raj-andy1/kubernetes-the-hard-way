# CKA Day 3 — Probes (Liveness, Readiness, Startup)

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

By the end of Day 3, you should be able to:

- Explain the difference between **liveness**, **readiness**, and **startup** probes
- Choose the correct probe type for a given scenario
- Implement probes using `httpGet` and `exec`
- Debug Pods failing due to misconfigured probes
- Read probe failures quickly using `describe` and `events`

---

## Tasks to Complete (Required)

### Task 1 — Readiness Probe (Traffic Control)

Create a Pod named `ready-pod` with:

- Namespace: `cka-practice`
- Image: `nginx`
- Readiness probe:
  - httpGet `/`
  - Port `80`
  - initialDelaySeconds `10`

---

### Task 2 — Liveness Probe (Restart Behavior)

Modify the Pod so that:

- A liveness probe checks `/` on port `80`
- Break the probe intentionally
- Observe container restarts

---

### Task 3 — Startup Probe (Slow Apps)

Create a Pod named `slow-start-pod` with:

- Image: `busybox`
- Command sleeps for 30 seconds
- Startup probe that allows delayed startup

---

### Task 4 — Inspect & Explain

Using `kubectl describe pod`, identify:

- Which probe failed
- What Kubernetes did in response

---

## Challenge Tasks

- Fix a crashloop caused by the wrong probe type
- Use an exec probe that checks for `/tmp/healthy`
- Demonstrate readiness failure without liveness failure

---

## Solutions (Only If Stuck)

```yaml
readinessProbe:
  httpGet:
    path: /
    port: 80
  initialDelaySeconds: 10
```

```yaml
livenessProbe:
  httpGet:
    path: /
    port: 80
  initialDelaySeconds: 15
```

```yaml
startupProbe:
  exec:
    command: ["sh", "-c", "test -f /tmp/started"]
  failureThreshold: 30
  periodSeconds: 1
```

---

## Speed Targets

- Add probes: ≤ 5 min
- Debug failures: ≤ 5 min
- Total: ≤ 40 min

---

## Pass Criteria

- You can explain probe differences without hesitation
- You can debug probe failures using events
- You know when NOT to use liveness probes

---

## Notes

- One probe mistake I made:
- One timing value to remember:
- One scenario that clicked:
