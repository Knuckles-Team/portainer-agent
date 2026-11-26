##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/edge_stacks/operation/EdgeStackParseRegistries)Parse registries from a stack file
**Access policy** : authenticated
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### Request Body schema: multipart/form-data
required
filerequired |  string <binary> stack file
---|---
### Responses
**200**
List of registries IDs
**400**
Invalid request payload
**500**
Server error
post/edge_stacks/parse_registries
https://api-docs.portainer.io/api/edge_stacks/parse_registries
###  Response samples
  * 200


Content type
application/json
Copy
`[
  * 0

 ]`
