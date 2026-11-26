##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/users/operation/UserAdminInit)Initialize administrator account
Initialize the 'admin' user account. **Access policy** : public
##### Request Body schema: application/json
required
User details
Passwordrequired |  string Password for the admin user
---|---
Usernamerequired |  string Username for the admin user
### Responses
**200**
Success
**400**
Invalid request
**409**
Admin user already initialized
**500**
Server error
post/users/admin/init
https://api-docs.portainer.io/api/users/admin/init
###  Request samples
  * Payload


Content type
application/json
Copy
`{

  *  "Password": "admin-password",

  *  "Username": "admin"

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
