##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/kubernetes/operation/DeleteClusterRoleBindings)Delete cluster role bindings
Delete the provided list of cluster role bindings. **Access policy** : Authenticated user.
##### Authorizations:
(_ApiKeyAuth_ _jwt_)
##### path Parameters
idrequired |  integer Environment identifier
---|---
##### Request Body schema: application/json
required
A list of cluster role bindings to delete
Array
string
### Responses
**204**
Success
**400**
Invalid request payload, such as missing required fields or fields not meeting validation criteria.
**401**
Unauthorized access - the user is not authenticated or does not have the necessary permissions. Ensure that you have provided a valid API key or JWT token, and that you have the required permissions.
**403**
Permission denied - the user is authenticated but does not have the necessary permissions to access the requested resource or perform the specified operation. Check your user roles and permissions.
**404**
Unable to find an environment with the specified identifier or unable to find a specific cluster role binding.
**500**
Server error occurred while attempting to delete cluster role bindings.
post/kubernetes/{id}/cluster_role_bindings/delete
https://api-docs.portainer.io/api/kubernetes/{id}/cluster_role_bindings/delete
###  Request samples
  * Payload


Content type
application/json
Copy
`[
  * "string"

 ]`
