##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/kubernetes/operation/GetAllKubernetesVolumes)Get Kubernetes volumes within the given Portainer environment
Get a list of all kubernetes volumes within the given environment (Endpoint). The Endpoint ID must be a valid Portainer environment identifier. **Access policy** : Authenticated user.
##### Authorizations:
(_ApiKeyAuth_ _jwt_)
##### path Parameters
idrequired |  integer Environment identifier
---|---
##### query Parameters
withApplications |  boolean When set to True, include the applications that are using the volumes. It is set to false by default
---|---
### Responses
**200**
Success
**400**
Invalid request payload, such as missing required fields or fields not meeting validation criteria.
**403**
Unauthorized access or operation not allowed.
**500**
Server error occurred while attempting to retrieve kubernetes volumes.
get/kubernetes/{id}/volumes
https://api-docs.portainer.io/api/kubernetes/{id}/volumes
###  Response samples
  * 200


Content type
application/json
Copy
Expand all  Collapse all
`{

  *  "property1": {
    *  "persistentVolume": {
      *  "accessModes": [
        * "ReadWriteOnce"
 ],

      *  "annotations": {
        *  "property1": "string",

        *  "property2": "string"
  },

      *  "capacity": {
        *  "property1": {
          *  "Format": "DecimalExponent"
 },

        *  "property2": {
          *  "Format": "DecimalExponent"
 }
  },

      *  "claimRef": {
        *  "apiVersion": "string",

        *  "fieldPath": "string",

        *  "kind": "string",

        *  "name": "string",

        *  "namespace": "string",

        *  "resourceVersion": "string",

        *  "uid": "string"
  },

      *  "csi": {
        *  "controllerExpandSecretRef": {
          *  "name": "string",

          *  "namespace": "string"
  },

        *  "controllerPublishSecretRef": {
          *  "name": "string",

          *  "namespace": "string"
  },

        *  "driver": "string",

        *  "fsType": "string",

        *  "nodeExpandSecretRef": {
          *  "name": "string",

          *  "namespace": "string"
  },

        *  "nodePublishSecretRef": {
          *  "name": "string",

          *  "namespace": "string"
  },

        *  "nodeStageSecretRef": {
          *  "name": "string",

          *  "namespace": "string"
  },

        *  "readOnly": true,

        *  "volumeAttributes": {
          *  "property1": "string",

          *  "property2": "string"
  },

        *  "volumeHandle": "string"
  },

      *  "name": "string",

      *  "persistentVolumeReclaimPolicy": "Recycle",

      *  "storageClassName": "string",

      *  "volumeMode": "Block"
  },

    *  "persistentVolumeClaim": {
      *  "accessModes": [
        * "ReadWriteOnce"
 ],

      *  "creationDate": "string",

      *  "id": "string",

      *  "labels": {
        *  "property1": "string",

        *  "property2": "string"
  },

      *  "name": "string",

      *  "namespace": "string",

      *  "owningApplications": [
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

          *  "CustomResourceMetadata": {
            *  "apiVersion": "string",

            *  "kind": "string",

            *  "name": "string",

            *  "plural": "string",

            *  "scope": "string"
  },

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

              *  "Resource": {
                *  "CpuLimit": 0,

                *  "CpuRequest": 0,

                *  "MemoryLimit": 0,

                *  "MemoryRequest": 0
  },

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
                    * null
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

          *  "StackKind": "string",

          *  "StackName": "string",

          *  "Status": "string",

          *  "TotalPodsCount": 0,

          *  "Uid": "string"
  }
 ],

      *  "phase": "Pending",

      *  "resourcesRequests": {
        *  "property1": {
          *  "Format": "DecimalExponent"
 },

        *  "property2": {
          *  "Format": "DecimalExponent"
 }
  },

      *  "storage": 0,

      *  "storageClass": "string",

      *  "volumeMode": "Block",

      *  "volumeName": "string"
  },

    *  "storageClass": {
      *  "allowVolumeExpansion": true,

      *  "name": "string",

      *  "provisioner": "string",

      *  "reclaimPolicy": "Recycle"
  }
  },

  *  "property2": {
    *  "persistentVolume": {
      *  "accessModes": [
        * "ReadWriteOnce"
 ],

      *  "annotations": {
        *  "property1": "string",

        *  "property2": "string"
  },

      *  "capacity": {
        *  "property1": {
          *  "Format": "DecimalExponent"
 },

        *  "property2": {
          *  "Format": "DecimalExponent"
 }
  },

      *  "claimRef": {
        *  "apiVersion": "string",

        *  "fieldPath": "string",

        *  "kind": "string",

        *  "name": "string",

        *  "namespace": "string",

        *  "resourceVersion": "string",

        *  "uid": "string"
  },

      *  "csi": {
        *  "controllerExpandSecretRef": {
          *  "name": "string",

          *  "namespace": "string"
  },

        *  "controllerPublishSecretRef": {
          *  "name": "string",

          *  "namespace": "string"
  },

        *  "driver": "string",

        *  "fsType": "string",

        *  "nodeExpandSecretRef": {
          *  "name": "string",

          *  "namespace": "string"
  },

        *  "nodePublishSecretRef": {
          *  "name": "string",

          *  "namespace": "string"
  },

        *  "nodeStageSecretRef": {
          *  "name": "string",

          *  "namespace": "string"
  },

        *  "readOnly": true,

        *  "volumeAttributes": {
          *  "property1": "string",

          *  "property2": "string"
  },

        *  "volumeHandle": "string"
  },

      *  "name": "string",

      *  "persistentVolumeReclaimPolicy": "Recycle",

      *  "storageClassName": "string",

      *  "volumeMode": "Block"
  },

    *  "persistentVolumeClaim": {
      *  "accessModes": [
        * "ReadWriteOnce"
 ],

      *  "creationDate": "string",

      *  "id": "string",

      *  "labels": {
        *  "property1": "string",

        *  "property2": "string"
  },

      *  "name": "string",

      *  "namespace": "string",

      *  "owningApplications": [
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

          *  "CustomResourceMetadata": {
            *  "apiVersion": "string",

            *  "kind": "string",

            *  "name": "string",

            *  "plural": "string",

            *  "scope": "string"
  },

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

              *  "Resource": {
                *  "CpuLimit": 0,

                *  "CpuRequest": 0,

                *  "MemoryLimit": 0,

                *  "MemoryRequest": 0
  },

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
                    * null
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

          *  "StackKind": "string",

          *  "StackName": "string",

          *  "Status": "string",

          *  "TotalPodsCount": 0,

          *  "Uid": "string"
  }
 ],

      *  "phase": "Pending",

      *  "resourcesRequests": {
        *  "property1": {
          *  "Format": "DecimalExponent"
 },

        *  "property2": {
          *  "Format": "DecimalExponent"
 }
  },

      *  "storage": 0,

      *  "storageClass": "string",

      *  "volumeMode": "Block",

      *  "volumeName": "string"
  },

    *  "storageClass": {
      *  "allowVolumeExpansion": true,

      *  "name": "string",

      *  "provisioner": "string",

      *  "reclaimPolicy": "Recycle"
  }
  }

 }`
