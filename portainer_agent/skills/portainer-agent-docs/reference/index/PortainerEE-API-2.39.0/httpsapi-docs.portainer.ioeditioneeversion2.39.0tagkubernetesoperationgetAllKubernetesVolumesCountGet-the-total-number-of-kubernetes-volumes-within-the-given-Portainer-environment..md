##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/kubernetes/operation/getAllKubernetesVolumesCount)Get the total number of kubernetes volumes within the given Portainer environment.
Get the total number of kubernetes volumes within the given environment (Endpoint). The total count depends on the user's role and permissions. The Endpoint ID must be a valid Portainer environment identifier. **Access policy** : Authenticated user.
##### Authorizations:
(_ApiKeyAuth_ _jwt_)
##### path Parameters
idrequired |  integer Environment identifier
---|---
### Responses
**200**
Success
**400**
Invalid request payload, such as missing required fields or fields not meeting validation criteria.
**403**
Unauthorized access or operation not allowed.
**500**
Server error occurred while attempting to retrieve kubernetes volumes count.
get/kubernetes/{id}/volumes/count
https://api-docs.portainer.io/api/kubernetes/{id}/volumes/count
###  Response samples
  * 200


Content type
application/json
Copy
0
`0`
