##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/kubernetes/operation/GetKubernetesMaxResourceLimits)Get max CPU and memory limits of all nodes within k8s cluster
Get max CPU and memory limits (unused resources) of all nodes within k8s cluster. **Access policy** : Authenticated user.
##### Authorizations:
(_ApiKeyAuth_ _jwt_)
##### path Parameters
idrequired |  integer Environment(Endpoint) identifier
---|---
### Responses
**200**
Success
**400**
Invalid request
**401**
Unauthorized access - the user is not authenticated or does not have the necessary permissions. Ensure that you have provided a valid API key or JWT token, and that you have the required permissions.
**403**
Permission denied - the user is authenticated but does not have the necessary permissions to access the requested resource or perform the specified operation. Check your user roles and permissions.
**404**
Unable to find an environment with the specified identifier.
**500**
Server error occurred while attempting to retrieve nodes limits.
get/kubernetes/{id}/max_resource_limits
https://api-docs.portainer.io/api/kubernetes/{id}/max_resource_limits
###  Response samples
  * 200


Content type
application/json
Copy
Expand all  Collapse all
`{

  *  "property1": {
    *  "CPU": 0,

    *  "Memory": 0
  },

  *  "property2": {
    *  "CPU": 0,

    *  "Memory": 0
  }

 }`
