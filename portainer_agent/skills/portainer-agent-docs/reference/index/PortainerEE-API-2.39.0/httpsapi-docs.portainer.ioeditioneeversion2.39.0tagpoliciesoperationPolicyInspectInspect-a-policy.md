##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/policies/operation/PolicyInspect)Inspect a policy
Retrieve details about a policy. **Access policy** : authenticated
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### path Parameters
idrequired |  integer Policy identifier
---|---
### Responses
**200**
Success
**400**
Invalid request
**404**
Policy not found
**500**
Server error
get/policies/{id}
https://api-docs.portainer.io/api/policies/{id}
###  Response samples
  * 200


Content type
application/json
Copy
Expand all  Collapse all
`{

  *  "CreatedAt": "string",

  *  "EnvironmentGroups": [
    * 0
 ],

  *  "EnvironmentType": "kubernetes",

  *  "Id": 0,

  *  "Name": "string",

  *  "StatusBreakdown": {
    *  "Applied": 0,

    *  "Failed": 0,

    *  "InProgress": 0,

    *  "NotSupported": 0,

    *  "Warning": 0
  },

  *  "Type": "rbac-k8s",

  *  "UpdatedAt": "string"

 }`
