##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/kaas/operation/kaasVersion)Get the current cluster version.
Get the current cluster version. **Access policy** : authenticated
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### path Parameters
environmentIdrequired |  integer Environment(Endpoint) identifier
---|---
### Responses
**200**
Success
**400**
Invalid request
**403**
Permission denied
**500**
Server error
**503**
Missing configuration
get/cloud/endpoints/{environmentId}/version
https://api-docs.portainer.io/api/cloud/endpoints/{environmentId}/version
