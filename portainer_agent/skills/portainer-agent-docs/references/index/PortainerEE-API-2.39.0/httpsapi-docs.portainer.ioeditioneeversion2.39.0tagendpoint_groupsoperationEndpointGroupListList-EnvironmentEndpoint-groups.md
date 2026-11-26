##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/endpoint_groups/operation/EndpointGroupList)List Environment(Endpoint) groups
List all environment(endpoint) groups based on the current user authorizations. Will return all environment(endpoint) groups if using an administrator account otherwise it will only return authorized environment(endpoint) groups. **Access policy** : restricted
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### query Parameters
size |  boolean If true, each environment(endpoint) group will include the number of environments(endpoints) associated to it
---|---
### Responses
**200**
Environment(Endpoint) group
**500**
Server error
get/endpoint_groups
https://api-docs.portainer.io/api/endpoint_groups
###  Response samples
  * 200


Content type
application/json
Copy
Expand all  Collapse all
`[
  *  {
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

    *  "Size": 0,

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
  }

 ]`
