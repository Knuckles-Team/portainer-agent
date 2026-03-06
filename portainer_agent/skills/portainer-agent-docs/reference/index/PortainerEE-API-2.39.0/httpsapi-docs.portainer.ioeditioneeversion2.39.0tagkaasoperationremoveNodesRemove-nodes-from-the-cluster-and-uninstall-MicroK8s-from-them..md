##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/kaas/operation/removeNodes)Remove nodes from the cluster and uninstall MicroK8s from them.
Remove nodes from the cluster and uninstall MicroK8s from them. **Access policy** : authenticated
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
post/cloud/endpoints/{environmentId}/nodes/remove
https://api-docs.portainer.io/api/cloud/endpoints/{environmentId}/nodes/remove
