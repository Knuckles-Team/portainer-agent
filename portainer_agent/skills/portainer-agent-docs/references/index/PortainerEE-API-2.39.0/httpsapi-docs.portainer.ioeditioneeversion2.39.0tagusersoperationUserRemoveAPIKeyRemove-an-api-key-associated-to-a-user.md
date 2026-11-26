##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/users/operation/UserRemoveAPIKey)Remove an api-key associated to a user
Remove an api-key associated to a user.. Only the calling user or admin can remove api-key. **Access policy** : authenticated
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### path Parameters
idrequired |  integer User identifier
---|---
keyIDrequired |  integer Api Key identifier
### Responses
**204**
Success
**400**
Invalid request
**403**
Permission denied
**404**
Not found
**500**
Server error
delete/users/{id}/tokens/{keyID}
https://api-docs.portainer.io/api/users/{id}/tokens/{keyID}
