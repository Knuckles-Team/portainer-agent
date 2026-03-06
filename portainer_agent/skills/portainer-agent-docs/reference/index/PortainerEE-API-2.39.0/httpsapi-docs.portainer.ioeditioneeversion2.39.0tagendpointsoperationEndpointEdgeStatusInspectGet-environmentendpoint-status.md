##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/endpoints/operation/EndpointEdgeStatusInspect)Get environment(endpoint) status
environment(endpoint) for edge agent to check status of environment(endpoint) **Access policy** : restricted only to Edge environments(endpoints)
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### path Parameters
idrequired |  integer Environment(Endpoint) identifier
---|---
### Responses
**200**
Success
**400**
Invalid request
**403**
Permission denied to access environment(endpoint)
**404**
Environment(Endpoint) not found
**500**
Server error
get/endpoints/{id}/edge/status
https://api-docs.portainer.io/api/endpoints/{id}/edge/status
