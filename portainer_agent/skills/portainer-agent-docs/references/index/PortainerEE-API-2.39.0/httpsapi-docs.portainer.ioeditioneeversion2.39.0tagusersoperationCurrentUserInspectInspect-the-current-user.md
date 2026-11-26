##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/users/operation/CurrentUserInspect)Inspect the current user
Retrieve details about the current user. User passwords are filtered out, and should never be accessible. **Access policy** : authenticated
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### query Parameters
noEndpointAuthorizationsrequired |  boolean Set to true to avoid including the environment authorizations in the response
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
get/users/me
https://api-docs.portainer.io/api/users/me
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
