##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/cloud_credentials/operation/getAll)getAll cloud credentials
getAll cloud credential **Access policy** : authenticated
##### Authorizations:
_ApiKeyAuth_ _jwt_
### Responses
**200**
OK
**400**
Invalid request
**500**
Server error
get/cloud/credentials
https://api-docs.portainer.io/api/cloud/credentials
###  Response samples
  * 200


Content type
application/json
Copy
Expand all  Collapse all
`{

  *  "created": 1650000000,

  *  "credentials": {
    *  "property1": "string",

    *  "property2": "string"
  },

  *  "id": 1,

  *  "name": "test-env",

  *  "provider": "aws"

 }`
