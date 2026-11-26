##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/tags/operation/TagDelete)Remove a tag
Remove a tag. **Access policy** : administrator
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### path Parameters
idrequired |  integer Tag identifier
---|---
### Responses
**204**
Success
**400**
Invalid request
**403**
Permission denied
**404**
Tag not found
**500**
Server error
delete/tags/{id}
https://api-docs.portainer.io/api/tags/{id}
