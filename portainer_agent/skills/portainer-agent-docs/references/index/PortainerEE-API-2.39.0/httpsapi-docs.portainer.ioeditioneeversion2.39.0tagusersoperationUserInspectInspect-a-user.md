##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/users/operation/UserInspect)Inspect a user
Retrieve details about a user. User passwords are filtered out, and should never be accessible. **Access policy** : authenticated
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
**404**
User not found
**500**
Server error
get/users/{id}
https://api-docs.portainer.io/api/users/{id}
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
