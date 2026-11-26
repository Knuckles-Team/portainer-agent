##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/intel/operation/openAMTActivate)Activate OpenAMT device and associate to agent endpoint  Deprecated
Activate OpenAMT device and associate to agent endpoint **Access policy** : administrator
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
post/open_amt/{id}/activate
https://api-docs.portainer.io/api/open_amt/{id}/activate
