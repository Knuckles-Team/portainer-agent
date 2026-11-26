##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/endpoint_groups/operation/EndpointGroupUpdate)Update an environment(endpoint) group
Update an environment(endpoint) group. **Access policy** : administrator
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### path Parameters
idrequired |  integer EndpointGroup identifier
---|---
##### Request Body schema: application/json
required
EndpointGroup details
AssociatedEndpoints |  Array of integers List of environment(endpoint) identifiers that will be part of this group
---|---
Description |  string Environment(Endpoint) group description
Name |  string Environment(Endpoint) group name
TagIDs |  Array of integers List of tag identifiers associated to the environment(endpoint) group
TeamAccessPolicies |  object (portainer.TeamAccessPolicies)
UserAccessPolicies |  object (portainer.UserAccessPolicies)
### Responses
**200**
Success
**400**
Invalid request
**404**
EndpointGroup not found
**500**
Server error
put/endpoint_groups/{id}
https://api-docs.portainer.io/api/endpoint_groups/{id}
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

  *  "Name": "my-environment-group",

  *  "TagIDs": [
    *  3,

    * 4
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
