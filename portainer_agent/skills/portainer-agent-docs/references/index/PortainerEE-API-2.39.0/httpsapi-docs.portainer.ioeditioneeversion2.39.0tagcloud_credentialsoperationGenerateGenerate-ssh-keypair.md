##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/cloud_credentials/operation/Generate)Generate ssh keypair
Generate an ssh public / private keypair **Access policy** : authenticated
##### Authorizations:
_ApiKeyAuth_ _jwt_
### Responses
**200**
OK
**500**
Server error
post/sshkeygen
https://api-docs.portainer.io/api/sshkeygen
###  Response samples
  * 200


Content type
application/json
Copy
`{

  *  "private": "string",

  *  "public": "string"

 }`
