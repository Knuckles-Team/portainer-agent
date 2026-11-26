##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/kubernetes/operation/UpdateKubernetesIngressControllers)Update (block/unblock) ingress controllers
Update (block/unblock) ingress controllers for the provided environment. **Access policy** : Authenticated user.
##### Authorizations:
(_ApiKeyAuth_ _jwt_)
##### path Parameters
idrequired |  integer Environment identifier
---|---
##### Request Body schema: application/json
required
Ingress controllers
Array
Availability |  boolean
---|---
ClassName |  string
Name |  string
New |  boolean
Type |  string
Used |  boolean
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
Unable to find an environment with the specified identifier or unable to find the ingress controllers to update.
**500**
Server error occurred while attempting to update ingress controllers.
put/kubernetes/{id}/ingresscontrollers
https://api-docs.portainer.io/api/kubernetes/{id}/ingresscontrollers
###  Request samples
  * Payload


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
