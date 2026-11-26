##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/users/operation/UserMembershipsInspect)Inspect a user memberships
Inspect a user memberships. **Access policy** : restricted
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
**500**
Server error
get/users/{id}/memberships
https://api-docs.portainer.io/api/users/{id}/memberships
###  Response samples
  * 200


Content type
application/json
Copy
`{

  *  "Id": 1,

  *  "Role": 1,

  *  "TeamID": 1,

  *  "UserID": 1

 }`
