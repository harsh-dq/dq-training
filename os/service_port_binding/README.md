# Create a OS level service with production grade setup, port bindings management  


### Create Systemd File for Service



Create `cd /etc/systemd/system/pythonapp.service` 

```
[Unit]
Description=<project description>

[Service]
User=<user e.g. root>
WorkingDirectory=<path to your project directory>
ExecStart=/bin/bash -c 'cd /home/ubuntu/project/ && source venv/bin/activate && python main.py'

[Install]
WantedBy=multi-user.target
```

### Reload the service files to include the new service.

```shell
sudo systemctl daemon-reload
```


### Start your service

```
sudo systemctl start your-service.service
```

### To check the status of your service

```
sudo systemctl status example.service
```

### To enable your service on every reboot

```
sudo systemctl enable example.service
```

### To disable your service on every reboot

```
sudo systemctl disable example.service
```


### Now Bind port To that service

Edit `/etc/service` file for binding service port

```shell
#local Service
Service_Name      Port_Number      #Comment

pythobapp           8080/tcp        # Pythonapp service
```