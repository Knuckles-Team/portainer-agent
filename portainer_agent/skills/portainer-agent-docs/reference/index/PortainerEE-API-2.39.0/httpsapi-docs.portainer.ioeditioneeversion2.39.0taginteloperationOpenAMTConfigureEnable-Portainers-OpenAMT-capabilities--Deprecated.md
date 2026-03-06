##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/intel/operation/OpenAMTConfigure)Enable Portainer's OpenAMT capabilities  Deprecated
Enable Portainer's OpenAMT capabilities **Access policy** : administrator
##### Authorizations:
_jwt_
##### Request Body schema: application/json
required
OpenAMT Settings
CertFileContent |  string
---|---
CertFileName |  string
CertFilePassword |  string
DomainName |  string
Enabled |  boolean
MPSPassword |  string
MPSServer |  string
MPSUser |  string
### Responses
**204**
Success
**400**
Invalid request
**403**
Permission denied to access settings
**500**
Server error
post/open_amt
https://api-docs.portainer.io/api/open_amt
###  Request samples
  * Payload


Content type
application/json
Copy
`{

  *  "CertFileContent": "string",

  *  "CertFileName": "string",

  *  "CertFilePassword": "string",

  *  "DomainName": "string",

  *  "Enabled": true,

  *  "MPSPassword": "string",

  *  "MPSServer": "string",

  *  "MPSUser": "string"

 }`
