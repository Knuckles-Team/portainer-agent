##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/license/operation/licensesList)fetches the list of licenses on Portainer
**Access policy** : administrator
##### Authorizations:
_ApiKeyAuth_ _jwt_
### Responses
**200**
Licenses
get/licenses
https://api-docs.portainer.io/api/licenses
###  Response samples
  * 200


Content type
application/json
Copy
Expand all  Collapse all
`[
  *  {
    *  "company": "string",

    *  "created": 0,

    *  "email": "string",

    *  "expiresAfter": 0,

    *  "expiresAt": 0,

    *  "firstCheckin": 0,

    *  "id": "string",

    *  "lastCheckin": 0,

    *  "licenseKey": "string",

    *  "multiCheckinCount": 0,

    *  "multiuseInstancesCount": 0,

    *  "nodes": 0,

    *  "productEdition": 0,

    *  "redisRef": "string",

    *  "reference": "string",

    *  "revoked": true,

    *  "revokedAt": 0,

    *  "type": 0,

    *  "uniqueId": "string",

    *  "version": 0
  }

 ]`
