##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/system/operation/systemUpdate)Update Portainer to latest version
Update Portainer to latest version **Access policy** : administrator
### Responses
**204**
Success
**409**
Conflict, an automatic patch operation is already in progress
**500**
Server error
post/system/update
https://api-docs.portainer.io/api/system/update
###  Response samples
  * 204


Content type
application/json
Copy
`{

  *  "InstanceID": "299ab403-70a8-4c05-92f7-bf7a994d50df",

  *  "Version": "2.0.0"

 }`
