##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/kubernetes/operation/CreateKubernetesService)Create a service
Create a service within a given namespace **Access policy** : Authenticated user.
##### Authorizations:
(_ApiKeyAuth_ _jwt_)
##### path Parameters
idrequired |  integer Environment identifier
---|---
namespacerequired |  string Namespace name
##### Request Body schema: application/json
required
Service definition
AllocateLoadBalancerNodePorts |  boolean
---|---
Annotations |  object
Applications |  Array of objects (models.K8sApplication)  serviceList screen
ClusterIPs |  Array of strings
CreationDate |  string
ExternalIPs |  Array of strings
ExternalName |  string
IngressStatus |  Array of objects (models.K8sServiceIngress)
Labels |  object
Name |  string
Namespace |  string
Ports |  Array of objects (models.K8sServicePort)
Selector |  object
Type |  string
UID |  string
### Responses
**204**
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
Server error occurred while attempting to create a service.
post/kubernetes/{id}/namespaces/{namespace}/services
https://api-docs.portainer.io/api/kubernetes/{id}/namespaces/{namespace}/services
###  Request samples
  * Payload


Content type
application/json
Copy
Expand all  Collapse all
`{

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
                  *  "hosts": [
                    * null
 ]
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

 }`
