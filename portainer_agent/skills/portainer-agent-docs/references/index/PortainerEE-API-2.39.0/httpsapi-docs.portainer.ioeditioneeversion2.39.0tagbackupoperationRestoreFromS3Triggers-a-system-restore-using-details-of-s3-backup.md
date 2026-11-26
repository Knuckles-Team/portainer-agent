##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/backup/operation/RestoreFromS3)Triggers a system restore using details of s3 backup
Triggers a system restore using details of s3 backup **Access policy** : public
##### Request Body schema: application/json
S3 Location Payload
AccessKeyID |  string AWS access key id
---|---
BucketName |  string AWS S3 bucket name
Filename |  string AWS S3 filename in the bucket
Password |  string
Region |  string AWS S3 region. Default to "us-east-1"
S3CompatibleHost |  string S3 compatible host
SecretAccessKey |  string AWS secret access key
### Responses
**200**
Success
**400**
Invalid request
**500**
Server error
post/backup/s3/restore
https://api-docs.portainer.io/api/backup/s3/restore
###  Request samples
  * Payload


Content type
application/json
Copy
`{

  *  "AccessKeyID": "string",

  *  "BucketName": "string",

  *  "Filename": "string",

  *  "Password": "string",

  *  "Region": "us-east-1",

  *  "S3CompatibleHost": "string",

  *  "SecretAccessKey": "string"

 }`
