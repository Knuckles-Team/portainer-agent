##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/settings/operation/SettingsAdditionalFunctionalityUpdate)Update Portainer additional functionality settings
Update Portainer additional functionality settings. **Access policy** : administrator
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### Request Body schema: application/json
required
New settings
Observabilityrequired |  boolean
---|---
Policiesrequired |  boolean
### Responses
**204**
Success
**400**
Invalid request
**500**
Server error
put/settings/additional_functionality
https://api-docs.portainer.io/api/settings/additional_functionality
###  Request samples
  * Payload


Content type
application/json
Copy
`{

  *  "Observability": true,

  *  "Policies": true

 }`
