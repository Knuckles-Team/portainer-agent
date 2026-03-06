##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/users/operation/UserUpdate)Update a user
Update user details. A regular user account can only update his details. A regular user account cannot change their username or role. **Access policy** : authenticated
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### path Parameters
idrequired |  integer User identifier
---|---
##### Request Body schema: application/json
required
User details
NewPasswordrequired |  string
---|---
Passwordrequired |  string
Rolerequired |  integer Enum: 0 1 2 3 User role 1 = administrator account 2 = regular account 3 = edge administrator account
Theme |  object (users.themePayload)
UseCacherequired |  boolean
Usernamerequired |  string
### Responses
**200**
Success
**400**
Invalid request
**403**
Permission denied
**404**
User not found
**409**
Username already exist or Edge Compute features are not enabled
**500**
Server error
put/users/{id}
https://api-docs.portainer.io/api/users/{id}
###  Request samples
  * Payload


Content type
application/json
Copy
Expand all  Collapse all
`{

  *  "NewPassword": "asfj2emv",

  *  "Password": "cg9Wgky3",

  *  "Role": 2,

  *  "Theme": {
    *  "color": "dark",

    *  "subtleUpgradeButton": false
  },

  *  "UseCache": true,

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
