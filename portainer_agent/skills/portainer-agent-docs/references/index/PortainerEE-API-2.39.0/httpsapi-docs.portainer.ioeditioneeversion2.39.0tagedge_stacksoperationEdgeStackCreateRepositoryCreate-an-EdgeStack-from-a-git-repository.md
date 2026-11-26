##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/edge_stacks/operation/EdgeStackCreateRepository)Create an EdgeStack from a git repository
**Access policy** : administrator
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### query Parameters
dryrun |  string if true, will not create an edge stack, but just will check the settings and return a non-persisted edge stack object
---|---
##### Request Body schema: application/json
required
stack config
AlwaysCloneGitRepoForRelativePath |  boolean Whether the edge stack always clones the git repository for relative path
---|---
AutoUpdate |  object Optional GitOps update configuration
CreatedFromCustomTemplateID |  integer CreatedFromCustomTemplateID used to determine whether the edge stack is created from a custom template
DeploymentType |  integer Enum: 0 1 Deployment type to deploy this stack Valid values are: 0 - 'compose', 1 - 'kubernetes' compose is enabled only for docker environments kubernetes is enabled only for kubernetes environments
EdgeGroupsrequired |  Array of integers List of identifiers of EdgeGroups
EnvVars |  Array of objects (portainer.Pair)  List of environment variables
FilePathInRepository |  string Default:  "docker-compose.yml" Path to the Stack file inside the Git repository
FilesystemPath |  string Local filesystem path
HelmConfig |  object HelmConfig is the configuration for the Helm chart
Namerequired |  string Name of the stack Max length: 255 Name must only contains lowercase characters, numbers, hyphens, or underscores Name must start with a lowercase character or number Example: stack-name or stack_123 or stackName
PerDeviceConfigsGroupMatchType |  string Enum: "file" "dir" " dir" Per device configs group match type
PerDeviceConfigsMatchType |  string Enum: "file" "dir" " dir" Per device configs match type
PerDeviceConfigsPath |  string Per device configs path
PrePullImage |  boolean Pre Pull image
Registries |  Array of integers List of Registries to use for this stack
RepositoryAuthentication |  boolean Use basic authentication to clone the Git repository
RepositoryAuthorizationType |  integer Enum: 0 1 RepositoryAuthorizationType is the authorization type to use
RepositoryGitCredentialID |  integer GitCredentialID used to identify the binded git credential
RepositoryPassword |  string Password used in basic authentication. Required when RepositoryAuthentication is true.
RepositoryReferenceName |  string Reference name of a Git repository hosting the Stack file
RepositoryURLrequired |  string URL of a Git repository hosting the Stack file
RepositoryUsername |  string Username used in basic authentication. Required when RepositoryAuthentication is true.
RetryDeploy |  boolean Retry deploy
RetryPeriod |  integer Retry period specifies the duration, in seconds, for which the agent should continue attempting to deploy the stack after a failure
StaggerConfig |  object Configuration for stagger updates
SupportPerDeviceConfigs |  boolean Whether the edge stack supports per device configs
SupportRelativePath |  boolean Whether the stack supports relative path volume
TLSSkipVerify |  boolean TLSSkipVerify skips SSL verification when cloning the Git repository
UseManifestNamespaces |  boolean Uses the manifest's namespaces instead of the default one
### Responses
**200**
OK
**400**
Bad request
**409**
Webhook ID already exists
**500**
Internal server error
**503**
Edge compute features are disabled
post/edge_stacks/create/repository
https://api-docs.portainer.io/api/edge_stacks/create/repository
###  Request samples
  * Payload


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

  *  "CreatedFromCustomTemplateID": 0,

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

  *  "FilePathInRepository": "docker-compose.yml",

  *  "FilesystemPath": "/mnt",

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

  *  "Name": "stack-name",

  *  "PerDeviceConfigsGroupMatchType": "file",

  *  "PerDeviceConfigsMatchType": "file",

  *  "PerDeviceConfigsPath": "configs",

  *  "PrePullImage": false,

  *  "Registries": [
    * 0
 ],

  *  "RepositoryAuthentication": true,

  *  "RepositoryAuthorizationType": 0,

  *  "RepositoryGitCredentialID": 0,

  *  "RepositoryPassword": "myGitPassword",

  *  "RepositoryReferenceName": "refs/heads/master",

  *  "RepositoryURL": "",

  *  "RepositoryUsername": "myGitUsername",

  *  "RetryDeploy": false,

  *  "RetryPeriod": 0,

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

  *  "SupportPerDeviceConfigs": false,

  *  "SupportRelativePath": false,

  *  "TLSSkipVerify": false,

  *  "UseManifestNamespaces": true

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
