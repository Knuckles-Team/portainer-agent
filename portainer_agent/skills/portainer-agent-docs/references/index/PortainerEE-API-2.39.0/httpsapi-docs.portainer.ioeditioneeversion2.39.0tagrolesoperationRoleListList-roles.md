##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/roles/operation/RoleList)List roles
List all roles available for use **Access policy** : authenticated
##### Authorizations:
_ApiKeyAuth_ _jwt_
### Responses
**200**
Success
**500**
Server error
get/roles
https://api-docs.portainer.io/api/roles
###  Response samples
  * 200


Content type
application/json
Copy
Expand all  Collapse all
`[
  *  {
    *  "Authorizations": {
      *  "property1": true,

      *  "property2": true
  },

    *  "Description": "Read-only access of all resources in an environment(endpoint)",

    *  "Id": 1,

    *  "Name": "HelpDesk",

    *  "Priority": 0,

    *  "Scope": {
      *  "property1": [
        * "string"
 ],

      *  "property2": [
        * "string"
 ]
  }
  }

 ]`
