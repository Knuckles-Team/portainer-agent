##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/users/operation/UserList)List users
List Portainer users. Non-administrator users only receive non-administrator accounts. Passwords are never included in any response. **Access policy** : authenticated
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### query Parameters
environmentId |  integer Identifier of the environment(endpoint) that will be used to filter the authorized users
---|---
### Responses
**200**
Success
**400**
Invalid request
**500**
Server error
get/users
https://api-docs.portainer.io/api/users
###  Response samples
  * 200


Content type
application/json
Copy
Expand all  Collapse all
`[
  *  {
    *  "Id": 1,

    *  "Role": 1,

    *  "Username": "bob"
  }

 ]`
