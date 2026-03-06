##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/kubernetes/operation/restartKubernetesApplication)Restart a Kubernetes application
Restart a Kubernetes deployment, statefulset and daemonset application, using a kubectl rollout-restart **Access policy** : authenticated
##### Authorizations:
(_ApiKeyAuth_ _jwt_)
##### path Parameters
idrequired |  integer Environment(Endpoint) identifier
---|---
namespacerequired |  string The namespace
kindrequired |  string deployment, statefulset or daemonset
namerequired |  string name of the application
### Responses
**204**
Success
**400**
Invalid request, such as missing required fields or fields not meeting validation criteria.
**401**
Unauthorized access - the user is not authenticated or does not have the necessary permissions. Ensure that you have provided a valid API key or JWT token, and that you have the required permissions.
**403**
Permission denied - the user is authenticated but does not have the necessary permissions to access the requested resource or perform the specified operation. Check your user roles and permissions.
**404**
Unable to find an environment with the specified identifier or unable to find a specific application.
**500**
Server error occurred while attempting to restart application.
post/kubernetes/{id}/namespaces/{namespace}/applications/{kind}/{name}/restart
https://api-docs.portainer.io/api/kubernetes/{id}/namespaces/{namespace}/applications/{kind}/{name}/restart
