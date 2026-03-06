##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/kubernetes/operation/getKubernetesPodSecurityRule)Get Pod Security Rule within k8s cluster, if not found, the frontend will create a default
Get Pod Security Rule within k8s cluster **Access policy** : authenticated
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### path Parameters
environmentIdrequired |  integer Environment identifier
---|---
### Responses
**200**
Success
**400**
Invalid request
**404**
Endpoint not found
**500**
Server error
get/kubernetes/{environmentId}/opa
https://api-docs.portainer.io/api/kubernetes/{environmentId}/opa
###  Response samples
  * 200


Content type
application/json
Copy
Expand all  Collapse all
`{

  *  "allowFlexVolumes": {
    *  "allowedVolumes": [
      * "string"
 ],

    *  "enabled": true
  },

  *  "allowPrivilegeEscalation": {
    *  "enabled": true
 },

  *  "allowProcMount": {
    *  "enabled": true,

    *  "procMountType": "string"
  },

  *  "appArmor": {
    *  "AppArmorType": [
      * "string"
 ],

    *  "enabled": true
  },

  *  "capabilities": {
    *  "allowedCapabilities": [
      * "string"
 ],

    *  "enabled": true,

    *  "requiredDropCapabilities": [
      * "string"
 ]
  },

  *  "enabled": true,

  *  "endPointID": 0,

  *  "forbiddenSysctlsList": {
    *  "enabled": true,

    *  "requiredDropCapabilities": [
      * "string"
 ]
  },

  *  "hostFilesystem": {
    *  "allowedPaths": [
      *  {
        *  "pathPrefix": "string",

        *  "readonly": true
  }
 ],

    *  "enabled": true
  },

  *  "hostNamespaces": {
    *  "enabled": true
 },

  *  "hostPorts": {
    *  "enabled": true,

    *  "hostNetwork": true,

    *  "max": 0,

    *  "min": 0
  },

  *  "id": 0,

  *  "privilegedContainers": {
    *  "enabled": true
 },

  *  "readOnlyRootFileSystem": {
    *  "enabled": true
 },

  *  "restrictDefaultNamespace": true,

  *  "restrictSecrets": true,

  *  "secComp": {
    *  "enabled": true,

    *  "secCompType": [
      * "string"
 ]
  },

  *  "selinux": {
    *  "allowedCapabilities": [
      *  {
        *  "level": "string",

        *  "role": "string",

        *  "type": "string",

        *  "user": "string"
  }
 ],

    *  "enabled": true
  },

  *  "users": {
    *  "enabled": true,

    *  "fsGroups": {
      *  "idrange": [
        *  {
          *  "max": 0,

          *  "min": 0
  }
 ],

      *  "type": "MayRunAs"
  },

    *  "runAsGroup": {
      *  "idrange": [
        *  {
          *  "max": 0,

          *  "min": 0
  }
 ],

      *  "type": "MayRunAs"
  },

    *  "runAsUser": {
      *  "idrange": [
        *  {
          *  "max": 0,

          *  "min": 0
  }
 ],

      *  "type": "MustRunAs"
  },

    *  "supplementalGroups": {
      *  "idrange": [
        *  {
          *  "max": 0,

          *  "min": 0
  }
 ],

      *  "type": "MayRunAs"
  }
  },

  *  "volumeTypes": {
    *  "allowedTypes": [
      * "azureFile"
 ],

    *  "enabled": true
  }

 }`
