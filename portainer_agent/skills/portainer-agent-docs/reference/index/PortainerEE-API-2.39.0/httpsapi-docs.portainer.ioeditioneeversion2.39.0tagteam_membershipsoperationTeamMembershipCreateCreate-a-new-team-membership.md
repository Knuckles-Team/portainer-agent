##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/team_memberships/operation/TeamMembershipCreate)Create a new team membership
Create a new team memberships. Access is only available to administrators leaders of the associated team. **Access policy** : administrator
##### Authorizations:
_ApiKeyAuth_ _jwt_
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
Permission denied to manage memberships
**409**
Team membership already registered
**500**
Server error
post/team_memberships
https://api-docs.portainer.io/api/team_memberships
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
