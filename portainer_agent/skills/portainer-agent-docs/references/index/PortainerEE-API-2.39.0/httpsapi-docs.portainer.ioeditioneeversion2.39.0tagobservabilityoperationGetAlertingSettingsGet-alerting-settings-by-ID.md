##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/observability/operation/GetAlertingSettings)Get alerting settings by ID
Get specific alerting settings by its identifier, including connection status. **Access policy** : Authenticated user.
##### Authorizations:
(_ApiKeyAuth_ _jwt_)
##### path Parameters
idrequired |  integer Alerting settings identifier
---|---
### Responses
**200**
Success
**401**
Unauthorized access - the user is not authenticated or does not have the necessary permissions. Ensure that you have provided a valid API key or JWT token, and that you have the required permissions.
**403**
Permission denied - the user is authenticated but does not have the necessary permissions to access the requested resource or perform the specified operation. Check your user roles and permissions.
**404**
Unable to find alerting settings with the specified identifier.
**500**
Server error occurred while attempting to retrieve the alerting settings.
get/observability/alerting/settings/{id}
https://api-docs.portainer.io/api/observability/alerting/settings/{id}
###  Response samples
  * 200


Content type
application/json
Copy
`{ }`
