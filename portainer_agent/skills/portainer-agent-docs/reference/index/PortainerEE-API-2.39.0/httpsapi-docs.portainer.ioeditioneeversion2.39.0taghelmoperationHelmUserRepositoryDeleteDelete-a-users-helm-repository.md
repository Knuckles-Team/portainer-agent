##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/helm/operation/HelmUserRepositoryDelete)Delete a users helm repository
**Access policy** : authenticated
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### path Parameters
idrequired |  integer User identifier
---|---
repositoryIDrequired |  integer Repository identifier
### Responses
**204**
Success
**400**
Invalid request
**403**
Permission denied
**500**
Server error
delete/users/{id}/helm/repositories/{repositoryID}
https://api-docs.portainer.io/api/users/{id}/helm/repositories/{repositoryID}
