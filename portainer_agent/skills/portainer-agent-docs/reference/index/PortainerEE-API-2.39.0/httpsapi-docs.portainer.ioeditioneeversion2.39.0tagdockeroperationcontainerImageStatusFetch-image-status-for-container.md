##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/docker/operation/containerImageStatus)Fetch image status for container
**Access policy** :
##### Authorizations:
_jwt_
##### path Parameters
environmentIdrequired |  integer Environment identifier
---|---
containerIdrequired |  integer Container identifier
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
get/docker/{environmentId}/containers/{containerId}/image_status
https://api-docs.portainer.io/api/docker/{environmentId}/containers/{containerId}/image_status
###  Response samples
  * 200


Content type
application/json
Copy
`{

  *  "Message": "string",

  *  "Status": "processing"

 }`
