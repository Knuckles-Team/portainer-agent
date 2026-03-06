##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/edge_stacks/operation/EdgeStackStatusUpdate)Update an EdgeStack status
Authorized only if the request is done by an Edge Environment(Endpoint)
##### path Parameters
idrequired |  integer EdgeStack Id
---|---
##### Request Body schema: application/json
required
EdgeStack status payload
EndpointID |  integer
---|---
Error |  string
RollbackTo |  integer RollbackTo specifies the stack file version to rollback to (only support to rollback to the last version currently)
Status |  integer (portainer.EdgeStackStatusType)  Enum: 0 1 2 3 4 5 6 7 8 9 10 11 12 13
Time |  integer
Version |  integer
### Responses
**200**
OK
**400**
Bad Request
**403**
Forbidden
**404**
Not Found
**500**
Internal Server Error
put/edge_stacks/{id}/status
https://api-docs.portainer.io/api/edge_stacks/{id}/status
###  Request samples
  * Payload


Content type
application/json
Copy
`{

  *  "EndpointID": 0,

  *  "Error": "string",

  *  "RollbackTo": 0,

  *  "Status": 0,

  *  "Time": 0,

  *  "Version": 0

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
