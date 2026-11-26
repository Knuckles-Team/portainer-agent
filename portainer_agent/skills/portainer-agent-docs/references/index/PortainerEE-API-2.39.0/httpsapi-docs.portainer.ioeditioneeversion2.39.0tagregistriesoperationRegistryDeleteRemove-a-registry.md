##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/registries/operation/RegistryDelete)Remove a registry
Remove a registry **Access policy** : restricted
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### path Parameters
idrequired |  integer Registry identifier
---|---
### Responses
**204**
Success
**400**
Invalid request
**404**
Registry not found
**500**
Server error
delete/registries/{id}
https://api-docs.portainer.io/api/registries/{id}
