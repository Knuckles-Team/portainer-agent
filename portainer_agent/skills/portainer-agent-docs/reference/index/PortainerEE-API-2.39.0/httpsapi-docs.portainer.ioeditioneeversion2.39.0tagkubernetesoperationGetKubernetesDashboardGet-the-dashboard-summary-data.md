##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/kubernetes/operation/GetKubernetesDashboard)Get the dashboard summary data
Get the dashboard summary data which is simply a count of a range of different commonly used kubernetes resources. **Access policy** : Authenticated user.
##### Authorizations:
(_ApiKeyAuth_ _jwt_)
##### path Parameters
idrequired |  integer Environment (Endpoint) identifier
---|---
### Responses
**200**
Success
**400**
Invalid request
**500**
Server error
get/kubernetes/{id}/dashboard
https://api-docs.portainer.io/api/kubernetes/{id}/dashboard
###  Response samples
  * 200


Content type
application/json
Copy
Expand all  Collapse all
`[
  *  {
    *  "applicationsCount": 0,

    *  "configMapsCount": 0,

    *  "ingressesCount": 0,

    *  "namespacesCount": 0,

    *  "secretsCount": 0,

    *  "servicesCount": 0,

    *  "volumesCount": 0
  }

 ]`
