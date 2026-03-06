##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/edge_groups/operation/EdgeGroupList)list EdgeGroups
**Access policy** : administrator
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### query Parameters
summarize |  boolean will summarize the env count
---|---
### Responses
**200**
EdgeGroups
**500**
Internal Server Error
**503**
Edge compute features are disabled
get/edge_groups
https://api-docs.portainer.io/api/edge_groups
###  Response samples
  * 200


Content type
application/json
Copy
Expand all  Collapse all
`[
  *  {
    *  "Dynamic": true,

    *  "EdgeUpdateID": 0,

    *  "EndpointIds": 0,

    *  "EndpointTypes": [
      * 0
 ],

    *  "Endpoints": [
      * 0
 ],

    *  "EndpointsCount": 0,

    *  "HasEdgeConfig": true,

    *  "HasEdgeJob": true,

    *  "HasEdgeStack": true,

    *  "Id": 1,

    *  "Name": "string",

    *  "PartialMatch": true,

    *  "TagIds": [
      * 0
 ],

    *  "TrustedEndpoints": [
      * 0
 ],

    *  "TrustedEndpointsCount": 0
  }

 ]`
