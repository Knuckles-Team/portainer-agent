##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/observability/operation/CreateSilence)Create an alert silence
Create a new silence for alerts in the specified AlertManager. **Access policy** : Authenticated user.
##### Authorizations:
(_ApiKeyAuth_ _jwt_)
##### Request Body schema: application/json
required
Silence details
alertManagerURLrequired |  string
---|---
silencerequired |  object (models.PostableSilence)
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
Server error occurred while attempting to create the alert silence.
post/observability/alerting/silence
https://api-docs.portainer.io/api/observability/alerting/silence
###  Request samples
  * Payload


Content type
application/json
Copy
Expand all  Collapse all
`{

  *  "alertManagerURL": "string",

  *  "silence": {
    *  "comment": "string",

    *  "createdBy": "string",

    *  "endsAt": "string",

    *  "id": "string",

    *  "matchers": [
      *  {
        *  "isEqual": true,

        *  "isRegex": true,

        *  "name": "string",

        *  "value": "string"
  }
 ],

    *  "startsAt": "string"
  }

 }`
###  Response samples
  * 200


Content type
application/json
Copy
`{ }`
