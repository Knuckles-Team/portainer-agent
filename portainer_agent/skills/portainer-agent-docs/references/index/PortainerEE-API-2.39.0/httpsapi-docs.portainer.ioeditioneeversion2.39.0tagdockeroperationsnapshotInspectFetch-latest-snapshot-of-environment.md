##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/docker/operation/snapshotInspect)Fetch latest snapshot of environment
**Access policy** :
##### Authorizations:
_jwt_
##### path Parameters
environmentIdrequired |  integer Environment identifier
---|---
### Responses
**200**
Success
**404**
Environment not found
get/docker/{environmentId}/snapshot
https://api-docs.portainer.io/api/docker/{environmentId}/snapshot
###  Response samples
  * 200


Content type
application/json
Copy
`{ }`
