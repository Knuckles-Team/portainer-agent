##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/intel/operation/DeviceFeatures)Enable features on an AMT managed device  Deprecated
Enable features on an AMT managed device **Access policy** : administrator
##### Authorizations:
_jwt_
##### path Parameters
idrequired |  integer Environment identifier
---|---
deviceIdrequired |  integer Device identifier
##### Request Body schema: application/json
required
Device Features
Features |  object (portainer.OpenAMTDeviceEnabledFeatures)
---|---
### Responses
**204**
Success
**400**
Invalid request
**403**
Permission denied to access settings
**500**
Server error
post/open_amt/{id}/devices_features/{deviceId}
https://api-docs.portainer.io/api/open_amt/{id}/devices_features/{deviceId}
###  Request samples
  * Payload


Content type
application/json
Copy
Expand all  Collapse all
`{
  *  "Features": {
    *  "IDER": true,

    *  "KVM": true,

    *  "SOL": true,

    *  "redirection": true,

    *  "userConsent": "string"
  }

 }`
