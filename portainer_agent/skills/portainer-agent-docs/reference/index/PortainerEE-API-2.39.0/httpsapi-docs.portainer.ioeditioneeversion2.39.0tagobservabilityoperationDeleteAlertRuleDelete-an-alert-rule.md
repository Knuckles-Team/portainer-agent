##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/observability/operation/DeleteAlertRule)Delete an alert rule
Delete a specific alert rule by its identifier. **Access policy** : Authenticated user.
##### Authorizations:
(_ApiKeyAuth_ _jwt_)
##### path Parameters
idrequired |  integer Alert rule identifier
---|---
### Responses
**204**
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
Server error occurred while attempting to delete the alert rule.
delete/observability/alerting/rules/{id}
https://api-docs.portainer.io/api/observability/alerting/rules/{id}
