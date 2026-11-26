##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/edge_configs/operation/EdgeConfigState)Update the state of an Edge configuration
Used by the standard edge agent to update the state of an Edge configuration.
##### path Parameters
idrequired |  integer Edge configuration identifier
---|---
staterequired |  integer Edge configuration state
### Responses
**204**
Success
**400**
Invalid request
**403**
Permission denied to access environment
**404**
Edge configuration not found
**500**
Server error
put/edge_configurations/{id}/{state}
https://api-docs.portainer.io/api/edge_configurations/{id}/{state}
