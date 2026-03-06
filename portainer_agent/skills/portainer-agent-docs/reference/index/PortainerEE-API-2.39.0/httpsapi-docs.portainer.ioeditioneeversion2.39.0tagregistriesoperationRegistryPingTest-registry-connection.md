##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/registries/operation/RegistryPing)Test registry connection
Test connection to a registry with provided credentials **Access policy** : authenticated
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### Request Body schema: application/json
required
Registry credentials to test
Password |  string Password used to authenticate against this registry
---|---
TLS |  boolean Use TLS
Typerequired |  integer Enum: 0 1 2 3 4 5 6 7 8 Registry Type. Valid values are: 1 (Quay.io), 2 (Azure container registry), 3 (custom registry), 4 (Gitlab registry), 5 (ProGet registry), 6 (DockerHub) 7 (ECR) 8 (Github registry)
URLrequired |  string URL or IP address of the Docker registry
Username |  string Username used to authenticate against this registry
### Responses
**200**
Success
**400**
Invalid request
**500**
Server error
post/registries/ping
https://api-docs.portainer.io/api/registries/ping
###  Request samples
  * Payload


Content type
application/json
Copy
`{

  *  "Password": "registry_password",

  *  "TLS": true,

  *  "Type": 6,

  *  "URL": "registry-1.docker.io",

  *  "Username": "registry_user"

 }`
###  Response samples
  * 200


Content type
application/json
Copy
`{

  *  "message": "Registry connection successful",

  *  "success": true

 }`
