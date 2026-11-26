##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/kubernetes/operation/GetKubernetesConfigMap)Get a ConfigMap
Get a ConfigMap by name for a given namespace. **Access policy** : Authenticated user.
##### Authorizations:
(_ApiKeyAuth_ _jwt_)
##### path Parameters
idrequired |  integer Environment identifier
---|---
namespacerequired |  string The namespace name where the configmap is located
configmaprequired |  string The configmap name to get details for
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
Unable to find an environment with the specified identifier or a configmap with the specified name in the given namespace.
**500**
Server error occurred while attempting to retrieve a configmap by name within the specified namespace.
get/kubernetes/{id}/namespaces/{namespace}/configmaps/{configmap}
https://api-docs.portainer.io/api/kubernetes/{id}/namespaces/{namespace}/configmaps/{configmap}
###  Response samples
  * 200


Content type
application/json
Copy
Expand all  Collapse all
`{

  *  "Annotations": {
    *  "property1": "string",

    *  "property2": "string"
  },

  *  "ConfigurationOwner": "string",

  *  "ConfigurationOwnerId": "string",

  *  "ConfigurationOwners": [
    *  {
      *  "Id": "string",

      *  "Name": "string",

      *  "ResourceKind": "string"
  }
 ],

  *  "CreationDate": "string",

  *  "Data": {
    *  "property1": "string",

    *  "property2": "string"
  },

  *  "IsUsed": true,

  *  "Labels": {
    *  "property1": "string",

    *  "property2": "string"
  },

  *  "Name": "string",

  *  "Namespace": "string",

  *  "UID": "string"

 }`
