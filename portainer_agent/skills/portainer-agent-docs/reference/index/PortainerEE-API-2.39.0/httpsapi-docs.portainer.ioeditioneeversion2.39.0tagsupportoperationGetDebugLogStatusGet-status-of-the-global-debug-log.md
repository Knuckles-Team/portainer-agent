##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/support/operation/GetDebugLogStatus)Get status of the global debug log
Checks if the global log level is enabled **Access policy** : administrator
##### Authorizations:
(_ApiKeyAuth_ _jwt_)
### Responses
**200**
Success
**500**
Server error occurred.
get/support/debug_log
https://api-docs.portainer.io/api/support/debug_log
###  Response samples
  * 200


Content type
application/json
Copy
`{
  *  "debugLogEnabled": true

 }`
