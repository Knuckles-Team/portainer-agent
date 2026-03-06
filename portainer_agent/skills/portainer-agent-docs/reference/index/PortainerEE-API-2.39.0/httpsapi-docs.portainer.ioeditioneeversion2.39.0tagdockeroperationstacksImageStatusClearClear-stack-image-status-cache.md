##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/docker/operation/stacksImageStatusClear)Clear stack image status cache
Clear the image status cache for all stacks in the environment **Access policy** :
##### Authorizations:
_jwt_
##### query Parameters
environmentId |  integer Identifier of the environment(endpoint) that will be used to filter the stacks to clear the image status cache for
---|---
swarmId |  string Identifier of the swarm cluster that will be used to filter the stacks to clear the image status cache for
### Responses
**204**
Success
**400**
Bad request
**500**
Internal server error
post/stacks/image_status/clear
https://api-docs.portainer.io/api/stacks/image_status/clear
