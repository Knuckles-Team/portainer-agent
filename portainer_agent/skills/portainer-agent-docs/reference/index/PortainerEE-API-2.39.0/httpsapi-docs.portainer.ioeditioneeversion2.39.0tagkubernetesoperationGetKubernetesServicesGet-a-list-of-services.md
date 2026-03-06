##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/kubernetes/operation/GetKubernetesServices)Get a list of services
Get a list of services that the user has access to. **Access policy** : Authenticated user.
##### Authorizations:
(_ApiKeyAuth_ _jwt_)
##### path Parameters
idrequired |  integer Environment identifier
---|---
##### query Parameters
withApplications |  boolean Lookup applications associated with each service
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
Server error occurred while attempting to retrieve all services.
get/kubernetes/{id}/services
https://api-docs.portainer.io/api/kubernetes/{id}/services
###  Response samples
  * 200


Content type
application/json
Copy
Expand all  Collapse all
`[
  *  {
    *  "AllocateLoadBalancerNodePorts": true,

    *  "Annotations": {
      *  "property1": "string",

      *  "property2": "string"
  },

    *  "Applications": [
      *  {
        *  "Annotations": {
          *  "property1": "string",

          *  "property2": "string"
  },

        *  "ApplicationOwner": "string",

        *  "ApplicationType": "string",

        *  "Configurations": [
          *  {
            *  "ConfigurationOwner": "string",

            *  "Data": {
              *  "property1": null,

              *  "property2": null
  },

            *  "Kind": "string"
  }
 ],

        *  "Containers": [
          * null
 ],

        *  "CreationDate": "string",

        *  "DeploymentType": "string",

        *  "Id": "string",

        *  "Image": "string",

        *  "Kind": "string",

        *  "Labels": {
          *  "property1": "string",

          *  "property2": "string"
  },

        *  "LoadBalancerIPAddress": "string",

        *  "MatchLabels": {
          *  "property1": "string",

          *  "property2": "string"
  },

        *  "Metadata": {
          *  "annotations": {
            *  "property1": "string",

            *  "property2": "string"
  },

          *  "labels": {
            *  "property1": "string",

            *  "property2": "string"
  }
  },

        *  "Name": "string",

        *  "Namespace": "string",

        *  "Pods": [
          *  {
            *  "ContainerName": "string",

            *  "CreationDate": "string",

            *  "Image": "string",

            *  "ImagePullPolicy": "string",

            *  "Name": "string",

            *  "NodeName": "string",

            *  "PodIP": "string",

            *  "Status": "string",

            *  "Uid": "string"
  }
 ],

        *  "PublishedPorts": [
          *  {
            *  "IngressRules": [
              *  {
                *  "Host": "string",

                *  "IP": "string",

                *  "Path": "string",

                *  "TLS": [
                  *  {
                    *  "hosts": [ ]
 }
 ]
  }
 ],

            *  "Port": 0
  }
 ],

        *  "Resource": {
          *  "CpuLimit": 0,

          *  "CpuRequest": 0,

          *  "MemoryLimit": 0,

          *  "MemoryRequest": 0
  },

        *  "ResourcePool": "string",

        *  "RunningPodsCount": 0,

        *  "ServiceId": "string",

        *  "ServiceName": "string",

        *  "ServiceType": "string",

        *  "StackId": "string",

        *  "StackName": "string",

        *  "Status": "string",

        *  "TotalPodsCount": 0,

        *  "Uid": "string"
  }
 ],

    *  "ClusterIPs": [
      * "string"
 ],

    *  "CreationDate": "string",

    *  "ExternalIPs": [
      * "string"
 ],

    *  "ExternalName": "string",

    *  "IngressStatus": [
      *  {
        *  "Host": "string",

        *  "IP": "string"
  }
 ],

    *  "Labels": {
      *  "property1": "string",

      *  "property2": "string"
  },

    *  "Name": "string",

    *  "Namespace": "string",

    *  "Ports": [
      *  {
        *  "Name": "string",

        *  "NodePort": 0,

        *  "Port": 0,

        *  "Protocol": "string",

        *  "TargetPort": "string"
  }
 ],

    *  "Selector": {
      *  "property1": "string",

      *  "property2": "string"
  },

    *  "Type": "string",

    *  "UID": "string"
  }

 ]`
