##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/backup/operation/BackupSettingsFetch)Fetch s3 backup settings/configurations
**Access policy** : administrator
##### Authorizations:
_ApiKeyAuth_ _jwt_
### Responses
**200**
Success
**401**
Unauthorized
**500**
Server error
get/backup/s3/settings
https://api-docs.portainer.io/api/backup/s3/settings
###  Response samples
  * 200


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
