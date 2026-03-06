##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/edge_jobs/operation/EdgeJobTasksCollect)Collect the log for a specifc task on an EdgeJob
**Access policy** : administrator
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### path Parameters
idrequired |  integer EdgeJob Id
---|---
taskIDrequired |  integer Task Id
### Responses
**204**
No Content
**400**
Bad Request
**500**
Internal Server Error
**503**
Edge compute features are disabled
post/edge_jobs/{id}/tasks/{taskID}/logs
https://api-docs.portainer.io/api/edge_jobs/{id}/tasks/{taskID}/logs
