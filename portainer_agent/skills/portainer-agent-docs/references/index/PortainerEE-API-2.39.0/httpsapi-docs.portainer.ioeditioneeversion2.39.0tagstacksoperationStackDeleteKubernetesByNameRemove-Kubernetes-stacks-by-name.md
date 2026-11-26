##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/stacks/operation/StackDeleteKubernetesByName)Remove Kubernetes stacks by name
Remove a stack. **Access policy** : restricted
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### path Parameters
namerequired |  string Stack name
---|---
##### query Parameters
external |  boolean Set to true to delete an external stack. Only external Swarm stacks are supported
---|---
endpointIdrequired |  integer Environment identifier
### Responses
**204**
Success
**400**
Invalid request
**403**
Permission denied
**404**
Not found
**500**
Server error
delete/stacks/name/{name}
https://api-docs.portainer.io/api/stacks/name/{name}
