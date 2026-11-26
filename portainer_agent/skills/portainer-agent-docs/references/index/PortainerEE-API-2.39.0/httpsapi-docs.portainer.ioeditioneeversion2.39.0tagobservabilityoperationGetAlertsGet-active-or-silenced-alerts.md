##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/observability/operation/GetAlerts)Get active or silenced alerts
Get a list of active or silenced alerts from the AlertManager. **Access policy** : Authenticated user.
##### Authorizations:
(_ApiKeyAuth_ _jwt_)
##### query Parameters
statusrequired |  string Status of alerts to retrieve. Possible values: 'active' or 'silenced'.
---|---
### Responses
**200**
Success
**401**
Unauthorized access - the user is not authenticated or does not have the necessary permissions. Ensure that you have provided a valid API key or JWT token, and that you have the required permissions.
**403**
Permission denied - the user is authenticated but does not have the necessary permissions to access the requested resource or perform the specified operation. Check your user roles and permissions.
**500**
Server error occurred while attempting to retrieve active or silenced alerts.
get/observability/alerting/alerts
https://api-docs.portainer.io/api/observability/alerting/alerts
###  Response samples
  * 200


Content type
application/json
Copy
Expand all  Collapse all
`[
  * { }

 ]`
