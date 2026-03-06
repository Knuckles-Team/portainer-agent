##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/kubernetes/operation/DeleteKubernetesNamespace)Delete a kubernetes namespace
Delete a kubernetes namespace within the given environment. **Access policy** : Authenticated user.
##### Authorizations:
(_ApiKeyAuth_ _jwt_)
##### path Parameters
idrequired |  integer Environment identifier
---|---
### Responses
**200**
Success
**400**
Invalid request payload, such as missing required fields or fields not meeting validation criteria.
**403**
Unauthorized access or operation not allowed.
**500**
Server error occurred while attempting to delete the namespace.
delete/kubernetes/{id}/namespaces
https://api-docs.portainer.io/api/kubernetes/{id}/namespaces
