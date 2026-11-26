##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/teams/operation/TeamUpdate)Update a team
Update a team. **Access policy** : administrator
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### path Parameters
idrequired |  integer Team identifier
---|---
##### Request Body schema: application/json
required
Team details
Name |  string Name
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
put/teams/{id}
https://api-docs.portainer.io/api/teams/{id}
###  Request samples
  * Payload


Content type
application/json
Copy
`{
  *  "Name": "developers"

 }`
###  Response samples
  * 200


Content type
application/json
Copy
`{

  *  "Id": 1,

  *  "Name": "developers"

 }`
