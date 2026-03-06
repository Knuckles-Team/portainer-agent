##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/edge_stacks/operation/EdgeStackCreateFile)Create an EdgeStack from file
**Access policy** : administrator
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### query Parameters
dryrun |  string if true, will not create an edge stack, but just will check the settings and return a non-persisted edge stack object
---|---
##### Request Body schema: multipart/form-data
required
Namerequired |  string Name of the stack. it must only consist of lowercase alphanumeric characters, hyphens, or underscores as well as start with a letter or number
---|---
filerequired |  string <binary> Content of the Stack file
EdgeGroupsrequired |  string JSON stringified array of Edge Groups ids
DeploymentTyperequired |  integer deploy type 0 - 'compose', 1 - 'kubernetes'
Registries |  string JSON stringified array of Registry ids to use for this stack
UseManifestNamespaces |  boolean Uses the manifest's namespaces instead of the default one, relevant only for kube environments
PrePullImage |  boolean Pre Pull image
RetryDeploy |  boolean Retry deploy
RetryPeriod |  integer Duration, in seconds, for which the agent should continue attempting to deploy the stack after a failure
Webhookrequired |  string unique webhook id
EnvVars |  string JSON stringified array of environment variables {name, value}
StaggerConfig |  string JSON stringified object of stagger config
### Responses
**200**
OK
**400**
Bad request
**500**
Internal server error
**503**
Edge compute features are disabled
post/edge_stacks/create/file
https://api-docs.portainer.io/api/edge_stacks/create/file
###  Response samples
  * 200


Content type
application/json
Copy
Expand all  Collapse all
`{

  *  "AlwaysCloneGitRepoForRelativePath": false,

  *  "AutoUpdate": {
    *  "ForcePullImage": false,

    *  "ForceUpdate": false,

    *  "Interval": "1m30s",

    *  "JobID": "15",

    *  "Webhook": "05de31a2-79fa-4644-9c12-faa67e5c49f0"
  },

  *  "CreatedBy": "admin",

  *  "CreatedByUserId": "1",

  *  "CreationDate": 0,

  *  "DeployerOptions": {
    *  "Prune": true,

    *  "RemoveVolumes": true
  },

  *  "DeploymentType": 0,

  *  "EdgeGroups": [
    * 0
 ],

  *  "EdgeUpdateID": 0,

  *  "EntryPoint": "string",

  *  "EnvVars": [
    *  {
      *  "name": "name",

      *  "value": "value"
  }
 ],

  *  "FilesystemPath": "/tmp",

  *  "GitConfig": {
    *  "Authentication": {
      *  "AuthorizationType": 0,

      *  "GitCredentialID": 0,

      *  "Password": "string",

      *  "Username": "string"
  },

    *  "ConfigFilePath": "docker-compose.yml",

    *  "ConfigHash": "bc4c183d756879ea4d173315338110b31004b8e0",

    *  "ReferenceName": "refs/heads/branch_name",

    *  "TLSSkipVerify": false,

    *  "URL": ""
  },

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

  *  "Id": 1,

  *  "ManifestPath": "string",

  *  "Name": "string",

  *  "NumDeployments": 0,

  *  "PerDeviceConfigsGroupMatchType": "file",

  *  "PerDeviceConfigsMatchType": "file",

  *  "PerDeviceConfigsPath": "configs",

  *  "PrePullImage": true,

  *  "PreviousDeploymentInfo": {
    *  "ConfigHash": "string",

    *  "FileVersion": 0,

    *  "Version": 0
  },

  *  "ProjectPath": "string",

  *  "RePullImage": true,

  *  "Registries": [
    * 0
 ],

  *  "RetryDeploy": false,

  *  "RetryPeriod": 0,

  *  "ScheduledTime": "2020-11-13 14:53:00",

  *  "StackFileVersion": 1,

  *  "StaggerConfig": {
    *  "DeviceNumber": 0,

    *  "DeviceNumberIncrementBy": 0,

    *  "DeviceNumberStartFrom": 0,

    *  "StaggerOption": 0,

    *  "StaggerParallelOption": 0,

    *  "Timeout": "5",

    *  "UpdateDelay": "5",

    *  "UpdateFailureAction": 0
  },

  *  "Status": {
    *  "property1": {
      *  "DeploymentInfo": {
        *  "ConfigHash": "string",

        *  "FileVersion": 0,

        *  "Version": 0
  },

      *  "Details": {
        *  "Acknowledged": true,

        *  "Error": true,

        *  "ImagesPulled": true,

        *  "Ok": true,

        *  "Pending": true,

        *  "RemoteUpdateSuccess": true,

        *  "Remove": true
  },

      *  "EndpointID": 0,

      *  "Error": "string",

      *  "ReadyRePullImage": true,

      *  "Status": [
        *  {
          *  "Error": "string",

          *  "RollbackTo": 0,

          *  "Time": 0,

          *  "Type": 0,

          *  "Version": 0
  }
 ],

      *  "Type": 0
  },

    *  "property2": {
      *  "DeploymentInfo": {
        *  "ConfigHash": "string",

        *  "FileVersion": 0,

        *  "Version": 0
  },

      *  "Details": {
        *  "Acknowledged": true,

        *  "Error": true,

        *  "ImagesPulled": true,

        *  "Ok": true,

        *  "Pending": true,

        *  "RemoteUpdateSuccess": true,

        *  "Remove": true
  },

      *  "EndpointID": 0,

      *  "Error": "string",

      *  "ReadyRePullImage": true,

      *  "Status": [
        *  {
          *  "Error": "string",

          *  "RollbackTo": 0,

          *  "Time": 0,

          *  "Type": 0,

          *  "Version": 0
  }
 ],

      *  "Type": 0
  }
  },

  *  "SupportPerDeviceConfigs": false,

  *  "SupportRelativePath": false,

  *  "UseManifestNamespaces": true,

  *  "Version": 0,

  *  "Webhook": "c11fdf23-183e-428a-9bb6-16db01032174"

 }`
