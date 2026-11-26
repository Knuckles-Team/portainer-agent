##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/observability/operation/GetAllAlertingSettings)Get all alerting settings
Get a list of all alerting settings with their connection status. **Access policy** : Authenticated user.
##### Authorizations:
(_ApiKeyAuth_ _jwt_)
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
Server error occurred while attempting to retrieve all alerting settings.
get/observability/alerting/settings
https://api-docs.portainer.io/api/observability/alerting/settings
###  Response samples
  * 200


Content type
application/json
Copy
Expand all  Collapse all
`[
  * { }

 ]`
