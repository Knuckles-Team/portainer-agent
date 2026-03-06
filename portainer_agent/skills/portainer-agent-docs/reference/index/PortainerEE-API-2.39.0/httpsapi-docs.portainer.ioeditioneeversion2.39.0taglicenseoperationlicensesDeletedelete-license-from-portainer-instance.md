##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/license/operation/licensesDelete)delete license from portainer instance
**Access policy** : administrator
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### Request Body schema: application/json
required
list of license keys to remove
LicenseKeys |  Array of strings List of license keys to remove
---|---
### Responses
**200**
OK
post/licenses/remove
https://api-docs.portainer.io/api/licenses/remove
###  Request samples
  * Payload


Content type
application/json
Copy
Expand all  Collapse all
`{
  *  "LicenseKeys": [
    * "string"
 ]

 }`
