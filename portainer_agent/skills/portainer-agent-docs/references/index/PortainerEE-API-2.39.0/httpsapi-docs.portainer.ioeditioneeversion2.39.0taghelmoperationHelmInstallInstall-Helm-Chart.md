##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/helm/operation/HelmInstall)Install Helm Chart
**Access policy** : authenticated
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### path Parameters
idrequired |  integer Environment(Endpoint) identifier
---|---
##### query Parameters
dryRun |  boolean Dry run
---|---
##### Request Body schema: application/json
required
Chart details
atomic |  boolean
---|---
chart |  string
name |  string
namespace |  string
registryId |  integer
repo |  string
values |  string
version |  string
### Responses
**201**
Created
**401**
Unauthorized
**404**
Environment(Endpoint) or ServiceAccount not found
**500**
Server error
post/endpoints/{id}/kubernetes/helm
https://api-docs.portainer.io/api/endpoints/{id}/kubernetes/helm
###  Request samples
  * Payload


Content type
application/json
Copy
`{

  *  "atomic": true,

  *  "chart": "string",

  *  "name": "string",

  *  "namespace": "string",

  *  "registryId": 0,

  *  "repo": "string",

  *  "values": "string",

  *  "version": "string"

 }`
###  Response samples
  * 201


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
