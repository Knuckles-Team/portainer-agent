##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/edge_groups/operation/EdgeGroupUpdate)Updates an EdgeGroup
**Access policy** : administrator
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### path Parameters
idrequired |  integer EdgeGroup Id
---|---
##### Request Body schema: application/json
required
EdgeGroup data
Dynamic |  boolean
---|---
Endpoints |  Array of integers
Name |  string
PartialMatch |  boolean
TagIDs |  Array of integers
### Responses
**200**
OK
**500**
Internal Server Error
**503**
Edge compute features are disabled
put/edge_groups/{id}
https://api-docs.portainer.io/api/edge_groups/{id}
###  Request samples
  * Payload


Content type
application/json
Copy
Expand all  Collapse all
`{

  *  "Dynamic": true,

  *  "Endpoints": [
    * 0
 ],

  *  "Name": "string",

  *  "PartialMatch": true,

  *  "TagIDs": [
    * 0
 ]

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
