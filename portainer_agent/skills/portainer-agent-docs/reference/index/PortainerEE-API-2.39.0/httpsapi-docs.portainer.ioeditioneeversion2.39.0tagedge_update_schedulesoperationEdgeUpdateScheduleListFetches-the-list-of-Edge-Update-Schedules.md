##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/edge_update_schedules/operation/EdgeUpdateScheduleList)Fetches the list of Edge Update Schedules
**Access policy** : administrator
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### query Parameters
includeEdgeStacks |  boolean Include Edge Stacks in the response
---|---
### Responses
**200**
OK
**500**
Internal Server Error
get/edge_update_schedules
https://api-docs.portainer.io/api/edge_update_schedules
###  Response samples
  * 200


Content type
application/json
Copy
Expand all  Collapse all
`[
  *  {
    *  "agentImage": "portainer/agent:latest",

    *  "created": 1564897200,

    *  "createdBy": 1,

    *  "edgeGroupIds": [
      * 0
 ],

    *  "edgeStackId": 1,

    *  "environmentsPreviousVersions": {
      *  "property1": "string",

      *  "property2": "string"
  },

    *  "id": 1,

    *  "name": "Update Schedule",

    *  "registryId": 1,

    *  "scheduledTime": "string",

    *  "status": 0,

    *  "statusMessage": "string",

    *  "type": 1,

    *  "updated": 1564897200,

    *  "updaterImage": "portainer/portainer-updater:latest",

    *  "version": "1.0.0"
  }

 ]`
