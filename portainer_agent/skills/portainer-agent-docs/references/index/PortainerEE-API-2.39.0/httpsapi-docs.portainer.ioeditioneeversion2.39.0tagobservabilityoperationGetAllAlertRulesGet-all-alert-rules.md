##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/observability/operation/GetAllAlertRules)Get all alert rules
Get a list of all alert rules from the AlertManager. **Access policy** : Authenticated user.
##### Authorizations:
(_ApiKeyAuth_ _jwt_)
### Responses
**200**
Success
**401**
Unauthorized access - the user is not authenticated or does not have the necessary permissions. Ensure that you have provided a valid API key or JWT token, and that you have the required permissions.
**403**
Permission denied - the user is authenticated but does not have the necessary permissions to access the requested resource or perform the specified operation. Check your user roles and permissions.
**500**
Server error occurred while attempting to retrieve all alert rules.
get/observability/alerting/rules
https://api-docs.portainer.io/api/observability/alerting/rules
###  Response samples
  * 200


Content type
application/json
Copy
Expand all  Collapse all
`[
  * { }

 ]`
