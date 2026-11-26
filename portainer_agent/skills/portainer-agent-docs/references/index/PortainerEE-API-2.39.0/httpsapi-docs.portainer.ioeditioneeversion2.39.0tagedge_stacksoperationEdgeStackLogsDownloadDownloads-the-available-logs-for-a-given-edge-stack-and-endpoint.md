##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/edge_stacks/operation/EdgeStackLogsDownload)Downloads the available logs for a given edge stack and endpoint
**Access policy** : administrator
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### path Parameters
idrequired |  integer EdgeStack Id
---|---
endpoint_idrequired |  integer Endpoint Id
### Responses
**200**
OK
**400**
Bad Request
**404**
Not Found
**500**
Internal Server Error
**503**
Edge compute features are disabled
get/edge_stacks/{id}/logs/{endpoint_id}/file
https://api-docs.portainer.io/api/edge_stacks/{id}/logs/{endpoint_id}/file
