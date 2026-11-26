##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/edge_configs/operation/EdgeConfigList)List available Edge Configurations
**Access policy** : authenticated
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### Request Body schema: application/json
required
body
BaseDir |  string
---|---
Category |  string (portaineree.EdgeConfigCategory)  Enum: "configuration" "secret"
EdgeGroupIDs |  Array of integers
Name |  string
Type |  string
### Responses
**200**
Success
**500**
Server error
get/edge_configurations
https://api-docs.portainer.io/api/edge_configurations
###  Request samples
  * Payload


Content type
application/json
Copy
Expand all  Collapse all
`{

  *  "BaseDir": "string",

  *  "Category": "configuration",

  *  "EdgeGroupIDs": [
    * 0
 ],

  *  "Name": "string",

  *  "Type": "string"

 }`
###  Response samples
  * 200


Content type
application/json
Copy
Expand all  Collapse all
`[
  *  {
    *  "baseDir": "string",

    *  "category": "configuration",

    *  "created": 0,

    *  "createdBy": 0,

    *  "edgeGroupIDs": [
      * 0
 ],

    *  "id": 0,

    *  "name": "string",

    *  "prev": { },

    *  "progress": {
      *  "success": 0,

      *  "total": 0
  },

    *  "state": 0,

    *  "type": 0,

    *  "updated": 0,

    *  "updatedBy": 0
  }

 ]`
