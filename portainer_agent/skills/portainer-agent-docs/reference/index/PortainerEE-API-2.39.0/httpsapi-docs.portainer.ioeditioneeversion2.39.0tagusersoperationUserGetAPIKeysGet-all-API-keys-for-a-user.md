##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/users/operation/UserGetAPIKeys)Get all API keys for a user
Gets all API keys for a user. Only the calling user or admin can retrieve api-keys. **Access policy** : authenticated
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
get/users/{id}/tokens
https://api-docs.portainer.io/api/users/{id}/tokens
###  Response samples
  * 200


Content type
application/json
Copy
Expand all  Collapse all
`[
  *  {
    *  "dateCreated": 0,

    *  "description": "portainer-api-key",

    *  "digest": "string",

    *  "id": 1,

    *  "lastUsed": 0,

    *  "prefix": "string",

    *  "userId": 1
  }

 ]`
