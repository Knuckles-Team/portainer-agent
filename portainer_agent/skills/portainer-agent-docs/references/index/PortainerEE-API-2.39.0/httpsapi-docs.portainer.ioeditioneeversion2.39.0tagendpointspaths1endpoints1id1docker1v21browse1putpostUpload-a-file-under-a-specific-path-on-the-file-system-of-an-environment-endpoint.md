##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/endpoints/paths/~1endpoints~1{id}~1docker~1v2~1browse~1put/post)Upload a file under a specific path on the file system of an environment (endpoint)
Use this environment(endpoint) to upload TLS files. **Access policy** : administrator
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### path Parameters
idrequired |  integer Environment(Endpoint) identifier
---|---
##### query Parameters
volumeID |  string Optional volume identifier to upload the file
---|---
##### Request Body schema: multipart/form-data
required
Pathrequired |  string The destination path to upload the file to
---|---
filerequired |  string <binary> The file to upload
### Responses
**204**
Success
**400**
Invalid request
**500**
Server error
post/endpoints/{id}/docker/v2/browse/put
https://api-docs.portainer.io/api/endpoints/{id}/docker/v2/browse/put
