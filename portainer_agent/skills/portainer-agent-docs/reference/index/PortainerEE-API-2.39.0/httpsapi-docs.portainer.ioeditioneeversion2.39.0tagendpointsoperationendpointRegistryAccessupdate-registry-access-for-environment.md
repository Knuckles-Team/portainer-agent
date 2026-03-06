##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/endpoints/operation/endpointRegistryAccess)update registry access for environment
**Access policy** : authenticated
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### path Parameters
idrequired |  integer Environment(Endpoint) identifier
---|---
registryIdrequired |  integer Registry identifier
##### Request Body schema: application/json
required
details
Namespaces |  Array of strings
---|---
TeamAccessPolicies |  object (portainer.TeamAccessPolicies)
UserAccessPolicies |  object (portainer.UserAccessPolicies)
### Responses
**204**
Success
**400**
Invalid request
**403**
Permission denied
**404**
Endpoint not found
**500**
Server error
put/endpoints/{id}/registries/{registryId}
https://api-docs.portainer.io/api/endpoints/{id}/registries/{registryId}
###  Request samples
  * Payload


Content type
application/json
Copy
Expand all  Collapse all
`{

  *  "Namespaces": [
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
