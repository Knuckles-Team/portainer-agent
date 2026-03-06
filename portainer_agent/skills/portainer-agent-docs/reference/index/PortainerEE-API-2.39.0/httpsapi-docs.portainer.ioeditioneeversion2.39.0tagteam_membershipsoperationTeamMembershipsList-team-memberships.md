##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/team_memberships/operation/TeamMemberships)List team memberships
List team memberships. Access is only available to administrators and team leaders. **Access policy** : restricted
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### path Parameters
idrequired |  integer Team Id
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
get/teams/{id}/memberships
https://api-docs.portainer.io/api/teams/{id}/memberships
###  Response samples
  * 200


Content type
application/json
Copy
Expand all  Collapse all
`[
  *  {
    *  "Id": 1,

    *  "Role": 1,

    *  "TeamID": 1,

    *  "UserID": 1
  }

 ]`
