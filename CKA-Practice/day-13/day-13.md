# Day 13 – Cluster Maintenance & Troubleshooting

## Learning Objectives
- Debug cluster components
- Understand kubelet failures
- Work with logs

## Tasks
1. Inspect node status
2. Debug NotReady node
3. Check kubelet logs
4. Restart failing pod

## Challenge
- Simulate failure and recover
- Identify root cause quickly

## Key Commands
kubectl get nodes
kubectl describe node
kubectl logs
journalctl -u kubelet
