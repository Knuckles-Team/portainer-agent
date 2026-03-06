##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/kubernetes/operation/DeleteClusterRoles)Delete cluster roles
Delete the provided list of cluster roles. **Access policy** : Authenticated user.
##### Authorizations:
(_ApiKeyAuth_ _jwt_)
##### path Parameters
idrequired |  integer Environment identifier
---|---
##### Request Body schema: application/json
required
A list of cluster roles to delete
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
Unable to find an environment with the specified identifier or unable to find a specific cluster role.
**500**
Server error occurred while attempting to delete cluster roles.
post/kubernetes/{id}/cluster_roles/delete
https://api-docs.portainer.io/api/kubernetes/{id}/cluster_roles/delete
###  Request samples
  * Payload


Content type
application/json
Copy
`[
  * "string"

 ]`
