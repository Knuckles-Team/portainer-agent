##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/backup/operation/BackupToS3)Execute backup to AWS S3 Bucket
Creates an archive with a system data snapshot and upload it to the target S3 bucket **Access policy** : administrator
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### Request Body schema: application/json
required
S3 backup settings
accessKeyID |  string AWS access key id
---|---
bucketName |  string AWS S3 bucket name
cronRule |  string Crontab rule to make periodical backups
password |  string Password to encrypt the backup with
region |  string AWS S3 region. Default to "us-east-1"
s3CompatibleHost |  string S3 compatible host
secretAccessKey |  string AWS secret access key
### Responses
**204**
Success
**400**
Invalid request
**500**
Server error
post/backup/s3/execute
https://api-docs.portainer.io/api/backup/s3/execute
###  Request samples
  * Payload


Content type
application/json
Copy
`{

  *  "accessKeyID": "string",

  *  "bucketName": "string",

  *  "cronRule": "string",

  *  "password": "string",

  *  "region": "us-east-1",

  *  "s3CompatibleHost": "string",

  *  "secretAccessKey": "string"

 }`
