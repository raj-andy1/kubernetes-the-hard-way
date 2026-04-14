# Day 10 – Networking (DNS, Network Policies)

## Learning Objectives
- Understand Kubernetes DNS
- Debug service discovery
- Create NetworkPolicies

## Tasks
1. Create two pods and test DNS resolution using service names
2. Use `nslookup` inside a pod
3. Create a NetworkPolicy to allow traffic only from specific pods
4. Break connectivity and debug

## Challenge
- Deny all traffic and selectively allow
- Verify using busybox pods

## Key Commands
kubectl exec
kubectl get svc
kubectl describe networkpolicy
