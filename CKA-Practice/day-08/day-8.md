# Day 8 – Deployments & ReplicaSets

## Learning Objectives
- Understand Deployments
- Understand ReplicaSets
- Perform rolling updates
- Rollback deployments

---

## Documentation

https://kubernetes.io/docs/concepts/workloads/controllers/deployment/

https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/

---

## Tasks

### Task 1 – Create Deployment

Create a deployment:

name: web-deploy  
image: nginx  
replicas: 3

Verify:

kubectl get deploy -n cka-practice  
kubectl get pods -n cka-practice

---

### Task 2 – Scale Deployment

Scale to 5 replicas:

kubectl scale deployment web-deploy --replicas=5 -n cka-practice

Verify:

kubectl get pods -n cka-practice

---

### Task 3 – Rolling Update

Update image:

kubectl set image deployment/web-deploy nginx=nginx:1.25 -n cka-practice

Check rollout:

kubectl rollout status deployment web-deploy -n cka-practice

---

### Task 4 – Rollback

Simulate bad update:

kubectl set image deployment/web-deploy nginx=nginx:fake -n cka-practice

Then rollback:

kubectl rollout undo deployment web-deploy -n cka-practice

---

## Challenge Tasks

1. Create deployment using YAML.
2. Pause a rollout.
3. Resume rollout.
4. Inspect ReplicaSets.

Commands:

kubectl rollout pause deployment web-deploy  
kubectl rollout resume deployment web-deploy  
kubectl get rs

---

## Expected Skills

- Manage Deployments
- Perform rollouts and rollbacks
- Understand ReplicaSet behavior