##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/edge_update_schedules/operation/EdgeUpdateScheduleActiveSchedulesList)Fetches the list of Active Edge Update Schedules
**Access policy** : administrator
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### Request Body schema: application/json
required
Active schedule query
EnvironmentIDs |  Array of integers
---|---
### Responses
**200**
OK
**500**
Internal Server Error
post/edge_update_schedules/active
https://api-docs.portainer.io/api/edge_update_schedules/active
###  Request samples
  * Payload


Content type
application/json
Copy
Expand all  Collapse all
`{
  *  "EnvironmentIDs": [
    * 0
 ]

 }`
###  Response samples
  * 200


Content type
application/json
Copy
Expand all  Collapse all
`[
  *  {
    *  "edgeStackId": 0,

    *  "environmentId": 0,

    *  "scheduleId": 0,

    *  "targetVersion": "string"
  }

 ]`
