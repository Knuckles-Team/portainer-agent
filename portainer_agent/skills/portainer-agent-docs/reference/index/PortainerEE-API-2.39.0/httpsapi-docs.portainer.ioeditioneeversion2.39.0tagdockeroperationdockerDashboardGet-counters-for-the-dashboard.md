##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/docker/operation/dockerDashboard)Get counters for the dashboard
**Access policy** : restricted
##### Authorizations:
_jwt_
##### path Parameters
environmentIdrequired |  integer Environment identifier
---|---
### Responses
**200**
Success
**400**
Bad request
**500**
Internal server error
get/docker/{environmentId}/dashboard
https://api-docs.portainer.io/api/docker/{environmentId}/dashboard
###  Response samples
  * 200


Content type
application/json
Copy
Expand all  Collapse all
`{

  *  "containers": {
    *  "healthy": 0,

    *  "running": 0,

    *  "stopped": 0,

    *  "total": 0,

    *  "unhealthy": 0
  },

  *  "images": {
    *  "size": 0,

    *  "total": 0
  },

  *  "networks": 0,

  *  "services": 0,

  *  "stacks": 0,

  *  "volumes": 0

 }`
