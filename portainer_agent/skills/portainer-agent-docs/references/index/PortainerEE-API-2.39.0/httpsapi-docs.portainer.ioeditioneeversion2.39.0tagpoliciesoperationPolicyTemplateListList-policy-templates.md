##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/policies/operation/PolicyTemplateList)List policy templates
List all built-in policy templates. Templates can be filtered by category or type. **Access policy** : administrator
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### query Parameters
category |  string Filter by category (rbac, security, setup, registry)
---|---
type |  string Filter by policy type (e.g., security-k8s, security-docker)
### Responses
**200**
Success
get/policies/templates
https://api-docs.portainer.io/api/policies/templates
###  Response samples
  * 200


Content type
application/json
Copy
Expand all  Collapse all
`{
  *  "templates": [
    *  {
      *  "category": "rbac",

      *  "data": {
        *  "property1": null,

        *  "property2": null
  },

      *  "description": "string",

      *  "id": "string",

      *  "name": "string",

      *  "type": "rbac-k8s"
  }
 ]

 }`
