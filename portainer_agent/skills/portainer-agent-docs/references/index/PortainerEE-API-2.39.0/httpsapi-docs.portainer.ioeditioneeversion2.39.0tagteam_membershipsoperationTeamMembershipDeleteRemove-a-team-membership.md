##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/team_memberships/operation/TeamMembershipDelete)Remove a team membership
Remove a team membership. Access is only available to administrators leaders of the associated team. **Access policy** : administrator
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### path Parameters
idrequired |  integer TeamMembership identifier
---|---
### Responses
**204**
Success
**400**
Invalid request
**403**
Permission denied
**404**
TeamMembership not found
**500**
Server error
delete/team_memberships/{id}
https://api-docs.portainer.io/api/team_memberships/{id}
