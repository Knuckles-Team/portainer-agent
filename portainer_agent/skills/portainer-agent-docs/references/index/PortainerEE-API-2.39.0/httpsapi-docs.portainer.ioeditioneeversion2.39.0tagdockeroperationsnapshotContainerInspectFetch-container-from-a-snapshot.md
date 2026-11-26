##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/docker/operation/snapshotContainerInspect)Fetch container from a snapshot
**Access policy** :
##### Authorizations:
_jwt_
##### path Parameters
environmentIdrequired |  integer Environment identifier
---|---
containerIdrequired |  integer Container identifier
### Responses
**200**
Success
**404**
Environment not found
get/docker/{environmentId}/snapshot/containers/{containerId}
https://api-docs.portainer.io/api/docker/{environmentId}/snapshot/containers/{containerId}
###  Response samples
  * 200


Content type
application/json
Copy
Expand all  Collapse all
`{

  *  "Command": "string",

  *  "Created": 0,

  *  "Env": [
    * "string"
 ],

  *  "HostConfig": {
    *  "Annotations": {
      *  "property1": "string",

      *  "property2": "string"
  },

    *  "NetworkMode": "string"
  },

  *  "Id": "string",

  *  "Image": "string",

  *  "ImageID": "string",

  *  "ImageManifestDescriptor": {
    *  "annotations": {
      *  "property1": "string",

      *  "property2": "string"
  },

    *  "artifactType": "string",

    *  "data": [
      * 0
 ],

    *  "digest": "string",

    *  "mediaType": "string",

    *  "platform": {
      *  "architecture": "string",

      *  "os": "string",

      *  "os.features": [
        * "string"
 ],

      *  "os.version": "string",

      *  "variant": "string"
  },

    *  "size": 0,

    *  "urls": [
      * "string"
 ]
  },

  *  "Labels": {
    *  "property1": "string",

    *  "property2": "string"
  },

  *  "Mounts": [
    *  {
      *  "Destination": "string",

      *  "Driver": "string",

      *  "Mode": "string",

      *  "Name": "string",

      *  "Propagation": "rprivate",

      *  "RW": true,

      *  "Source": "string",

      *  "Type": "bind"
  }
 ],

  *  "Names": [
    * "string"
 ],

  *  "NetworkSettings": {
    *  "Networks": {
      *  "property1": {
        *  "Aliases": [
          * "string"
 ],

        *  "DNSNames": [
          * "string"
 ],

        *  "DriverOpts": {
          *  "property1": "string",

          *  "property2": "string"
  },

        *  "EndpointID": "string",

        *  "Gateway": "string",

        *  "GlobalIPv6Address": "string",

        *  "GlobalIPv6PrefixLen": 0,

        *  "GwPriority": 0,

        *  "IPAMConfig": {
          *  "IPv4Address": "string",

          *  "IPv6Address": "string",

          *  "LinkLocalIPs": [
            * "string"
 ]
  },

        *  "IPAddress": "string",

        *  "IPPrefixLen": 0,

        *  "IPv6Gateway": "string",

        *  "Links": [
          * "string"
 ],

        *  "MacAddress": "string",

        *  "NetworkID": "string"
  },

      *  "property2": {
        *  "Aliases": [
          * "string"
 ],

        *  "DNSNames": [
          * "string"
 ],

        *  "DriverOpts": {
          *  "property1": "string",

          *  "property2": "string"
  },

        *  "EndpointID": "string",

        *  "Gateway": "string",

        *  "GlobalIPv6Address": "string",

        *  "GlobalIPv6PrefixLen": 0,

        *  "GwPriority": 0,

        *  "IPAMConfig": {
          *  "IPv4Address": "string",

          *  "IPv6Address": "string",

          *  "LinkLocalIPs": [
            * "string"
 ]
  },

        *  "IPAddress": "string",

        *  "IPPrefixLen": 0,

        *  "IPv6Gateway": "string",

        *  "Links": [
          * "string"
 ],

        *  "MacAddress": "string",

        *  "NetworkID": "string"
  }
  }
 },

  *  "Ports": [
    *  {
      *  "IP": "string",

      *  "PrivatePort": 0,

      *  "PublicPort": 0,

      *  "Type": "string"
  }
 ],

  *  "SizeRootFs": 0,

  *  "SizeRw": 0,

  *  "State": "created",

  *  "Status": "string"

 }`
