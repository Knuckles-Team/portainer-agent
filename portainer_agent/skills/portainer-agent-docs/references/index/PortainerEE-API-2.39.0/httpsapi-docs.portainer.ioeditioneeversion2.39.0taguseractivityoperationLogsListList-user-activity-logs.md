##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/useractivity/operation/LogsList)List user activity logs
List logs by provided query **Access policy** : admin
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### query Parameters
offset |  integer Pagination offset
---|---
limit |  integer Limit results
before |  integer Results before timestamp (unix)
after |  integer Results after timestamp (unix)
sortBy |  string Sort by this column
sortDesc |  boolean Sort order, if true will return results by descending order
keyword |  string Query logs by this keyword
context |  Array of strings Filter by context
username |  Array of strings Filter by usernames
### Responses
**200**
Success
**500**
Server error
get/useractivity/logs
https://api-docs.portainer.io/api/useractivity/logs
###  Response samples
  * 200


Content type
application/json
Copy
Expand all  Collapse all
`{

  *  "logs": [
    *  {
      *  "action": "string",

      *  "context": "string",

      *  "id": 0,

      *  "payload": [
        * 0
 ],

      *  "timestamp": 0,

      *  "username": "string"
  }
 ],

  *  "totalCount": 0

 }`
