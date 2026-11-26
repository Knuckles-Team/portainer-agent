##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/teams/operation/TeamCreate)Create a new team
Create a new team. **Access policy** : administrator
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### Request Body schema: application/json
required
details
Namerequired |  string Name
---|---
TeamLeaders |  Array of integers TeamLeaders
### Responses
**200**
Success
**400**
Invalid request
**409**
A team with the same name already exists
**500**
Server error
post/teams
https://api-docs.portainer.io/api/teams
###  Request samples
  * Payload


Content type
application/json
Copy
Expand all  Collapse all
`{

  *  "Name": "developers",

  *  "TeamLeaders": [
    *  3,

    * 5
  ]

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
