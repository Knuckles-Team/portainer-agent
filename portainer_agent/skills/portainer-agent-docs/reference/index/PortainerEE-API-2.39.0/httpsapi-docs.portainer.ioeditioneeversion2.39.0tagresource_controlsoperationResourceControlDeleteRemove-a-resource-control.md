##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/resource_controls/operation/ResourceControlDelete)Remove a resource control
Remove a resource control. **Access policy** : administrator
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### path Parameters
idrequired |  integer Resource control identifier
---|---
### Responses
**204**
Success
**400**
Invalid request
**404**
Resource control not found
**500**
Server error
delete/resource_controls/{id}
https://api-docs.portainer.io/api/resource_controls/{id}
