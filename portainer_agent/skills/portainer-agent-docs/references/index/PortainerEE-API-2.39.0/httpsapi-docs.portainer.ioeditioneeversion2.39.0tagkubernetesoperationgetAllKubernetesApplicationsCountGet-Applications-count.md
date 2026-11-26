##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/kubernetes/operation/getAllKubernetesApplicationsCount)Get Applications count
Get the count of Applications across all namespaces in the cluster. If the nodeName is provided, it will return the count of applications running on that node. **Access policy** : Authenticated user.
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
**403**
Unauthorized access or operation not allowed.
**500**
Server error occurred while attempting to retrieve the count of all applications from the cluster.
get/kubernetes/{id}/applications/count
https://api-docs.portainer.io/api/kubernetes/{id}/applications/count
###  Response samples
  * 200


Content type
application/json
Copy
0
`0`
