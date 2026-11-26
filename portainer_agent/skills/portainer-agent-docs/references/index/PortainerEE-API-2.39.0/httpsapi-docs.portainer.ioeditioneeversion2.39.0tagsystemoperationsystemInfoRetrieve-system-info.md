##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/system/operation/systemInfo)Retrieve system info
**Access policy** : authenticated
##### Authorizations:
_ApiKeyAuth_ _jwt_
### Responses
**200**
Success
**500**
Server error
get/system/info
https://api-docs.portainer.io/api/system/info
###  Response samples
  * 200


Content type
application/json
Copy
`{

  *  "agents": 0,

  *  "edgeAgents": 0,

  *  "edgeDevices": 0,

  *  "platform": "Docker"

 }`
