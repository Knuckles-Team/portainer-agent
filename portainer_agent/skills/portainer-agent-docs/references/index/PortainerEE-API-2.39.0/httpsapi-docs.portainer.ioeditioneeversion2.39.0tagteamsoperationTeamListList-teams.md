##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/teams/operation/TeamList)List teams
List teams. All authenticated users can list all teams (teams only expose ID and Name). **Access policy** : authenticated
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### query Parameters
onlyLedTeams |  boolean Only list teams that the user is leader of
---|---
environmentId |  integer Identifier of the environment(endpoint) that will be used to filter the authorized teams
### Responses
**200**
Success
**500**
Server error
get/teams
https://api-docs.portainer.io/api/teams
###  Response samples
  * 200


Content type
application/json
Copy
Expand all  Collapse all
`[
  *  {
    *  "Id": 1,

    *  "Name": "developers"
  }

 ]`
