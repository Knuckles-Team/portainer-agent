##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/cloud_credentials/operation/cloudCredsDelete)Delete a cloud credential
Delete a cloud credential **Access policy** : authenticated
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
**403**
Forbidden: the requested credential is associated with endpoint(s)
**500**
Server error
delete/cloud/credentials/{id}
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
