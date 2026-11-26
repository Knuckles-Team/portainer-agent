##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/edge_stacks/operation/EdgeStackLogsDelete)Deletes the available logs for a given edge stack and endpoint
**Access policy** : administrator
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### path Parameters
idrequired |  integer EdgeStack Id
---|---
endpoint_idrequired |  integer Endpoint Id
### Responses
**204**
No Content
**400**
Bad Request
**503**
Edge compute features are disabled
delete/edge_stacks/{id}/logs/{endpoint_id}
https://api-docs.portainer.io/api/edge_stacks/{id}/logs/{endpoint_id}
