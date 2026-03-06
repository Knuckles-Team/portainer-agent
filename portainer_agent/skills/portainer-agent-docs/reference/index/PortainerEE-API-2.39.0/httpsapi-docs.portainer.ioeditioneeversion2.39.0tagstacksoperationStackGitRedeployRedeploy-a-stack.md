##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/stacks/operation/StackGitRedeploy)Redeploy a stack
Pull and redeploy a stack via Git **Access policy** : authenticated
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### path Parameters
idrequired |  integer Stack identifier
---|---
##### query Parameters
endpointId |  integer Stacks created before version 1.18.0 might not have an associated environment(endpoint) identifier. Use this optional parameter to set the environment(endpoint) identifier used by the stack.
---|---
##### Request Body schema: application/json
required
Git configs for pull and redeploy of a stack. **StackName** may only be populated for Kuberenetes stacks, and if specified with a blank string, it will be set to blank
Env |  Array of objects (portainer.Pair)
---|---
Prune |  boolean
PullImage |  boolean Deprecated(2.36): use RepullImageAndRedeploy instead for cleaner responsibility Force a pulling to current image with the original tag though the image is already the latest
RepositoryAuthentication |  boolean
RepositoryAuthorizationType |  integer (gittypes.GitCredentialAuthType)  Enum: 0 1
RepositoryGitCredentialID |  integer
RepositoryPassword |  string
RepositoryReferenceName |  string
RepositoryUsername |  string
RepullImageAndRedeploy |  boolean RepullImageAndRedeploy indicates whether to force repulling images and redeploying the stack
StackName |  string
### Responses
**200**
Success
**400**
Invalid request
**403**
Permission denied
**404**
Not found
**500**
Server error
put/stacks/{id}/git/redeploy
https://api-docs.portainer.io/api/stacks/{id}/git/redeploy
###  Request samples
  * Payload


Content type
application/json
Copy
Expand all  Collapse all
`{

  *  "Env": [
    *  {
      *  "name": "name",

      *  "value": "value"
  }
 ],

  *  "Prune": false,

  *  "PullImage": false,

  *  "RepositoryAuthentication": true,

  *  "RepositoryAuthorizationType": 0,

  *  "RepositoryGitCredentialID": 0,

  *  "RepositoryPassword": "string",

  *  "RepositoryReferenceName": "string",

  *  "RepositoryUsername": "string",

  *  "RepullImageAndRedeploy": true,

  *  "StackName": "string"

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
