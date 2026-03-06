##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/endpoints/operation/TrustEdgeEndpoints)Associate one or more Edge environments in the waiting room to environments
Associate one or more Edge environments, currently in the waiting room, with Portainer environments. This action effectively grants trust to these environments. **Access policy** : Administrator only.
##### Authorizations:
(_ApiKeyAuth_ _jwt_)
##### Request Body schema: application/json
required
Information about the environments to trust
EndpointIDs |  Array of integers
---|---
Relations |  object
### Responses
**204**
Environment(s) successfully associated.
**400**
Invalid request payload, such as missing required fields or fields not meeting validation criteria.
**500**
Server error occurred while attempting to associate the environments.
post/endpoints/edge/trust
https://api-docs.portainer.io/api/endpoints/edge/trust
###  Request samples
  * Payload


Content type
application/json
Copy
Expand all  Collapse all
`{

  *  "EndpointIDs": [
    * 0
 ],

  *  "Relations": {
    *  "property1": {
      *  "EdgeGroups": [
        * 0
 ],

      *  "Group": 0,

      *  "Tags": [
        * 0
 ]
  },

    *  "property2": {
      *  "EdgeGroups": [
        * 0
 ],

      *  "Group": 0,

      *  "Tags": [
        * 0
 ]
  }
  }

 }`
