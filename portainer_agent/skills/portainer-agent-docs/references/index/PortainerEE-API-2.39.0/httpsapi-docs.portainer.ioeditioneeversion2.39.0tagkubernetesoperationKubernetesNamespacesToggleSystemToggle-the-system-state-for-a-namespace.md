##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/kubernetes/operation/KubernetesNamespacesToggleSystem)Toggle the system state for a namespace
Toggle the system state for a namespace **Access policy** : Administrator or environment administrator.
##### Authorizations:
(_ApiKeyAuth_ _jwt_)
##### path Parameters
idrequired |  integer Environment identifier
---|---
namespacerequired |  string Namespace name
##### Request Body schema: application/json
required
Update details
System |  boolean Toggle the system state of this namespace to true or false
---|---
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
Unable to find an environment with the specified identifier or unable to find the namespace to update.
**500**
Server error occurred while attempting to update the system state of the namespace.
put/kubernetes/{id}/namespaces/{namespace}/system
https://api-docs.portainer.io/api/kubernetes/{id}/namespaces/{namespace}/system
###  Request samples
  * Payload


Content type
application/json
Copy
`{
  *  "System": true

 }`
