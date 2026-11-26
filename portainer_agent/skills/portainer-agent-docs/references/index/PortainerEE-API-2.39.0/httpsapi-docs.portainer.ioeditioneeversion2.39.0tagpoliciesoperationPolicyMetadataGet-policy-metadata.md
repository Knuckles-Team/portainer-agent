##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/policies/operation/PolicyMetadata)Get policy metadata
Retrieve policy metadata including minimum agent versions for each policy type. **Access policy** : administrator
##### Authorizations:
_ApiKeyAuth_ _jwt_
### Responses
**200**
Success
**500**
Server error
get/policies/metadata
https://api-docs.portainer.io/api/policies/metadata
###  Response samples
  * 200


Content type
application/json
Copy
Expand all  Collapse all
`{
  *  "minimumAgentVersions": {
    *  "property1": "string",

    *  "property2": "string"
  }

 }`
