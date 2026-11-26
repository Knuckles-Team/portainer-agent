##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/users/operation/UserCreateGitCredential)Store a Git Credential for a user
Store a Git Credential for a user. Only the calling user can store a git credential for themselves. **Access policy** : restricted
##### Authorizations:
_jwt_
##### path Parameters
idrequired |  integer User identifier
---|---
##### Request Body schema: application/json
required
details
authorizationTyperequired |  integer (gittypes.GitCredentialAuthType)  Enum: 0 1
---|---
namerequired |  string
passwordrequired |  string
usernamerequired |  string
### Responses
**201**
Created
**400**
Invalid request
**401**
Unauthorized
**403**
Permission denied
**500**
Server error
post/users/{id}/gitcredentials
https://api-docs.portainer.io/api/users/{id}/gitcredentials
###  Request samples
  * Payload


Content type
application/json
Copy
`{

  *  "authorizationType": 0,

  *  "name": "my-credential",

  *  "password": "string",

  *  "username": "string"

 }`
###  Response samples
  * 201


Content type
application/json
Copy
Expand all  Collapse all
`{
  *  "gitCredential": {
    *  "authorizationType": 0,

    *  "creationDate": 1587399600,

    *  "id": 1,

    *  "name": "string",

    *  "password": "string",

    *  "userId": 1,

    *  "username": "string"
  }

 }`
