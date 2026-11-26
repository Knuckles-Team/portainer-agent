##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/users/operation/UserDelete)Remove a user
Remove a user. **Access policy** : administrator
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### path Parameters
idrequired |  integer User identifier
---|---
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
delete/users/{id}
https://api-docs.portainer.io/api/users/{id}
