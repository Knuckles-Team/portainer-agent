##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/kubernetes/operation/CreateKubernetesIngress)Create an Ingress
Create an Ingress for the provided environment. **Access policy** : Authenticated user.
##### Authorizations:
(_ApiKeyAuth_ _jwt_)
##### path Parameters
idrequired |  integer Environment identifier
---|---
namespacerequired |  string Namespace name
##### Request Body schema: application/json
required
Ingress details
Annotations |  object
---|---
ClassName |  string
CreationDate |  string
Hosts |  Array of strings
Labels |  object
Name |  string
Namespace |  string
Paths |  Array of objects (models.K8sIngressPath)
TLS |  Array of objects (models.K8sIngressTLS)
Type |  string
UID |  string
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
Unable to find an environment with the specified identifier.
**409**
Conflict - an ingress with the same name already exists in the specified namespace.
**500**
Server error occurred while attempting to create an ingress.
post/kubernetes/{id}/namespaces/{namespace}/ingresses
https://api-docs.portainer.io/api/kubernetes/{id}/namespaces/{namespace}/ingresses
###  Request samples
  * Payload


Content type
application/json
Copy
Expand all  Collapse all
`{

  *  "Annotations": {
    *  "property1": "string",

    *  "property2": "string"
  },

  *  "ClassName": "string",

  *  "CreationDate": "string",

  *  "Hosts": [
    * "string"
 ],

  *  "Labels": {
    *  "property1": "string",

    *  "property2": "string"
  },

  *  "Name": "string",

  *  "Namespace": "string",

  *  "Paths": [
    *  {
      *  "HasService": true,

      *  "Host": "string",

      *  "IngressName": "string",

      *  "Path": "string",

      *  "PathType": "string",

      *  "Port": 0,

      *  "ServiceName": "string"
  }
 ],

  *  "TLS": [
    *  {
      *  "Hosts": [
        * "string"
 ],

      *  "SecretName": "string"
  }
 ],

  *  "Type": "string",

  *  "UID": "string"

 }`
