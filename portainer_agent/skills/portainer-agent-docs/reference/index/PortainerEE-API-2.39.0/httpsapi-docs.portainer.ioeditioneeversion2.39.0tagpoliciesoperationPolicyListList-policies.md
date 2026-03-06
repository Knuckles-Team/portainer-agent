##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/policies/operation/PolicyList)List policies
List all policies in the bucket. **Access policy** : administrator
##### Authorizations:
_ApiKeyAuth_ _jwt_
### Responses
**200**
Success
**500**
Server error
get/policies
https://api-docs.portainer.io/api/policies
###  Response samples
  * 200


Content type
application/json
Copy
Expand all  Collapse all
`{
  *  "policies": [
    *  {
      *  "CreatedAt": "string",

      *  "Data": {
        *  "property1": null,

        *  "property2": null
  },

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
  }
 ]

 }`
