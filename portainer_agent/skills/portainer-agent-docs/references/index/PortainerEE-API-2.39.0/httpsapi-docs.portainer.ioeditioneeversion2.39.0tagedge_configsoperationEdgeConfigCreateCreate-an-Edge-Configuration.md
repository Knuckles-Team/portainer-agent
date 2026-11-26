##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/edge_configs/operation/EdgeConfigCreate)Create an Edge Configuration
Create an Edge Configuration. **Access policy** : authenticated
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### Request Body schema: multipart/form-data
BaseDir |  string
---|---
Category |  string Enum: "configuration" "secret"
EdgeGroupIDs |  Array of integers
Name |  string
Type |  string
Filerequired |  string <binary> File
### Responses
**204**
No Content
**400**
Invalid request
post/edge_configurations
https://api-docs.portainer.io/api/edge_configurations
