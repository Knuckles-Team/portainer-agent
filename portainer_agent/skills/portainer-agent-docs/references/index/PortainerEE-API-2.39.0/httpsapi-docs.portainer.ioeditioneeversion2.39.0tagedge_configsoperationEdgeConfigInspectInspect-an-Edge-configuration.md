##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/edge_configs/operation/EdgeConfigInspect)Inspect an Edge configuration
Retrieve details about an Edge configuration. **Access policy** : authenticated
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### path Parameters
idrequired |  integer Edge configuration identifier
---|---
### Responses
**200**
Success
**400**
Invalid request
**404**
Edge configuration not found
**500**
Server error
get/edge_configurations/{id}
https://api-docs.portainer.io/api/edge_configurations/{id}
