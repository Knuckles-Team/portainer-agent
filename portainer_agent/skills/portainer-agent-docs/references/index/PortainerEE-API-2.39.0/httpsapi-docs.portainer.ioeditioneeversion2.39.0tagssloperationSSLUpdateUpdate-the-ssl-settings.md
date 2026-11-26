##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/ssl/operation/SSLUpdate)Update the ssl settings
Update the ssl settings. **Access policy** : administrator
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### Request Body schema: application/json
required
SSL Settings
Cert |  string SSL Certificates
---|---
HTTPEnabled |  boolean
Key |  string
clientCert |  string SSL Client Certificates
### Responses
**204**
Success
**400**
Invalid request
**403**
Permission denied to access settings
**500**
Server error
put/ssl
https://api-docs.portainer.io/api/ssl
###  Request samples
  * Payload


Content type
application/json
Copy
`{

  *  "Cert": "string",

  *  "HTTPEnabled": true,

  *  "Key": "string",

  *  "clientCert": "string"

 }`
