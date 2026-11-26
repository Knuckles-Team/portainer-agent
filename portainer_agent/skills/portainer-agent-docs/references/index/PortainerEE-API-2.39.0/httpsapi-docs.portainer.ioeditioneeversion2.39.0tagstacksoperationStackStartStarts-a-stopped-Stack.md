##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/stacks/operation/StackStart)Starts a stopped Stack
Starts a stopped Stack. **Access policy** : authenticated
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
**409**
Stack name is not unique
**500**
Server error
post/stacks/{id}/start
https://api-docs.portainer.io/api/stacks/{id}/start
