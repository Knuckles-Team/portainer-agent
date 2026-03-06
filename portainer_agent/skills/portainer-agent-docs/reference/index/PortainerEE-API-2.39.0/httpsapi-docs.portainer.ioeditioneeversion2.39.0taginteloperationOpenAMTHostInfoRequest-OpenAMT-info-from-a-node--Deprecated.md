##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/intel/operation/OpenAMTHostInfo)Request OpenAMT info from a node  Deprecated
Request OpenAMT info from a node **Access policy** : administrator
##### Authorizations:
_jwt_
##### path Parameters
idrequired |  integer Environment identifier
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
get/open_amt/{id}/info
https://api-docs.portainer.io/api/open_amt/{id}/info
