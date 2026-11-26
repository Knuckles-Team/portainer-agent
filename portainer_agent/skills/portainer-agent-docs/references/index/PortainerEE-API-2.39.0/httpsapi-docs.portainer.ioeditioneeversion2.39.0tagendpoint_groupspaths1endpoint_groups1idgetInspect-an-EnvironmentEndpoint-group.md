##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/endpoint_groups/paths/~1endpoint_groups~1{id}/get)Inspect an Environment(Endpoint) group
Retrieve details abont an environment(endpoint) group. **Access policy** : administrator
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### path Parameters
idrequired |  integer Environment(Endpoint) group identifier
---|---
### Responses
**200**
Success
**400**
Invalid request
**404**
EndpointGroup not found
**500**
Server error
get/endpoint_groups/{id}
https://api-docs.portainer.io/api/endpoint_groups/{id}
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

  *  "Policies": [
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
 ],

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
