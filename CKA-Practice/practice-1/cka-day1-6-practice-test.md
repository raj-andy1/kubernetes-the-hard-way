# CKA Practice Test (Days 1–6)

Namespace for all tasks:
```
cka-practice
```

Time limit: **75 minutes**

Topics covered:
- Pods
- Multi-container pods
- Probes
- ConfigMaps
- Secrets
- Resources / QoS
- Debugging

---

# Section 1 — Pod Basics

## Task 1
Create a Pod named **web-pod** in namespace `cka-practice` with:

- image: `nginx:1.25`
- label: `app=web`
- containerPort: `80`
- environment variable `ENV=prod`

Verify:
```
kubectl exec -n cka-practice web-pod -- curl localhost
```

---

# Section 2 — Multi‑Container Pod

## Task 2
Create a Pod named **sidecar-pod** with two containers.

Container **app**
- image: busybox
- command writes date to `/var/log/app.log` every 5 seconds

Container **sidecar**
- image: busybox
- command tails `/var/log/app.log`

Use a shared `emptyDir` volume.

Verify:
```
kubectl logs sidecar-pod -n cka-practice -c sidecar
```

---

# Section 3 — Probes

## Task 3
Create a Pod named **ready-pod** using image `nginx` with a **readinessProbe**:

- httpGet
- path: `/`
- port: `80`
- initialDelaySeconds: `10`

Verify Pod becomes Ready.

---

## Task 4
Create a Pod named **bad-liveness-pod** with a broken **livenessProbe**:

- httpGet `/badpath`
- port `80`

Observe restart behavior and then fix it.

---

# Section 4 — ConfigMaps

## Task 5

Create ConfigMap:

```
app-config
MODE=production
```

Create Pod **cm-env-pod** that loads `MODE` as an environment variable and prints it.

Verify with:

```
kubectl logs cm-env-pod -n cka-practice
```

---

# Section 5 — Secrets

## Task 6

Create Secret:

```
db-secret
password=admin123
```

Create Pod **secret-vol-pod** that mounts the Secret at `/etc/secret`.

Verify:

```
kubectl exec -n cka-practice secret-vol-pod -- cat /etc/secret/password
```

---

# Section 6 — Resources / QoS

## Task 7

Create Pod **qos-guaranteed**:

- image: busybox
- command: sleep 3600

Resources:

```
requests:
  cpu: 200m
  memory: 128Mi
limits:
  cpu: 200m
  memory: 128Mi
```

Verify QoS:

```
kubectl describe pod qos-guaranteed -n cka-practice | grep -i qos
```

Expected: **Guaranteed**

---

## Task 8

Create Pod **qos-besteffort** with no requests or limits.

Expected QoS: **BestEffort**

---

## Task 9

Create Pod **qos-burstable**

```
requests:
  cpu: 100m
limits:
  cpu: 500m
```

Expected QoS: **Burstable**

---

# Section 7 — Debugging

## Task 10

Create Pod **bad-image-pod**

```
image: nginx:fake
```

Tasks:
- identify failure
- fix image
- verify Pod runs

---

## Task 11

Create Pod **crashing-pod**

```
command: ["sh","-c"]
args: ["exit 1"]
```

Tasks:
- observe CrashLoopBackOff
- inspect logs
- inspect previous logs
- fix Pod

---

## Task 12

Create Pod **missing-config-pod** referencing ConfigMap **does-not-exist**.

Tasks:
- find error with `describe`
- fix with minimal change

---

# Section 8 — Commands

## Task 13

Show last 5 events in namespace:

```
kubectl get events -n cka-practice --sort-by=.metadata.creationTimestamp | tail -n 5
```

---

## Task 14

Delete all pods in namespace:

```
kubectl delete pods --all -n cka-practice
```

---

# Scoring

2 points per task

Total tasks: **14**
Maximum score: **28**

Benchmarks:

- 24+ : Ready for next topics
- 20‑23 : Good but needs speed
- <20 : Repeat Days 1–6
