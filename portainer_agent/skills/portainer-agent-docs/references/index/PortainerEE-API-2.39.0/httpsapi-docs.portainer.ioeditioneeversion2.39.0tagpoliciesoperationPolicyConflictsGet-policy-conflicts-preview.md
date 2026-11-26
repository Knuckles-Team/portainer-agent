##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/policies/operation/PolicyConflicts)Get policy conflicts preview
Returns detailed information about what will be affected when creating or updating a policy with specific environment groups. **Access policy** : administrator
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### Request Body schema: application/json
required
Conflict check details
object (policies.policyConflictsPayload)
### Responses
**200**
Success
**400**
Invalid request payload
**500**
Server error
post/policies/conflicts
https://api-docs.portainer.io/api/policies/conflicts
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

  *  "conflicts": [
    *  {
      *  "environmentCount": 0,

      *  "environmentGroupId": 0,

      *  "environmentGroupName": "string",

      *  "existingPolicyId": 0,

      *  "existingPolicyName": "string",

      *  "supportedEnvironments": 0,

      *  "unsupportedEnvironments": 0
  }
 ],

  *  "newGroups": [
    *  {
      *  "environmentCount": 0,

      *  "environmentGroupId": 0,

      *  "environmentGroupName": "string",

      *  "supportedEnvironments": 0,

      *  "unsupportedEnvironments": 0
  }
 ],

  *  "supportedEnvironments": 0,

  *  "totalEnvironments": 0,

  *  "unsupportedEnvironments": 0

 }`
