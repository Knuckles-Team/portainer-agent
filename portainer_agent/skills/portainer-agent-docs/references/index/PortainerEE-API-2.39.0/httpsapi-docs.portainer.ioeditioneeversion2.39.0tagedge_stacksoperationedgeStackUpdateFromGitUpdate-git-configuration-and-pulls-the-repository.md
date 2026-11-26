##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/edge_stacks/operation/edgeStackUpdateFromGit)Update git configuration and pulls the repository
**Access policy** : authenticated
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### path Parameters
idrequired |  integer Stack identifier
---|---
##### Request Body schema: application/json
required
Git configurations
Atomic |  boolean Enable automatic rollback on deployment failure (equivalent to helm --atomic flag)
---|---
Authentication |  object (gittypes.GitAuthentication)
AutoUpdate |  object (portainer.AutoUpdateSettings)
DeployerOptions |  object Options to control the deployer behaviour
DeploymentType |  integer (portainer.EdgeStackDeploymentType)  Enum: 0 1
EnvVars |  Array of objects (portainer.Pair)
GroupIds |  Array of integers
PrePullImage |  boolean
RePullImage |  boolean Deprecated(2.36): to be removed in future versions (2.44+) Use RepullImageAndRedeploy instead
RefName |  string
Registries |  Array of integers List of Registries to use for this stack
RepullImageAndRedeploy |  boolean RepullImageAndRedeploy indicates whether the edge stack is manually forced to redeploy
RetryDeploy |  boolean
RetryPeriod |  integer RetryPeriod specifies the duration, in seconds, for which the agent should continue attempting to deploy the stack after a failure
StaggerConfig |  object Configuration for stagger updates
Timeout |  string Timeout for Helm operations (equivalent to helm --timeout flag)
UpdateVersion |  boolean Update the stack file content from the git repository If this is set to true, it indicates that the stack is being redeployed (Pull and update stack), if it is false, it indicates that the stack is being updated (Update settings)
ValuesFiles |  Array of strings Array of paths to Helm values YAML files for Helm git deployments
### Responses
**204**
Success
**400**
Invalid request
**403**
Permission denied
**404**
Not found
**500**
Server error
put/edge_stacks/{id}/git
https://api-docs.portainer.io/api/edge_stacks/{id}/git
###  Request samples
  * Payload


Content type
application/json
Copy
Expand all  Collapse all
`{

  *  "Atomic": true,

  *  "Authentication": {
    *  "AuthorizationType": 0,

    *  "GitCredentialID": 0,

    *  "Password": "string",

    *  "Username": "string"
  },

  *  "AutoUpdate": {
    *  "ForcePullImage": false,

    *  "ForceUpdate": false,

    *  "Interval": "1m30s",

    *  "JobID": "15",

    *  "Webhook": "05de31a2-79fa-4644-9c12-faa67e5c49f0"
  },

  *  "DeployerOptions": {
    *  "Prune": true,

    *  "RemoveVolumes": true
  },

  *  "DeploymentType": 0,

  *  "EnvVars": [
    *  {
      *  "name": "name",

      *  "value": "value"
  }
 ],

  *  "GroupIds": [
    * 0
 ],

  *  "PrePullImage": true,

  *  "RePullImage": true,

  *  "RefName": "string",

  *  "Registries": [
    * 0
 ],

  *  "RepullImageAndRedeploy": true,

  *  "RetryDeploy": true,

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

  *  "Timeout": "5m0s",

  *  "UpdateVersion": true,

  *  "ValuesFiles": [
    *  "['values/prod.yaml'",

    * " 'values/secrets.yaml']"
  ]

 }`
