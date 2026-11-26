##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/kaas/operation/microk8sUpdateAddons)Get a list of addons which are installed in a MicroK8s cluster.
The information returned can be used to query the MircoK8s cluster. **Access policy** : authenticated
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### path Parameters
environmentIdrequired |  integer Environment(Endpoint) identifier
---|---
##### Request Body schema: application/json
required
The list of addons to install in the cluster.
addons |  Array of objects (portaineree.MicroK8sAddon)
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
post/cloud/endpoints/{environmentId}/addons
https://api-docs.portainer.io/api/cloud/endpoints/{environmentId}/addons
###  Request samples
  * Payload


Content type
application/json
Copy
Expand all  Collapse all
`{
  *  "addons": [
    *  {
      *  "arguments": "string",

      *  "name": "string",

      *  "repository": "string"
  }
 ]

 }`
