##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/edge_groups/operation/EdgeGroupInspect)Inspects an EdgeGroup
**Access policy** : administrator
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### path Parameters
idrequired |  integer EdgeGroup Id
---|---
### Responses
**200**
OK
**500**
Internal Server Error
**503**
Edge compute features are disabled
get/edge_groups/{id}
https://api-docs.portainer.io/api/edge_groups/{id}
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
