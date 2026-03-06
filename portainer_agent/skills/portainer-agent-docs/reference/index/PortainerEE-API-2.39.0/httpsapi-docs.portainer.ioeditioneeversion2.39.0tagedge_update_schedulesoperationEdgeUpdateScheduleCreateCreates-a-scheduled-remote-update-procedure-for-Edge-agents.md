##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/edge_update_schedules/operation/EdgeUpdateScheduleCreate)Creates a scheduled remote update procedure for Edge agents
Creates a scheduled remote update process that will update or rollback the Edge agents in the specified Edge groups. **Access policy** : Administrator only.
##### Authorizations:
(_ApiKeyAuth_ _jwt_)
##### Request Body schema: application/json
required
Schedule details
AgentImage |  string default to "" == portainer/agent:
---|---
GroupIDs |  Array of integers
Name |  string
RegistryID |  integer default to 0 = dockerhub
ScheduledTime |  string
Type |  integer (types.UpdateScheduleType)  Enum: 0 1 2
UpdaterImage |  string default to "" == portainer/portainer-updater:
### Responses
**200**
Remote update procedure successfully created
**400**
Invalid request payload, such as missing required fields or fields not meeting validation criteria.
**403**
Unauthorized access or operation not allowed.
**409**
Edge update schedule name already in use.
**500**
Server error occurred while attempting to create the remote update procedure.
post/edge_update_schedules
https://api-docs.portainer.io/api/edge_update_schedules
###  Request samples
  * Payload


Content type
application/json
Copy
Expand all  Collapse all
`{

  *  "AgentImage": "string",

  *  "GroupIDs": [
    * 0
 ],

  *  "Name": "string",

  *  "RegistryID": 0,

  *  "ScheduledTime": "string",

  *  "Type": 0,

  *  "UpdaterImage": "string"

 }`
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

  *  "environmentsPreviousVersions": {
    *  "property1": "string",

    *  "property2": "string"
  },

  *  "id": 1,

  *  "name": "Update Schedule",

  *  "registryId": 1,

  *  "type": 1,

  *  "updated": 1564897200,

  *  "updaterImage": "portainer/portainer-updater:latest",

  *  "version": "1.0.0"

 }`
