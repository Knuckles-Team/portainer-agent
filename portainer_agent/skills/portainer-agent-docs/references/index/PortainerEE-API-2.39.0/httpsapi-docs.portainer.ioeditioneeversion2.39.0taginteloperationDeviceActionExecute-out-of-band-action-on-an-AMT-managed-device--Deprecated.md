##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/intel/operation/DeviceAction)Execute out of band action on an AMT managed device  Deprecated
Execute out of band action on an AMT managed device **Access policy** : administrator
##### Authorizations:
_jwt_
##### path Parameters
idrequired |  integer Environment identifier
---|---
deviceIdrequired |  integer Device identifier
##### Request Body schema: application/json
required
Device Action
Action |  string
---|---
### Responses
**204**
Success
**400**
Invalid request
**403**
Permission denied to access settings
**500**
Server error
post/open_amt/{id}/devices/{deviceId}/action
https://api-docs.portainer.io/api/open_amt/{id}/devices/{deviceId}/action
###  Request samples
  * Payload


Content type
application/json
Copy
`{
  *  "Action": "string"

 }`
