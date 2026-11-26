##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/endpoints/paths/~1endpoints~1edge~1generate-key/post)Generate an EdgeKey
Generates a general edge key **Access policy** : admin
##### Request Body schema: application/json
required
Generate Key Info
edgeKey |  string
---|---
### Responses
**200**
OK
**400**
Bad Request
**500**
Internal Server Error
post/endpoints/edge/generate-key
https://api-docs.portainer.io/api/endpoints/edge/generate-key
###  Request samples
  * Payload


Content type
application/json
Copy
`{
  *  "edgeKey": "string"

 }`
