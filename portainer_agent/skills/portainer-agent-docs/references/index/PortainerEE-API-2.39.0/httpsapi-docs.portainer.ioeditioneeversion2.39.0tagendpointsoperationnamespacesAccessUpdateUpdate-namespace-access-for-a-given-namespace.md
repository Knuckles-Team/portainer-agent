##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/endpoints/operation/namespacesAccessUpdate)Update namespace access for a given namespace
Update the access permissions on a namespace in the given environment. This endpoint allows adding or removing users and teams that can access the specified namespace. Please note that users or teams must be added to the environment before they can be added to the namespace. **Access policy** : Restricted. User must be an administrator or have appropriate permissions to modify namespace access.
##### Authorizations:
(_ApiKeyAuth_ _jwt_)
##### path Parameters
idrequired |  integer Environment identifier
---|---
rpnrequired |  integer Namespace identifier
##### Request Body schema: application/json
required
Payload containing lists of users and teams to add or remove access for
TeamsToAdd |  Array of integers
---|---
TeamsToRemove |  Array of integers
UsersToAdd |  Array of integers
UsersToRemove |  Array of integers
### Responses
**204**
Success - Access permissions were successfully updated
**400**
Invalid request payload, such as missing required fields or fields not meeting validation criteria.
**403**
Permission denied - the user is authenticated but does not have the necessary permissions to access the requested resource or perform the specified operation. Check your user roles and permissions.
**404**
Unable to find an environment with the specified identifier.
**500**
Server error occurred while attempting to update namespace access permissions.
put/endpoints/{id}/pools/{rpn}/access
https://api-docs.portainer.io/api/endpoints/{id}/pools/{rpn}/access
###  Request samples
  * Payload


Content type
application/json
Copy
Expand all  Collapse all
`{

  *  "TeamsToAdd": [
    * 0
 ],

  *  "TeamsToRemove": [
    * 0
 ],

  *  "UsersToAdd": [
    * 0
 ],

  *  "UsersToRemove": [
    * 0
 ]

 }`
