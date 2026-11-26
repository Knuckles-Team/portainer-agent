##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/docker/operation/dockerContainerGpusInspect)Fetch container gpus data
**Access policy** :
##### Authorizations:
_jwt_
##### path Parameters
environmentIdrequired |  integer Environment identifier
---|---
containerIdrequired |  integer Container identifier
### Responses
**200**
Success
**400**
Bad request
**404**
Environment or container not found
**500**
Internal server error
get/docker/{environmentId}/containers/{containerId}/gpus
https://api-docs.portainer.io/api/docker/{environmentId}/containers/{containerId}/gpus
###  Response samples
  * 200


Content type
application/json
Copy
`{
  *  "gpus": "string"

 }`
