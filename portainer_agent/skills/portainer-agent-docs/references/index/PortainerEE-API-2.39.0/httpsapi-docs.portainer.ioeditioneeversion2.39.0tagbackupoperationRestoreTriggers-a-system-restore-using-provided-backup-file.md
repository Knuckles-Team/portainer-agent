##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/backup/operation/Restore)Triggers a system restore using provided backup file
Triggers a system restore using provided backup file **Access policy** : public
##### Request Body schema: application/json
required
Restore request payload
FileContentrequired |  Array of integers Content of the backup
---|---
FileNamerequired |  string File name
Password |  string Password to decrypt the backup with
### Responses
**200**
Success
**400**
Invalid request
**500**
Server error
post/restore
https://api-docs.portainer.io/api/restore
###  Request samples
  * Payload


Content type
application/json
Copy
Expand all  Collapse all
`{

  *  "FileContent": [
    * 0
 ],

  *  "FileName": "string",

  *  "Password": "string"

 }`
