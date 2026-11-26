##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/useractivity/operation/AuthLogsCSV)Download auth logs as CSV
Download auth logs as CSV by provided query **Access policy** : admin
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### query Parameters
before |  integer Results before timestamp (unix)
---|---
after |  integer Results after timestamp (unix)
sortBy |  string Sort by this column
sortDesc |  boolean Sort order, if true will return results by descending order
limit |  integer Limit results
keyword |  string Query logs by this keyword
### Responses
**200**
Success
**500**
Server error
get/useractivity/authlogs.csv
https://api-docs.portainer.io/api/useractivity/authlogs.csv
