# 1. Configure a JOB that can run as a service, Daemon, CRON 

## This job should create a backup of the DB volume in docker and save that at a location


### Run Backup Script

```shell
 bash createdb_backup.sh mongodb mongodb_data
```

Here in above command the container name is `mongodb` and Volume name is `mongodb_data`

## Run As Cron Job


Here We Create CronJob For backing up DB Volume at Every Night

```shell
crontab -e
```

Select Any Editor and add the following line at the last 

```
0 3 * * * /path/to/script/createdb_backup.sh $COTAINER_NAME $VOLUME_NAME
```

## Run Script in  Deamon (Background Task)

```shell
createdb_backup.sh $COTAINER_NAME $VOLUME_NAME > /dev/null &
```



### Explored New Tool For Backup And Restore

https://github.com/discordianfish/docker-backup