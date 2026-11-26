##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/intel/operation/OpenAMTDevices)Fetch OpenAMT managed devices information for endpoint  Deprecated
Fetch OpenAMT managed devices information for endpoint **Access policy** : administrator
##### Authorizations:
_jwt_
##### path Parameters
idrequired |  integer Environment(Endpoint) identifier
---|---
### Responses
**200**
Success
**400**
Invalid request
**403**
Permission denied to access settings
**500**
Server error
get/open_amt/{id}/devices
https://api-docs.portainer.io/api/open_amt/{id}/devices
