##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/users/operation/UserGetGitCredentials)Get all saved git credentials for a user
Gets all saved git credentials for a user. Only the calling user can retrieve git credentials **Access policy** : authenticated
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### path Parameters
idrequired |  integer User identifier
---|---
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
get/users/{id}/gitcredentials
https://api-docs.portainer.io/api/users/{id}/gitcredentials
###  Response samples
  * 200


Content type
application/json
Copy
Expand all  Collapse all
`[
  *  {
    *  "authorizationType": 0,

    *  "creationDate": 1587399600,

    *  "id": 1,

    *  "name": "string",

    *  "password": "string",

    *  "userId": 1,

    *  "username": "string"
  }

 ]`
