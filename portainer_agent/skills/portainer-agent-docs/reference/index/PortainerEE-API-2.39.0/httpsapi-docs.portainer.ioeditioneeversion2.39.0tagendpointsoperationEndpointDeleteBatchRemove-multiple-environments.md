##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/endpoints/operation/EndpointDeleteBatch)Remove multiple environments
Remove multiple environments and optionally clean-up associated resources. **Access policy** : Administrator only.
##### Authorizations:
(_ApiKeyAuth_ _jwt_)
##### Request Body schema: application/json
required
List of environments to delete, with optional deleteCluster flag to clean-up associated resources (cloud environments only)
endpoints |  Array of objects (endpoints.endpointDeleteRequest)
---|---
### Responses
**204**
Environment(s) successfully deleted.
**207**
Partial success. Some environments were deleted successfully, while others failed.
**400**
Invalid request payload, such as missing required fields or fields not meeting validation criteria.
**403**
Unauthorized access or operation not allowed.
**500**
Server error occurred while attempting to delete the specified environments.
post/endpoints/delete
https://api-docs.portainer.io/api/endpoints/delete
###  Request samples
  * Payload


Content type
application/json
Copy
Expand all  Collapse all
`{
  *  "endpoints": [
    *  {
      *  "deleteCluster": true,

      *  "id": 0
  }
 ]

 }`
###  Response samples
  * 207


Content type
application/json
Copy
Expand all  Collapse all
`{

  *  "deleted": [
    * 0
 ],

  *  "errors": [
    * 0
 ]

 }`
