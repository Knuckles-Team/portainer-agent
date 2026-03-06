##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/helm/operation/HelmUserRepositoriesList)List a users helm repositories
Inspect a user helm repositories. **Access policy** : authenticated
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### path Parameters
idrequired |  integer User identifier
---|---
### Responses
**200**
Success
**400**
Invalid request
**403**
Permission denied
**500**
Server error
get/users/{id}/helm/repositories
https://api-docs.portainer.io/api/users/{id}/helm/repositories
###  Response samples
  * 200


Content type
application/json
Copy
Expand all  Collapse all
`{

  *  "GlobalRepository": "string",

  *  "UserRepositories": [
    *  {
      *  "Id": 1,

      *  "URL": "",

      *  "UserId": 1
  }
 ]

 }`
