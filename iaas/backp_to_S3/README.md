# Backup Of Some Data To S3

Create a s3 Bucket with Versioning enable 


Command to upload data to s3 with private access

```shell
(ishu㉿kali)-[~]
└─$ aws s3 cp db-backup.tar.gz s3://custom-2/db-backup.tar.gz --acl private
upload: ./db-backup.tar.gz to s3://custom-2/db-backup.tar.gz      
                                                                                
┌──(ishu㉿kali)-[~]
└─$ aws s3 cp db-backup.tar.gz s3://custom-2/db-backup.tar.gz --acl private
upload: ./db-backup.tar.gz to s3://custom-2/db-backup.tar.gz      
```

Here We have uploaded a file 2 times  so you can look into  versioning