##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/registries/operation/RegistryConfigure)Configures a registry
Configures a registry. **Access policy** : restricted
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### path Parameters
idrequired |  integer Registry identifier
---|---
##### Request Body schema: application/json
required
Registry configuration
Authenticationrequired |  boolean Is authentication against this registry enabled
---|---
Password |  string Password used to authenticate against this registry. required when Authentication is true
Region |  string ECR region
TLS |  boolean Use TLS
TLSCACertFile |  Array of integers The TLS CA certificate file
TLSCertFile |  Array of integers The TLS client certificate file
TLSKeyFile |  Array of integers The TLS client key file
TLSSkipVerify |  boolean Skip the verification of the server TLS certificate
Username |  string Username used to authenticate against this registry. Required when Authentication is true
### Responses
**204**
Success
**400**
Invalid request
**403**
Permission denied
**404**
Registry not found
**500**
Server error
post/registries/{id}/configure
https://api-docs.portainer.io/api/registries/{id}/configure
###  Request samples
  * Payload


Content type
application/json
Copy
Expand all  Collapse all
`{

  *  "Authentication": false,

  *  "Password": "registry_password",

  *  "Region": "string",

  *  "TLS": true,

  *  "TLSCACertFile": [
    * 0
 ],

  *  "TLSCertFile": [
    * 0
 ],

  *  "TLSKeyFile": [
    * 0
 ],

  *  "TLSSkipVerify": false,

  *  "Username": "registry_user"

 }`
