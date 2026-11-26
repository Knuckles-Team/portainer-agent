##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/users/operation/UserCreate)Create a new user
Create a new Portainer user. Only administrators can create users. **Access policy** : restricted
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### Request Body schema: application/json
required
User details
Passwordrequired |  string
---|---
Rolerequired |  integer Enum: 0 1 2 User role 1 = administrator account 2 = regular account
Usernamerequired |  string
### Responses
**200**
Success
**400**
Invalid request
**403**
Permission denied
**409**
User already exists
**500**
Server error
post/users
https://api-docs.portainer.io/api/users
###  Request samples
  * Payload


Content type
application/json
Copy
`{

  *  "Password": "cg9Wgky3",

  *  "Role": 1,

  *  "Username": "bob"

 }`
###  Response samples
  * 200


Content type
application/json
Copy
Expand all  Collapse all
`{

  *  "EndpointAuthorizations": {
    *  "property1": {
      *  "property1": true,

      *  "property2": true
  },

    *  "property2": {
      *  "property1": true,

      *  "property2": true
  }
  },

  *  "Id": 1,

  *  "PortainerAuthorizations": {
    *  "property1": true,

    *  "property2": true
  },

  *  "Role": 1,

  *  "ThemeSettings": {
    *  "color": "dark",

    *  "subtleUpgradeButton": true
  },

  *  "TokenIssueAt": 1639408208,

  *  "UseCache": true,

  *  "UserTheme": "dark",

  *  "Username": "bob"

 }`
