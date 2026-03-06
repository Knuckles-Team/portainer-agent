##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/websocket/paths/~1websocket~1attach/get)Attach a websocket
If the nodeName query parameter is present, the request will be proxied to the underlying agent environment(endpoint). If the nodeName query parameter is not specified, the request will be upgraded to the websocket protocol and an AttachStart operation HTTP request will be created and hijacked. **Access policy** : authenticated
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
**403**
Forbidden
**404**
Not Found
**500**
Internal Server Error
get/websocket/attach
https://api-docs.portainer.io/api/websocket/attach
