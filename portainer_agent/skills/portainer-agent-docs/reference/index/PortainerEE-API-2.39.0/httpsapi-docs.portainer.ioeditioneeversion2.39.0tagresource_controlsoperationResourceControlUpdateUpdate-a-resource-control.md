##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/resource_controls/operation/ResourceControlUpdate)Update a resource control
Update a resource control **Access policy** : authenticated
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### path Parameters
idrequired |  integer Resource control identifier
---|---
##### Request Body schema: application/json
required
Resource control details
AdministratorsOnly |  boolean Permit access to resource only to admins
---|---
Public |  boolean Permit access to the associated resource to any user
Teams |  Array of integers List of team identifiers with access to the associated resource
Users |  Array of integers List of user identifiers with access to the associated resource
### Responses
**200**
Success
**400**
Invalid request
**403**
Unauthorized
**404**
Resource control not found
**500**
Server error
put/resource_controls/{id}
https://api-docs.portainer.io/api/resource_controls/{id}
###  Request samples
  * Payload


Content type
application/json
Copy
Expand all  Collapse all
`{

  *  "AdministratorsOnly": true,

  *  "Public": true,

  *  "Teams": [
    * 7
 ],

  *  "Users": [
    * 4
 ]

 }`
###  Response samples
  * 200


Content type
application/json
Copy
Expand all  Collapse all
`{

  *  "AccessLevel": 0,

  *  "AdministratorsOnly": true,

  *  "Id": 1,

  *  "OwnerId": 0,

  *  "Public": true,

  *  "ResourceId": "617c5f22bb9b023d6daab7cba43a57576f83492867bc767d1c59416b065e5f08",

  *  "SubResourceIds": [
    * "617c5f22bb9b023d6daab7cba43a57576f83492867bc767d1c59416b065e5f08"
 ],

  *  "System": true,

  *  "TeamAccesses": [
    *  {
      *  "AccessLevel": 0,

      *  "TeamId": 0
  }
 ],

  *  "Type": 1,

  *  "UserAccesses": [
    *  {
      *  "AccessLevel": 0,

      *  "UserId": 0
  }
 ]

 }`
