##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/edge_configs/operation/EdgeConfigFiles)Get the files for an Edge configuration
Used by the standard edge agent to retrieve the files for an Edge configuration.
##### path Parameters
idrequired |  integer Edge configuration identifier
---|---
### Responses
**200**
Success
**400**
Invalid request
**403**
Permission denied to access environment
**404**
Edge configuration not found
**500**
Server error
get/edge_configurations/{id}/files
https://api-docs.portainer.io/api/edge_configurations/{id}/files
