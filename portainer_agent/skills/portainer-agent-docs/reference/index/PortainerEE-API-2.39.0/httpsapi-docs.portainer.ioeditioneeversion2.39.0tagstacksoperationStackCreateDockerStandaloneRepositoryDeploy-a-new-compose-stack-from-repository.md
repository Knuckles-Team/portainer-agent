##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/stacks/operation/StackCreateDockerStandaloneRepository)Deploy a new compose stack from repository
Deploy a new stack into a Docker environment specified via the environment identifier. **Access policy** : authenticated
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### query Parameters
endpointIdrequired |  integer Identifier of the environment that will be used to deploy the stack
---|---
##### Request Body schema: application/json
required
stack config
AdditionalFiles |  Array of strings Applicable when deploying with multiple stack files
---|---
AutoUpdate |  object Optional GitOps update configuration
ComposeFile |  string Default:  "docker-compose.yml" Path to the Stack file inside the Git repository
Env |  Array of objects (portainer.Pair)  A list of environment variables used during stack deployment
FilesystemPath |  string Local filesystem path
FromAppTemplate |  boolean Whether the stack is from a app template
Namerequired |  string Name of the stack
Registries |  Array of integers List of Registries to use for this stack
RepositoryAuthentication |  boolean Use basic authentication to clone the Git repository
RepositoryAuthorizationType |  integer Enum: 0 1 RepositoryAuthorizationType is the authorization type to use
RepositoryGitCredentialID |  integer GitCredentialID used to identify the bound git credential. Required when RepositoryAuthentication is true and RepositoryUsername/RepositoryPassword are not provided
RepositoryPassword |  string Password used in basic authentication. Required when RepositoryAuthentication is true and RepositoryGitCredentialID is 0
RepositoryReferenceName |  string Reference name of a Git repository hosting the Stack file
RepositoryURLrequired |  string URL of a Git repository hosting the Stack file
RepositoryUsername |  string Username used in basic authentication. Required when RepositoryAuthentication is true and RepositoryGitCredentialID is 0
SupportRelativePath |  boolean Whether the stack supports relative path volume
TLSSkipVerify |  boolean TLSSkipVerify skips SSL verification when cloning the Git repository
### Responses
**200**
OK
**400**
Invalid request
**500**
Server error
post/stacks/create/standalone/repository
https://api-docs.portainer.io/api/stacks/create/standalone/repository
###  Request samples
  * Payload


Content type
application/json
Copy
Expand all  Collapse all
`{

  *  "AdditionalFiles": [
    *  "[nz.compose.yml",

    * " uat.compose.yml]"
  ],

  *  "AutoUpdate": {
    *  "ForcePullImage": false,

    *  "ForceUpdate": false,

    *  "Interval": "1m30s",

    *  "JobID": "15",

    *  "Webhook": "05de31a2-79fa-4644-9c12-faa67e5c49f0"
  },

  *  "ComposeFile": "docker-compose.yml",

  *  "Env": [
    *  {
      *  "name": "name",

      *  "value": "value"
  }
 ],

  *  "FilesystemPath": "/tmp",

  *  "FromAppTemplate": false,

  *  "Name": "myStack",

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

  *  "SupportRelativePath": false,

  *  "TLSSkipVerify": false

 }`
###  Response samples
  * 200


Content type
application/json
Copy
Expand all  Collapse all
`{

  *  "AdditionalFiles": [
    * "string"
 ],

  *  "AutoUpdate": {
    *  "ForcePullImage": false,

    *  "ForceUpdate": false,

    *  "Interval": "1m30s",

    *  "JobID": "15",

    *  "Webhook": "05de31a2-79fa-4644-9c12-faa67e5c49f0"
  },

  *  "CreatedBy": "admin",

  *  "CreatedByUserId": "1",

  *  "CreationDate": 1587399600,

  *  "EndpointId": 1,

  *  "EntryPoint": "docker-compose.yml",

  *  "Env": [
    *  {
      *  "name": "name",

      *  "value": "value"
  }
 ],

  *  "FilesystemPath": "/tmp",

  *  "FromAppTemplate": false,

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

  *  "HelmChartPath": "charts/my-app",

  *  "HelmValuesFiles": [
    *  "['values/prod.yaml'",

    * " 'values/secrets.yaml']"
  ],

  *  "Id": 1,

  *  "IsDetachedFromGit": false,

  *  "Name": "myStack",

  *  "Namespace": "default",

  *  "Option": {
    *  "HelmAtomic": false,

    *  "Prune": false
  },

  *  "PreviousDeploymentInfo": {
    *  "ConfigHash": "string",

    *  "FileVersion": 0,

    *  "Version": 0
  },

  *  "ProjectPath": "/data/compose/myStack_jpofkc0i9uo9wtx1zesuk649w",

  *  "Registries": [
    * 0
 ],

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

  *  "StackFileVersion": 1,

  *  "Status": 1,

  *  "SupportRelativePath": false,

  *  "SwarmId": "jpofkc0i9uo9wtx1zesuk649w",

  *  "Type": 2,

  *  "UpdateDate": 1587399600,

  *  "UpdatedBy": "bob",

  *  "Webhook": "c11fdf23-183e-428a-9bb6-16db01032174"

 }`
