          from a Docker Compose file
        example: false
        type: boolean
      Logo:
        description: URL of the template's logo
        example: https://portainer.io/img/logo.svg
        type: string
      Note:
        description: A note that will be displayed in the UI. Supports HTML content
        example: This is my <b>custom</b> template
        type: string
      Platform:
        allOf:
        - $ref: '#/definitions/portainer.CustomTemplatePlatform'
        description: |-
          Platform associated to the template.
          Valid values are: 1 - 'linux', 2 - 'windows'
        enum:
        - 1
        - 2
        example: 1
      ProjectPath:
        description: Path on disk to the repository hosting the Stack file
        example: /data/custom_template/3
        type: string
      ResourceControl:
        $ref: '#/definitions/portainer.ResourceControl'
      Title:
        description: Title of the template
        example: Nginx
        type: string
      Type:
        allOf:
        - $ref: '#/definitions/portainer.StackType'
        description: |-
          Type of created stack:
          * 1 - swarm
          * 2 - compose
          * 3 - kubernetes
        enum:
        - 1
        - 2
        - 3
        example: 1
      Variables:
        items:
          $ref: '#/definitions/portainer.CustomTemplateVariableDefinition'
        type: array
    type: object
  portaineree.CustomTemplateEdgeSettings:
    properties:
      PrePullImage:
        description: Pre Pull Image
        type: boolean
      PrivateRegistryId:
        type: integer
      RelativePathSettings:
        $ref: '#/definitions/portaineree.CustomTemplateRelativePathSettings'
      RetryDeploy:
        description: Retry deploy
        example: false
        type: boolean
      RetryPeriod:
        type: integer
      StaggerConfig:
        allOf:
        - $ref: '#/definitions/portaineree.EdgeStaggerConfig'
        description: StaggerConfig is the configuration for staggered update
    type: object
  portaineree.CustomTemplateRelativePathSettings:
    properties:
      FilesystemPath:
        description: Local filesystem path
        example: /tmp
        type: string
      PerDeviceConfigsGroupMatchType:
        allOf:
        - $ref: '#/definitions/portainer.PerDevConfigsFilterType'
        description: Per device configs group match type
        enum:
        - file
        - ' dir'
        example: file
      PerDeviceConfigsMatchType:
        allOf:
        - $ref: '#/definitions/portainer.PerDevConfigsFilterType'
        description: Per device configs match type
        enum:
        - file
        - ' dir'
        example: file
      PerDeviceConfigsPath:
        description: Per device configs path
        example: configs
        type: string
      SupportPerDeviceConfigs:
        description: Whether the edge stack supports per device configs
        example: false
        type: boolean
      SupportRelativePath:
        description: Whether the stack supports relative path volume
        example: false
        type: boolean
    type: object
  portaineree.DeploymentOptions:
    properties:
      hideAddWithForm:
        description: Hide manual deploy forms in portainer
        example: true
        type: boolean
      hideFileUpload:
        description: Hide the file upload option in the remaining visible forms
        example: false
        type: boolean
      hideWebEditor:
        description: Hide the webeditor in the remaining visible forms
        example: false
        type: boolean
      overrideGlobalOptions:
        type: boolean
    type: object
  portaineree.Edge:
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
      MTLS:
        $ref: '#/definitions/portaineree.MTLSSettings'
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
      TunnelServerAddress:
        description: The address where the tunneling server can be reached by Edge
          agents
        example: portainer.domain.tld
        type: string
    type: object
  portaineree.EdgeAsyncCommand:
    properties:
      endpointID:
        type: integer
      executed:
        type: boolean
      id:
        type: integer
      op:
        $ref: '#/definitions/portaineree.EdgeAsyncCommandOperation'
      path:
        type: string
      scheduledTime:
        type: string
      timestamp:
        type: string
      type:
        $ref: '#/definitions/portaineree.EdgeAsyncCommandType'
      value: {}
    type: object
  portaineree.EdgeAsyncCommandOperation:
    enum:
    - add
    - remove
    - replace
    type: string
    x-enum-varnames:
    - EdgeAsyncCommandOpAdd
    - EdgeAsyncCommandOpRemove
    - EdgeAsyncCommandOpReplace
  portaineree.EdgeAsyncCommandType:
    enum:
    - edgeConfig
    - edgeStack
    - edgeJob
    - edgeLog
    - container
    - image
    - volume
    - normalStack
    type: string
    x-enum-varnames:
    - EdgeAsyncCommandTypeConfig
    - EdgeAsyncCommandTypeStack
    - EdgeAsyncCommandTypeJob
    - EdgeAsyncCommandTypeLog
    - EdgeAsyncCommandTypeContainer
    - EdgeAsyncCommandTypeImage
    - EdgeAsyncCommandTypeVolume
    - EdgeAsyncCommandTypeNormalStack
  portaineree.EdgeConfig:
    properties:
      baseDir:
        type: string
      category:
        $ref: '#/definitions/portaineree.EdgeConfigCategory'
      created:
        type: integer
      createdBy:
        type: integer
      edgeGroupIDs:
        items:
          type: integer
        type: array
      id:
        type: integer
      name:
        type: string
      prev:
        $ref: '#/definitions/portaineree.EdgeConfig'
      progress:
        $ref: '#/definitions/portaineree.EdgeConfigProgress'
      state:
        $ref: '#/definitions/portaineree.EdgeConfigStateType'
      type:
        type: integer
      updated:
        type: integer
      updatedBy:
        type: integer
    type: object
  portaineree.EdgeConfigCategory:
    enum:
    - configuration
    - secret
    type: string
    x-enum-varnames:
    - EdgeConfigCategoryConfig
    - EdgeConfigCategorySecret
  portaineree.EdgeConfigProgress:
    properties:
      success:
        type: integer
      total:
        type: integer
    type: object
  portaineree.EdgeConfigStateType:
    enum:
    - 0
    - 1
    - 2
    - 3
    - 4
    type: integer
    x-enum-varnames:
    - EdgeConfigIdleState
    - EdgeConfigFailureState
    - EdgeConfigSavingState
    - EdgeConfigDeletingState
    - EdgeConfigUpdatingState
  portaineree.EdgeGroup:
    properties:
      Dynamic:
        type: boolean
      EdgeUpdateID:
        type: integer
      EndpointIds:
        $ref: '#/definitions/roar.Roar-portainer_EndpointID'
      Endpoints:
        description: 'Deprecated: only used for API responses'
        items:
          type: integer
        type: array
      Id:
        description: EdgeGroup Identifier
        example: 1
        type: integer
      Name:
        type: string
      PartialMatch:
        type: boolean
      TagIds:
        items:
          type: integer
        type: array
    type: object
  portaineree.EdgeStack:
    properties:
      AlwaysCloneGitRepoForRelativePath:
        description: Whether the edge stack always clones the git repository for relative
          path
        example: false
        type: boolean
      AutoUpdate:
        allOf:
        - $ref: '#/definitions/portainer.AutoUpdateSettings'
        description: The GitOps update settings of a git stack
      CreatedBy:
        description: The username which created this stack
        example: admin
        type: string
      CreatedByUserId:
        description: The username id which created this stack
        example: "1"
        type: string
      CreationDate:
        description: StatusArray    map[EndpointID][]EdgeStackStatus `json:"StatusArray"`
        type: integer
      DeployerOptions:
        allOf:
        - $ref: '#/definitions/portaineree.EdgeStackDeployerOptions'
        description: Options to control the Deployer behaviour
      DeploymentType:
        $ref: '#/definitions/portainer.EdgeStackDeploymentType'
      EdgeGroups:
        items:
          type: integer
        type: array
      EdgeUpdateID:
        description: EdgeUpdateID represents the parent update ID, will be zero if
          this stack is not part of an update
        type: integer
      EntryPoint:
        type: string
      EnvVars:
        description: EnvVars is a list of environment variables to inject into the
          stack
        items:
          $ref: '#/definitions/portainer.Pair'
        type: array
      FilesystemPath:
        description: Local filesystem path
        example: /tmp
        type: string
      GitConfig:
        allOf:
        - $ref: '#/definitions/gittypes.RepoConfig'
        description: The git configuration of a git stack
      HelmConfig:
        allOf:
        - $ref: '#/definitions/portainer.HelmConfig'
        description: HelmConfig is the configuration for a Helm based deployment of
          an edge stack (Helm Chart)
      Id:
        description: EdgeStack Identifier
        example: 1
        type: integer
      ManifestPath:
        type: string
      Name:
        type: string
      NumDeployments:
        type: integer
      PerDeviceConfigsGroupMatchType:
        allOf:
        - $ref: '#/definitions/portainer.PerDevConfigsFilterType'
        description: Per device configs group match type
        enum:
        - file
        - ' dir'
        example: file
      PerDeviceConfigsMatchType:
        allOf:
        - $ref: '#/definitions/portainer.PerDevConfigsFilterType'
        description: Per device configs match type
        enum:
        - file
        - ' dir'
        example: file
      PerDeviceConfigsPath:
        description: Per device configs path
        example: configs
        type: string
      PrePullImage:
        description: Pre Pull Image
        type: boolean
      PreviousDeploymentInfo:
        allOf:
        - $ref: '#/definitions/portainer.StackDeploymentInfo'
        description: PreviousDeploymentInfo represents the previous deployment info
          of the stack
      ProjectPath:
        type: string
      RePullImage:
        description: |-
          Deprecated(2.36): keep it for backward compatibility. To remove in future versions (2.44+)
          Re-Pull Image
        type: boolean
      Registries:
        items:
          type: integer
        type: array
      RetryDeploy:
        description: Retry deploy
        example: false
        type: boolean
      RetryPeriod:
        description: RetryPeriod specifies the duration, in seconds, for which the
          agent should continue attempting to deploy the stack after a failure
        type: integer
      ScheduledTime:
        description: Schedule represents the schedule of the Edge stack (optional,
          format - 'YYYY-MM-DD HH:mm:ss')
        example: "2020-11-13 14:53:00"
        type: string
      StackFileVersion:
        description: StackFileVersion represents the version of the stack file, such
          yaml, hcl, manifest file
        example: 1
        type: integer
      StaggerConfig:
        allOf:
        - $ref: '#/definitions/portaineree.EdgeStaggerConfig'
        description: StaggerConfig is the configuration for staggered update
      Status:
        additionalProperties:
          $ref: '#/definitions/portainer.EdgeStackStatus'
        type: object
      SupportPerDeviceConfigs:
        description: Whether the edge stack supports per device configs
        example: false
        type: boolean
      SupportRelativePath:
        description: Whether the stack supports relative path volume
        example: false
        type: boolean
      UseManifestNamespaces:
        description: Uses the manifest's namespaces instead of the default one
        type: boolean
      Version:
        type: integer
      Webhook:
        description: A UUID to identify a webhook. The stack will be force updated
          and pull the latest image when the webhook was invoked.
        example: c11fdf23-183e-428a-9bb6-16db01032174
        type: string
    type: object
  portaineree.EdgeStackDeployerOptions:
    properties:
      Prune:
        description: Drives `compose up --remove-orphans` and `stack up --prune` options
        type: boolean
      RemoveVolumes:
        description: Drives `compose down --volumes` option
        type: boolean
    type: object
  portaineree.EdgeStaggerConfig:
    properties:
      DeviceNumber:
        type: integer
      DeviceNumberIncrementBy:
        type: integer
      DeviceNumberStartFrom:
        type: integer
      StaggerOption:
        $ref: '#/definitions/portaineree.EdgeStaggerOption'
      StaggerParallelOption:
        $ref: '#/definitions/portaineree.EdgeStaggerParallelOption'
      Timeout:
        description: Timeout unit is minute
        example: "5"
        type: string
      UpdateDelay:
        description: UpdateDelay unit is minute
        example: "5"
        type: string
      UpdateFailureAction:
        $ref: '#/definitions/portaineree.EdgeUpdateFailureAction'
    type: object
  portaineree.EdgeStaggerOption:
    enum:
    - 0
    - 1
    - 2
    type: integer
    x-enum-varnames:
    - _
    - EdgeStaggerOptionAllAtOnce
    - EdgeStaggerOptionParallel
  portaineree.EdgeStaggerParallelOption:
    enum:
    - 0
    - 1
    - 2
    type: integer
    x-enum-varnames:
    - _
    - EdgeStaggerParallelOptionFixed
    - EdgeStaggerParallelOptionIncremental
  portaineree.EdgeUpdateFailureAction:
    enum:
    - 0
    - 1
    - 2
    - 3
    type: integer
    x-enum-varnames:
    - _
    - EdgeUpdateFailureActionContinue
    - EdgeUpdateFailureActionPause
    - EdgeUpdateFailureActionRollback
  portaineree.Endpoint:
    properties:
      AMTDeviceGUID:
        description: The identifier of the AMT Device associated with this environment(endpoint)
        example: 4c4c4544-004b-3910-8037-b6c04f504633
        type: string
      Agent:
        $ref: '#/definitions/portaineree.EnvironmentAgentData'
      AuthorizedTeams:
        items:
          type: integer
        type: array
      AuthorizedUsers:
        description: Deprecated in DBVersion == 18
        items:
          type: integer
        type: array
      AzureCredentials:
        $ref: '#/definitions/portainer.AzureCredentials'
      ChangeWindow:
        allOf:
        - $ref: '#/definitions/portaineree.EndpointChangeWindow'
        description: GitOps update change window restriction for stacks and apps
      CloudProvider:
        allOf:
        - $ref: '#/definitions/portaineree.CloudProvider'
        description: |-
          A Kubernetes as a service cloud provider. Only included if this
          endpoint was created using KaaS provisioning.
      ComposeSyntaxMaxVersion:
        description: Maximum version of docker-compose
        example: "3.8"
        type: string
      ContainerEngine:
        description: ContainerEngine represents the container engine type. This can
          be 'docker' or 'podman' when interacting directly with these environmentes,
          otherwise '' for kubernetes environments.
        example: docker
        type: string
      DeploymentOptions:
        allOf:
        - $ref: '#/definitions/portaineree.DeploymentOptions'
        description: Hide manual deployment forms for an environment
      Edge:
        $ref: '#/definitions/portainer.EnvironmentEdgeSettings'
      EdgeCheckinInterval:
        description: The check in interval for edge agent (in seconds)
        example: 5
        type: integer
      EdgeID:
        description: The identifier of the edge agent associated with this environment(endpoint)
        type: string
      EdgeKey:
        description: The key which is used to map the agent to Portainer
        type: string
      EnableGPUManagement:
        type: boolean
      EnableImageNotification:
        type: boolean
      Gpus:
        items:
          $ref: '#/definitions/portainer.Pair'
        type: array
      GroupId:
        description: Environment(Endpoint) group identifier
        example: 1
        type: integer
      Heartbeat:
        description: Heartbeat indicates the heartbeat status of an edge environment
        example: true
        type: boolean
      Id:
        description: Environment(Endpoint) Identifier
        example: 1
        type: integer
      IsEdgeDevice:
        description: Deprecated v2.18
        type: boolean
      Kubernetes:
        allOf:
        - $ref: '#/definitions/portaineree.KubernetesData'
        description: Associated Kubernetes data
      LastCheckInDate:
        description: LastCheckInDate mark last check-in date on checkin
        type: integer
      LocalTimeZone:
        description: LocalTimeZone is the local time zone of the endpoint
        type: string
      MTLSStatus:
        $ref: '#/definitions/portaineree.MTLSStatus'
      Name:
        description: Environment(Endpoint) name
        example: my-environment
        type: string
      Policies:
        $ref: '#/definitions/portaineree.EndpointPolicies'
      PostInitMigrations:
        allOf:
        - $ref: '#/definitions/portaineree.EndpointPostInitMigrations'
        description: Whether we need to run any "post init migrations".
      PublicURL:
        description: URL or IP address where exposed containers will be reachable
        example: docker.mydomain.tld:2375
        type: string
      SecuritySettings:
        allOf:
        - $ref: '#/definitions/portainer.EndpointSecuritySettings'
        description: Environment(Endpoint) specific security settings
      Snapshots:
        description: List of snapshots
        items:
          $ref: '#/definitions/portainer.DockerSnapshot'
        type: array
      Status:
        allOf:
        - $ref: '#/definitions/portainer.EndpointStatus'
        description: The status of the environment(endpoint) (1 - up, 2 - down)
        example: 1
      StatusMessage:
        allOf:
        - $ref: '#/definitions/portaineree.EndpointStatusMessage'
        description: |-
          A message that describes the status. Should be included for Status 3
          or 4.
      TLS:
        description: |-
          Deprecated fields
          Deprecated in DBVersion == 4
        type: boolean
      TLSCACert:
        type: string
      TLSCert:
        type: string
      TLSConfig:
        $ref: '#/definitions/portainer.TLSConfiguration'
      TLSKey:
        type: string
      TagIds:
        description: List of tag identifiers to which this environment(endpoint) is
          associated
        items:
          type: integer
        type: array
      Tags:
        description: Deprecated in DBVersion == 22
        items:
          type: string
        type: array
      TeamAccessPolicies:
        allOf:
        - $ref: '#/definitions/portainer.TeamAccessPolicies'
        description: List of team identifiers authorized to connect to this environment(endpoint)
      Type:
        allOf:
        - $ref: '#/definitions/portainer.EndpointType'
        description: Environment(Endpoint) environment(endpoint) type. 1 for a Docker
          environment(endpoint), 2 for an agent on Docker environment(endpoint) or
          3 for an Azure environment(endpoint).
        example: 1
      URL:
        description: URL or IP address of the Docker host associated to this environment(endpoint)
        example: docker.mydomain.tld:2375
        type: string
      UserAccessPolicies:
        allOf:
        - $ref: '#/definitions/portainer.UserAccessPolicies'
        description: List of user identifiers authorized to connect to this environment(endpoint)
      UserTrusted:
        description: Whether the device has been trusted or not by the user
        type: boolean
    type: object
  portaineree.EndpointChangeWindow:
    properties:
      Enabled:
        example: true
        type: boolean
      EndTime:
        example: "02:00"
        type: string
      StartTime:
        example: "22:00"
        type: string
    type: object
  portaineree.EndpointOperationStatus:
    enum:
    - processing
    - warning
    - error
    - ""
    type: string
    x-enum-varnames:
    - EndpointOperationStatusProcessing
    - EndpointOperationStatusWarning
    - EndpointOperationStatusError
    - EndpointOperationStatusDone
  portaineree.EndpointPolicies:
    properties:
      dockerRBACPolicy:
        $ref: '#/definitions/portaineree.AppliedPolicy'
      dockerRegistryPolicy:
        $ref: '#/definitions/portaineree.AppliedPolicy'
      dockerSecurityPolicy:
        $ref: '#/definitions/portaineree.AppliedPolicy'
      dockerSetupPolicy:
        $ref: '#/definitions/portaineree.AppliedPolicy'
      k8sRBACPolicy:
        $ref: '#/definitions/portaineree.AppliedPolicy'
      k8sRegistryPolicy:
        $ref: '#/definitions/portaineree.AppliedPolicy'
      k8sSecurityPolicy:
        $ref: '#/definitions/portaineree.AppliedPolicy'
      k8sSetupPolicy:
        $ref: '#/definitions/portaineree.AppliedPolicy'
    type: object
  portaineree.EndpointPostInitMigrations:
    properties:
      MigrateGPUs:
        type: boolean
      MigrateGateKeeper:
        type: boolean
      MigrateIngresses:
        type: boolean
      MigrateSecretOwners:
        type: boolean
    type: object
  portaineree.EndpointStatusMessage:
    properties:
      detail:
        type: string
      operation:
        description: |-
          TODO: in future versions, we should think about removing these fields and
          create a separate bucket to store cluster operation messages instead or try to find a better way.
          Operation/OperationStatus blank means, nothing is happening
        type: string
      operationStatus:
        allOf:
        - $ref: '#/definitions/portaineree.EndpointOperationStatus'
        description: ',processing,error'
      summary:
        type: string
      warnings:
        items:
          type: string
        type: array
    type: object
  portaineree.EnvironmentAgentData:
    properties:
      PreviousVersion:
        example: 1.0.0
        type: string
      Version:
        example: 1.0.0
        type: string
    type: object
  portaineree.ExperimentalFeatures:
    type: object
  portaineree.GitCredential:
    properties:
      authorizationType:
        allOf:
        - $ref: '#/definitions/gittypes.GitCredentialAuthType'
        example: 0
      creationDate:
        example: 1587399600
        type: integer
      id:
        example: 1
        type: integer
      name:
        type: string
      password:
        type: string
      userId:
        example: 1
        type: integer
      username:
        type: string
    type: object
  portaineree.GithubRegistryData:
    properties:
      OrganisationName:
        type: string
      UseOrganisation:
        type: boolean
    type: object
  portaineree.GlobalDeploymentOptions:
    properties:
      hideAddWithForm:
        description: Hide manual deploy forms in portainer
        example: false
        type: boolean
      hideFileUpload:
        description: Hide the file upload option in the remaining visible forms
        example: false
        type: boolean
      hideStacksFunctionality:
        example: false
        type: boolean
      hideWebEditor:
        description: Hide the webeditor in the remaining visible forms
        example: false
        type: boolean
      minApplicationNoteLength:
        example: 10
        type: integer
      perEnvOverride:
        description: Configure this per environment or globally
        example: false
        type: boolean
      requireNoteOnApplications:
        description: Make note field mandatory if enabled
        example: false
        type: boolean
    type: object
  portaineree.KubernetesConfiguration:
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
      RestrictSecrets:
        type: boolean
      RestrictStandardUserIngressW:
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
  portaineree.KubernetesData:
    properties:
      Configuration:
        $ref: '#/definitions/portaineree.KubernetesConfiguration'
      Flags:
        $ref: '#/definitions/portainer.KubernetesFlags'
      Snapshots:
        items:
          $ref: '#/definitions/portainer.KubernetesSnapshot'
        type: array
    type: object
  portaineree.LDAPKerberosSettings:
    properties:
      Configuration:
        type: string
      Password:
        type: string
      Realm:
        type: string
