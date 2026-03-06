##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/stacks/operation/StackDelete)Remove a stack
Remove a stack. **Access policy** : restricted
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### path Parameters
idrequired |  integer Stack identifier
---|---
##### query Parameters
external |  boolean Set to true to delete an external stack. Only external Swarm stacks are supported
---|---
removeVolumes |  boolean Set to true to delete named volumes declared in the stack file and anonymous volumes attached to containers. Only affects Docker Standalone stacks.
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
delete/stacks/{id}
https://api-docs.portainer.io/api/stacks/{id}
