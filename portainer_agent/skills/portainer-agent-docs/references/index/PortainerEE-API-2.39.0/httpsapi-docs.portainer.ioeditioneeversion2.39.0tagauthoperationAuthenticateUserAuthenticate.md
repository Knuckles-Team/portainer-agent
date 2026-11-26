##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/auth/operation/AuthenticateUser)Authenticate
**Access policy** : public Use this environment(endpoint) to authenticate against Portainer using a username and password.
##### Request Body schema: application/json
required
Credentials used for authentication
apiKeyrequired |  string API Key
---|---
passwordrequired |  string Password
usernamerequired |  string Username
### Responses
**200**
Success
**400**
Invalid request
**422**
Invalid Credentials
**500**
Server error
post/auth
https://api-docs.portainer.io/api/auth
###  Request samples
  * Payload


Content type
application/json
Copy
`{

  *  "apiKey": "1234567890",

  *  "password": "mypassword",

  *  "username": "admin"

 }`
###  Response samples
  * 200


Content type
application/json
Copy
`{
  *  "jwt": "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyzAB"

 }`
