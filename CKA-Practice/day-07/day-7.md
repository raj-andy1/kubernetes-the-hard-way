# Day 7 – Services (ClusterIP & NodePort)

## Learning Objectives

By the end of this session you should be able to:

- Create a ClusterIP Service
- Create a NodePort Service
- Use selectors correctly
- Inspect Endpoints
- Debug Service connectivity problems

Estimated time: 30–45 minutes

---

# Documentation

Open these pages during practice (same as CKA exam):

https://kubernetes.io/docs/concepts/services-networking/service/

https://kubernetes.io/docs/concepts/services-networking/service/#publishing-services-service-types

Kubectl Cheat Sheet

https://kubernetes.io/docs/reference/kubectl/cheatsheet/

---

# Tasks

## Task 1 — Create a Pod

Create a Pod called:

web-svc-pod

Image:

nginx

Namespace:

cka-practice

Add label:

app=web

Verify:

kubectl get pods -n cka-practice

---

## Task 2 — Create a ClusterIP Service

Expose the Pod using a Service called:

web-service

Ports:

port: 80  
targetPort: 80

Command:

kubectl expose pod web-svc-pod \
--name web-service \
--port 80 \
--target-port 80 \
-n cka-practice

Verify:

kubectl get svc -n cka-practice

Expected:

TYPE = ClusterIP

---

## Task 3 — Test Service Connectivity

Launch a temporary pod:

kubectl run curlpod \
--image busybox \
-n cka-practice \
--rm -it -- sh

Inside the container:

wget -O- http://web-service

You should see nginx HTML.

---

## Task 4 — Inspect Service Endpoints

Run:

kubectl get endpoints -n cka-practice

Expected:

web-service -> Pod IP

Example:

10.200.1.6:80

Important concept:

Service → Endpoints → Pod

---

## Task 5 — Create a NodePort Service

Create a Service called:

web-nodeport

Type:

NodePort

Expose port 80.

Example YAML:

apiVersion: v1
kind: Service
metadata:
  name: web-nodeport
  namespace: cka-practice
spec:
  type: NodePort
  selector:
    app: web
  ports:
  - port: 80
    targetPort: 80

Apply:

kubectl apply -f nodeport.yaml

---

## Task 6 — Find the NodePort

Run:

kubectl get svc web-nodeport -n cka-practice

Example output:

80:30007/TCP

Test it:

curl <NODE-IP>:30007

Example:

curl 192.168.1.22:30007

---

# Challenge Tasks

## Challenge 1 — Multiple Pods

Create another Pod:

web-svc-pod-2

Same label:

app=web

Check endpoints:

kubectl get endpoints web-service -n cka-practice

You should now see **two Pod IPs**.

---

## Challenge 2 — Break the Service

Edit the service selector:

app: wronglabel

Observe:

kubectl get endpoints

Expected:

<none>

Fix the selector.

---

## Challenge 3 — Delete a Pod

Delete one Pod:

kubectl delete pod web-svc-pod -n cka-practice

Observe endpoints automatically update.

---

# Key Concepts

ClusterIP

Internal-only service.

NodePort

Exposes service on every node.

Traffic flow:

Client  
↓  
NodeIP:NodePort  
↓  
Service  
↓  
Pod

---

# Useful Commands

kubectl get svc

kubectl describe svc

kubectl get endpoints

kubectl expose pod

kubectl expose deployment

---

# Skills You Should Have After Day 7

You should be able to:

- Create ClusterIP services quickly
- Create NodePort services
- Test connectivity from inside cluster
- Debug broken Service selectors
- Inspect Endpoints