##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/stacks/operation/StackFileInspect)Retrieve the content of the Stack file for the specified stack
Get Stack file content. **Access policy** : restricted
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### path Parameters
idrequired |  integer Stack identifier
---|---
##### query Parameters
version |  integer Stack file version maintained by Portainer. If both version and commitHash are provided, the commitHash will be used
---|---
commitHash |  string Git repository commit hash. If both version and commitHash are provided, the commitHash will be used
### Responses
**200**
Success
**400**
Invalid request
**403**
Permission denied
**404**
Stack not found
**500**
Server error
get/stacks/{id}/file
https://api-docs.portainer.io/api/stacks/{id}/file
###  Response samples
  * 200


Content type
application/json
Copy
`{
  *  "StackFileContent": "version: 3\n services:\n web:\n image:nginx"

 }`
