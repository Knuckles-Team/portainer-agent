##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/kubernetes/operation/GetAllKubernetesApplications)Get a list of applications across all namespaces in the cluster. If the nodeName is provided, it will return the applications running on that node.
Get a list of applications across all namespaces in the cluster. If the nodeName is provided, it will return the applications running on that node. **Access policy** : authenticated
##### Authorizations:
(_ApiKeyAuth_ _jwt_)
##### path Parameters
idrequired |  integer Environment(Endpoint) identifier
---|---
##### query Parameters
namespacerequired |  string Namespace name
---|---
nodeNamerequired |  string Node name
### Responses
**200**
Success
**400**
Invalid request
**401**
Unauthorized
**403**
Permission denied
**404**
Environment(Endpoint) not found
**500**
Server error
get/kubernetes/{id}/applications
https://api-docs.portainer.io/api/kubernetes/{id}/applications
###  Response samples
  * 200


Content type
application/json
Copy
Expand all  Collapse all
`[
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
                  * "string"
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

 ]`
