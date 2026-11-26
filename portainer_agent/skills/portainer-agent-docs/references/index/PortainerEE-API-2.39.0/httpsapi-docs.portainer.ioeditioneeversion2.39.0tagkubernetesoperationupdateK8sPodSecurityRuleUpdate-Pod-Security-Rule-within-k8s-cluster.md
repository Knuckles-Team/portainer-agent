##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/kubernetes/operation/updateK8sPodSecurityRule)Update Pod Security Rule within k8s cluster
Update Pod Security Rule within k8s cluster **Access policy** : authenticated
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
**404**
Pod Security Rule not found
**500**
Server error
put/kubernetes/{environmentId}/opa
https://api-docs.portainer.io/api/kubernetes/{environmentId}/opa
