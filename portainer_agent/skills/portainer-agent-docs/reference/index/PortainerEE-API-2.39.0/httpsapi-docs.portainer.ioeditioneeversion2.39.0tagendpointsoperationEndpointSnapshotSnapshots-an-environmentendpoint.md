##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/endpoints/operation/EndpointSnapshot)Snapshots an environment(endpoint)
Snapshots an environment(endpoint) **Access policy** : authenticated
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
**404**
Environment(Endpoint) not found
**500**
Server error
post/endpoints/{id}/snapshot
https://api-docs.portainer.io/api/endpoints/{id}/snapshot
