# Day 12 – Security (RBAC, Service Accounts)

## Learning Objectives
- Understand RBAC
- Create Roles and RoleBindings
- Use ServiceAccounts

## Tasks
1. Create ServiceAccount
2. Create Role to allow pod listing
3. Bind Role to ServiceAccount
4. Test using kubectl with SA token

## Challenge
- Create least privilege access
- Debug forbidden errors

## Key Commands
kubectl auth can-i
kubectl create role
kubectl create rolebinding
