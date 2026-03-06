##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/registries/operation/RepositoryTagsDelete)Delete repository tags
Delete tags for a given repository **Access policy** : restricted
##### Authorizations:
(_ApiKeyAuth_ _jwt_)
##### path Parameters
idrequired |  integer Registry identifier
---|---
repositoryNamerequired |  string Repository name
##### Request Body schema: application/json
required
Tags to delete
tags |  Array of strings
---|---
### Responses
**204**
Success
**400**
Invalid request
**403**
Permission denied to access registry
**404**
Registry not found
**500**
Server error
delete/registries/{id}/repositories/{repositoryName}/tags
https://api-docs.portainer.io/api/registries/{id}/repositories/{repositoryName}/tags
###  Request samples
  * Payload


Content type
application/json
Copy
Expand all  Collapse all
`{
  *  "tags": [
    * "string"
 ]

 }`
