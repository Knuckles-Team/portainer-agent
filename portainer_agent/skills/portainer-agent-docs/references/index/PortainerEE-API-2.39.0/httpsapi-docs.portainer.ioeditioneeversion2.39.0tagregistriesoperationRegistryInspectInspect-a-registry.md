##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/registries/operation/RegistryInspect)Inspect a registry
Retrieve details about a registry. If endpointId is provided, applies policy overrides for that environment. **Access policy** : restricted
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### path Parameters
idrequired |  integer Registry identifier
---|---
##### query Parameters
endpointId |  integer Environment identifier (applies policy overrides if provided)
---|---
### Responses
**200**
Success
**400**
Invalid request
**403**
Permission denied to access registry
**404**
Registry not found
**500**
Server error
get/registries/{id}
https://api-docs.portainer.io/api/registries/{id}
###  Response samples
  * 200


Content type
application/json
Copy
Expand all  Collapse all
`{

  *  "AccessToken": "string",

  *  "AccessTokenExpiry": 0,

  *  "Authentication": true,

  *  "AuthorizedTeams": [
    * 0
 ],

  *  "AuthorizedUsers": [
    * 0
 ],

  *  "BaseURL": "registry.mydomain.tld:2375",

  *  "Ecr": {
    *  "Region": "ap-southeast-2"
 },

  *  "Github": {
    *  "OrganisationName": "string",

    *  "UseOrganisation": true
  },

  *  "Gitlab": {
    *  "InstanceURL": "string",

    *  "ProjectId": 0,

    *  "ProjectPath": "string"
  },

  *  "Id": 1,

  *  "ManagementConfiguration": {
    *  "AccessToken": "string",

    *  "AccessTokenExpiry": 0,

    *  "Authentication": true,

    *  "Ecr": {
      *  "Region": "ap-southeast-2"
 },

    *  "Password": "string",

    *  "TLSConfig": {
      *  "TLS": true,

      *  "TLSCACert": "/data/tls/ca.pem",

      *  "TLSCert": "/data/tls/cert.pem",

      *  "TLSKey": "/data/tls/key.pem",

      *  "TLSSkipVerify": false
  },

    *  "Type": 0,

    *  "Username": "string"
  },

  *  "Name": "my-registry",

  *  "Password": "registry_password",

  *  "Quay": {
    *  "OrganisationName": "string",

    *  "UseOrganisation": true
  },

  *  "RegistryAccesses": {
    *  "property1": {
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
  },

    *  "property2": {
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
  }
  },

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

  *  "Type": 1,

  *  "URL": "registry.mydomain.tld:2375",

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
  },

  *  "Username": "registry user"

 }`
