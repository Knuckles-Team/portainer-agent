##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/policies/operation/PolicyTemplateInspect)Inspect a policy template
Retrieve a specific policy template by ID. **Access policy** : administrator
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### path Parameters
idrequired |  string Template ID
---|---
### Responses
**200**
Success
**404**
Template not found
get/policies/templates/{id}
https://api-docs.portainer.io/api/policies/templates/{id}
###  Response samples
  * 200


Content type
application/json
Copy
Expand all  Collapse all
`{

  *  "category": "rbac",

  *  "data": {
    *  "property1": null,

    *  "property2": null
  },

  *  "description": "string",

  *  "id": "string",

  *  "name": "string",

  *  "type": "rbac-k8s"

 }`
