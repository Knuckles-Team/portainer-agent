##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/auto_updates/operation/AutoUpdateList)List auto updates
**Access policy** : administrator
##### Authorizations:
_ApiKeyAuth_ _jwt_
### Responses
**200**
OK
**403**
Forbidden
**500**
Internal Server Error
get/auto_updates
https://api-docs.portainer.io/api/auto_updates
###  Response samples
  * 200


Content type
application/json
Copy
Expand all  Collapse all
`{
  *  "autoUpdates": [
    *  {
      *  "doneAtUnix": 0,

      *  "startedAtUnix": 0,

      *  "status": "inProgress",

      *  "version": "string"
  }
 ]

 }`
