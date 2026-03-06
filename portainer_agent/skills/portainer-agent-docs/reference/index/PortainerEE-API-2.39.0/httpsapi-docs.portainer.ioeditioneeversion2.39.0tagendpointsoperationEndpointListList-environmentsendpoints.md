##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/endpoints/operation/EndpointList)List environments(endpoints)
List all environments(endpoints) based on the current user authorizations. Will return all environments(endpoints) if using an administrator or team leader account otherwise it will only return authorized environments(endpoints). **Access policy** : restricted
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### query Parameters
start |  integer Start searching from
---|---
limit |  integer Limit results to this value
sort |  string Enum: "Name" "Group" "Status" "LastCheckIn" "EdgeID" Sort results by this value
order |  integer Order sorted results by desc/asc
updateInformation |  boolean If true, an `X-Update-Available` header will be added to the response to indicate if an update is available
k8sEnvAdmin |  boolean If true, an `X-K8S-Env-Admin` header will be added to the response to indicate if the user is a K8S environment admin for any of the returned environments
search |  string Search query
groupIds |  Array of integers List environments(endpoints) of these groups
status |  Array of integers List environments(endpoints) by this status
types |  Array of integers List environments(endpoints) of this type
tagIds |  Array of integers search environments(endpoints) with these tags (depends on tagsPartialMatch)
tagsPartialMatch |  boolean If true, will return environment(endpoint) which has one of tagIds, if false (or missing) will return only environments(endpoints) that has all the tags
endpointIds |  Array of integers will return only these environments(endpoints)
excludeIds |  Array of integers will exclude these environments(endpoints)
provisioned |  boolean If true, will return environment(endpoint) that were provisioned
agentVersions |  Array of strings will return only environments with on of these agent versions
edgeAsync |  boolean if exists true show only edge async agents, false show only standard edge agents. if missing, will show both types (relevant only for edge agents)
edgeDeviceUntrusted |  boolean if true, show only untrusted edge agents, if false show only trusted edge agents (relevant only for edge agents)
edgeCheckInPassedSeconds |  number if bigger then zero, show only edge agents that checked-in in the last provided seconds (relevant only for edge agents)
excludeSnapshots |  boolean if true, the snapshot data won't be retrieved
name |  string will return only environments(endpoints) with this name
nameFilter |  string Filter environments by partial name match (case-insensitive, searches name only)
edgeStackStatus |  string only applied when edgeStackId exists. Filter the returned environments based on their deployment status in the stack (not the environment status!)
edgeGroupIds |  Array of integers List environments(endpoints) of these edge groups
excludeEdgeGroupIds |  Array of integers Exclude environments(endpoints) of these edge groups
policy |  boolean If true, will apply policy data to the returned environments(endpoints)
policyIds |  Array of integers List environments(endpoints) associated with these policies
policyStatus |  Array of strings Filter environments by policy status (applied, failed, in_progress, warning, not_supported). Only applies when policyIds is specified.
### Responses
**200**
Endpoints
**500**
Server error
get/endpoints
https://api-docs.portainer.io/api/endpoints
###  Response samples
  * 200


Content type
application/json
Copy
Expand all  Collapse all
`[
  *  {
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
  }

 ]`
