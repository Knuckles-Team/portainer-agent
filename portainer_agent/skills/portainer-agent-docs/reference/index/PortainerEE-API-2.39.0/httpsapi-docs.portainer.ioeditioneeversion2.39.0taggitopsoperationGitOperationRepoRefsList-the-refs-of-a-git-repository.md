##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/gitops/operation/GitOperationRepoRefs)List the refs of a git repository
List all the refs of a git repository Will return all refs of a git repository **Access policy** : authenticated
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### query Parameters
force |  boolean list the results without using cache
---|---
##### Request Body schema: application/json
required
details
TLSSkipVerify |  boolean TLSSkipVerify skips SSL verification when cloning the Git repository
---|---
authorizationType |  integer Enum: 0 1
createdFromCustomTemplateID |  integer
gitCredentialID |  integer
password |  string
repositoryrequired |  string
stackID |  integer
username |  string
### Responses
**200**
Success
**400**
Invalid request
**500**
Server error
post/gitops/repo/refs
https://api-docs.portainer.io/api/gitops/repo/refs
###  Request samples
  * Payload


Content type
application/json
Copy
`{

  *  "TLSSkipVerify": false,

  *  "authorizationType": 0,

  *  "createdFromCustomTemplateID": 0,

  *  "gitCredentialID": 0,

  *  "password": "string",

  *  "repository": "string",

  *  "stackID": 0,

  *  "username": "string"

 }`
