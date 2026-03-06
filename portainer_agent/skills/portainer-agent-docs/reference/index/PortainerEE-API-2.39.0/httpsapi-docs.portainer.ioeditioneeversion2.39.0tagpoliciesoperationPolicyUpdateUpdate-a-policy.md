##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/policies/operation/PolicyUpdate)Update a policy
Update an existing policy. **Access policy** : administrator
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### path Parameters
idrequired |  integer Policy identifier
---|---
##### Request Body schema: application/json
required
Policy details
AllowOverride |  boolean
---|---
Data |  object
EnvironmentGroups |  Array of integers
EnvironmentType |  string
Name |  string
Type |  string (policies.PolicyType)  Enum: "rbac-k8s" "security-k8s" "setup-k8s" "registry-k8s" "rbac-docker" "security-docker" "setup-docker" "registry-docker" "rbac-k8s" "security-k8s" "setup-k8s" "registry-k8s" "rbac-docker" "security-docker" "setup-docker" "registry-docker"
### Responses
**200**
Success
**400**
Invalid request
**404**
Policy not found
**500**
Server error
put/policies/{id}
https://api-docs.portainer.io/api/policies/{id}
###  Request samples
  * Payload


Content type
application/json
Copy
Expand all  Collapse all
`{

  *  "AllowOverride": false,

  *  "Data": {
    *  "property1": null,

    *  "property2": null
  },

  *  "EnvironmentGroups": [
    * 0
 ],

  *  "EnvironmentType": "kubernetes",

  *  "Name": "Updated Development Policy",

  *  "Type": "rbac-k8s"

 }`
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
