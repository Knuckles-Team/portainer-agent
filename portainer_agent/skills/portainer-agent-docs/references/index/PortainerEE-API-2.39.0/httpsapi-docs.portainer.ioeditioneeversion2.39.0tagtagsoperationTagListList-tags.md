##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/tags/operation/TagList)List tags
List tags. **Access policy** : authenticated
##### Authorizations:
_ApiKeyAuth_ _jwt_
### Responses
**200**
Success
**500**
Server error
get/tags
https://api-docs.portainer.io/api/tags
###  Response samples
  * 200


Content type
application/json
Copy
Expand all  Collapse all
`[
  *  {
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
  }

 ]`
