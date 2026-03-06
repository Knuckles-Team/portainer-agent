##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/observability/operation/UpdateAlertingSettings)Update alerting settings
Update alerting settings and manage internal AlertManager lifecycle. **Access policy** : Authenticated user.
##### Authorizations:
(_ApiKeyAuth_ _jwt_)
##### Request Body schema: application/json
required
Alerting settings details
AlertingSettings |  object (portaineree.AlertingSettings)
---|---
### Responses
**200**
Success
**400**
Invalid request payload, such as missing required fields or fields not meeting validation criteria.
**401**
Unauthorized access - the user is not authenticated or does not have the necessary permissions. Ensure that you have provided a valid API key or JWT token, and that you have the required permissions.
**403**
Permission denied - the user is authenticated but does not have the necessary permissions to access the requested resource or perform the specified operation. Check your user roles and permissions.
**500**
Server error occurred while attempting to update the alerting settings.
put/observability/alerting/settings
https://api-docs.portainer.io/api/observability/alerting/settings
###  Request samples
  * Payload


Content type
application/json
Copy
Expand all  Collapse all
`{
  *  "AlertingSettings": {
    *  "createdAt": "string",

    *  "createdBy": "string",

    *  "enabled": true,

    *  "id": 0,

    *  "isInternal": true,

    *  "name": "string",

    *  "notificationChannels": [
      *  {
        *  "config": {
          *  "property1": null,

          *  "property2": null
  },

        *  "enabled": true,

        *  "id": 0,

        *  "name": "string",

        *  "type": "slack"
  }
 ],

    *  "portainerURL": "string",

    *  "status": "disabled",

    *  "uptime": "string",

    *  "url": "string"
  }

 }`
###  Response samples
  * 200


Content type
application/json
Copy
`{ }`
