##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/policies/operation/PolicyDelete)Delete a policy
Delete a policy. **Access policy** : administrator
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### path Parameters
idrequired |  integer Policy identifier
---|---
### Responses
**204**
Success
**400**
Invalid request
**404**
Policy not found
**500**
Server error
delete/policies/{id}
https://api-docs.portainer.io/api/policies/{id}
