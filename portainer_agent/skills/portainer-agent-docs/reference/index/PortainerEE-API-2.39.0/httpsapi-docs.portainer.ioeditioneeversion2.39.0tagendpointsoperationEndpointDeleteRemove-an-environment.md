##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/endpoints/operation/EndpointDelete)Remove an environment
Remove the environment associated to the specified identifier and optionally clean-up associated resources. **Access policy** : Administrator only.
##### Authorizations:
(_ApiKeyAuth_ _jwt_)
##### path Parameters
idrequired |  integer Environment(Endpoint) identifier
---|---
### Responses
**204**
Environment successfully deleted.
**400**
Invalid request payload, such as missing required fields or fields not meeting validation criteria.
**403**
Unauthorized access or operation not allowed.
**404**
Unable to find the environment with the specified identifier inside the database.
**500**
Server error occurred while attempting to delete the environment.
delete/endpoints/{id}
https://api-docs.portainer.io/api/endpoints/{id}
