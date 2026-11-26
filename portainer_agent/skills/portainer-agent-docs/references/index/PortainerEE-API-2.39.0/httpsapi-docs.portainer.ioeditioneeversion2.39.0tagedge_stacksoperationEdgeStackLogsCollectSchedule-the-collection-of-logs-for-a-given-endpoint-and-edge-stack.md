##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/edge_stacks/operation/EdgeStackLogsCollect)Schedule the collection of logs for a given endpoint and edge stack
**Access policy** : administrator
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### path Parameters
idrequired |  integer EdgeStack Id
---|---
endpoint_idrequired |  integer Environment Id
##### query Parameters
tail |  integer Number of lines to request for the logs
---|---
container_id |  string Container Id
since |  string Start time to request for the logs
until |  string End time to request for the logs
### Responses
**204**
No Content
**400**
Bad Request
**404**
Not Found
**500**
Internal Server Error
**503**
Edge compute features are disabled
put/edge_stacks/{id}/logs/{endpoint_id}
https://api-docs.portainer.io/api/edge_stacks/{id}/logs/{endpoint_id}
