# Day 15 – Ingress

## Learning Objectives
- Understand Ingress resource
- Route traffic using host/path
- Debug Ingress issues

Estimated time: 30–45 minutes

## Documentation
https://kubernetes.io/docs/concepts/services-networking/ingress/

## Tasks
### Task 1 — Deployment + Service
Create deployment web-deploy (nginx, 2 replicas)
Expose as ClusterIP web-service

### Task 2 — Create Ingress
Create ingress web-ingress routing host web.local → web-service:80

### Task 3 — Test
Add to /etc/hosts:
127.0.0.1 web.local

curl http://web.local

### Task 4 — Debug
Break service name or port and fix

## Challenge Tasks
- Add path routing (/app)
- Add second backend
- Debug 404 issues

## Skills
- Create ingress
- Debug routing issues
