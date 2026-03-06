##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/kubernetes/operation/deleteKubernetesClusterScopedCustomResource)Delete a cluster-scoped kubernetes Custom Resource
Delete a cluster-scoped kubernetes Custom Resource that the user has access to. **Access policy** : Authenticated user.
##### Authorizations:
(_ApiKeyAuth_ _jwt_)
##### path Parameters
idrequired |  integer Environment identifier
---|---
namerequired |  string The name of the custom resource, e.g. 'pg-cluster'
##### query Parameters
definitionrequired |  string The CustomResourceDefinition name of the custom resource, e.g. 'clusters.postgresql.cnpg.io'
---|---
### Responses
**204**
No Content
**400**
Invalid request payload, such as missing required fields or fields not meeting validation criteria.
**401**
Unauthorized access - the user is not authenticated or does not have the necessary permissions. Ensure that you have provided a valid API key or JWT token, and that you have the required permissions.
**403**
Permission denied - the user is authenticated but does not have the necessary permissions to access the requested resource or perform the specified operation. Check your user roles and permissions.
**404**
Unable to find an environment with the specified identifier.
**500**
Server error occurred while attempting to delete the custom resource.
delete/kubernetes/{id}/customresources/{name}
https://api-docs.portainer.io/api/kubernetes/{id}/customresources/{name}
