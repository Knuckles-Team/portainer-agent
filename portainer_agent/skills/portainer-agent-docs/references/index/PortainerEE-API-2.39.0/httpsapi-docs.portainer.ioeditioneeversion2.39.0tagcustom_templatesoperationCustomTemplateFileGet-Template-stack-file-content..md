##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/custom_templates/operation/CustomTemplateFile)Get Template stack file content.
Retrieve the content of the Stack file for the specified custom template **Access policy** : authenticated
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
**404**
Custom template not found
**500**
Server error
get/custom_templates/{id}/file
https://api-docs.portainer.io/api/custom_templates/{id}/file
###  Response samples
  * 200


Content type
application/json
Copy
`{
  *  "FileContent": "string"

 }`
