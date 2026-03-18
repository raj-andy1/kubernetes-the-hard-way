# Day 9 – Volumes & Storage

## Learning Objectives
- Understand Kubernetes volumes
- Use emptyDir
- Use hostPath
- Use NFS persistent storage
- Create PersistentVolume and PersistentVolumeClaim

---

## Documentation

https://kubernetes.io/docs/concepts/storage/volumes/

https://kubernetes.io/docs/concepts/storage/persistent-volumes/

---

## Tasks

### Task 1 – emptyDir Volume

Create pod:

name: volume-pod

Container writes to:

/data/log.txt

Mount emptyDir volume.

Verify file exists.

---

### Task 2 – Multi Container Shared Volume

Create Pod with two containers.

Container 1 writes timestamps.

Container 2 tails file.

Use shared emptyDir.

---

### Task 3 – hostPath Volume

Create pod mounting hostPath:

/tmp/test

Verify inside container.

---

### Task 4 – PersistentVolume

Create PV:

capacity: 1Gi  
accessMode: ReadWriteOnce

---

### Task 5 – PersistentVolumeClaim

Create PVC requesting 1Gi.

Verify binding:

kubectl get pv  
kubectl get pvc

---

### Task 6 – Mount PVC

Create pod mounting the PVC.

Verify storage works.

---

## Challenge Tasks

1. Use your NFS server to create a PV.
2. Bind a PVC.
3. Mount it to a pod.
4. Write data and verify persistence after pod restart.

---

## Expected Skills

- Create volumes
- Understand PV/PVC lifecycle
- Debug storage binding issues