# Setup Nginx/Apache web server for serving the above application with redirection rules


## Run 2 same app Container with diffrent port

```shell
docker run -d -p 5000:8080 prydonius/todo:latest
docker run -d -p 5001:8080 prydonius/todo:latest
```



## Install Nginx

```shell
sudo apt install -y nginx
```


## Nginx Config

```

upstream reversebackend {       
    server http://127.0.0.1:5000 weight=5 max_fails=3 fail_timeout=30s;  # Change Ip to Instance IP
    server http://127.0.0.1:500 weight=2 max_fails=3 fail_timeout=30s;    # Change Ip to Instance IP
}


server {
    listen [::]:443 ssl; 
    listen 443 ssl; 
    server_name example.com;

    # Permanent redirect to www
    rewrite ^/(.*)$ http://www.example.com/$1 permanent;

    # Content Directory 
    root /var/www/html/example.com;
    index index.php index.html; 

    
    
    ssl_certificate /etc/letsencrypt/live/example.com/fullchain.pem; 
    ssl_certificate_key /etc/letsencrypt/live/example.com/privkey.pem; 


    
    ssl_session_cache shared:SSL:10m;


    # DAta Upload Size
    client_max_body_size 5M;



    location / {
        proxy_set_header   X-Forwarded-For $remote_addr;
        proxy_set_header   Host $http_host;
        proxy_pass         http://reversebackend;
    }
}



server {
    if ($host = example.com) {
        return 301 https://$host$request_uri;
    } 

    listen 80 default_server;
    listen [::]:80 default_server;
    server_name example.com;
    return 404; 


}


```





## Generate SSl Certificate 

```shell
sudo apt install certbot python3-certbot-nginx
```

```shell
sudo certbot --nginx -d domian.com -d www.domain.com
```