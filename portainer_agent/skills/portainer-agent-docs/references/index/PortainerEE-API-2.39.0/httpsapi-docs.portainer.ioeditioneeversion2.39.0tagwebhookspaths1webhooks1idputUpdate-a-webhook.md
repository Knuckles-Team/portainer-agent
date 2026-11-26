##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/webhooks/paths/~1webhooks~1{id}/put)Update a webhook
**Access policy** : authenticated
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### path Parameters
idrequired |  integer Webhook id
---|---
##### Request Body schema: application/json
required
Webhook data
RegistryID |  integer
---|---
### Responses
**200**
OK
**400**
Bad Request
**409**
Conflict
**500**
Internal Server Error
put/webhooks/{id}
https://api-docs.portainer.io/api/webhooks/{id}
###  Request samples
  * Payload


Content type
application/json
Copy
`{
  *  "RegistryID": 0

 }`
###  Response samples
  * 200


Content type
application/json
Copy
`{

  *  "EndpointId": 0,

  *  "Id": 1,

  *  "RegistryId": 0,

  *  "ResourceId": "string",

  *  "Token": "string",

  *  "Type": 0

 }`
