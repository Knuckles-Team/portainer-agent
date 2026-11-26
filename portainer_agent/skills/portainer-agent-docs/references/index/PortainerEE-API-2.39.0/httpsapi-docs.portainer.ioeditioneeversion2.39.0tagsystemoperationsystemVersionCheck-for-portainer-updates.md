##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/system/operation/systemVersion)Check for portainer updates
Check if portainer has an update available **Access policy** : authenticated
##### Authorizations:
_ApiKeyAuth_ _jwt_
### Responses
**200**
Success
get/system/version
https://api-docs.portainer.io/api/system/version
###  Response samples
  * 200


Content type
application/json
Copy
Expand all  Collapse all
`{

  *  "Build": {
    *  "BuildNumber": "string",

    *  "GitCommit": "string",

    *  "GoVersion": "string",

    *  "ImageTag": "string",

    *  "NodejsVersion": "string",

    *  "PnpmVersion": "string",

    *  "WebpackVersion": "string"
  },

  *  "DatabaseVersion": "string",

  *  "Dependencies": {
    *  "ComposeVersion": "string",

    *  "DockerVersion": "string",

    *  "HelmVersion": "string",

    *  "KubectlVersion": "string"
  },

  *  "LatestVersion": "2.0.0",

  *  "Runtime": {
    *  "Env": [
      * "string"
 ]
 },

  *  "ServerEdition": "CE/EE",

  *  "ServerVersion": "string",

  *  "UpdateAvailable": false,

  *  "VersionSupport": "STS/LTS"

 }`
