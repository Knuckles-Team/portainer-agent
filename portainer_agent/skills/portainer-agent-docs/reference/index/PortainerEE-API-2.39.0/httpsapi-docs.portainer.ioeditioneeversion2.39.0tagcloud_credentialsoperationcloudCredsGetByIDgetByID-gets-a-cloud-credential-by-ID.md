##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/cloud_credentials/operation/cloudCredsGetByID)getByID gets a cloud credential by ID
getByID gets a cloud credential by ID **Access policy** : authenticated
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### path Parameters
idrequired |  string ID of the cloud credential
---|---
### Responses
**200**
OK
**400**
Invalid request
**500**
Server error
get/cloud/credentials/{id}
https://api-docs.portainer.io/api/cloud/credentials/{id}
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
