##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/gitops/operation/GitOperationRepoFilesSearch)Search the file path from a git repository files with specified extensions
Search the file path from the git repository based on partial or completed filename **Access policy** : authenticated
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### query Parameters
force |  boolean list the results without using cache
---|---
##### Request Body schema: application/json
required
details
TLSSkipVerify |  boolean TLSSkipVerify skips SSL verification when cloning the Git repository
---|---
authorizationType |  integer Enum: 0 1
createdFromCustomTemplateID |  integer
dirOnly |  boolean DirOnly List directories only
gitCredentialID |  integer
include |  string Allow to provide specific file extension as the search result. If empty, the file extensions yml,yaml,hcl,json will be set by default
keyword |  string Partial or completed file name. If empty, all filenames with included extensions will be returned
password |  string
reference |  string Specific Git repository reference. If empty, the reference ref/heads/main will be set by default
repositoryrequired |  string
username |  string
### Responses
**200**
Success
**400**
Invalid request
**500**
Server error
post/gitops/repo/files/search
https://api-docs.portainer.io/api/gitops/repo/files/search
###  Request samples
  * Payload


Content type
application/json
Copy
`{

  *  "TLSSkipVerify": false,

  *  "authorizationType": 0,

  *  "createdFromCustomTemplateID": 0,

  *  "dirOnly": false,

  *  "gitCredentialID": 0,

  *  "include": "json,yml",

  *  "keyword": "docker-compose",

  *  "password": "string",

  *  "reference": "refs/heads/develop",

  *  "repository": "string",

  *  "username": "string"

 }`
