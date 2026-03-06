##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/edge_stacks/operation/EdgeStackUpdate)Update an EdgeStack
**Access policy** : administrator
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### path Parameters
idrequired |  integer EdgeStack Id
---|---
##### Request Body schema: application/json
required
EdgeStack data
DeployerOptions |  object Options to control the deployer behaviour
---|---
DeploymentType |  integer (portainer.EdgeStackDeploymentType)  Enum: 0 1
EdgeGroups |  Array of integers
EnvVars |  Array of objects (portainer.Pair)  Environment variables to inject into the stack
PrePullImage |  boolean
RePullImage |  boolean Deprecated(2.36): use RepullImageAndRedeploy instead
Registries |  Array of integers
RepullImageAndRedeploy |  boolean RepullImageAndRedeploy indicates whether the edge stack is manually forced to redeploy
RetryDeploy |  boolean
RetryPeriod |  integer RetryPeriod specifies the duration, in seconds, for which the agent should continue attempting to deploy the stack after a failure
RollbackTo |  integer RollbackTo specifies the stack file version to rollback to (only support to rollback to the last version currently)
StackFileContent |  string
StaggerConfig |  object Configuration for stagger updates
UpdateVersion |  boolean
UseManifestNamespaces |  boolean Uses the manifest's namespaces instead of the default one
Webhook |  string Optional webhook configuration
### Responses
**200**
OK
**400**
Bad Request
**500**
Internal Server Error
**503**
Edge compute features are disabled
put/edge_stacks/{id}
https://api-docs.portainer.io/api/edge_stacks/{id}
###  Request samples
  * Payload


Content type
application/json
Copy
Expand all  Collapse all
`{

  *  "DeployerOptions": {
    *  "Prune": true,

    *  "RemoveVolumes": true
  },

  *  "DeploymentType": 0,

  *  "EdgeGroups": [
    * 0
 ],

  *  "EnvVars": [
    *  {
      *  "name": "name",

      *  "value": "value"
  }
 ],

  *  "PrePullImage": true,

  *  "RePullImage": true,

  *  "Registries": [
    * 0
 ],

  *  "RepullImageAndRedeploy": true,

  *  "RetryDeploy": true,

  *  "RetryPeriod": 0,

  *  "RollbackTo": 0,

  *  "StackFileContent": "string",

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

  *  "UpdateVersion": true,

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
