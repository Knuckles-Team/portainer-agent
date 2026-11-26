##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/custom_templates/operation/CustomTemplateDelete)Remove a template
Remove a template. **Access policy** : authenticated
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### path Parameters
idrequired |  integer Template identifier
---|---
### Responses
**204**
Success
**400**
Invalid request
**403**
Access denied to resource
**404**
Template not found
**500**
Server error
delete/custom_templates/{id}
https://api-docs.portainer.io/api/custom_templates/{id}
