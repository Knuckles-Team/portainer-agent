##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/edge/paths/~1endpoints~1{id}~1edge~1jobs~1{jobID}~1logs/post)Update the logs collected from an Edge Job
Authorized only if the request is done by an Edge Environment(Endpoint)
##### path Parameters
idrequired |  integer Environment(Endpoint) Id
---|---
jobIDrequired |  integer Job Id
### Responses
**200**
OK
**400**
Bad Request
**403**
Forbidden
**500**
Internal Server Error
post/endpoints/{id}/edge/jobs/{jobID}/logs
https://api-docs.portainer.io/api/endpoints/{id}/edge/jobs/{jobID}/logs
