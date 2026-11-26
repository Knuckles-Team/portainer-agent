##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/websocket/paths/~1websocket~1pod/get)Execute a websocket on pod
The request will be upgraded to the websocket protocol. **Access policy** : authenticated
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### query Parameters
endpointIdrequired |  integer environment(endpoint) ID of the environment(endpoint) where the resource is located
---|---
namespacerequired |  string namespace where the container is located
podNamerequired |  string name of the pod containing the container
containerNamerequired |  string name of the container
commandrequired |  string command to execute in the container
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
get/websocket/pod
https://api-docs.portainer.io/api/websocket/pod
