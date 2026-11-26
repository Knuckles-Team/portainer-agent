##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/license/operation/licensesInfo)summarizes licenses on Portainer
**Access policy** : administrator
##### Authorizations:
_ApiKeyAuth_ _jwt_
### Responses
**200**
License info
get/licenses/info
https://api-docs.portainer.io/api/licenses/info
###  Response samples
  * 200


Content type
application/json
Copy
`{

  *  "company": "string",

  *  "enforcedAt": 0,

  *  "expiresAt": 0,

  *  "nodes": 0,

  *  "overuseStartedTimestamp": 0,

  *  "type": 0,

  *  "valid": true

 }`
