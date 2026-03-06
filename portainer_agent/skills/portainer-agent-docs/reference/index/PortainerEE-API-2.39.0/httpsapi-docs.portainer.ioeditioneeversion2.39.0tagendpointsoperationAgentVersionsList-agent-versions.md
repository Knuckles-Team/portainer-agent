##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/endpoints/operation/AgentVersions)List agent versions
List all agent versions based on the current user authorizations and query parameters. **Access policy** : restricted
##### Authorizations:
_ApiKeyAuth_ _jwt_
### Responses
**200**
List of available agent versions
**500**
Server error
get/endpoints/agent_versions
https://api-docs.portainer.io/api/endpoints/agent_versions
###  Response samples
  * 200


Content type
application/json
Copy
`[
  * "string"

 ]`
