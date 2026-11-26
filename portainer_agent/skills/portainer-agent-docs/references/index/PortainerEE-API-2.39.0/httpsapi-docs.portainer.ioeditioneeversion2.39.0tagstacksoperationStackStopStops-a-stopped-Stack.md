##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/stacks/operation/StackStop)Stops a stopped Stack
Stops a stopped Stack. **Access policy** : authenticated
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### path Parameters
idrequired |  integer Stack identifier
---|---
##### query Parameters
endpointIdrequired |  integer Environment identifier
---|---
### Responses
**200**
Success
**400**
Invalid request
**403**
Permission denied
**404**
Not found
**500**
Server error
post/stacks/{id}/stop
https://api-docs.portainer.io/api/stacks/{id}/stop
