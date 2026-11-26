##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/users/operation/UserGetGitCredential)Get the specific saved git credential for a user
Gets the specific saved git credential for a user. Only the calling user can retrieve git credential **Access policy** : authenticated
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### path Parameters
idrequired |  integer User identifier
---|---
credentialIDrequired |  integer Git Credential identifier
### Responses
**200**
Success
**400**
Invalid request
**403**
Permission denied
**404**
User not found
**500**
Server error
get/users/{id}/gitcredentials/{credentialID}
https://api-docs.portainer.io/api/users/{id}/gitcredentials/{credentialID}
###  Response samples
  * 200


Content type
application/json
Copy
`{

  *  "authorizationType": 0,

  *  "creationDate": 1587399600,

  *  "id": 1,

  *  "name": "string",

  *  "password": "string",

  *  "userId": 1,

  *  "username": "string"

 }`
