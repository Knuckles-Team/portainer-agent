##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/endpoints/operation/endpointEdgeAsync)Get environment(endpoint) status
Environment(Endpoint) for edge agent to check status of environment(endpoint) **Access policy** : restricted only to Edge environments(endpoints)
##### Authorizations:
_ApiKeyAuth_ _jwt_
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
post/endpoints/edge/async
https://api-docs.portainer.io/api/endpoints/edge/async
