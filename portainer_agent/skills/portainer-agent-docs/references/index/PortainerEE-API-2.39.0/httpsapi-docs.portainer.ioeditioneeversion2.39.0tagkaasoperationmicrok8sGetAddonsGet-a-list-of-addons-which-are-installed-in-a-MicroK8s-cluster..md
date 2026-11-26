##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/kaas/operation/microk8sGetAddons)Get a list of addons which are installed in a MicroK8s cluster.
The information returned can be used to query the MircoK8s cluster. **Access policy** : authenticated
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
get/cloud/endpoints/{environmentId}/addons
https://api-docs.portainer.io/api/cloud/endpoints/{environmentId}/addons
