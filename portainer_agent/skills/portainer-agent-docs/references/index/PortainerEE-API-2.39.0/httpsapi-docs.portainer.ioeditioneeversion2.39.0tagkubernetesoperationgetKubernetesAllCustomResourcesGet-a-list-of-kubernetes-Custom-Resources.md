##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/kubernetes/operation/getKubernetesAllCustomResources)Get a list of kubernetes Custom Resources
Get a list of kubernetes Custom Resources that the user has access to. **Access policy** : Authenticated user.
##### Authorizations:
(_ApiKeyAuth_ _jwt_)
##### path Parameters
idrequired |  integer Environment identifier
---|---
##### query Parameters
definitionrequired |  string The CustomResourceDefinition name of the custom resource, e.g. 'clusters.postgresql.cnpg.io'
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
Server error occurred while attempting to retrieve the custom resources.
get/kubernetes/{id}/customresources
https://api-docs.portainer.io/api/kubernetes/{id}/customresources
###  Response samples
  * 200


Content type
application/json
Copy
Expand all  Collapse all
`[
  *  {
    *  "creationDate": "string",

    *  "definitionName": "string",

    *  "name": "string",

    *  "namespace": "string",

    *  "uid": "string"
  }

 ]`
