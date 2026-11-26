##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/edge_stacks/operation/EdgeStackFile)Fetches the stack file for an EdgeStack
**Access policy** : administrator
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### path Parameters
idrequired |  integer EdgeStack Id
---|---
##### query Parameters
version |  integer Stack file version maintained by Portainer. If both version and commitHash are provided, the commitHash will be used
---|---
commitHash |  string Git repository commit hash. If both version and commitHash are provided, the commitHash will be used
### Responses
**200**
OK
**400**
Bad Request
**500**
Internal Server Error
**503**
Edge compute features are disabled
get/edge_stacks/{id}/file
https://api-docs.portainer.io/api/edge_stacks/{id}/file
###  Response samples
  * 200


Content type
application/json
Copy
`{
  *  "StackFileContent": "string"

 }`
