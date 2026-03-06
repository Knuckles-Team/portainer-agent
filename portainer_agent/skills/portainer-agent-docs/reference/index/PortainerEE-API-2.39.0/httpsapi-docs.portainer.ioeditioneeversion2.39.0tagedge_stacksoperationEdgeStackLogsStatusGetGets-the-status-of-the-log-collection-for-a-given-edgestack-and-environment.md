##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/edge_stacks/operation/EdgeStackLogsStatusGet)Gets the status of the log collection for a given edgestack and environment
**Access policy** : administrator
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### path Parameters
idrequired |  integer EdgeStack Id
---|---
endpoint_idrequired |  integer Environment Id
### Responses
**200**
OK
**400**
Bad Request
**500**
Internal Server Error
**503**
Edge compute features are disabled
get/edge_stacks/{id}/logs/{endpoint_id}
https://api-docs.portainer.io/api/edge_stacks/{id}/logs/{endpoint_id}
