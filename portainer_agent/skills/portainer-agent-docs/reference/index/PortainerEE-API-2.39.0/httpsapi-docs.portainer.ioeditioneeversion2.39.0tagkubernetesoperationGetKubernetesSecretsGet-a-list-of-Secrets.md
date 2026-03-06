##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/kubernetes/operation/GetKubernetesSecrets)Get a list of Secrets
Get a list of Secrets for a given namespace. If isUsed is set to true, information about the applications that use the secrets is also returned. **Access policy** : Authenticated user.
##### Authorizations:
(_ApiKeyAuth_ _jwt_)
##### path Parameters
idrequired |  integer Environment identifier
---|---
##### query Parameters
isUsedrequired |  boolean When set to true, associate the Secrets with the applications that use them
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
**404**
Unable to find an environment with the specified identifier.
**500**
Server error occurred while attempting to retrieve all secrets from the cluster.
get/kubernetes/{id}/secrets
https://api-docs.portainer.io/api/kubernetes/{id}/secrets
###  Response samples
  * 200


Content type
application/json
Copy
Expand all  Collapse all
`[
  *  {
    *  "Annotations": {
      *  "property1": "string",

      *  "property2": "string"
  },

    *  "ConfigurationOwner": "string",

    *  "ConfigurationOwnerId": "string",

    *  "ConfigurationOwners": [
      *  {
        *  "Id": "string",

        *  "Name": "string",

        *  "ResourceKind": "string"
  }
 ],

    *  "CreationDate": "string",

    *  "Data": {
      *  "property1": "string",

      *  "property2": "string"
  },

    *  "IsUsed": true,

    *  "Labels": {
      *  "property1": "string",

      *  "property2": "string"
  },

    *  "Name": "string",

    *  "Namespace": "string",

    *  "SecretType": "string",

    *  "UID": "string"
  }

 ]`
