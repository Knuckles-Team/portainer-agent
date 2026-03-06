##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/team_memberships/operation/TeamMembershipUpdate)Update a team membership
Update a team membership. Access is only available to administrators or leaders of the associated team. **Access policy** : administrator or leaders of the associated team
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### path Parameters
idrequired |  integer Team membership identifier
---|---
##### Request Body schema: application/json
required
Team membership details
Rolerequired |  integer Enum: 1 2 Role for the user inside the team (1 for leader and 2 for regular member)
---|---
TeamIDrequired |  integer Team identifier
UserIDrequired |  integer User identifier
### Responses
**200**
Success
**400**
Invalid request
**403**
Permission denied
**404**
TeamMembership not found
**500**
Server error
put/team_memberships/{id}
https://api-docs.portainer.io/api/team_memberships/{id}
###  Request samples
  * Payload


Content type
application/json
Copy
`{

  *  "Role": 1,

  *  "TeamID": 1,

  *  "UserID": 1

 }`
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
