##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/edge_jobs/operation/EdgeJobCreateFile)Create an EdgeJob from a file
**Access policy** : administrator
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### Request Body schema: multipart/form-data
required
filerequired |  string <binary> Content of the Stack file
---|---
Namerequired |  string Name of the stack
CronExpressionrequired |  string A cron expression to schedule this job
EdgeGroupsrequired |  string JSON stringified array of Edge Groups ids
Endpointsrequired |  string JSON stringified array of Environment ids
Recurring |  boolean If recurring
### Responses
**200**
OK
**500**
Internal Server Error
**503**
Edge compute features are disabled
post/edge_jobs/create/file
https://api-docs.portainer.io/api/edge_jobs/create/file
###  Response samples
  * 200


Content type
application/json
Copy
Expand all  Collapse all
`{

  *  "Dynamic": true,

  *  "EdgeUpdateID": 0,

  *  "EndpointIds": { },

  *  "Endpoints": [
    * 0
 ],

  *  "Id": 1,

  *  "Name": "string",

  *  "PartialMatch": true,

  *  "TagIds": [
    * 0
 ]

 }`
