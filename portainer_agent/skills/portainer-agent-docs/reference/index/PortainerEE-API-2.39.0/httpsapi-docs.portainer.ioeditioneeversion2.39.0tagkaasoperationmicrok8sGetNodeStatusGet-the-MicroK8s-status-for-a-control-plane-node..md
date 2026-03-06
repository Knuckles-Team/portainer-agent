##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/kaas/operation/microk8sGetNodeStatus)Get the MicroK8s status for a control plane node.
Get the MicroK8s status for a control plane node in a MicroK8s cluster. **Access policy** : authenticated
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### path Parameters
environmentIdrequired |  integer Environment(Endpoint) identifier
---|---
##### query Parameters
nodeIPrequired |  string The external node ip of the control plane node.
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
get/cloud/endpoints/{environmentId}/nodes/nodestatus
https://api-docs.portainer.io/api/cloud/endpoints/{environmentId}/nodes/nodestatus
