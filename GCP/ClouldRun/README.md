# Deploy Docker Image with Cloud Run

Cloud Run is a managed compute platform that enables you to run containers that are invocable via requests or events. Cloud Run is serverless: it abstracts away all infrastructure management, so you can focus on what matters most — building great applications.


## 1. Build And Push Image to your repo 

Here We Use GCR for image repository 


```shell
gcloud builds submit --tag gcr.io/<PROJECT_ID>/demo-image .
```