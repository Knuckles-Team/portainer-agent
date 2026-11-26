##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/teams/operation/TeamDelete)Remove a team
Remove a team. **Access policy** : administrator
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### path Parameters
idrequired |  integer Team Id
---|---
### Responses
**204**
Success
**400**
Invalid request
**403**
Permission denied
**404**
Team not found
**500**
Server error
delete/teams/{id}
https://api-docs.portainer.io/api/teams/{id}
