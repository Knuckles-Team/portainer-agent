##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/tags/operation/TagCreate)Create a new tag
Create a new tag. **Access policy** : administrator
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### Request Body schema: application/json
required
Tag details
Namerequired |  string
---|---
### Responses
**200**
Success
**409**
This name is already associated to a tag
**500**
Server error
post/tags
https://api-docs.portainer.io/api/tags
###  Request samples
  * Payload


Content type
application/json
Copy
`{
  *  "Name": "org/acme"

 }`
###  Response samples
  * 200


Content type
application/json
Copy
Expand all  Collapse all
`{

  *  "EndpointGroups": {
    *  "property1": true,

    *  "property2": true
  },

  *  "Endpoints": {
    *  "property1": true,

    *  "property2": true
  },

  *  "ID": 1,

  *  "Name": "org/acme"

 }`
