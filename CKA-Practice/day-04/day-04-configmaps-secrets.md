# CKA Day 4 — ConfigMaps & Secrets

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

By the end of Day 4, you should be able to:

- Explain the difference between ConfigMaps and Secrets
- Create ConfigMaps and Secrets imperatively and declaratively
- Consume ConfigMaps and Secrets as environment variables and volumes
- Understand update and propagation behavior
- Debug Pods failing due to missing configuration

---

## Tasks to Complete (Required)

### Task 1 — Create a ConfigMap
Create a ConfigMap named `app-config` with:
- Key: MODE
- Value: production
- Namespace: cka-practice

---

### Task 2 — Consume ConfigMap as Env Var
Create a Pod that reads MODE from the ConfigMap and prints it.

---

### Task 3 — Consume ConfigMap as Volume
Mount the ConfigMap at `/etc/config` and read the file.

---

### Task 4 — Create a Secret
Create a Secret named `db-secret` with:
- Key: password
- Value: admin123

---

### Task 5 — Consume Secret as Env Var
Inject the secret as an environment variable.

---

### Task 6 — Consume Secret as Volume
Mount the secret at `/etc/secret` and read the file.

---

## Challenge Tasks

- Break a ConfigMap reference and fix it
- Update ConfigMap values and observe behavior
- Explain security differences between env vars and volumes

---

## Solutions (Only If Stuck)

```bash
kubectl create configmap app-config --from-literal=MODE=production -n cka-practice
kubectl create secret generic db-secret --from-literal=password=admin123 -n cka-practice
```

---

## Pass Criteria

- You can wire ConfigMaps and Secrets without docs
- You understand update behavior differences
- You can debug config-related failures quickly

---

## Notes

- One mistake I made:
- One command to remember:
- One behavior that surprised me:
