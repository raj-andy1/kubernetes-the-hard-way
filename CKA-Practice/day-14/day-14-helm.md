# Day 14 – Helm (Basics for CKA)

## Learning Objectives
- Understand Helm basics
- Install a chart
- Inspect values.yaml
- Override values
- Debug Helm releases

Estimated time: 30–45 minutes

## Documentation
https://helm.sh/docs/intro/quickstart/

## Tasks
### Task 1 — Install Helm Chart
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo update
helm install my-nginx bitnami/nginx -n cka-practice

Verify:
kubectl get pods -n cka-practice

### Task 2 — Inspect Values
helm show values bitnami/nginx

### Task 3 — Override Values
helm upgrade my-nginx bitnami/nginx --set service.type=NodePort -n cka-practice

Verify:
kubectl get svc -n cka-practice

### Task 4 — Get Release Info
helm list -n cka-practice
helm get values my-nginx -n cka-practice

## Challenge Tasks
- Change replica count
- Rollback a release
- Uninstall release

## Skills
- Install/manage Helm charts
- Override values quickly
