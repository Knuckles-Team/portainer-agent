##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/endpoints/operation/EndpointGetCharts)Get environment(endpoint) charts to install
environment(endpoint) for edge agent to get contents of requested Helm charts environment(endpoint) **Access policy** : restricted only to Edge environments(endpoints)
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### path Parameters
idrequired |  integer Environment(Endpoint) identifier
---|---
##### query Parameters
chartNames |  string JSON encoded list of charts to install
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
get/endpoints/{id}/edge/charts
https://api-docs.portainer.io/api/endpoints/{id}/edge/charts
