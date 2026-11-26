##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/helm/operation/HelmDelete)Delete Helm Release
**Access policy** : authenticated
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### path Parameters
idrequired |  integer Environment(Endpoint) identifier
---|---
releaserequired |  string The name of the release/application to uninstall
##### query Parameters
namespace |  string An optional namespace
---|---
### Responses
**204**
Success
**400**
Invalid environment(endpoint) id or bad request
**401**
Unauthorized
**404**
Environment(Endpoint) or ServiceAccount not found
**500**
Server error or helm error
delete/endpoints/{id}/kubernetes/helm/{release}
https://api-docs.portainer.io/api/endpoints/{id}/kubernetes/helm/{release}
