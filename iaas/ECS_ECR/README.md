#  ECS and ECR, re-configure the ALB for this

## Build an image 

```shell 
cd falsk-demo
sudo docker build -t flask-demo:latest .
```

## Create Docker Repo at ECR


### Using Command Line

Create Repo on ECR 

```shell
 aws ecr create-repository --repository-name falask-demo
```
`output`

```json output
{
    "repository": {
        "repositoryArn": "arn:aws:ecr:us-east-2:575196606097:repository/flask-demo",
        "registryId": "575196606097",
        "repositoryName": "flask-demo",
        "repositoryUri": "575196606097.dkr.ecr.us-east-2.amazonaws.com/flask-demo",
        "createdAt": 1625644088.0,
        "imageTagMutability": "MUTABLE",
        "imageScanningConfiguration": {
            "scanOnPush": false
        }
    }
}

```


Retrieve an authentication token and authenticate your Docker client to your registry.

```shell
aws ecr get-login-password --region us-east-2 | docker login --username AWS --password-stdin 575196606097.dkr.ecr.us-east-2.amazonaws.com
```

Tag & Push Image to ECR Repo

```shell
docker tag flask-demo:latest 575196606097.dkr.ecr.us-east-2.amazonaws.com/flask-demo:latest
docker push 575196606097.dkr.ecr.us-east-2.amazonaws.com/flask-demo:latest
```



## Create Task defination and add container

Create a Task Defination and Add Container 




Create ALB 

