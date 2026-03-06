##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/websocket/paths/~1websocket~1microk8s-shell/get)Connect to a remote SSH Shell via a websocket
When called, an SSH session to a microk8s cluster node will be created an ssh session will be created and hijacked. **Access policy** : authenticated
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### query Parameters
endpointIdrequired |  integer environment(endpoint) ID of the environment(endpoint) where the resource is located
---|---
nodeIprequired |  string node ip address
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
get/websocket/microk8s-shell
https://api-docs.portainer.io/api/websocket/microk8s-shell
