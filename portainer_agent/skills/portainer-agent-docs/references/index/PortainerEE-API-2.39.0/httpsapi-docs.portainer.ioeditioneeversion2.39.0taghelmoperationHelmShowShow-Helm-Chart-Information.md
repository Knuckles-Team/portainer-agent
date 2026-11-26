##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/helm/operation/HelmShow)Show Helm Chart Information
**Access policy** : authenticated Either `repo` or `registryId` parameter is required (but not both)
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### path Parameters
commandrequired |  string chart/values/readme
---|---
##### query Parameters
repo |  string Helm repository URL (required if registryId not provided)
---|---
registryId |  string Helm registry ID (required if repo not provided)
environmentId |  string Environment ID (required if registryId is provided and user is not an admin)
chartrequired |  string Chart name
versionrequired |  string Chart version
### Responses
**200**
Success
**401**
Unauthorized
**404**
Environment(Endpoint) or ServiceAccount not found
**500**
Server error
get/templates/helm/{command}
https://api-docs.portainer.io/api/templates/helm/{command}
