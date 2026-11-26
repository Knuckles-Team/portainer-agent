    - rbac
    - security
    - setup
    - registry
    type: string
    x-enum-varnames:
    - CategoryRBAC
    - CategorySecurity
    - CategorySetup
    - CategoryRegistry
  policies.PolicyStatusBreakdown:
    properties:
      Applied:
        type: integer
      Failed:
        type: integer
      InProgress:
        type: integer
      NotSupported:
        type: integer
      Warning:
        type: integer
    type: object
  policies.PolicyTemplate:
    properties:
      category:
        $ref: '#/definitions/policies.PolicyCategory'
      data:
        additionalProperties: {}
        type: object
      description:
        type: string
      id:
        type: string
      name:
        type: string
      type:
        $ref: '#/definitions/policies.PolicyType'
    type: object
  policies.PolicyType:
    enum:
    - rbac-k8s
    - security-k8s
    - setup-k8s
    - registry-k8s
    - rbac-docker
    - security-docker
    - setup-docker
    - registry-docker
    - rbac-k8s
    - security-k8s
    - setup-k8s
    - registry-k8s
    - rbac-docker
    - security-docker
    - setup-docker
    - registry-docker
    type: string
    x-enum-varnames:
    - RbacK8s
    - SecurityK8s
    - SetupK8s
    - RegistryK8s
    - RbacDocker
    - SecurityDocker
    - SetupDocker
    - RegistryDocker
  policies.conflictInfo:
    properties:
      environmentCount:
        type: integer
      environmentGroupId:
        type: integer
      environmentGroupName:
        type: string
      existingPolicyId:
        type: integer
      existingPolicyName:
        type: string
      supportedEnvironments:
        type: integer
      unsupportedEnvironments:
        type: integer
    type: object
  policies.newGroupInfo:
    properties:
      environmentCount:
        type: integer
      environmentGroupId:
        type: integer
      environmentGroupName:
        type: string
      supportedEnvironments:
        type: integer
      unsupportedEnvironments:
        type: integer
    type: object
  policies.policyConflictsPayload:
    type: object
  policies.policyConflictsResponse:
    properties:
      conflicts:
        items:
          $ref: '#/definitions/policies.conflictInfo'
        type: array
      newGroups:
        items:
          $ref: '#/definitions/policies.newGroupInfo'
        type: array
      supportedEnvironments:
        type: integer
      totalEnvironments:
        type: integer
      unsupportedEnvironments:
        type: integer
    type: object
  policies.policyCreatePayload:
    type: object
  policies.policyListResponse:
    properties:
      policies:
        items:
          $ref: '#/definitions/policies.GenericPolicy'
        type: array
    type: object
  policies.policyMetadataResponse:
    properties:
      minimumAgentVersions:
        additionalProperties:
          type: string
        type: object
    type: object
  policies.policyUpdatePayload:
    properties:
      AllowOverride:
        example: false
        type: boolean
      Data:
        additionalProperties: {}
        type: object
      EnvironmentGroups:
        items:
          type: integer
        type: array
      EnvironmentType:
        example: kubernetes
        type: string
      Name:
        example: Updated Development Policy
        type: string
      Type:
        $ref: '#/definitions/policies.PolicyType'
    type: object
  policies.templateListResponse:
    properties:
      templates:
        items:
          $ref: '#/definitions/policies.PolicyTemplate'
        type: array
    type: object
  portainer.APIKey:
    properties:
      dateCreated:
        description: Unix timestamp (UTC) when the API key was created
        type: integer
      description:
        example: portainer-api-key
        type: string
      digest:
        description: Digest represents SHA256 hash of the raw API key
        type: string
      id:
        example: 1
        type: integer
      lastUsed:
        description: Unix timestamp (UTC) when the API key was last used
        type: integer
      prefix:
        description: API key identifier (7 char prefix)
        type: string
      userId:
        example: 1
        type: integer
    type: object
  portainer.AccessPolicy:
    properties:
      Namespaces:
        description: Namespaces is a list of namespaces that this access policy applies
          to. Only used for namespaced level roles
        items:
          type: string
        type: array
      RoleId:
        description: Role identifier. Reference the role that will be associated to
          this access policy
        example: 1
        type: integer
    type: object
  portainer.AuthenticationMethod:
    enum:
    - 0
    - 1
    - 2
    - 3
    type: integer
    x-enum-varnames:
    - _
    - AuthenticationInternal
    - AuthenticationLDAP
    - AuthenticationOAuth
  portainer.Authorizations:
    additionalProperties:
      type: boolean
    type: object
  portainer.AutoUpdateSettings:
    properties:
      ForcePullImage:
        description: Pull latest image
        example: false
        type: boolean
      ForceUpdate:
        description: Force update ignores repo changes
        example: false
        type: boolean
      Interval:
        description: Auto update interval
        example: 1m30s
        type: string
      JobID:
        description: Autoupdate job id
        example: "15"
        type: string
      Webhook:
        description: A UUID generated from client
        example: 05de31a2-79fa-4644-9c12-faa67e5c49f0
        type: string
    type: object
  portainer.AzureCredentials:
    properties:
      ApplicationID:
        description: Azure application ID
        example: eag7cdo9-o09l-9i83-9dO9-f0b23oe78db4
        type: string
      AuthenticationKey:
        description: Azure authentication key
        example: cOrXoK/1D35w8YQ8nH1/8ZGwzz45JIYD5jxHKXEQknk=
        type: string
      TenantID:
        description: Azure tenant ID
        example: 34ddc78d-4fel-2358-8cc1-df84c8o839f5
        type: string
    type: object
  portainer.CustomTemplatePlatform:
    enum:
    - 0
    - 1
    - 2
    type: integer
    x-enum-varnames:
    - _
    - CustomTemplatePlatformLinux
    - CustomTemplatePlatformWindows
  portainer.CustomTemplateVariableDefinition:
    properties:
      defaultValue:
        example: default value
        type: string
      description:
        example: Description
        type: string
      label:
        example: My Variable
        type: string
      name:
        example: MY_VAR
        type: string
    type: object
  portainer.DiagnosticsData:
    properties:
      DNS:
        additionalProperties:
          type: string
        type: object
      Log:
        type: string
      Proxy:
        additionalProperties:
          type: string
        type: object
      Telnet:
        additionalProperties:
          type: string
        type: object
    type: object
  portainer.DockerContainerSnapshot:
    properties:
      Command:
        type: string
      Created:
        type: integer
      Env:
        description: EE-5240
        items:
          type: string
        type: array
      HostConfig:
        properties:
          Annotations:
            additionalProperties:
              type: string
            type: object
          NetworkMode:
            type: string
        type: object
      Id:
        type: string
      Image:
        type: string
      ImageID:
        type: string
      ImageManifestDescriptor:
        $ref: '#/definitions/v1.Descriptor'
      Labels:
        additionalProperties:
          type: string
        type: object
      Mounts:
        items:
          $ref: '#/definitions/container.MountPoint'
        type: array
      Names:
        items:
          type: string
        type: array
      NetworkSettings:
        $ref: '#/definitions/container.NetworkSettingsSummary'
      Ports:
        items:
          $ref: '#/definitions/container.Port'
        type: array
      SizeRootFs:
        type: integer
      SizeRw:
        type: integer
      State:
        $ref: '#/definitions/container.ContainerState'
      Status:
        type: string
    type: object
  portainer.DockerSnapshot:
    properties:
      ContainerCount:
        type: integer
      DiagnosticsData:
        $ref: '#/definitions/portainer.DiagnosticsData'
      DockerSnapshotRaw:
        $ref: '#/definitions/portainer.DockerSnapshotRaw'
      DockerVersion:
        type: string
      GpuUseAll:
        type: boolean
      GpuUseList:
        items:
          type: string
        type: array
      HealthyContainerCount:
        type: integer
      ImageCount:
        type: integer
      IsPodman:
        type: boolean
      NodeCount:
        type: integer
      PerformanceMetrics:
        $ref: '#/definitions/portainer.PerformanceMetrics'
      RunningContainerCount:
        type: integer
      ServiceCount:
        type: integer
      StackCount:
        type: integer
      StoppedContainerCount:
        type: integer
      Swarm:
        type: boolean
      Time:
        type: integer
      TotalCPU:
        type: integer
      TotalMemory:
        type: integer
      UnhealthyContainerCount:
        type: integer
      VolumeCount:
        type: integer
    type: object
  portainer.DockerSnapshotRaw:
    type: object
  portainer.EcrData:
    properties:
      Region:
        example: ap-southeast-2
        type: string
    type: object
  portainer.Edge:
    properties:
      AsyncMode:
        description: Deprecated 2.18
        example: false
        type: boolean
      CommandInterval:
        description: The command list interval for edge agent - used in edge async
          mode (in seconds)
        example: 5
        type: integer
      PingInterval:
        description: The ping interval for edge agent - used in edge async mode (in
          seconds)
        example: 5
        type: integer
      SnapshotInterval:
        description: The snapshot interval for edge agent - used in edge async mode
          (in seconds)
        example: 5
        type: integer
    type: object
  portainer.EdgeJob:
    properties:
      Created:
        type: integer
      CronExpression:
        type: string
      EdgeGroups:
        items:
          type: integer
        type: array
      Endpoints:
        additionalProperties:
          $ref: '#/definitions/portainer.EdgeJobEndpointMeta'
        type: object
      GroupLogsCollection:
        additionalProperties:
          $ref: '#/definitions/portainer.EdgeJobEndpointMeta'
        description: Field used for log collection of Endpoints belonging to EdgeGroups
        type: object
      Id:
        description: EdgeJob Identifier
        example: 1
        type: integer
      Name:
        type: string
      Recurring:
        type: boolean
      ScriptPath:
        type: string
      Version:
        type: integer
    type: object
  portainer.EdgeJobEndpointMeta:
    properties:
      CollectLogs:
        type: boolean
      LogsStatus:
        $ref: '#/definitions/portainer.EdgeJobLogsStatus'
    type: object
  portainer.EdgeJobLogsStatus:
    enum:
    - 0
    - 1
    - 2
    - 3
    type: integer
    x-enum-varnames:
    - _
    - EdgeJobLogsStatusIdle
    - EdgeJobLogsStatusPending
    - EdgeJobLogsStatusCollected
  portainer.EdgeStackDeploymentStatus:
    properties:
      Error:
        type: string
      RollbackTo:
        description: EE only feature
        type: integer
      Time:
        type: integer
      Type:
        $ref: '#/definitions/portainer.EdgeStackStatusType'
      Version:
        type: integer
    type: object
  portainer.EdgeStackDeploymentType:
    enum:
    - 0
    - 1
    type: integer
    x-enum-varnames:
    - EdgeStackDeploymentCompose
    - EdgeStackDeploymentKubernetes
  portainer.EdgeStackStatus:
    properties:
      DeploymentInfo:
        allOf:
        - $ref: '#/definitions/portainer.StackDeploymentInfo'
        description: EE only feature
      Details:
        allOf:
        - $ref: '#/definitions/portainer.EdgeStackStatusDetails'
        description: Deprecated
      EndpointID:
        type: integer
      Error:
        description: Deprecated
        type: string
      ReadyRePullImage:
        description: ReadyRePullImage is a flag to indicate whether the auto update
          is trigger to re-pull image
        type: boolean
      Status:
        items:
          $ref: '#/definitions/portainer.EdgeStackDeploymentStatus'
        type: array
      Type:
        allOf:
        - $ref: '#/definitions/portainer.EdgeStackStatusType'
        description: Deprecated
    type: object
  portainer.EdgeStackStatusDetails:
    properties:
      Acknowledged:
        type: boolean
      Error:
        type: boolean
      ImagesPulled:
        type: boolean
      Ok:
        type: boolean
      Pending:
        type: boolean
      RemoteUpdateSuccess:
        type: boolean
      Remove:
        type: boolean
    type: object
  portainer.EdgeStackStatusType:
    enum:
    - 0
    - 1
    - 2
    - 3
    - 4
    - 5
    - 6
    - 7
    - 8
    - 9
    - 10
    - 11
    - 12
    - 13
    type: integer
    x-enum-varnames:
    - EdgeStackStatusPending
    - EdgeStackStatusDeploymentReceived
    - EdgeStackStatusError
    - EdgeStackStatusAcknowledged
    - EdgeStackStatusRemoved
    - EdgeStackStatusRemoteUpdateSuccess
    - EdgeStackStatusImagesPulled
    - EdgeStackStatusRunning
    - EdgeStackStatusDeploying
    - EdgeStackStatusRemoving
    - EdgeStackStatusPausedDeploying
    - EdgeStackStatusRollingBack
    - EdgeStackStatusRolledBack
    - EdgeStackStatusCompleted
  portainer.EndpointAuthorizations:
    additionalProperties:
      $ref: '#/definitions/portainer.Authorizations'
    type: object
  portainer.EndpointGroup:
    properties:
      AuthorizedTeams:
        items:
          type: integer
        type: array
      AuthorizedUsers:
        description: Deprecated in DBVersion == 18
        items:
          type: integer
        type: array
      Description:
        description: Description associated to the environment(endpoint) group
        example: Environment(Endpoint) group description
        type: string
      Id:
        description: Environment(Endpoint) group Identifier
        example: 1
        type: integer
      Labels:
        description: Deprecated fields
        items:
          $ref: '#/definitions/portainer.Pair'
        type: array
      Name:
        description: Environment(Endpoint) group name
        example: my-environment-group
        type: string
      TagIds:
        description: List of tags associated to this environment(endpoint) group
        items:
          type: integer
        type: array
      Tags:
        description: Deprecated in DBVersion == 22
        items:
          type: string
        type: array
      TeamAccessPolicies:
        $ref: '#/definitions/portainer.TeamAccessPolicies'
      UserAccessPolicies:
        $ref: '#/definitions/portainer.UserAccessPolicies'
    type: object
  portainer.EndpointPostInitMigrations:
    properties:
      MigrateGPUs:
        type: boolean
      MigrateIngresses:
        type: boolean
    type: object
  portainer.EndpointSecuritySettings:
    properties:
      allowBindMountsForRegularUsers:
        description: Whether non-administrator should be able to use bind mounts when
          creating containers
        example: false
        type: boolean
      allowContainerCapabilitiesForRegularUsers:
        description: Whether non-administrator should be able to use container capabilities
        example: true
        type: boolean
      allowDeviceMappingForRegularUsers:
        description: Whether non-administrator should be able to use device mapping
        example: true
        type: boolean
      allowHostNamespaceForRegularUsers:
        description: Whether non-administrator should be able to use the host pid
        example: true
        type: boolean
      allowPrivilegedModeForRegularUsers:
        description: Whether non-administrator should be able to use privileged mode
          when creating containers
        example: false
        type: boolean
      allowStackManagementForRegularUsers:
        description: Whether non-administrator should be able to manage stacks
        example: true
        type: boolean
      allowSysctlSettingForRegularUsers:
        description: Whether non-administrator should be able to use sysctl settings
        example: true
        type: boolean
      allowVolumeBrowserForRegularUsers:
        description: Whether non-administrator should be able to browse volumes
        example: true
        type: boolean
      enableHostManagementFeatures:
        description: Whether host management features are enabled
        example: true
        type: boolean
    type: object
  portainer.EndpointStatus:
    enum:
    - 0
    - 1
    - 2
    type: integer
    x-enum-varnames:
    - _
    - EndpointStatusUp
    - EndpointStatusDown
  portainer.EndpointType:
    enum:
    - 0
    - 1
    - 2
    - 3
    - 4
    - 5
    - 6
    - 7
    type: integer
    x-enum-varnames:
    - _
    - DockerEnvironment
    - AgentOnDockerEnvironment
    - AzureEnvironment
    - EdgeAgentOnDockerEnvironment
    - KubernetesLocalEnvironment
    - AgentOnKubernetesEnvironment
    - EdgeAgentOnKubernetesEnvironment
  portainer.EnvironmentEdgeSettings:
    properties:
      AsyncMode:
        description: Whether the device has been started in edge async mode
        type: boolean
      CommandInterval:
        description: The command list interval for edge agent - used in edge async
          mode [seconds]
        example: 60
        type: integer
      PingInterval:
        description: The ping interval for edge agent - used in edge async mode [seconds]
        example: 60
        type: integer
      SnapshotInterval:
        description: The snapshot interval for edge agent - used in edge async mode
          [seconds]
        example: 60
        type: integer
    type: object
  portainer.GithubRegistryData:
    properties:
      OrganisationName:
        type: string
      UseOrganisation:
        type: boolean
    type: object
  portainer.GitlabRegistryData:
    properties:
      InstanceURL:
        type: string
      ProjectId:
        type: integer
      ProjectPath:
        type: string
    type: object
  portainer.GlobalDeploymentOptions:
    properties:
      hideStacksFunctionality:
        example: false
        type: boolean
    type: object
  portainer.HelmConfig:
    properties:
      Atomic:
        description: Enable automatic rollback on deployment failure (equivalent to
          helm --atomic flag)
        example: true
        type: boolean
      ChartPath:
        description: Path to a Helm chart folder for Helm git deployments
        example: charts/my-app
        type: string
      Timeout:
        description: Timeout for Helm operations (equivalent to helm --timeout flag)
        example: 5m0s
        type: string
      ValuesFiles:
        description: Array of paths to Helm values YAML files for Helm git deployments
        example:
        - '[''values/prod.yaml'''
        - ' ''values/secrets.yaml'']'
        items:
          type: string
        type: array
      Version:
        description: Helm chart version from Chart.yaml (read-only, extracted during
          Git sync)
        example: 1.2.3
        type: string
    type: object
  portainer.HelmUserRepository:
    properties:
      Id:
        description: Membership Identifier
        example: 1
        type: integer
      URL:
        description: Helm repository URL
        example: https://charts.bitnami.com/bitnami
        type: string
      UserId:
        description: User identifier
        example: 1
        type: integer
    type: object
  portainer.InternalAuthSettings:
    properties:
      RequiredPasswordLength:
        type: integer
    type: object
  portainer.K8sNamespaceInfo:
    properties:
      Annotations:
        additionalProperties:
          type: string
        type: object
      CreationDate:
        type: string
      Id:
        type: string
      IsDefault:
        type: boolean
      IsSystem:
        type: boolean
      Name:
        type: string
      NamespaceOwner:
        type: string
      ResourceQuota:
        $ref: '#/definitions/v1.ResourceQuota'
      Status:
        $ref: '#/definitions/v1.NamespaceStatus'
      UnhealthyEventCount:
        type: integer
    type: object
  portainer.K8sNodeLimits:
    properties:
      CPU:
        type: integer
      Memory:
        type: integer
    type: object
  portainer.K8sNodesLimits:
    additionalProperties:
      $ref: '#/definitions/portainer.K8sNodeLimits'
    type: object
  portainer.KubernetesConfiguration:
    properties:
      AllowNoneIngressClass:
        type: boolean
      EnableResourceOverCommit:
        type: boolean
      IngressAvailabilityPerNamespace:
        type: boolean
      IngressClasses:
        items:
          $ref: '#/definitions/portainer.KubernetesIngressClassConfig'
        type: array
      ResourceOverCommitPercentage:
        type: integer
      RestrictDefaultNamespace:
        type: boolean
      StorageClasses:
        items:
          $ref: '#/definitions/portainer.KubernetesStorageClassConfig'
        type: array
      UseLoadBalancer:
        type: boolean
      UseServerMetrics:
        type: boolean
    type: object
  portainer.KubernetesData:
    properties:
      Configuration:
        $ref: '#/definitions/portainer.KubernetesConfiguration'
      Flags:
        $ref: '#/definitions/portainer.KubernetesFlags'
      Snapshots:
        items:
          $ref: '#/definitions/portainer.KubernetesSnapshot'
        type: array
    type: object
  portainer.KubernetesFlags:
    properties:
      IsServerIngressClassDetected:
        type: boolean
      IsServerMetricsDetected:
        type: boolean
      IsServerStorageDetected:
        type: boolean
    type: object
  portainer.KubernetesIngressClassConfig:
    properties:
      Blocked:
        type: boolean
      BlockedNamespaces:
        items:
          type: string
        type: array
      Name:
        type: string
      Type:
        type: string
    type: object
  portainer.KubernetesSnapshot:
    properties:
      DiagnosticsData:
        $ref: '#/definitions/portainer.DiagnosticsData'
      KubernetesVersion:
        type: string
      NodeCount:
        type: integer
      PerformanceMetrics:
        $ref: '#/definitions/portainer.PerformanceMetrics'
      Time:
        type: integer
      TotalCPU:
        type: integer
      TotalMemory:
        type: integer
    type: object
  portainer.KubernetesStorageClassConfig:
    properties:
      AccessModes:
        items:
          type: string
        type: array
      AllowVolumeExpansion:
        type: boolean
      Name:
        type: string
      Provisioner:
        type: string
    type: object
  portainer.LDAPGroupSearchSettings:
    properties:
      GroupAttribute:
        description: LDAP attribute which denotes the group membership
        example: member
        type: string
      GroupBaseDN:
        description: The distinguished name of the element from which the LDAP server
          will search for groups
        example: dc=ldap,dc=domain,dc=tld
        type: string
      GroupFilter:
        description: The LDAP search filter used to select group elements, optional
        example: (objectClass=account
        type: string
    type: object
  portainer.LDAPSearchSettings:
    properties:
      BaseDN:
        description: The distinguished name of the element from which the LDAP server
          will search for users
        example: dc=ldap,dc=domain,dc=tld
        type: string
      Filter:
        description: Optional LDAP search filter used to select user elements
        example: (objectClass=account)
        type: string
      UserNameAttribute:
        description: LDAP attribute which denotes the username
        example: uid
        type: string
    type: object
  portainer.LDAPSettings:
    properties:
      AnonymousMode:
        description: Enable this option if the server is configured for Anonymous
          access. When enabled, ReaderDN and Password will not be used
        example: true
        type: boolean
      AutoCreateUsers:
        description: Automatically provision users and assign them to matching LDAP
          group names
        example: true
        type: boolean
      GroupSearchSettings:
        items:
          $ref: '#/definitions/portainer.LDAPGroupSearchSettings'
        type: array
      Password:
        description: Password of the account that will be used to search users
        example: readonly-password
        type: string
      ReaderDN:
        description: Account that will be used to search for users
        example: cn=readonly-account,dc=ldap,dc=domain,dc=tld
        type: string
      SearchSettings:
        items:
          $ref: '#/definitions/portainer.LDAPSearchSettings'
        type: array
      StartTLS:
        description: Whether LDAP connection should use StartTLS
        example: true
        type: boolean
      TLSConfig:
        $ref: '#/definitions/portainer.TLSConfiguration'
      URL:
        description: URL or IP address of the LDAP server
        example: myldap.domain.tld:389
        type: string
    type: object
  portainer.LDAPUser:
    properties:
      Groups:
        items:
          type: string
        type: array
      Name:
        type: string
    type: object
