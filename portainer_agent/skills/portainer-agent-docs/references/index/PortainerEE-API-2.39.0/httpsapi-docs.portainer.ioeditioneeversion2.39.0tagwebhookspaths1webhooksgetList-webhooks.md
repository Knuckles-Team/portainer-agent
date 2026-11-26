##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/webhooks/paths/~1webhooks/get)List webhooks
**Access policy** : authenticated
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### query Parameters
filters |  string Example:  filters={"EndpointID":1,"ResourceID":"abc12345-abcd-2345-ab12-58005b4a0260"} Filters (json-string)
---|---
### Responses
**200**
OK
**400**
Bad Request
**500**
Internal Server Error
get/webhooks
https://api-docs.portainer.io/api/webhooks
###  Response samples
  * 200


Content type
application/json
Copy
Expand all  Collapse all
`[
  *  {
    *  "EndpointId": 0,

    *  "Id": 1,

    *  "RegistryId": 0,

    *  "ResourceId": "string",

    *  "Token": "string",

    *  "Type": 0
  }

 ]`
