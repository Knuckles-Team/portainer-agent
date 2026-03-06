##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/policies/operation/PolicyCreate)Create a new policy
Create a new policy. **Access policy** : administrator
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### Request Body schema: application/json
required
Policy details
object (policies.policyCreatePayload)
### Responses
**200**
Success
**400**
Invalid request payload
**409**
This name is already associated to a policy
**500**
Server error
post/policies
https://api-docs.portainer.io/api/policies
###  Request samples
  * Payload


Content type
application/json
Copy
`{ }`
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
