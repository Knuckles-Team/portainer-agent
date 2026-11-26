##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/users/operation/CurrentUserEndpointAuthorizationsInspect)Inspect environment authorizations for the current user
Retrieve environment authorizations for the current user. **Access policy** : authenticated
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### path Parameters
endpointIDrequired |  integer Environment identifier
---|---
### Responses
**200**
Success
**400**
Invalid request
**403**
Permission denied
**404**
User not found
**500**
Server error
get/users/me/auth/{endpointID}
https://api-docs.portainer.io/api/users/me/auth/{endpointID}
###  Response samples
  * 200


Content type
application/json
Copy
Expand all  Collapse all
`{
  *  "Authorizations": {
    *  "property1": true,

    *  "property2": true
  }

 }`
