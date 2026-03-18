# Kubernetes CKA – Core Documentation Links

These official Kubernetes documentation pages cover a large portion of tasks commonly encountered in the **Certified Kubernetes Administrator (CKA)** exam.

Use these during practice and bookmark them for the exam.

---

## 1. Pods
Primary documentation for Pod structure and configuration.

https://kubernetes.io/docs/concepts/workloads/pods/

Use this page for:
- Pod YAML structure
- container fields
- commands and args
- restartPolicy
- volume configuration

---

## 2. Multi‑Container Pods (Sidecars)

https://kubernetes.io/docs/concepts/workloads/pods/#multi-container-pods

Use this page for:
- sidecar containers
- shared volumes
- logging containers

---

## 3. Liveness, Readiness, and Startup Probes

https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/

Use this page for:
- livenessProbe
- readinessProbe
- startupProbe
- httpGet checks
- exec probes

---

## 4. ConfigMaps

https://kubernetes.io/docs/concepts/configuration/configmap/

Use this page for:
- environment variables from ConfigMaps
- configMapKeyRef
- envFrom
- mounting ConfigMaps as volumes

---

## 5. Secrets

https://kubernetes.io/docs/concepts/configuration/secret/

Use this page for:
- creating secrets
- secret environment variables
- secret volumes

---

## 6. Resource Requests and Limits

https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/

Use this page for:
- CPU requests
- memory limits
- resource enforcement
- OOMKilled behavior

---

## 7. Pod Lifecycle

https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/

Use this page for:
- container states
- CrashLoopBackOff
- restart behavior
- lifecycle events

---

## 8. kubectl Cheat Sheet

https://kubernetes.io/docs/reference/kubectl/cheatsheet/

Use this page for quick command lookup:
- kubectl run
- kubectl exec
- kubectl logs
- kubectl expose
- kubectl port-forward

---

## 9. Kubernetes API Reference

https://kubernetes.io/docs/reference/generated/kubernetes-api/

Use this page when you need exact YAML fields such as:
- envFrom
- volumeMounts
- resources
- probes

---

## 10. Debug Running Pods

https://kubernetes.io/docs/tasks/debug/debug-application/debug-running-pod/

Use this page for debugging techniques:
- kubectl describe
- kubectl logs
- kubectl exec
- checking events

---

## Suggested Exam Tabs

Open these first during the exam:

1. kubectl cheat sheet
2. probe documentation
3. ConfigMap documentation

These help solve many tasks quickly.

---

## Navigation Tip

Use **Ctrl/Cmd + F** inside the documentation page to quickly find fields such as:

readinessProbe  
configMapKeyRef  
volumeMounts  
resources  

This saves time during the exam.
