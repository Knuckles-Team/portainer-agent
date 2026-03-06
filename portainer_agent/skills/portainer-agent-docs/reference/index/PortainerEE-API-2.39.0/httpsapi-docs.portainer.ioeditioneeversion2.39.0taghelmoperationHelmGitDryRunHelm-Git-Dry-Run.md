##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/helm/operation/HelmGitDryRun)Helm Git Dry Run
**Access policy** : authenticated
##### Authorizations:
(_ApiKeyAuth_ _jwt_)
##### path Parameters
idrequired |  integer Environment(Endpoint) identifier
---|---
##### Request Body schema: application/json
required
Git Helm dry run details
helmChartPath |  string
---|---
helmValuesFiles |  Array of strings
name |  string
namespace |  string
repositoryAuthentication |  boolean
repositoryAuthorizationType |  integer (gittypes.GitCredentialAuthType)  Enum: 0 1
repositoryGitCredentialID |  integer
repositoryPassword |  string
repositoryReferenceName |  string
repositoryURL |  string
repositoryUsername |  string
tlsSkipVerify |  boolean
### Responses
**200**
Success
**400**
Bad request
**401**
Unauthorized
**404**
Environment(Endpoint) not found
**500**
Server error
post/endpoints/{id}/kubernetes/helm/git/dryrun
https://api-docs.portainer.io/api/endpoints/{id}/kubernetes/helm/git/dryrun
###  Request samples
  * Payload


Content type
application/json
Copy
Expand all  Collapse all
`{

  *  "helmChartPath": "string",

  *  "helmValuesFiles": [
    * "string"
 ],

  *  "name": "string",

  *  "namespace": "string",

  *  "repositoryAuthentication": true,

  *  "repositoryAuthorizationType": 0,

  *  "repositoryGitCredentialID": 0,

  *  "repositoryPassword": "string",

  *  "repositoryReferenceName": "string",

  *  "repositoryURL": "string",

  *  "repositoryUsername": "string",

  *  "tlsSkipVerify": true

 }`
###  Response samples
  * 200


Content type
application/json
Copy
Expand all  Collapse all
`{

  *  "appVersion": "string",

  *  "chart": {
    *  "files": [
      *  {
        *  "data": [
          * 0
 ],

        *  "name": "string"
  }
 ],

    *  "lock": {
      *  "dependencies": [
        *  {
          *  "alias": "string",

          *  "condition": "string",

          *  "enabled": true,

          *  "import-values": [
            * null
 ],

          *  "name": "string",

          *  "repository": "string",

          *  "tags": [
            * "string"
 ],

          *  "version": "string"
  }
 ],

      *  "digest": "string",

      *  "generated": "string"
  },

    *  "metadata": {
      *  "annotations": {
        *  "property1": "string",

        *  "property2": "string"
  },

      *  "apiVersion": "string",

      *  "appVersion": "string",

      *  "condition": "string",

      *  "dependencies": [
        *  {
          *  "alias": "string",

          *  "condition": "string",

          *  "enabled": true,

          *  "import-values": [
            * null
 ],

          *  "name": "string",

          *  "repository": "string",

          *  "tags": [
            * "string"
 ],

          *  "version": "string"
  }
 ],

      *  "deprecated": true,

      *  "description": "string",

      *  "home": "string",

      *  "icon": "string",

      *  "keywords": [
        * "string"
 ],

      *  "kubeVersion": "string",

      *  "maintainers": [
        *  {
          *  "email": "string",

          *  "name": "string",

          *  "url": "string"
  }
 ],

      *  "name": "string",

      *  "sources": [
        * "string"
 ],

      *  "tags": "string",

      *  "type": "string",

      *  "version": "string"
  },

    *  "schema": [
      * 0
 ],

    *  "templates": [
      *  {
        *  "data": [
          * 0
 ],

        *  "name": "string"
  }
 ],

    *  "values": {
      *  "property1": null,

      *  "property2": null
  }
  },

  *  "chartReference": {
    *  "chartPath": "string",

    *  "registryID": 0,

    *  "repoURL": "string"
  },

  *  "config": {
    *  "property1": null,

    *  "property2": null
  },

  *  "hooks": [
    *  {
      *  "delete_policies": [
        * "string"
 ],

      *  "events": [
        * "string"
 ],

      *  "kind": "string",

      *  "last_run": {
        *  "completed_at": "string",

        *  "phase": "string",

        *  "started_at": "string"
  },

      *  "manifest": "string",

      *  "name": "string",

      *  "path": "string",

      *  "weight": 0
  }
 ],

  *  "info": {
    *  "deleted": "string",

    *  "description": "string",

    *  "first_deployed": "string",

    *  "last_deployed": "string",

    *  "notes": "string",

    *  "resources": [
      *  {
        *  "Object": { }
 }
 ],

    *  "status": "string"
  },

  *  "manifest": "string",

  *  "name": "string",

  *  "namespace": "string",

  *  "stackID": 0,

  *  "values": {
    *  "computedValues": "string",

    *  "userSuppliedValues": "string"
  },

  *  "version": 0

 }`
