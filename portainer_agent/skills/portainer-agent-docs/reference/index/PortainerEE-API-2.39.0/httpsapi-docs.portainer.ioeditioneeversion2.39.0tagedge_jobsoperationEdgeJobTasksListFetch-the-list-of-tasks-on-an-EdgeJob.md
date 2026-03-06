##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/edge_jobs/operation/EdgeJobTasksList)Fetch the list of tasks on an EdgeJob
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
get/edge_jobs/{id}/tasks
https://api-docs.portainer.io/api/edge_jobs/{id}/tasks
###  Response samples
  * 200


Content type
application/json
Copy
Expand all  Collapse all
`[
  *  {
    *  "EndpointId": 0,

    *  "EndpointName": "string",

    *  "Id": "string",

    *  "LogsStatus": 0
  }

 ]`
