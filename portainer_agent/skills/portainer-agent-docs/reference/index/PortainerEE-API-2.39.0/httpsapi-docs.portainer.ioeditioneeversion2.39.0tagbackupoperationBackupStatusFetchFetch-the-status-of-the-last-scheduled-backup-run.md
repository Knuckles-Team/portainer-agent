##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/backup/operation/BackupStatusFetch)Fetch the status of the last scheduled backup run
**Access policy** : public
### Responses
**200**
Success
**500**
Server error
get/backup/s3/status
https://api-docs.portainer.io/api/backup/s3/status
###  Response samples
  * 200


Content type
application/json
Copy
`{

  *  "Failed": true,

  *  "TimestampUTC": "string"

 }`
