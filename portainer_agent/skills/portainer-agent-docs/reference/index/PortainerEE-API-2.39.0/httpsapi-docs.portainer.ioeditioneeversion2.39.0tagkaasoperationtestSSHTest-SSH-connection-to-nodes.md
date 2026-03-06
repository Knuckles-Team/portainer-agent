##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/kaas/operation/testSSH)Test SSH connection to nodes
Test SSH connection to nodes. **Access policy** : administrator
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### Request Body schema: application/json
required
Node IPs and credential ID
credentialIDrequired |  integer
---|---
nodeIPsrequired |  Array of strings
### Responses
**200**
Success
**400**
Invalid request
**500**
Server error
**503**
Missing configuration
post/cloud/testssh
https://api-docs.portainer.io/api/cloud/testssh
###  Request samples
  * Payload


Content type
application/json
Copy
Expand all  Collapse all
`{

  *  "credentialID": 1,

  *  "nodeIPs": [
    * "string"
 ]

 }`
###  Response samples
  * 200


Content type
application/json
Copy
Expand all  Collapse all
`[
  *  {
    *  "address": "string",

    *  "error": "string"
  }

 ]`
