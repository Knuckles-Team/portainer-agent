##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/stacks/operation/stackImagesStatus)Fetch image status for stack
**Access policy** :
##### Authorizations:
_jwt_
##### path Parameters
idrequired |  integer Stack identifier
---|---
##### query Parameters
refresh |  boolean Refresh will force a refresh of the image status cache
---|---
### Responses
**200**
Success
**400**
Bad request
**500**
Internal server error
get/stacks/{id}/images_status
https://api-docs.portainer.io/api/stacks/{id}/images_status
###  Response samples
  * 200


Content type
application/json
Copy
`{

  *  "Message": "string",

  *  "Status": "processing"

 }`
