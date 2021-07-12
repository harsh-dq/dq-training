
## Install minikube 
  


## Start Minikube with 3 nodejs 

```shell
 minikube start --nodes 2 -p multinode
```
## To Add a node to minikube Cluster

```shell 
minikube node add
```


# StatefulSet

StatefulSet is also a Controller but unlike Deployments, it doesn’t create ReplicaSet rather itself creates the Pod with a unique naming convention. e.g. If you create a StatefulSet with name counter, it will create a pod with name counter-0, and for multiple replicas of a statefulset, their names will increment like counter-0, counter-1, counter-2, etc


Every replica of a stateful set will have its own state, and each of the pods will be creating its own PVC(Persistent Volume Claim). So a statefulset with 3 replicas will create 3 pods, each having its own Volume, so total 3 PVCs.
