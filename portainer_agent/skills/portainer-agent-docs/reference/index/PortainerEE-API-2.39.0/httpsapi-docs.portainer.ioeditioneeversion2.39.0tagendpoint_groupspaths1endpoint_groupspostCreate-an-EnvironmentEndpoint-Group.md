##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/endpoint_groups/paths/~1endpoint_groups/post)Create an Environment(Endpoint) Group
Create a new environment(endpoint) group. **Access policy** : administrator
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### Request Body schema: application/json
required
Environment(Endpoint) Group details
AssociatedEndpoints |  Array of integers List of environment(endpoint) identifiers that will be part of this group
---|---
Description |  string Environment(Endpoint) group description
Namerequired |  string Environment(Endpoint) group name
TagIDs |  Array of integers List of tag identifiers to which this environment(endpoint) group is associated
### Responses
**200**
Success
**400**
Invalid request
**500**
Server error
post/endpoint_groups
https://api-docs.portainer.io/api/endpoint_groups
###  Request samples
  * Payload


Content type
application/json
Copy
Expand all  Collapse all
`{

  *  "AssociatedEndpoints": [
    *  1,

    * 3
  ],

  *  "Description": "description",

  *  "Name": "my-Environment-group",

  *  "TagIDs": [
    *  1,

    * 2
  ]

 }`
###  Response samples
  * 200


Content type
application/json
Copy
Expand all  Collapse all
`{

  *  "AuthorizedTeams": [
    * 0
 ],

  *  "AuthorizedUsers": [
    * 0
 ],

  *  "Description": "Environment(Endpoint) group description",

  *  "Id": 1,

  *  "Labels": [
    *  {
      *  "name": "name",

      *  "value": "value"
  }
 ],

  *  "Name": "my-environment-group",

  *  "TagIds": [
    * 0
 ],

  *  "Tags": [
    * "string"
 ],

  *  "TeamAccessPolicies": {
    *  "property1": {
      *  "Namespaces": [
        * "string"
 ],

      *  "RoleId": 1
  },

    *  "property2": {
      *  "Namespaces": [
        * "string"
 ],

      *  "RoleId": 1
  }
  },

  *  "UserAccessPolicies": {
    *  "property1": {
      *  "Namespaces": [
        * "string"
 ],

      *  "RoleId": 1
  },

    *  "property2": {
      *  "Namespaces": [
        * "string"
 ],

      *  "RoleId": 1
  }
  }

 }`
