##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/endpoints/operation/endpointDockerhubStatus)fetch docker pull limits
get docker pull limits for a docker hub registry in the environment **Access policy** :
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### path Parameters
idrequired |  integer endpoint ID
---|---
registryIdrequired |  integer registry ID
### Responses
**200**
Success
**400**
Invalid request
**403**
Permission denied
**404**
registry or endpoint not found
**500**
Server error
get/endpoints/{id}/dockerhub/{registryId}
https://api-docs.portainer.io/api/endpoints/{id}/dockerhub/{registryId}
###  Response samples
  * 200


Content type
application/json
Copy
`{

  *  "limit": 0,

  *  "remaining": 0

 }`
