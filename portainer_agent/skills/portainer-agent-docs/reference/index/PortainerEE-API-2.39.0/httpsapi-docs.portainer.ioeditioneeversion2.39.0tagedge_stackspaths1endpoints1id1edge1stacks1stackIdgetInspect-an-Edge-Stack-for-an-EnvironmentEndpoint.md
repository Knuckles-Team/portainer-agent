##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/edge_stacks/paths/~1endpoints~1{id}~1edge~1stacks~1{stackId}/get)Inspect an Edge Stack for an Environment(Endpoint)
**Access policy** : public
##### path Parameters
idrequired |  integer Environment(Endpoint) Id
---|---
stackIdrequired |  integer EdgeStack Id
##### query Parameters
version |  integer Stack file version maintained by Portainer
---|---
### Responses
**200**
OK
**400**
Bad Request
**404**
Not Found
**500**
Internal Server Error
get/endpoints/{id}/edge/stacks/{stackId}
https://api-docs.portainer.io/api/endpoints/{id}/edge/stacks/{stackId}
###  Response samples
  * 200


Content type
application/json
Copy
Expand all  Collapse all
`{

  *  "AlwaysCloneGitRepoForRelativePath": true,

  *  "CreatedBy": "string",

  *  "CreatedByUserId": "string",

  *  "DeployerOptionsPayload": {
    *  "ForceRecreate": true,

    *  "Prune": true,

    *  "RemoveVolumes": true
  },

  *  "DirEntries": [
    *  {
      *  "Content": "string",

      *  "IsFile": true,

      *  "Name": "string",

      *  "Permissions": 2147483648
  }
 ],

  *  "EdgeUpdateID": 0,

  *  "EntryFileName": "string",

  *  "EnvVars": [
    *  {
      *  "name": "name",

      *  "value": "value"
  }
 ],

  *  "FilesystemPath": "string",

  *  "ForceUpdate": true,

  *  "HelmConfig": {
    *  "Atomic": true,

    *  "ChartPath": "charts/my-app",

    *  "Timeout": "5m0s",

    *  "ValuesFiles": [
      *  "['values/prod.yaml'",

      * " 'values/secrets.yaml']"
  ],

    *  "Version": "1.2.3"
  },

  *  "ID": 0,

  *  "Name": "string",

  *  "Namespace": "string",

  *  "PrePullImage": true,

  *  "RePullImage": true,

  *  "ReadyRePullImage": true,

  *  "RegistryCredentials": [
    *  {
      *  "Secret": "string",

      *  "ServerURL": "string",

      *  "Username": "string"
  }
 ],

  *  "RetryDeploy": true,

  *  "RetryPeriod": 0,

  *  "RollbackTo": 0,

  *  "StackFileContent": "string",

  *  "SupportRelativePath": true,

  *  "Version": 0

 }`
