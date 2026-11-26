##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/resource_controls/operation/ResourceControlCreate)Create a new resource control
Create a new resource control to restrict access to a Docker resource. **Access policy** : administrator
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### Request Body schema: application/json
required
Resource control details
AdministratorsOnly |  boolean Permit access to resource only to admins
---|---
Public |  boolean Permit access to the associated resource to any user
ResourceIDrequired |  string
SubResourceIDs |  Array of strings List of Docker resources that will inherit this access control
Teams |  Array of integers List of team identifiers with access to the associated resource
Typerequired |  integer Enum: 0 1 2 3 4 5 6 7 8 9 Type of Resource. Valid values are: 1 - container, 2 - service 3 - volume, 4 - network, 5 - secret, 6 - stack, 7 - config, 8 - custom template, 9 - azure-container-group
Users |  Array of integers List of user identifiers with access to the associated resource
### Responses
**200**
Success
**400**
Invalid request
**409**
A resource control is already associated to this resource
**500**
Server error
post/resource_controls
https://api-docs.portainer.io/api/resource_controls
###  Request samples
  * Payload


Content type
application/json
Copy
Expand all  Collapse all
`{

  *  "AdministratorsOnly": true,

  *  "Public": true,

  *  "ResourceID": "617c5f22bb9b023d6daab7cba43a57576f83492867bc767d1c59416b065e5f08",

  *  "SubResourceIDs": [
    * "617c5f22bb9b023d6daab7cba43a57576f83492867bc767d1c59416b065e5f08"
 ],

  *  "Teams": [
    *  56,

    * 7
  ],

  *  "Type": 1,

  *  "Users": [
    *  1,

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
