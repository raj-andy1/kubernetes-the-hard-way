# CKA Full-Length Mock Exam (Day 1–13)

Namespace for all tasks:
cka-practice

Time Limit:
90–120 minutes

---

# Section 1 – Pods & Debugging

## Task 1
Create a Pod named web-pod using nginx:1.25 with label app=web and env ENV=prod.

---

## Task 2
Fix a crashing pod named crash-pod (currently exits immediately).

---

# Section 2 – Multi-Container & Volumes

## Task 3
Create a multi-container pod sharing logs via emptyDir.

---

## Task 4
Create a hostPath pod mounting /tmp/test.

---

# Section 3 – Services

## Task 5
Expose web-pod via ClusterIP service web-service.

## Task 6
Create NodePort service web-nodeport.

## Task 7
Fix broken service selector.

---

# Section 4 – ConfigMaps & Secrets

## Task 8
Create ConfigMap and inject into pod.

## Task 9
Create Secret and mount into pod.

---

# Section 5 – Deployments

## Task 10
Create deployment web-deploy with 3 replicas.

## Task 11
Perform rolling update and rollback.

---

# Section 6 – Storage

## Task 12
Create PV and PVC.

## Task 13
Mount PVC into pod.

---

# Section 7 – Networking

## Task 14
Test DNS resolution between pods.

## Task 15
Create NetworkPolicy allowing traffic only from specific pod.

---

# Section 8 – Scheduling

## Task 16
Schedule pod using nodeSelector.

## Task 17
Use taints and tolerations.

---

# Section 9 – RBAC

## Task 18
Create ServiceAccount.

## Task 19
Create Role and RoleBinding.

## Task 20
Verify access using kubectl auth can-i.

---

# Section 10 – Troubleshooting

## Task 21
Fix ImagePullBackOff pod.

## Task 22
Fix pod failing readiness probe.

## Task 23
Investigate NotReady node.

---

# Scoring

Each task = 2 points  
Total = 46 points

40+ = Ready  
30–39 = Almost ready  
<30 = Review weak areas

---

# Tips

- Use kubectl describe heavily
- Check endpoints for services
- Check logs for failures
- Use official docs efficiently
