##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/webhooks/paths/~1webhooks~1{id}~1reassign/put)Reassign a webhook to another resource
**Access policy** : authenticated
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### path Parameters
idrequired |  integer Webhook id
---|---
##### Request Body schema: application/json
required
Webhook data
ResourceID |  string
---|---
WebhookType |  integer Enum: 0 1 Type of webhook (1 - service, 2 - container)
### Responses
**200**
OK
**204**
No Content
**400**
Bad Request
**404**
Not Found
**500**
Internal Server Error
put/webhooks/{id}/reassign
https://api-docs.portainer.io/api/webhooks/{id}/reassign
###  Request samples
  * Payload


Content type
application/json
Copy
`{

  *  "ResourceID": "string",

  *  "WebhookType": 0

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
