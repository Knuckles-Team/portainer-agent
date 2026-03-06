##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/registries/operation/ecrDeleteRepository)Delete ECR repository
Delete ECR repository. **Access policy** : restricted
##### Authorizations:
_jwt_
##### path Parameters
idrequired |  integer Registry identifier
---|---
repositoryNamerequired |  string Repository name
### Responses
**200**
Success
**400**
Invalid request
**403**
Permission denied to access registry
**404**
Registry not found
**500**
Server error
delete/registries/{id}/ecr/repositories/{repositoryName}
https://api-docs.portainer.io/api/registries/{id}/ecr/repositories/{repositoryName}
