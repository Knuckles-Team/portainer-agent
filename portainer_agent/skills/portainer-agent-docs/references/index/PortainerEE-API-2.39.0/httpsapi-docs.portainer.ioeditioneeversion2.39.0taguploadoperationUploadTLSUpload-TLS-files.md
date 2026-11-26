##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/upload/operation/UploadTLS)Upload TLS files
Use this environment(endpoint) to upload TLS files. **Access policy** : administrator
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### path Parameters
certificaterequired |  string Enum: "ca" "cert" "key" TLS file type. Valid values are 'ca', 'cert' or 'key'.
---|---
##### Request Body schema: multipart/form-data
required
folderrequired |  string Folder where the TLS file will be stored. Will be created if not existing
---|---
filerequired |  string <binary> The file to upload
### Responses
**204**
Success
**400**
Invalid request
**500**
Server error
post/upload/tls/{certificate}
https://api-docs.portainer.io/api/upload/tls/{certificate}
