##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/edge_update_schedules/operation/EdgeUpdateScheduleInspect)Returns the Edge Update Schedule with the given ID
**Access policy** : administrator
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### path Parameters
idrequired |  integer EdgeUpdate Id
---|---
### Responses
**200**
OK
**500**
Internal Server Error
get/edge_update_schedules/{id}
https://api-docs.portainer.io/api/edge_update_schedules/{id}
###  Response samples
  * 200


Content type
application/json
Copy
Expand all  Collapse all
`{

  *  "agentImage": "portainer/agent:latest",

  *  "created": 1564897200,

  *  "createdBy": 1,

  *  "edgeGroupIds": [
    * 1
 ],

  *  "edgeStackId": 1,

  *  "environmentIds": [
    * 0
 ],

  *  "environmentsPreviousVersions": {
    *  "property1": "string",

    *  "property2": "string"
  },

  *  "id": 1,

  *  "isActive": true,

  *  "name": "Update Schedule",

  *  "registryId": 1,

  *  "scheduledTime": "string",

  *  "type": 1,

  *  "updated": 1564897200,

  *  "updaterImage": "portainer/portainer-updater:latest",

  *  "version": "1.0.0"

 }`
