##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/endpoint_groups/operation/EndpointGroupDelete)Remove an environment(endpoint) group
Remove an environment(endpoint) group. **Access policy** : administrator
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### path Parameters
idrequired |  integer EndpointGroup identifier
---|---
### Responses
**204**
Success
**400**
Invalid request
**404**
EndpointGroup not found
**500**
Server error
delete/endpoint_groups/{id}
https://api-docs.portainer.io/api/endpoint_groups/{id}
