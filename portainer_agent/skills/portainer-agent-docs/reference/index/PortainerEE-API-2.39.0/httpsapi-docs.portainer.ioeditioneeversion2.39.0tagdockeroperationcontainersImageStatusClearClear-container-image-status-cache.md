##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/docker/operation/containersImageStatusClear)Clear container image status cache
Clear the image status cache for all containers in the environment **Access policy** :
##### Authorizations:
_jwt_
##### path Parameters
environmentIdrequired |  integer Environment identifier
---|---
### Responses
**204**
Success
**400**
Bad request
**500**
Internal server error
post/docker/{environmentId}/containers/image_status/clear
https://api-docs.portainer.io/api/docker/{environmentId}/containers/image_status/clear
