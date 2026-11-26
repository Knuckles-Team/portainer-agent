##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/ssl/operation/SSLInspect)Inspect the ssl settings
Retrieve the ssl settings. **Access policy** : administrator
##### Authorizations:
_ApiKeyAuth_ _jwt_
### Responses
**200**
Success
**400**
Invalid request
**403**
Permission denied to access settings
**500**
Server error
get/ssl
https://api-docs.portainer.io/api/ssl
###  Response samples
  * 200


Content type
application/json
Copy
`{

  *  "caCertPath": "string",

  *  "certPath": "string",

  *  "httpEnabled": true,

  *  "keyPath": "string",

  *  "selfSigned": true

 }`
