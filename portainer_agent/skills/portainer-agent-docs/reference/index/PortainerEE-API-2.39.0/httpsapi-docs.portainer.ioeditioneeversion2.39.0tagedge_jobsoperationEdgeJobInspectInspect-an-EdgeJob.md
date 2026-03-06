##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/edge_jobs/operation/EdgeJobInspect)Inspect an EdgeJob
**Access policy** : administrator
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### path Parameters
idrequired |  integer EdgeJob Id
---|---
### Responses
**200**
OK
**400**
Bad Request
**500**
Internal Server Error
**503**
Edge compute features are disabled
get/edge_jobs/{id}
https://api-docs.portainer.io/api/edge_jobs/{id}
###  Response samples
  * 200


Content type
application/json
Copy
Expand all  Collapse all
`{

  *  "Created": 0,

  *  "CronExpression": "string",

  *  "EdgeGroups": [
    * 0
 ],

  *  "Endpoints": {
    *  "property1": {
      *  "CollectLogs": true,

      *  "LogsStatus": 0
  },

    *  "property2": {
      *  "CollectLogs": true,

      *  "LogsStatus": 0
  }
  },

  *  "GroupLogsCollection": {
    *  "property1": {
      *  "CollectLogs": true,

      *  "LogsStatus": 0
  },

    *  "property2": {
      *  "CollectLogs": true,

      *  "LogsStatus": 0
  }
  },

  *  "Id": 1,

  *  "Name": "string",

  *  "Recurring": true,

  *  "ScriptPath": "string",

  *  "Version": 0

 }`
