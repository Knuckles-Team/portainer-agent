##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/edge_configs/operation/EdgeConfigUpdate)Update an Edge Configuration
Update an Edge Configuration. **Access policy** : authenticated
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### path Parameters
idrequired |  integer Edge configuration identifier
---|---
##### Request Body schema: multipart/form-data
EdgeGroupIDs |  Array of integers
---|---
Type |  string
Filerequired |  string <binary> File
### Responses
**204**
No Content
**400**
Invalid request
put/edge_configurations/{id}
https://api-docs.portainer.io/api/edge_configurations/{id}
