##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/motd/operation/MOTD)fetches the message of the day
**Access policy** : restricted
##### Authorizations:
_ApiKeyAuth_ _jwt_
### Responses
**200**
OK
get/motd
https://api-docs.portainer.io/api/motd
###  Response samples
  * 200


Content type
application/json
Copy
Expand all  Collapse all
`{

  *  "ContentLayout": {
    *  "property1": "string",

    *  "property2": "string"
  },

  *  "Hash": [
    * 0
 ],

  *  "Message": "string",

  *  "Style": "string",

  *  "Title": "string"

 }`
