##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/kubernetes/operation/GetAllKubernetesIngressControllers)Get a list of ingress controllers
Get a list of ingress controllers for the given environment. If the allowedOnly query parameter is set, only ingress controllers that are allowed by the environment's ingress configuration will be returned. **Access policy** : Authenticated user.
##### Authorizations:
(_ApiKeyAuth_ _jwt_)
##### path Parameters
idrequired |  integer Environment identifier
---|---
##### query Parameters
allowedOnly |  boolean Only return allowed ingress controllers
---|---
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
Unable to find an environment with the specified identifier.
**500**
Server error occurred while attempting to retrieve ingress controllers
get/kubernetes/{id}/ingresscontrollers
https://api-docs.portainer.io/api/kubernetes/{id}/ingresscontrollers
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
