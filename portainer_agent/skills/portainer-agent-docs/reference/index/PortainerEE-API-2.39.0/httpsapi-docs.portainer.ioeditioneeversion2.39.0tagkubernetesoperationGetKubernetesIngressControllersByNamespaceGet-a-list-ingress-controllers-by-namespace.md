##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/kubernetes/operation/GetKubernetesIngressControllersByNamespace)Get a list ingress controllers by namespace
Get a list of ingress controllers for the given environment in the provided namespace. **Access policy** : Authenticated user.
##### Authorizations:
(_ApiKeyAuth_ _jwt_)
##### path Parameters
idrequired |  integer Environment identifier
---|---
namespacerequired |  string Namespace
### Responses
**200**
Success
**400**
Invalid request payload, such as missing required fields or fields not meeting validation criteria.
**401**
Unauthorized access - the user is not authenticated or does not have the necessary permissions. Ensure that you have provided a valid API key or JWT token, and that you have the required permissions.
**403**
Permission denied - the user is authenticated but does not have the necessary permissions to access the requested resource or perform the specified operation. Check your user roles and permissions.
**404**
Unable to find an environment with the specified identifier or a namespace with the specified name.
**500**
Server error occurred while attempting to retrieve ingress controllers by a namespace
get/kubernetes/{id}/namespaces/{namespace}/ingresscontrollers
https://api-docs.portainer.io/api/kubernetes/{id}/namespaces/{namespace}/ingresscontrollers
###  Response samples
  * 200


Content type
application/json
Copy
Expand all  Collapse all
`[
  *  {
    *  "Availability": true,

    *  "ClassName": "string",

    *  "Name": "string",

    *  "New": true,

    *  "Type": "string",

    *  "Used": true
  }

 ]`
