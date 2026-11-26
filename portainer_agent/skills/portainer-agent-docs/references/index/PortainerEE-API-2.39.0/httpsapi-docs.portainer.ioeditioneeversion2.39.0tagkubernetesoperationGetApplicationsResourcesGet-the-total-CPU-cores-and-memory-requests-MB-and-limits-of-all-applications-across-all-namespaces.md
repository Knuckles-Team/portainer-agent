##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/kubernetes/operation/GetApplicationsResources)Get the total CPU (cores) and memory requests (MB) and limits of all applications across all namespaces
Get the total CPU (cores) and memory (bytes) requests and limits of all applications across all namespaces. **Access policy** : authenticated
##### Authorizations:
(_ApiKeyAuth_ _jwt_)
##### path Parameters
idrequired |  integer Environment(Endpoint) identifier
---|---
##### query Parameters
noderequired |  string Node name
---|---
### Responses
**200**
Success
**400**
Invalid request
**401**
Unauthorized
**403**
Permission denied
**404**
Environment(Endpoint) not found
**500**
Server error
get/kubernetes/{id}/metrics/applications_resources
https://api-docs.portainer.io/api/kubernetes/{id}/metrics/applications_resources
###  Response samples
  * 200


Content type
application/json
Copy
`{

  *  "CpuLimit": 0,

  *  "CpuRequest": 0,

  *  "MemoryLimit": 0,

  *  "MemoryRequest": 0

 }`
