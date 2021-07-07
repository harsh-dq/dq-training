#!/bin/bash


CONTAINER_NAME=$1
VOLUME_NAME=$2
DATE=date "+%Y-%m-%d"


usage() {
  echo "Usage: $0 [container name] [volume name]"
  exit 1
}

if [ -z $CONTAINER_NAME ]
then
  echo "Error: missing container name parameter."
  usage
fi

if [ -z $VOLUME_NAME ]
then
  echo "Error: missing volume name parameter."
  usage
fi


#delete 5 Days Old backup

find /etc/dbbackup/ -type f -mtime +4 -name "$VOLUME_NAME*" -exec rm -rf "{}" \;


# We are Saving Backup at location `/etc/dbbackup/`
sudo docker run --rm --volumes-from $CONTAINER_NAME -v /etc/dbbackup/:/backup busybox tar cvf /backup/$VOLUME_NAME-$DATE.tar data 



#  can also direct upload to S3 

# aws s3 cp $VOLUME_NAME.tar s3://custom-2/$VOLUME_NAME.tar --acl private 