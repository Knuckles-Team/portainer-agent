##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/endpoints/operation/EndpointCreate)Create a new environment(endpoint)
Create a new environment(endpoint) that will be used to manage an environment(endpoint). **Access policy** : administrator
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### Request Body schema: multipart/form-data
required
Namerequired |  string Name that will be used to identify this environment(endpoint) (example: my-environment)
---|---
EndpointCreationTyperequired |  integer Environment(Endpoint) type. Value must be one of: 1 (Local Docker environment), 2 (Agent environment), 3 (Azure environment), 4 (Edge agent environment) or 5 (Local Kubernetes Environment)
ContainerEngine |  string Container engine used by the environment(endpoint). Value must be one of: 'docker' or 'podman'
URL |  string URL or IP address of a Docker host (example: docker.mydomain.tld:2375). Defaults to local if not specified (Linux: /var/run/docker.sock, Windows: //./pipe/docker_engine). Cannot be empty if EndpointCreationType is set to 4 (Edge agent environment)
PublicURL |  string URL or IP address where exposed containers will be reachable. Defaults to URL if not specified (example: docker.mydomain.tld:2375)
GroupID |  integer Environment(Endpoint) group identifier. If not specified will default to 1 (unassigned).
TLS |  boolean Require TLS to connect against this environment(endpoint). Must be true if EndpointCreationType is set to 2 (Agent environment)
TLSSkipVerify |  boolean Skip server verification when using TLS. Must be true if EndpointCreationType is set to 2 (Agent environment)
TLSSkipClientVerify |  boolean Skip client verification when using TLS. Must be true if EndpointCreationType is set to 2 (Agent environment)
TLSCACertFile |  string <binary> TLS CA certificate file
TLSCertFile |  string <binary> TLS client certificate file
TLSKeyFile |  string <binary> TLS client key file
AzureApplicationID |  string Azure application ID. Required if environment(endpoint) type is set to 3
AzureTenantID |  string Azure tenant ID. Required if environment(endpoint) type is set to 3
AzureAuthenticationKey |  string Azure authentication key. Required if environment(endpoint) type is set to 3
TagIds |  Array of integers List of tag identifiers to which this environment(endpoint) is associated
EdgeCheckinInterval |  integer The check in interval for edge agent (in seconds)
EdgeTunnelServerAddress |  string URL or IP address that will be used to establish a reverse tunnel. Required when settings.EnableEdgeComputeFeatures is set to false or when settings.Edge.TunnelServerAddress is not set
EdgeAsyncMode |  boolean Enable async mode for edge agent
Gpus |  string List of GPUs - json stringified array of {name, value} structs
### Responses
**200**
Success
**400**
Invalid request
**409**
Name is not unique
**500**
Server error
post/endpoints
https://api-docs.portainer.io/api/endpoints
###  Response samples
  * 200


Content type
application/json
Copy
Expand all  Collapse all
`{

  *  "AMTDeviceGUID": "4c4c4544-004b-3910-8037-b6c04f504633",

  *  "Agent": {
    *  "PreviousVersion": "1.0.0",

    *  "Version": "1.0.0"
  },

  *  "AuthorizedTeams": [
    * 0
 ],

  *  "AuthorizedUsers": [
    * 0
 ],

  *  "AzureCredentials": {
    *  "ApplicationID": "eag7cdo9-o09l-9i83-9dO9-f0b23oe78db4",

    *  "AuthenticationKey": "cOrXoK/1D35w8YQ8nH1/8ZGwzz45JIYD5jxHKXEQknk=",

    *  "TenantID": "34ddc78d-4fel-2358-8cc1-df84c8o839f5"
  },

  *  "ChangeWindow": {
    *  "Enabled": true,

    *  "EndTime": "02:00",

    *  "StartTime": "22:00"
  },

  *  "CloudProvider": {
    *  "AddonWithArgs": [
      *  {
        *  "arguments": "string",

        *  "name": "string",

        *  "repository": "string"
  }
 ],

    *  "AmiType": "string",

    *  "CPU": 0,

    *  "CredentialID": 0,

    *  "DNSPrefix": "string",

    *  "HDD": 0,

    *  "InstanceType": "string",

    *  "KubernetesVersion": "string",

    *  "Name": "string",

    *  "NetworkID": "string",

    *  "NodeCount": 0,

    *  "NodeIPs": "string",

    *  "NodeVolumeSize": 0,

    *  "OfflineInstall": true,

    *  "PoolName": "string",

    *  "Provider": "string",

    *  "RAM": 0,

    *  "Region": "string",

    *  "ResourceGroup": "string",

    *  "Size": "string",

    *  "Tier": "string",

    *  "URL": "string"
  },

  *  "ComposeSyntaxMaxVersion": "3.8",

  *  "ContainerEngine": "docker",

  *  "DeploymentOptions": {
    *  "hideAddWithForm": true,

    *  "hideFileUpload": false,

    *  "hideWebEditor": false,

    *  "overrideGlobalOptions": true
  },

  *  "Edge": {
    *  "AsyncMode": true,

    *  "CommandInterval": 60,

    *  "PingInterval": 60,

    *  "SnapshotInterval": 60
  },

  *  "EdgeCheckinInterval": 5,

  *  "EdgeID": "string",

  *  "EdgeKey": "string",

  *  "EnableGPUManagement": true,

  *  "EnableImageNotification": true,

  *  "Gpus": [
    *  {
      *  "name": "name",

      *  "value": "value"
  }
 ],

  *  "GroupId": 1,

  *  "Heartbeat": true,

  *  "Id": 1,

  *  "IsEdgeDevice": true,

  *  "Kubernetes": {
    *  "Configuration": {
      *  "AllowNoneIngressClass": true,

      *  "EnableResourceOverCommit": true,

      *  "IngressAvailabilityPerNamespace": true,

      *  "IngressClasses": [
        *  {
          *  "Blocked": true,

          *  "BlockedNamespaces": [
            * "string"
 ],

          *  "Name": "string",

          *  "Type": "string"
  }
 ],

      *  "ResourceOverCommitPercentage": 0,

      *  "RestrictDefaultNamespace": true,

      *  "RestrictSecrets": true,

      *  "RestrictStandardUserIngressW": true,

      *  "StorageClasses": [
        *  {
          *  "AccessModes": [
            * "string"
 ],

          *  "AllowVolumeExpansion": true,

          *  "Name": "string",

          *  "Provisioner": "string"
  }
 ],

      *  "UseLoadBalancer": true,

      *  "UseServerMetrics": true
  },

    *  "Flags": {
      *  "IsServerIngressClassDetected": true,

      *  "IsServerMetricsDetected": true,

      *  "IsServerStorageDetected": true
  },

    *  "Snapshots": [
      *  {
        *  "DiagnosticsData": {
          *  "DNS": {
            *  "property1": "string",

            *  "property2": "string"
  },

          *  "Log": "string",

          *  "Proxy": {
            *  "property1": "string",

            *  "property2": "string"
  },

          *  "Telnet": {
            *  "property1": "string",

            *  "property2": "string"
  }
  },

        *  "KubernetesVersion": "string",

        *  "NodeCount": 0,

        *  "PerformanceMetrics": {
          *  "CPUUsage": 0,

          *  "MemoryUsage": 0,

          *  "NetworkUsage": 0
  },

        *  "Time": 0,

        *  "TotalCPU": 0,

        *  "TotalMemory": 0
  }
 ]
  },

  *  "LastCheckInDate": 0,

  *  "LocalTimeZone": "string",

  *  "MTLSStatus": {
    *  "enabled": true,

    *  "ok": true
  },

  *  "Name": "my-environment",

  *  "Policies": {
    *  "dockerRBACPolicy": {
      *  "policyID": 0,

      *  "policyName": "string",

      *  "policyStatus": {
        *  "LastAttemptTime": 0,

        *  "Message": "string",

        *  "Status": "applied"
  }
  },

    *  "dockerRegistryPolicy": {
      *  "policyID": 0,

      *  "policyName": "string",

      *  "policyStatus": {
        *  "LastAttemptTime": 0,

        *  "Message": "string",

        *  "Status": "applied"
  }
  },

    *  "dockerSecurityPolicy": {
      *  "policyID": 0,

      *  "policyName": "string",

      *  "policyStatus": {
        *  "LastAttemptTime": 0,

        *  "Message": "string",

        *  "Status": "applied"
  }
  },

    *  "dockerSetupPolicy": {
      *  "policyID": 0,

      *  "policyName": "string",

      *  "policyStatus": {
        *  "LastAttemptTime": 0,

        *  "Message": "string",

        *  "Status": "applied"
  }
  },

    *  "k8sRBACPolicy": {
      *  "policyID": 0,

      *  "policyName": "string",

      *  "policyStatus": {
        *  "LastAttemptTime": 0,

        *  "Message": "string",

        *  "Status": "applied"
  }
  },

    *  "k8sRegistryPolicy": {
      *  "policyID": 0,

      *  "policyName": "string",

      *  "policyStatus": {
        *  "LastAttemptTime": 0,

        *  "Message": "string",

        *  "Status": "applied"
  }
  },

    *  "k8sSecurityPolicy": {
      *  "policyID": 0,

      *  "policyName": "string",

      *  "policyStatus": {
        *  "LastAttemptTime": 0,

        *  "Message": "string",

        *  "Status": "applied"
  }
  },

    *  "k8sSetupPolicy": {
      *  "policyID": 0,

      *  "policyName": "string",

      *  "policyStatus": {
        *  "LastAttemptTime": 0,

        *  "Message": "string",

        *  "Status": "applied"
  }
  }
  },

  *  "PostInitMigrations": {
    *  "MigrateGPUs": true,

    *  "MigrateGateKeeper": true,

    *  "MigrateIngresses": true,

    *  "MigrateSecretOwners": true
  },

  *  "PublicURL": "docker.mydomain.tld:2375",

  *  "SecuritySettings": {
    *  "allowBindMountsForRegularUsers": false,

    *  "allowContainerCapabilitiesForRegularUsers": true,

    *  "allowDeviceMappingForRegularUsers": true,

    *  "allowHostNamespaceForRegularUsers": true,

    *  "allowPrivilegedModeForRegularUsers": false,

    *  "allowStackManagementForRegularUsers": true,

    *  "allowSysctlSettingForRegularUsers": true,

    *  "allowVolumeBrowserForRegularUsers": true,

    *  "enableHostManagementFeatures": true
  },

  *  "Snapshots": [
    *  {
      *  "ContainerCount": 0,

      *  "DiagnosticsData": {
        *  "DNS": {
          *  "property1": "string",

          *  "property2": "string"
  },

        *  "Log": "string",

        *  "Proxy": {
          *  "property1": "string",

          *  "property2": "string"
  },

        *  "Telnet": {
          *  "property1": "string",

          *  "property2": "string"
  }
  },

      *  "DockerSnapshotRaw": { },

      *  "DockerVersion": "string",

      *  "GpuUseAll": true,

      *  "GpuUseList": [
        * "string"
 ],

      *  "HealthyContainerCount": 0,

      *  "ImageCount": 0,

      *  "IsPodman": true,

      *  "NodeCount": 0,

      *  "PerformanceMetrics": {
        *  "CPUUsage": 0,

        *  "MemoryUsage": 0,

        *  "NetworkUsage": 0
  },

      *  "RunningContainerCount": 0,

      *  "ServiceCount": 0,

      *  "StackCount": 0,

      *  "StoppedContainerCount": 0,

      *  "Swarm": true,

      *  "Time": 0,

      *  "TotalCPU": 0,

      *  "TotalMemory": 0,

      *  "UnhealthyContainerCount": 0,

      *  "VolumeCount": 0
  }
 ],

  *  "Status": 1,

  *  "StatusMessage": {
    *  "detail": "string",

    *  "operation": "string",

    *  "operationStatus": "processing",

    *  "summary": "string",

    *  "warnings": [
      * "string"
 ]
  },

  *  "TLS": true,

  *  "TLSCACert": "string",

  *  "TLSCert": "string",

  *  "TLSConfig": {
    *  "TLS": true,

    *  "TLSCACert": "/data/tls/ca.pem",

    *  "TLSCert": "/data/tls/cert.pem",

    *  "TLSKey": "/data/tls/key.pem",

    *  "TLSSkipVerify": false
  },

  *  "TLSKey": "string",

  *  "TagIds": [
    * 0
 ],

  *  "Tags": [
    * "string"
 ],

  *  "TeamAccessPolicies": {
    *  "property1": {
      *  "Namespaces": [
        * "string"
 ],

      *  "RoleId": 1
  },

    *  "property2": {
      *  "Namespaces": [
        * "string"
 ],

      *  "RoleId": 1
  }
  },

  *  "Type": 1,

  *  "URL": "docker.mydomain.tld:2375",

  *  "UserAccessPolicies": {
    *  "property1": {
      *  "Namespaces": [
        * "string"
 ],

      *  "RoleId": 1
  },

    *  "property2": {
      *  "Namespaces": [
        * "string"
 ],

      *  "RoleId": 1
  }
  },

  *  "UserTrusted": true

 }`
