##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/cloud_credentials/operation/Create)Create a cloud credential
Create a cloud credential **Access policy** : authenticated
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### Request Body schema: multipart/form-data
required
providerrequired |  string cloud provider such as aws, aks, civo, digitalocean, etc.
---|---
namerequired |  string name of the credentials such as rnd-test-credential
credentialsrequired |  string credentials in json format
### Responses
**200**
OK
**400**
Invalid request
**500**
Server error
post/cloud/credentials
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
