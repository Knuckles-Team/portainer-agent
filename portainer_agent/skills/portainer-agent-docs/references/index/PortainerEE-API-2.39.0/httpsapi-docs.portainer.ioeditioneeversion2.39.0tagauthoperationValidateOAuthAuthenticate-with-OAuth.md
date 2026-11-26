##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/auth/operation/ValidateOAuth)Authenticate with OAuth
**Access policy** : public
##### Request Body schema: application/json
required
OAuth Credentials used for authentication
Code |  string OAuth code returned from OAuth Provided
---|---
### Responses
**200**
Success
**400**
Invalid request
**422**
Invalid Credentials
**500**
Server error
post/auth/oauth/validate
https://api-docs.portainer.io/api/auth/oauth/validate
###  Request samples
  * Payload


Content type
application/json
Copy
`{
  *  "Code": "string"

 }`
###  Response samples
  * 200


Content type
application/json
Copy
`{
  *  "jwt": "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyzAB"

 }`
