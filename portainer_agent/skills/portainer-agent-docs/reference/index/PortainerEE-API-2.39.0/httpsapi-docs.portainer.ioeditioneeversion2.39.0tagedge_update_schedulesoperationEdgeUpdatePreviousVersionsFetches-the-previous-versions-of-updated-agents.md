##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/edge_update_schedules/operation/EdgeUpdatePreviousVersions)Fetches the previous versions of updated agents
**Access policy** : administrator
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### query Parameters
environmentIds |  Array of integers Environment IDs
---|---
edgeGroupIds |  Array of integers Edge Group IDs
### Responses
**200**
OK
**400**
Invalid request
**500**
Server error
get/edge_update_schedules/previous_versions
https://api-docs.portainer.io/api/edge_update_schedules/previous_versions
###  Response samples
  * 200


Content type
application/json
Copy
`{

  *  "property1": "string",

  *  "property2": "string"

 }`
