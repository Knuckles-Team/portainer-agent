##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/helm/operation/HelmUserRepositoryCreate)Create a user helm repository
Create a user helm repository. **Access policy** : authenticated
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### path Parameters
idrequired |  integer User identifier
---|---
##### Request Body schema: application/json
required
Helm Repository
url |  string
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
post/users/{id}/helm/repositories
https://api-docs.portainer.io/api/users/{id}/helm/repositories
###  Request samples
  * Payload


Content type
application/json
Copy
`{
  *  "url": "string"

 }`
###  Response samples
  * 200


Content type
application/json
Copy
`{

  *  "Id": 1,

  *  "URL": "",

  *  "UserId": 1

 }`
