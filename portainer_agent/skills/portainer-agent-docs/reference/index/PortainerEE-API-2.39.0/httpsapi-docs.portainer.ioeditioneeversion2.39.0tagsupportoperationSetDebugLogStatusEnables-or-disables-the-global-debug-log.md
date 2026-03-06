##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/support/operation/SetDebugLogStatus)Enables or disables the global debug log
Enables the debug log by setting the global log level to debug or info if disabled **Access policy** : administrator
##### Authorizations:
(_ApiKeyAuth_ _jwt_)
##### Request Body schema: application/json
required
Debug log should be set to enabled or disabled
debugLogEnabled |  boolean
---|---
### Responses
**200**
Success
**400**
Invalid request payload
**500**
Server error occurred.
put/support/debug_log
https://api-docs.portainer.io/api/support/debug_log
###  Request samples
  * Payload


Content type
application/json
Copy
`{
  *  "debugLogEnabled": true

 }`
###  Response samples
  * 200


Content type
application/json
Copy
`{
  *  "debugLogEnabled": true

 }`
