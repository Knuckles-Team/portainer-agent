##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/edge_update_schedules/operation/EdgeUpdateScheduleInfo)Returns informations the help create edge update schedules
**Access policy** : administrator
##### Authorizations:
_ApiKeyAuth_ _jwt_
### Responses
**200**
OK
**500**
Internal Server Error
get/edge_update_schedules/info
https://api-docs.portainer.io/api/edge_update_schedules/info
###  Response samples
  * 200


Content type
application/json
Copy
`{

  *  "HasLocalTimeZone": true,

  *  "HasNoLocalTimeZone": true,

  *  "MinAgentVersion": "string",

  *  "OutdatedCount": 0,

  *  "UpToDateCount": 0

 }`
