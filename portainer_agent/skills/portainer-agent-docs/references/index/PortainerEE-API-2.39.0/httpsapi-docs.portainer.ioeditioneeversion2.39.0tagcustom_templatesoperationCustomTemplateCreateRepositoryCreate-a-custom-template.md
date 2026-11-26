##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/custom_templates/operation/CustomTemplateCreateRepository)Create a custom template
Create a custom template. **Access policy** : authenticated
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### Request Body schema: application/json
required
Required when using method=repository
ComposeFilePathInRepository |  string Default:  "docker-compose.yml" Path to the Stack file inside the Git repository
---|---
Descriptionrequired |  string Description of the template
EdgeSettings |  object (portaineree.CustomTemplateEdgeSettings)
EdgeTemplate |  boolean EdgeTemplate indicates if this template purpose for Edge Stack
IsComposeFormat |  boolean IsComposeFormat indicates if the Kubernetes template is created from a Docker Compose file
Logo |  string URL of the template's logo
Note |  string A note that will be displayed in the UI. Supports HTML content
Platform |  integer Enum: 0 1 2 Platform associated to the template. Valid values are: 1 - 'linux', 2 - 'windows' Required for Docker stacks
RepositoryAuthentication |  boolean Use basic authentication to clone the Git repository
RepositoryAuthorizationType |  integer Enum: 0 1 RepositoryAuthorizationType is the authorization type to use
RepositoryGitCredentialID |  integer GitCredentialID used to identify the bound git credential. Required when RepositoryAuthentication is true and RepositoryUsername/RepositoryPassword are not provided
RepositoryPassword |  string Password used in basic authentication. Required when RepositoryAuthentication is true and RepositoryGitCredentialID is 0
RepositoryReferenceName |  string Reference name of a Git repository hosting the Stack file
RepositoryURLrequired |  string URL of a Git repository hosting the Stack file
RepositoryUsername |  string Username used in basic authentication. Required when RepositoryAuthentication is true and RepositoryGitCredentialID is 0
TLSSkipVerify |  boolean TLSSkipVerify skips SSL verification when cloning the Git repository
Titlerequired |  string Title of the template
Typerequired |  integer Enum: 0 1 2 3 Type of created stack:
  * 1 - swarm
  * 2 - compose
  * 3 - kubernetes


Variables |  Array of objects (portainer.CustomTemplateVariableDefinition)  Definitions of variables in the stack file
### Responses
**200**
OK
**400**
Invalid request
**500**
Server error
post/custom_templates/create/repository
https://api-docs.portainer.io/api/custom_templates/create/repository
###  Request samples
  * Payload


Content type
application/json
Copy
Expand all  Collapse all
`{

  *  "ComposeFilePathInRepository": "docker-compose.yml",

  *  "Description": "High performance web server",

  *  "EdgeSettings": {
    *  "PrePullImage": true,

    *  "PrivateRegistryId": 0,

    *  "RelativePathSettings": {
      *  "FilesystemPath": "/tmp",

      *  "PerDeviceConfigsGroupMatchType": "file",

      *  "PerDeviceConfigsMatchType": "file",

      *  "PerDeviceConfigsPath": "configs",

      *  "SupportPerDeviceConfigs": false,

      *  "SupportRelativePath": false
  },

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
  }
  },

  *  "EdgeTemplate": false,

  *  "IsComposeFormat": false,

  *  "Logo": "https://portainer.io/img/logo.svg[](https://portainer.io/img/logo.svg)",

  *  "Note": "This is my <b>custom</b> template",

  *  "Platform": 1,

  *  "RepositoryAuthentication": true,

  *  "RepositoryAuthorizationType": 0,

  *  "RepositoryGitCredentialID": 0,

  *  "RepositoryPassword": "myGitPassword",

  *  "RepositoryReferenceName": "refs/heads/master",

  *  "RepositoryURL": "",

  *  "RepositoryUsername": "myGitUsername",

  *  "TLSSkipVerify": false,

  *  "Title": "Nginx",

  *  "Type": 1,

  *  "Variables": [
    *  {
      *  "defaultValue": "default value",

      *  "description": "Description",

      *  "label": "My Variable",

      *  "name": "MY_VAR"
  }
 ]

 }`
###  Response samples
  * 200


Content type
application/json
Copy
Expand all  Collapse all
`{

  *  "CreatedByUserId": 3,

  *  "Description": "High performance web server",

  *  "EdgeSettings": {
    *  "PrePullImage": true,

    *  "PrivateRegistryId": 0,

    *  "RelativePathSettings": {
      *  "FilesystemPath": "/tmp",

      *  "PerDeviceConfigsGroupMatchType": "file",

      *  "PerDeviceConfigsMatchType": "file",

      *  "PerDeviceConfigsPath": "configs",

      *  "SupportPerDeviceConfigs": false,

      *  "SupportRelativePath": false
  },

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
  }
  },

  *  "EdgeTemplate": false,

  *  "EntryPoint": "docker-compose.yml",

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

  *  "Id": 1,

  *  "IsComposeFormat": false,

  *  "Logo": "https://portainer.io/img/logo.svg[](https://portainer.io/img/logo.svg)",

  *  "Note": "This is my <b>custom</b> template",

  *  "Platform": 1,

  *  "ProjectPath": "/data/custom_template/3",

  *  "ResourceControl": {
    *  "AccessLevel": 0,

    *  "AdministratorsOnly": true,

    *  "Id": 1,

    *  "OwnerId": 0,

    *  "Public": true,

    *  "ResourceId": "617c5f22bb9b023d6daab7cba43a57576f83492867bc767d1c59416b065e5f08",

    *  "SubResourceIds": [
      * "617c5f22bb9b023d6daab7cba43a57576f83492867bc767d1c59416b065e5f08"
 ],

    *  "System": true,

    *  "TeamAccesses": [
      *  {
        *  "AccessLevel": 0,

        *  "TeamId": 0
  }
 ],

    *  "Type": 1,

    *  "UserAccesses": [
      *  {
        *  "AccessLevel": 0,

        *  "UserId": 0
  }
 ]
  },

  *  "Title": "Nginx",

  *  "Type": 1,

  *  "Variables": [
    *  {
      *  "defaultValue": "default value",

      *  "description": "Description",

      *  "label": "My Variable",

      *  "name": "MY_VAR"
  }
 ]

 }`
