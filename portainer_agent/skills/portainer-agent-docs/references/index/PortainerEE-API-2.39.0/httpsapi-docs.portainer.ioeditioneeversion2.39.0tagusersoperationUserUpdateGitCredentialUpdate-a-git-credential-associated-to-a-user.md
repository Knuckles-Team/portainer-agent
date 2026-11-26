##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/users/operation/UserUpdateGitCredential)Update a git-credential associated to a user
Update a git-credential associated to a user.. Only the calling user can update git-credential **Access policy** : authenticated
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### path Parameters
idrequired |  integer User identifier
---|---
credentialIDrequired |  integer Git Credential identifier
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
put/users/{id}/gitcredentials/{credentialID}
https://api-docs.portainer.io/api/users/{id}/gitcredentials/{credentialID}
