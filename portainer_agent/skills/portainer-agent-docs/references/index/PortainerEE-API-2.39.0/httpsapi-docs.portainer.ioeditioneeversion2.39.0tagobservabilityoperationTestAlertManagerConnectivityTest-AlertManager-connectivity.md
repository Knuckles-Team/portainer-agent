##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/observability/operation/TestAlertManagerConnectivity)Test AlertManager connectivity
Test connectivity to an AlertManager instance by retrieving its status. **Access policy** : Authenticated user.
##### Authorizations:
(_ApiKeyAuth_ _jwt_)
##### query Parameters
urlrequired |  string AlertManager URL
---|---
### Responses
**200**
Success
**401**
Unauthorized access - the user is not authenticated or does not have the necessary permissions. Ensure that you have provided a valid API key or JWT token, and that you have the required permissions.
**403**
Permission denied - the user is authenticated but does not have the necessary permissions to access the requested resource or perform the specified operation. Check your user roles and permissions.
**500**
Server error occurred while attempting to test AlertManager connectivity.
get/observability/alerting/connectivity
https://api-docs.portainer.io/api/observability/alerting/connectivity
###  Response samples
  * 200


Content type
application/json
Copy
`{ }`
