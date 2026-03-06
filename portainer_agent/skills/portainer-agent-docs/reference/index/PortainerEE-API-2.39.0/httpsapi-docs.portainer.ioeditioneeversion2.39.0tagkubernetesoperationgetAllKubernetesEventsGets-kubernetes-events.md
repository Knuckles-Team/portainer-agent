##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/kubernetes/operation/getAllKubernetesEvents)Gets kubernetes events
Get events by query param resourceId **Access policy** : Authenticated user.
##### Authorizations:
(_ApiKeyAuth_ _jwt_)
##### path Parameters
idrequired |  integer Environment identifier
---|---
##### query Parameters
resourceId |  string The resource id of the involved kubernetes object
---|---
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
Server error occurred while attempting to retrieve the events.
get/kubernetes/{id}/events
https://api-docs.portainer.io/api/kubernetes/{id}/events
###  Response samples
  * 200


Content type
application/json
Copy
Expand all  Collapse all
`[
  *  {
    *  "count": 0,

    *  "eventTime": "string",

    *  "firstTimestamp": "string",

    *  "involvedObject": {
      *  "kind": "string",

      *  "name": "string",

      *  "namespace": "string",

      *  "uid": "string"
  },

    *  "kind": "string",

    *  "lastTimestamp": "string",

    *  "message": "string",

    *  "name": "string",

    *  "namespace": "string",

    *  "reason": "string",

    *  "type": "string",

    *  "uid": "string"
  }

 ]`
