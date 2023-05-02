```
> kubectl create deployment hello-minikube --image=kicbase/echo-server:1.0
deployment.apps/hello-minikube created

> kubectl expose deployment hello-minikube --type=NodePort --port=8080
service/hello-minikube exposed

> kubectl get services hello-minikube
NAME             TYPE       CLUSTER-IP     EXTERNAL-IP   PORT(S)          AGE
hello-minikube   NodePort   10.96.63.248   <none>        8080:30192/TCP   23s

> minikube service hello-minikube
|-----------|----------------|-------------|---------------------------|
| NAMESPACE |      NAME      | TARGET PORT |            URL            |
|-----------|----------------|-------------|---------------------------|
| default   | hello-minikube |        8080 | http://192.168.49.2:30192 |
|-----------|----------------|-------------|---------------------------|
🏃  Starting tunnel for service hello-minikube.
|-----------|----------------|-------------|------------------------|
| NAMESPACE |      NAME      | TARGET PORT |          URL           |
|-----------|----------------|-------------|------------------------|
| default   | hello-minikube |             | http://127.0.0.1:55693 |
|-----------|----------------|-------------|------------------------|
🎉  Opening service default/hello-minikube in default browser...
❗  Because you are using a Docker driver on darwin, the terminal needs to be open to run it.
```
