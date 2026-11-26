##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/docker/operation/dockerImagesList)Fetch images
**Access policy** :
##### Authorizations:
_jwt_
##### path Parameters
environmentIdrequired |  integer Environment identifier
---|---
##### query Parameters
withUsage |  boolean Include image usage information
---|---
### Responses
**200**
Success
**400**
Bad request
**500**
Internal server error
get/docker/{environmentId}/images
https://api-docs.portainer.io/api/docker/{environmentId}/images
###  Response samples
  * 200


Content type
application/json
Copy
Expand all  Collapse all
`[
  *  {
    *  "created": 0,

    *  "id": "string",

    *  "nodeName": "string",

    *  "size": 0,

    *  "tags": [
      * "string"
 ],

    *  "used": true
  }

 ]`
