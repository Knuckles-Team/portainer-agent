##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/templates/operation/TemplateFile)Get a template's file
Get a template's file **Access policy** : authenticated
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### path Parameters
idrequired |  integer Template identifier
---|---
### Responses
**200**
Success
**400**
Invalid request
**500**
Server error
post/templates/{id}/file
https://api-docs.portainer.io/api/templates/{id}/file
###  Response samples
  * 200


Content type
application/json
Copy
`{
  *  "FileContent": "version:2"

 }`
