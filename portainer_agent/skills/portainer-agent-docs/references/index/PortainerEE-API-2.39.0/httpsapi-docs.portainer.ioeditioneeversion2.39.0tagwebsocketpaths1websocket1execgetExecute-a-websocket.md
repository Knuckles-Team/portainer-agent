##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/websocket/paths/~1websocket~1exec/get)Execute a websocket
If the nodeName query parameter is present, the request will be proxied to the underlying agent environment(endpoint). If the nodeName query parameter is not specified, the request will be upgraded to the websocket protocol and an ExecStart operation HTTP request will be created and hijacked.
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### query Parameters
endpointIdrequired |  integer environment(endpoint) ID of the environment(endpoint) where the resource is located
---|---
nodeName |  string node name
tokenrequired |  string JWT token used for authentication against this environment(endpoint)
### Responses
**200**
OK
**400**
Bad Request
**409**
Conflict
**500**
Internal Server Error
get/websocket/exec
https://api-docs.portainer.io/api/websocket/exec
