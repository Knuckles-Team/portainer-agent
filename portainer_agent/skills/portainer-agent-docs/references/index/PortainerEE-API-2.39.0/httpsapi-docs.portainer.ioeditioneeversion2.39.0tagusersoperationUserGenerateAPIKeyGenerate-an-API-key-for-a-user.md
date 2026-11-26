##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/users/operation/UserGenerateAPIKey)Generate an API key for a user
Generates an API key for a user. Only the calling user can generate a token for themselves. Password is required only for internal authentication. **Access policy** : restricted
##### Authorizations:
_jwt_
##### path Parameters
idrequired |  integer User identifier
---|---
##### Request Body schema: application/json
required
details
descriptionrequired |  string
---|---
passwordrequired |  string
### Responses
**200**
Success
**400**
Invalid request
**401**
Unauthorized
**403**
Permission denied
**404**
User not found
**500**
Server error
post/users/{id}/tokens
https://api-docs.portainer.io/api/users/{id}/tokens
###  Request samples
  * Payload


Content type
application/json
Copy
`{

  *  "description": "github-api-key",

  *  "password": "password"

 }`
###  Response samples
  * 200


Content type
application/json
Copy
Expand all  Collapse all
`{

  *  "apiKey": {
    *  "dateCreated": 0,

    *  "description": "portainer-api-key",

    *  "digest": "string",

    *  "id": 1,

    *  "lastUsed": 0,

    *  "prefix": "string",

    *  "userId": 1
  },

  *  "rawAPIKey": "string"

 }`
