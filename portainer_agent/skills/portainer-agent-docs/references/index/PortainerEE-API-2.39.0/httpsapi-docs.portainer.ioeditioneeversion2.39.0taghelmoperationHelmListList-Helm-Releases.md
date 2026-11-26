##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/helm/operation/HelmList)List Helm Releases
**Access policy** : authenticated
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### path Parameters
idrequired |  integer Environment(Endpoint) identifier
---|---
##### query Parameters
namespace |  string specify an optional namespace
---|---
filter |  string specify an optional filter
selector |  string specify an optional selector
### Responses
**200**
Success
**400**
Invalid environment(endpoint) identifier
**401**
Unauthorized
**404**
Environment(Endpoint) or ServiceAccount not found
**500**
Server error
get/endpoints/{id}/kubernetes/helm
https://api-docs.portainer.io/api/endpoints/{id}/kubernetes/helm
###  Response samples
  * 200


Content type
application/json
Copy
Expand all  Collapse all
`[
  *  {
    *  "appVersion": "string",

    *  "chart": "string",

    *  "name": "string",

    *  "namespace": "string",

    *  "revision": "string",

    *  "status": "string",

    *  "updated": "string"
  }

 ]`
