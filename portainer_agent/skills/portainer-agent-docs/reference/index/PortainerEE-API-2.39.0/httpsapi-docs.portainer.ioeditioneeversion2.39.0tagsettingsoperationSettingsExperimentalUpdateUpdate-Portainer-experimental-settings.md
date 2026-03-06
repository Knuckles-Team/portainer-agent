##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/settings/operation/SettingsExperimentalUpdate)Update Portainer experimental settings
Update Portainer experimental settings. **Access policy** : administrator
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### Request Body schema: application/json
required
New settings
fleetManagement |  boolean
---|---
### Responses
**204**
Success
**400**
Invalid request
**500**
Server error
put/settings/experimental
https://api-docs.portainer.io/api/settings/experimental
###  Request samples
  * Payload


Content type
application/json
Copy
`{
  *  "fleetManagement": false

 }`
