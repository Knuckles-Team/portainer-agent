##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/settings/operation/SettingsAdditionalFunctionalityInspect)Retrieve Portainer additional functionality settings
Retrieve Portainer additional functionality settings. **Access policy** : authenticated
##### Authorizations:
_ApiKeyAuth_ _jwt_
### Responses
**200**
Success
**500**
Server error
get/settings/additional_functionality
https://api-docs.portainer.io/api/settings/additional_functionality
###  Response samples
  * 200


Content type
application/json
Copy
Expand all  Collapse all
`{
  *  "additionalFunctionality": {
    *  "Observability": true
 }

 }`
