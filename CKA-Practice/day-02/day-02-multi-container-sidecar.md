# CKA Day 2 — Multi-Container Pods (Sidecar Pattern)

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

By the end of Day 2, you should be able to:

- Explain **why** multiple containers run in a single Pod
- Implement the **sidecar pattern**
- Share data between containers using `emptyDir`
- Debug multi-container Pods using container-specific logs
- Exec into a **specific container** using `-c`
- Understand Pod-level vs container-level configuration

---

## Tasks to Complete (Required)

### Task 1 — Create a Sidecar Pod with Shared Volume

Create a Pod named `sidecar-pod` with:

- Namespace: `cka-practice`
- Volume: `emptyDir`
- Container `app`
  - Image: `busybox`
  - Writes the current date to `/var/log/app.log` every 5 seconds
- Container `sidecar`
  - Image: `busybox`
  - Continuously tails `/var/log/app.log`

---

### Task 2 — Verify Container Interaction

```bash
kubectl logs sidecar-pod -n cka-practice -c sidecar
```

---

### Task 3 — Exec into a Specific Container

Exec into both containers and verify `/var/log/app.log`.

---

## Challenge Tasks

- Break the shared volume mount and fix it
- Run `kubectl logs` without `-c` and explain the error
- Crash the `app` container and observe restart behavior

---

## Solutions (Only If Stuck)

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: sidecar-pod
  namespace: cka-practice
spec:
  volumes:
  - name: shared-logs
    emptyDir: {}
  containers:
  - name: app
    image: busybox
    command: ["/bin/sh", "-c"]
    args:
    - |
      while true; do
        date >> /var/log/app.log;
        sleep 5;
      done
    volumeMounts:
    - name: shared-logs
      mountPath: /var/log
  - name: sidecar
    image: busybox
    command: ["/bin/sh", "-c"]
    args:
    - tail -f /var/log/app.log
    volumeMounts:
    - name: shared-logs
      mountPath: /var/log
```

---

## Pass Criteria

- You never forget `-c <container>`
- You can explain the sidecar pattern clearly
- You can debug shared-volume issues confidently
