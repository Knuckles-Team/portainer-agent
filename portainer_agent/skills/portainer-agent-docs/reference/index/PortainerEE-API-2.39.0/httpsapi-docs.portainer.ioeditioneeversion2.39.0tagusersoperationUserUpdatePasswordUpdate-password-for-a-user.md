##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/users/operation/UserUpdatePassword)Update password for a user
Update password for the specified user. **Access policy** : authenticated
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### path Parameters
idrequired |  integer identifier
---|---
##### Request Body schema: application/json
required
details
NewPasswordrequired |  string New Password
---|---
Passwordrequired |  string Current Password
### Responses
**204**
Success
**400**
Invalid request
**403**
Permission denied
**404**
User not found
**500**
Server error
put/users/{id}/passwd
https://api-docs.portainer.io/api/users/{id}/passwd
###  Request samples
  * Payload


Content type
application/json
Copy
`{

  *  "NewPassword": "new_passwd",

  *  "Password": "passwd"

 }`
