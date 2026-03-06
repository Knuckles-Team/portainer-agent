##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/gitops/operation/GitOperationRepoHelmValues)Preview merged Helm values files from git repository
Load and merge multiple Helm values files from a Git repository, mimicking Helm CLI behavior **Access policy** : authenticated
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### Request Body schema: application/json
required
Helm values preview request
authorizationType |  integer Enum: 0 1
---|---
gitCredentialID |  integer
password |  string
reference |  string
repositoryrequired |  string
tlsSkipVerify |  boolean
username |  string
valuesFilesrequired |  Array of strings ValuesFiles is an array of paths to Helm values files (matches Stack.HelmValuesFiles)
### Responses
**200**
Success
**400**
Invalid request
**500**
Server error
post/gitops/repo/helm/values
https://api-docs.portainer.io/api/gitops/repo/helm/values
###  Request samples
  * Payload


Content type
application/json
Copy
Expand all  Collapse all
`{

  *  "authorizationType": 0,

  *  "gitCredentialID": 0,

  *  "password": "myGitPassword",

  *  "reference": "refs/heads/main",

  *  "repository": "",

  *  "tlsSkipVerify": false,

  *  "username": "myGitUsername",

  *  "valuesFiles": [
    *  "[\"values/base.yaml\"",

    * "\"values/prod.yaml\"]"
  ]

 }`
###  Response samples
  * 200


Content type
application/json
Copy
Expand all  Collapse all
`{

  *  "commitHash": "string",

  *  "filesProcessed": [
    * "string"
 ],

  *  "mergedValues": "string"

 }`
