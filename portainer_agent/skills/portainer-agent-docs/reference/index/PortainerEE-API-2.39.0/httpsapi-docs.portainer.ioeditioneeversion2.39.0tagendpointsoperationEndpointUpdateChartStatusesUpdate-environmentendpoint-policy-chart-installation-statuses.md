##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/endpoints/operation/EndpointUpdateChartStatuses)Update environment(endpoint) policy chart installation statuses
environment(endpoint) for edge agent to report back installation statuses of Helm charts **Access policy** : restricted only to Edge environments(endpoints)
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### path Parameters
idrequired |  integer Environment(Endpoint) identifier
---|---
### Responses
**204**
Success
**400**
Invalid request
**403**
Permission denied to access environment(endpoint)
**404**
Environment(Endpoint) not found
**500**
Server error
put/endpoints/{id}/edge/charts/statuses
https://api-docs.portainer.io/api/endpoints/{id}/edge/charts/statuses
