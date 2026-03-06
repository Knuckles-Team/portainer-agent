##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/helm/operation/HelmRepoSearch)Search Helm Charts
**Access policy** : authenticated
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### query Parameters
repo |  string Helm repository URL (required if registryId not provided)
---|---
registryId |  string Helm registry ID (required if repo not provided)
chart |  string Helm chart name
useCache |  string If true will use cache to search
### Responses
**200**
Success
**400**
Bad request
**401**
Unauthorized
**404**
Not found
**500**
Server error
get/templates/helm
https://api-docs.portainer.io/api/templates/helm
###  Response samples
  * 200


Content type
application/json
Copy
`"string"`
