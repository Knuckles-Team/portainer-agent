##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/gitops/operation/GitOperationRepoFilePreview)preview the content of target file in the git repository
Retrieve the compose file content based on git repository configuration **Access policy** : authenticated
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### Request Body schema: application/json
required
Template details
TLSSkipVerify |  boolean TLSSkipVerify skips SSL verification when cloning the Git repository
---|---
authorizationType |  integer Enum: 0 1
gitCredentialID |  integer
password |  string
reference |  string
repositoryrequired |  string
targetFile |  string Path to file whose content will be read
username |  string
### Responses
**200**
Success
**400**
Invalid request
**500**
Server error
post/gitops/repo/file/preview
https://api-docs.portainer.io/api/gitops/repo/file/preview
###  Request samples
  * Payload


Content type
application/json
Copy
`{

  *  "TLSSkipVerify": false,

  *  "authorizationType": 0,

  *  "gitCredentialID": 0,

  *  "password": "myGitPassword",

  *  "reference": "refs/heads/master",

  *  "repository": "",

  *  "targetFile": "docker-compose.yml",

  *  "username": "myGitUsername"

 }`
###  Response samples
  * 200


Content type
application/json
Copy
`{
  *  "FileContent": "string"

 }`
