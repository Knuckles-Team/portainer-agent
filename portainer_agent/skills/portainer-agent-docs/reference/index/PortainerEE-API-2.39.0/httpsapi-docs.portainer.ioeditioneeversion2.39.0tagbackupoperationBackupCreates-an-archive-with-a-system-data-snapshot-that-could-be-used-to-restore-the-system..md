##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/backup/operation/Backup)Creates an archive with a system data snapshot that could be used to restore the system.
Creates an archive with a system data snapshot that could be used to restore the system. **Access policy** : admin
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### Request Body schema: application/json
An object contains the password to encrypt the backup with
Password |  string
---|---
### Responses
**200**
Success
**400**
Invalid request
**500**
Server error
post/backup
https://api-docs.portainer.io/api/backup
###  Request samples
  * Payload


Content type
application/json
Copy
`{
  *  "Password": "string"

 }`
