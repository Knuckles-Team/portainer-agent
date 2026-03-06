##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/kubernetes/operation/GetAllKubernetesClusterRoleBindings)Get a list of kubernetes cluster role bindings
Get a list of kubernetes cluster role bindings within the given environment at the cluster level. **Access policy** : Authenticated user.
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
**401**
Unauthorized access - the user is not authenticated or does not have the necessary permissions. Ensure that you have provided a valid API key or JWT token, and that you have the required permissions.
**403**
Permission denied - the user is authenticated but does not have the necessary permissions to access the requested resource or perform the specified operation. Check your user roles and permissions.
**404**
Unable to find an environment with the specified identifier.
**500**
Server error occurred while attempting to retrieve the list of cluster role bindings.
get/kubernetes/{id}/clusterrolebindings
https://api-docs.portainer.io/api/kubernetes/{id}/clusterrolebindings
###  Response samples
  * 200


Content type
application/json
Copy
Expand all  Collapse all
`[
  *  {
    *  "creationDate": "string",

    *  "isSystem": true,

    *  "name": "string",

    *  "namespace": "string",

    *  "roleRef": {
      *  "apiGroup": "string",

      *  "kind": "string",

      *  "name": "string"
  },

    *  "subjects": [
      *  {
        *  "apiGroup": "string",

        *  "kind": "string",

        *  "name": "string",

        *  "namespace": "string"
  }
 ],

    *  "uid": "string"
  }

 ]`
