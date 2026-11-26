##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/kubernetes/operation/GetKubernetesRBACStatus)Check if RBAC is enabled
Check if RBAC is enabled in the specified Kubernetes cluster. **Access policy** : Authenticated user.
##### Authorizations:
(_ApiKeyAuth_ _jwt_)
##### path Parameters
idrequired |  integer Environment(Endpoint) identifier
---|---
### Responses
**200**
RBAC status
**401**
Unauthorized access - the user is not authenticated or does not have the necessary permissions. Ensure that you have provided a valid API key or JWT token, and that you have the required permissions.
**403**
Permission denied - the user is authenticated but does not have the necessary permissions to access the requested resource or perform the specified operation. Check your user roles and permissions.
**404**
Unable to find an environment with the specified identifier.
**500**
Server error occurred while attempting to retrieve the RBAC status.
get/kubernetes/{id}/rbac_enabled
https://api-docs.portainer.io/api/kubernetes/{id}/rbac_enabled
###  Response samples
  * 200


Content type
application/json
Copy
`true`
