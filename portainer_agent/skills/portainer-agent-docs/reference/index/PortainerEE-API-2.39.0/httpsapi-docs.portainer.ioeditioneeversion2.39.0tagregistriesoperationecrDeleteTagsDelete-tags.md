##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/registries/operation/ecrDeleteTags)Delete tags
Delete tags for a given ECR repository **Access policy** : restricted
##### Authorizations:
_jwt_
##### path Parameters
idrequired |  integer Registry identifier
---|---
repositoryNamerequired |  integer Repository name
##### Request Body schema: application/json
required
Tag Array
Tags |  Array of strings
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
delete/registries/{id}/ecr/repositories/{repositoryName}/tags
https://api-docs.portainer.io/api/registries/{id}/ecr/repositories/{repositoryName}/tags
###  Request samples
  * Payload


Content type
application/json
Copy
Expand all  Collapse all
`{
  *  "Tags": [
    * "string"
 ]

 }`
