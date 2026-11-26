##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/helm/operation/HelmRollback)Rollback a helm release
Rollback a helm release to a previous revision **Access policy** : authenticated
##### Authorizations:
(_ApiKeyAuth_ _jwt_)
##### path Parameters
idrequired |  integer Environment(Endpoint) identifier
---|---
releaserequired |  string Helm release name
##### query Parameters
namespace |  string specify an optional namespace
---|---
revision |  integer specify the revision to rollback to (defaults to previous revision if not specified)
wait |  boolean wait for resources to be ready (default: false)
waitForJobs |  boolean wait for jobs to complete before marking the release as successful (default: false)
recreate |  boolean performs pods restart for the resource if applicable (default: true)
force |  boolean force resource update through delete/recreate if needed (default: false)
timeout |  integer time to wait for any individual Kubernetes operation in seconds (default: 300)
### Responses
**200**
Success
**400**
Invalid request payload, such as missing required fields or fields not meeting validation criteria.
**401**
Unauthorized access - the user is not authenticated or does not have the necessary permissions. Ensure that you have provided a valid API key or JWT token, and that you have the required permissions.
**403**
Permission denied - the user is authenticated but does not have the necessary permissions to access the requested resource or perform the specified operation. Check your user roles and permissions.
**404**
Unable to find an environment with the specified identifier or release name.
**500**
Server error occurred while attempting to rollback the release.
post/endpoints/{id}/kubernetes/helm/{release}/rollback
https://api-docs.portainer.io/api/endpoints/{id}/kubernetes/helm/{release}/rollback
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
