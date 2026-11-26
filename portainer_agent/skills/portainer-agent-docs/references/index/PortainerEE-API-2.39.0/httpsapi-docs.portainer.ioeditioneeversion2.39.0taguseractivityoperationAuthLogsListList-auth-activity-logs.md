##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/useractivity/operation/AuthLogsList)List auth activity logs
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
### Responses
**200**
Success
**500**
Server error
get/useractivity/authlogs
https://api-docs.portainer.io/api/useractivity/authlogs
###  Response samples
  * 200


Content type
application/json
Copy
Expand all  Collapse all
`[
  *  {
    *  "context": 0,

    *  "id": 0,

    *  "origin": "string",

    *  "timestamp": 0,

    *  "type": 0,

    *  "username": "string"
  }

 ]`
