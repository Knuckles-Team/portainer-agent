##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/webhooks/paths/~1webhooks/post)Create a webhook
**Access policy** : authenticated
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### Request Body schema: application/json
required
Webhook data
EndpointID |  integer
---|---
RegistryID |  integer
ResourceID |  string
WebhookType |  integer Enum: 0 1 Type of webhook (1 - service, 2 - container)
### Responses
**200**
OK
**400**
Invalid request
**409**
A webhook for this resource already exists
**500**
Server error
post/webhooks
https://api-docs.portainer.io/api/webhooks
###  Request samples
  * Payload


Content type
application/json
Copy
`{

  *  "EndpointID": 0,

  *  "RegistryID": 0,

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
