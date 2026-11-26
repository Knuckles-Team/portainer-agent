##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/registries/operation/RegistryCreate)Create a new registry
Create a new registry. **Access policy** : restricted
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### Request Body schema: application/json
required
Registry details
Authenticationrequired |  boolean Is authentication against this registry enabled
---|---
BaseURL |  string BaseURL required for ProGet registry
Ecr |  object ECR specific details, required when type = 7
Github |  object Github specific details, required when type = 8
Gitlab |  object Gitlab specific details, required when type = 4
Namerequired |  string Name that will be used to identify this registry
Password |  string Password used to authenticate against this registry. required when Authentication is true
Quay |  object Quay specific details, required when type = 1
TLS |  boolean Use TLS
Typerequired |  integer Enum: 0 1 2 3 4 5 6 7 8 Registry Type. Valid values are: 1 (Quay.io), 2 (Azure container registry), 3 (custom registry), 4 (Gitlab registry), 5 (ProGet registry), 6 (DockerHub) 7 (ECR) 8 (Github registry)
URLrequired |  string URL or IP address of the Docker registry
Username |  string Username used to authenticate against this registry. Required when Authentication is true
### Responses
**200**
Success
**400**
Invalid request
**409**
Another registry with either the same name or same URL & credeintials already exists
**500**
Server error
post/registries
https://api-docs.portainer.io/api/registries
###  Request samples
  * Payload


Content type
application/json
Copy
Expand all  Collapse all
`{

  *  "Authentication": false,

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

  *  "Name": "my-registry",

  *  "Password": "registry_password",

  *  "Quay": {
    *  "OrganisationName": "string",

    *  "UseOrganisation": true
  },

  *  "TLS": true,

  *  "Type": 1,

  *  "URL": "registry.mydomain.tld:2375/feed",

  *  "Username": "registry_user"

 }`
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
