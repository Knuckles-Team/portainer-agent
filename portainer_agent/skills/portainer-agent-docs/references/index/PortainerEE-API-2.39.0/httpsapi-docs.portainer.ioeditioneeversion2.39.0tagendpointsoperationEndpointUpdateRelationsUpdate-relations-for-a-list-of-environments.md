##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/endpoints/operation/EndpointUpdateRelations)Update relations for a list of environments
Update relations for a list of environments Edge groups, tags and environment group can be updated.
**Access policy** : administrator
##### Authorizations:
_jwt_
##### Request Body schema: application/json
required
Environment relations data
Relations |  object
---|---
### Responses
**204**
Success
**400**
Invalid request
**401**
Unauthorized
**404**
Not found
**500**
Server error
put/endpoints/relations
https://api-docs.portainer.io/api/endpoints/relations
###  Request samples
  * Payload


Content type
application/json
Copy
Expand all  Collapse all
`{
  *  "Relations": {
    *  "property1": {
      *  "EdgeGroups": [
        * 0
 ],

      *  "Group": 0,

      *  "Tags": [
        * 0
 ]
  },

    *  "property2": {
      *  "EdgeGroups": [
        * 0
 ],

      *  "Group": 0,

      *  "Tags": [
        * 0
 ]
  }
  }

 }`
