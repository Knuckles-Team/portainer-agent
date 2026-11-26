##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/users/operation/UserNamespaces)Retrieves all k8s namespaces for an user
Retrieves user's role authorizations of all namespaces in all k8s environments(endpoints) **Access policy** : restricted
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
get/users/{id}/namespaces
https://api-docs.portainer.io/api/users/{id}/namespaces
###  Response samples
  * 200


Content type
application/json
Copy
Expand all  Collapse all
`{

  *  "property1": {
    *  "property1": {
      *  "property1": true,

      *  "property2": true
  },

    *  "property2": {
      *  "property1": true,

      *  "property2": true
  }
  },

  *  "property2": {
    *  "property1": {
      *  "property1": true,

      *  "property2": true
  },

    *  "property2": {
      *  "property1": true,

      *  "property2": true
  }
  }

 }`
