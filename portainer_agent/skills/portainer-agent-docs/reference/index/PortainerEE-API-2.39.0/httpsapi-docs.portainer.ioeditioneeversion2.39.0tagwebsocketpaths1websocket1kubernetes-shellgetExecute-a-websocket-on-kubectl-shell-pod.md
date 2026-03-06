##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/websocket/paths/~1websocket~1kubernetes-shell/get)Execute a websocket on kubectl shell pod
The request will be upgraded to the websocket protocol. The request will proxy input from the client to the pod via long-lived websocket connection. **Access policy** : authenticated
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### query Parameters
endpointIdrequired |  integer environment(endpoint) ID of the environment(endpoint) where the resource is located
---|---
tokenrequired |  string JWT token used for authentication against this environment(endpoint)
### Responses
**200**
Success
**400**
Invalid request
**403**
Permission denied
**500**
Server error
get/websocket/kubernetes-shell
https://api-docs.portainer.io/api/websocket/kubernetes-shell
