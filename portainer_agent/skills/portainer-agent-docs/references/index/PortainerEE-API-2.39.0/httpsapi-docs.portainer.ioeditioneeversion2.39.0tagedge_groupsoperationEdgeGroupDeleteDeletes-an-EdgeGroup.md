##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/edge_groups/operation/EdgeGroupDelete)Deletes an EdgeGroup
**Access policy** : administrator
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### path Parameters
idrequired |  integer EdgeGroup Id
---|---
### Responses
**204**
No Content
**409**
Edge group is in use by an Edge stack, Edge job or Edge config
**500**
Server error
**503**
Edge compute features are disabled
delete/edge_groups/{id}
https://api-docs.portainer.io/api/edge_groups/{id}
