##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/license/operation/licensesAttach)attaches a list of licenses to Portainer
**Access policy** : administrator
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### query Parameters
force |  boolean remove conflicting licenses
---|---
##### Request Body schema: application/json
required
list of licenses keys to attach
key |  string
---|---
### Responses
**200**
Success license data will be in `body.Licenses`, Failures will be in `body.ConflictingKeys = error`
post/licenses/add
https://api-docs.portainer.io/api/licenses/add
###  Request samples
  * Payload


Content type
application/json
Copy
`{
  *  "key": "string"

 }`
###  Response samples
  * 200


Content type
application/json
Copy
Expand all  Collapse all
`{
  *  "conflictingKeys": [
    * "string"
 ]

 }`
