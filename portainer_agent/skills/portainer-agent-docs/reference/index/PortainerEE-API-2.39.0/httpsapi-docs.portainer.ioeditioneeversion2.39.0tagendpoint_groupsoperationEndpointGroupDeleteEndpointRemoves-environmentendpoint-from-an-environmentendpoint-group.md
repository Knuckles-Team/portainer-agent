##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/endpoint_groups/operation/EndpointGroupDeleteEndpoint)Removes environment(endpoint) from an environment(endpoint) group
**Access policy** : administrator
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### path Parameters
idrequired |  integer EndpointGroup identifier
---|---
endpointIdrequired |  integer Environment(Endpoint) identifier
### Responses
**204**
Success
**400**
Invalid request
**404**
EndpointGroup not found
**500**
Server error
delete/endpoint_groups/{id}/endpoints/{endpointId}
https://api-docs.portainer.io/api/endpoint_groups/{id}/endpoints/{endpointId}
