##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/custom_templates/operation/CustomTemplateGitFetch)Fetch the latest config file content based on custom template's git repository configuration
Retrieve details about a template created from git repository method. **Access policy** : authenticated
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
put/custom_templates/{id}/git_fetch
https://api-docs.portainer.io/api/custom_templates/{id}/git_fetch
###  Response samples
  * 200


Content type
application/json
Copy
`{
  *  "FileContent": "string"

 }`
