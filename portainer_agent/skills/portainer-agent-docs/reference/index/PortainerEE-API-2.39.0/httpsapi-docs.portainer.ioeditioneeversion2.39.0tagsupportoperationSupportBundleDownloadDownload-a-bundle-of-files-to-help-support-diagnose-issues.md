##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/support/operation/SupportBundleDownload)Download a bundle of files to help support diagnose issues
**Access policy** : administrator
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
Failed to create support archive
post/support/download
https://api-docs.portainer.io/api/support/download
