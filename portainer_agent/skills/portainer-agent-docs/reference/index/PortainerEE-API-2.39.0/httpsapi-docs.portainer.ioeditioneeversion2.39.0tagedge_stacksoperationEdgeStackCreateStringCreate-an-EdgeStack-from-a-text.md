##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/edge_stacks/operation/EdgeStackCreateString)Create an EdgeStack from a text
**Access policy** : administrator
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### query Parameters
dryrun |  string if true, will not create an edge stack, but just will check the settings and return a non-persisted edge stack object
---|---
##### Request Body schema: application/json
required
stack config
DeploymentType |  integer Enum: 0 1 Deployment type to deploy this stack Valid values are: 0 - 'compose', 1 - 'kubernetes' compose is enabled only for docker environments kubernetes is enabled only for kubernetes environments
---|---
EdgeGroups |  Array of integers List of identifiers of EdgeGroups
EnvVars |  Array of objects (portainer.Pair)  List of environment variables
Namerequired |  string Name of the stack Max length: 255 Name must only contains lowercase characters, numbers, hyphens, or underscores Name must start with a lowercase character or number Example: stack-name or stack_123 or stackName
PrePullImage |  boolean Pre Pull image
Registries |  Array of integers List of Registries to use for this stack
RetryDeploy |  boolean Retry deploy
RetryPeriod |  integer Retry period specifies the duration, in seconds, for which the agent should continue attempting to deploy the stack after a failure
StackFileContentrequired |  string Content of the Stack file
StaggerConfig |  object Configuration for stagger updates
UseManifestNamespaces |  boolean Uses the manifest's namespaces instead of the default one
Webhook |  string Optional webhook configuration
### Responses
**200**
OK
**400**
Bad request
**500**
Internal server error
**503**
Edge compute features are disabled
post/edge_stacks/create/string
https://api-docs.portainer.io/api/edge_stacks/create/string
###  Request samples
  * Payload


Content type
application/json
Copy
Expand all  Collapse all
`{

  *  "DeploymentType": 0,

  *  "EdgeGroups": [
    * 1
 ],

  *  "EnvVars": [
    *  {
      *  "name": "name",

      *  "value": "value"
  }
 ],

  *  "Name": "stack-name",

  *  "PrePullImage": false,

  *  "Registries": [
    * 0
 ],

  *  "RetryDeploy": false,

  *  "RetryPeriod": 0,

  *  "StackFileContent": "version: 3\n services:\n web:\n image:nginx",

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

  *  "UseManifestNamespaces": true,

  *  "Webhook": "c11fdf23-183e-428a-9bb6-16db01032174"

 }`
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
