##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/edge_stacks/operation/EdgeStackList)Fetches the list of EdgeStacks
**Access policy** : administrator
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### query Parameters
summarizeStatuses |  boolean when true summarize the edge stack statuses in the StatusSummary field and void the Status field.
---|---
### Responses
**200**
OK
**400**
Bad Request
**500**
Internal Server Error
**503**
Edge compute features are disabled
get/edge_stacks
https://api-docs.portainer.io/api/edge_stacks
###  Response samples
  * 200


Content type
application/json
Copy
Expand all  Collapse all
`[
  *  {
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

    *  "StatusSummary": {
      *  "AggregatedStatus": {
        *  "property1": 0,

        *  "property2": 0
  },

      *  "Reason": "string",

      *  "Status": "Unavailable"
  },

    *  "SupportPerDeviceConfigs": false,

    *  "SupportRelativePath": false,

    *  "UseManifestNamespaces": true,

    *  "Version": 0,

    *  "Webhook": "c11fdf23-183e-428a-9bb6-16db01032174"
  }

 ]`
