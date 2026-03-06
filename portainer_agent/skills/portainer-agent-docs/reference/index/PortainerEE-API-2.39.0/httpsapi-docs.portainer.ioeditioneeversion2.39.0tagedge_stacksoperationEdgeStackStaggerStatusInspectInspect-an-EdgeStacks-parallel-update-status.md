##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/edge_stacks/operation/EdgeStackStaggerStatusInspect)Inspect an EdgeStack's parallel update status
**Access policy** : administrator
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### path Parameters
idrequired |  integer EdgeStack Id
---|---
### Responses
**200**
OK
**400**
Bad Request
**500**
Internal Server Error
**503**
Edge compute features are disabled
get/edge_stacks/{id}/stagger/status
https://api-docs.portainer.io/api/edge_stacks/{id}/stagger/status
###  Response samples
  * 200


Content type
application/json
Copy
`{
  *  "status": "string"

 }`
