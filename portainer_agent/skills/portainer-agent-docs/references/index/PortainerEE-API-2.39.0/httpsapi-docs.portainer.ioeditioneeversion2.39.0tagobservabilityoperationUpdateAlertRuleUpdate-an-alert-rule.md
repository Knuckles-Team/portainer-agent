##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/observability/operation/UpdateAlertRule)Update an alert rule
Update a specific alert rule by its identifier. **Access policy** : Authenticated user.
##### Authorizations:
(_ApiKeyAuth_ _jwt_)
##### path Parameters
idrequired |  integer Alert rule identifier
---|---
##### Request Body schema: application/json
required
Alert rule details
AlertingRule |  object (portaineree.AlertingRule)
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
**404**
Unable to find an alert rule with the specified identifier.
**500**
Server error occurred while attempting to update the alert rule.
put/observability/alerting/rules/{id}
https://api-docs.portainer.io/api/observability/alerting/rules/{id}
###  Request samples
  * Payload


Content type
application/json
Copy
Expand all  Collapse all
`{
  *  "AlertingRule": {
    *  "alertManagerID": 0,

    *  "conditionOperator": ">",

    *  "createdAt": "string",

    *  "createdBy": "string",

    *  "description": "string",

    *  "duration": 0,

    *  "enabled": true,

    *  "id": 0,

    *  "isEditable": true,

    *  "isInternal": true,

    *  "labels": {
      *  "property1": "string",

      *  "property2": "string"
  },

    *  "metricType": "percentage",

    *  "name": "string",

    *  "severity": "critical",

    *  "summary": "string",

    *  "supportedAgentVersion": "string",

    *  "supportedEnvironmentTypes": "docker",

    *  "threshold": 0,

    *  "updatedAt": "string"
  }

 }`
###  Response samples
  * 200


Content type
application/json
Copy
`{ }`
