##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/helm/operation/HelmGetHistory)Get a historical list of releases
Get a historical list of releases by release name **Access policy** : authenticated
##### Authorizations:
(_ApiKeyAuth_ _jwt_)
##### path Parameters
idrequired |  integer Environment(Endpoint) identifier
---|---
namerequired |  string Helm release name
##### query Parameters
namespace |  string specify an optional namespace
---|---
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
Unable to find an environment with the specified identifier.
**500**
Server error occurred while attempting to retrieve the historical list of releases.
get/endpoints/{id}/kubernetes/helm/{release}/history
https://api-docs.portainer.io/api/endpoints/{id}/kubernetes/helm/{release}/history
###  Response samples
  * 200


Content type
application/json
Copy
Expand all  Collapse all
`[
  *  {
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
  }

 ]`
