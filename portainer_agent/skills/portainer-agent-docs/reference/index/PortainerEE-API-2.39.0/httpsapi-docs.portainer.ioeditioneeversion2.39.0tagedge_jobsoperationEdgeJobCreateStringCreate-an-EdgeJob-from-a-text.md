##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/edge_jobs/operation/EdgeJobCreateString)Create an EdgeJob from a text
**Access policy** : administrator
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### Request Body schema: application/json
required
EdgeGroup data when method is string
CronExpression |  string
---|---
EdgeGroups |  Array of integers
Endpoints |  Array of integers
FileContent |  string
Name |  string
Recurring |  boolean
### Responses
**200**
OK
**500**
Internal Server Error
**503**
Edge compute features are disabled
post/edge_jobs/create/string
https://api-docs.portainer.io/api/edge_jobs/create/string
###  Request samples
  * Payload


Content type
application/json
Copy
Expand all  Collapse all
`{

  *  "CronExpression": "string",

  *  "EdgeGroups": [
    * 0
 ],

  *  "Endpoints": [
    * 0
 ],

  *  "FileContent": "string",

  *  "Name": "string",

  *  "Recurring": true

 }`
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
