##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/teams/operation/TeamInspect)Inspect a team
Retrieve details about a team. Access is only available for administrator and leaders of that team. **Access policy** : administrator or team leader
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### path Parameters
idrequired |  integer Team identifier
---|---
### Responses
**200**
Success
**400**
Invalid request
**403**
Permission denied
**404**
Team not found
**500**
Server error
get/teams/{id}
https://api-docs.portainer.io/api/teams/{id}
###  Response samples
  * 200


Content type
application/json
Copy
`{

  *  "Id": 1,

  *  "Name": "developers"

 }`
