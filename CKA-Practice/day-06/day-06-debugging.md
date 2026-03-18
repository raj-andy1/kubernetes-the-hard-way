# CKA Day 6 — Pod & Application Debugging

## Exam Setup

Run at the start of every practice session.

### kubectl Alias
```bash
alias k=kubectl
Autocomplete
source <(kubectl completion bash)
complete -F __start_kubectl k
Learning Objectives

By the end of Day 6 you should be able to debug:

CrashLoopBackOff

ImagePullBackOff

ErrImagePull

Misconfigured commands

Missing ConfigMaps / Secrets

Probe failures

You should rely on:

get → describe → logs → events

Never guess.

Debugging Order (Memorize)

1️⃣ Check pod state

k get pods -n <ns>

2️⃣ Describe pod

k describe pod <pod> -n <ns>

3️⃣ Check logs

k logs <pod> -n <ns>

or

k logs <pod> -n <ns> --previous

4️⃣ Inspect events

k get events -n <ns> --sort-by=.metadata.creationTimestamp | tail
Task 1 — ImagePullBackOff

Create a pod with a bad image.

apiVersion: v1
kind: Pod
metadata:
  name: bad-image
  namespace: cka-practice
spec:
  containers:
  - name: nginx
    image: nginx:notreal

Observe:

ImagePullBackOff

Fix it by updating the image.

Task 2 — CrashLoopBackOff

Create a crashing pod.

apiVersion: v1
kind: Pod
metadata:
  name: crash-pod
  namespace: cka-practice
spec:
  containers:
  - name: crash
    image: busybox
    command: ["sh","-c"]
    args: ["exit 1"]

Observe:

CrashLoopBackOff

Inspect logs and events.

Fix by changing command:

sleep 3600
Task 3 — Logs from Previous Container

When pods restart, use:

k logs crash-pod -n cka-practice --previous

This retrieves logs from the container before restart.

Task 4 — Multi-Container Debugging

Create pod with two containers.

One fails.

Use:

k logs <pod> -c <container>

Identify failing container.

Task 5 — Missing ConfigMap

Create a pod referencing a missing ConfigMap.

Observe:

CreateContainerConfigError

Fix by creating the ConfigMap.

Challenge Tasks
Challenge 1

Break a pod using wrong command.

Diagnose and fix in <3 minutes.

Challenge 2

Debug a failing pod using only events.

Challenge 3

Given a broken pod:

Identify root cause in under 2 minutes.

Mental Model

Status → WHAT happened

Describe → WHY it happened

Logs → WHAT the application did

Events → WHEN it happened


---

# Practice Test (Days 1–6)

Time limit: **60 minutes**

Namespace for all tasks:


cka-practice


---

# Question 1 — Pod Creation

Create a pod named:


nginx-test


Requirements:

- image: nginx
- label: `app=web`
- containerPort: 80

Verify it is running.

---

# Question 2 — Multi-Container Pod

Create pod:


log-pod


Containers:

1️⃣ writer


busybox


Command:


while true; do date >> /var/log/app.log; sleep 5; done


2️⃣ reader


busybox


Command:


tail -f /var/log/app.log


Use shared `emptyDir`.

Verify logs.

---

# Question 3 — ConfigMap

Create ConfigMap:


app-config


Data:


MODE=production


Create pod:


config-test


Inject env variable from ConfigMap.

Verify value inside container.

---

# Question 4 — Secret

Create secret:


db-secret


Key:


password=admin123


Create pod that prints the password.

---

# Question 5 — QoS Classes

Create three pods:

### Pod A
No requests/limits

Expected:


BestEffort


### Pod B


requests: 100m CPU
limits: 500m CPU


Expected:


Burstable


### Pod C


requests == limits


Expected:


Guaranteed


Verify QoS.

---

# Question 6 — CrashLoop Debug

Create a pod:


broken-pod


Command:


exit 1


Observe failure.

Fix it so pod runs.

---

# Question 7 — ImagePullBackOff

Create pod with invalid image:


redis:fake


Diagnose error.

Fix it.

---

# Question 8 — Event Debugging

Find the **last 5 events** in namespace.

Command:

```bash
k get events -n cka-practice --sort-by=.metadata.creationTimestamp | tail

Explain what happened.

Passing Criteria

You should be able to:

✔ Create pods quickly
✔ Debug CrashLoopBackOff
✔ Use ConfigMaps/Secrets
✔ Identify QoS classes
✔ Diagnose failures with describe/logs/events

Target completion time:

45–60 minutes