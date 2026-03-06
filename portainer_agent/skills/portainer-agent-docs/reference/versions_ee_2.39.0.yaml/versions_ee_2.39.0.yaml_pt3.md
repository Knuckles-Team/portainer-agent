        - 1
        - 2
        items:
          type: integer
        type: array
      TeamAccessPolicies:
        $ref: '#/definitions/portainer.TeamAccessPolicies'
      URL:
        description: URL or IP address of a Docker host
        example: docker.mydomain.tld:2375
        type: string
      UserAccessPolicies:
        $ref: '#/definitions/portainer.UserAccessPolicies'
    type: object
  endpoints.endpointUpdateRelation:
    properties:
      EdgeGroups:
        items:
          type: integer
        type: array
      Group:
        type: integer
      Tags:
        items:
          type: integer
        type: array
    type: object
  endpoints.endpointUpdateRelationsPayload:
    properties:
      Relations:
        additionalProperties:
          $ref: '#/definitions/endpoints.endpointUpdateRelation'
        type: object
    type: object
  endpoints.forceUpdateServicePayload:
    properties:
      PullImage:
        description: PullImage if true will pull the image
        type: boolean
      ServiceID:
        description: ServiceId to update
        type: string
    type: object
  endpoints.registryAccessPayload:
    properties:
      Namespaces:
        items:
          type: string
        type: array
      TeamAccessPolicies:
        $ref: '#/definitions/portainer.TeamAccessPolicies'
      UserAccessPolicies:
        $ref: '#/definitions/portainer.UserAccessPolicies'
    type: object
  endpoints.resourcePoolUpdatePayload:
    properties:
      TeamsToAdd:
        items:
          type: integer
        type: array
      TeamsToRemove:
        items:
          type: integer
        type: array
      UsersToAdd:
        items:
          type: integer
        type: array
      UsersToRemove:
        items:
          type: integer
        type: array
    type: object
  filesystem.DirEntry:
    properties:
      Content:
        type: string
      IsFile:
        type: boolean
      Name:
        type: string
      Permissions:
        $ref: '#/definitions/os.FileMode'
    type: object
  github_com_portainer_portainer-ee_api_docker_images.Status:
    enum:
    - processing
    - outdated
    - updated
    - skipped
    - preparing
    - error
    type: string
    x-enum-varnames:
    - Processing
    - Outdated
    - Updated
    - Skipped
    - Preparing
    - Error
  github_com_portainer_portainer-ee_api_http_handler_edgestacks.aggregatedStatusesMap:
    additionalProperties:
      type: integer
    type: object
  github_com_portainer_portainer-ee_api_http_handler_edgestacks.edgeStackFromGitRepositoryPayload:
    properties:
      AlwaysCloneGitRepoForRelativePath:
        description: Whether the edge stack always clones the git repository for relative
          path
        example: false
        type: boolean
      AutoUpdate:
        allOf:
        - $ref: '#/definitions/portainer.AutoUpdateSettings'
        description: Optional GitOps update configuration
      CreatedFromCustomTemplateID:
        description: CreatedFromCustomTemplateID used to determine whether the edge
          stack is created from a custom template
        type: integer
      DeploymentType:
        allOf:
        - $ref: '#/definitions/portainer.EdgeStackDeploymentType'
        description: |-
          Deployment type to deploy this stack
          Valid values are: 0 - 'compose', 1 - 'kubernetes'
          compose is enabled only for docker environments
          kubernetes is enabled only for kubernetes environments
        enum:
        - 0
        - 1
        example: 0
      EdgeGroups:
        description: List of identifiers of EdgeGroups
        example:
        - 1
        items:
          type: integer
        type: array
      EnvVars:
        description: List of environment variables
        items:
          $ref: '#/definitions/portainer.Pair'
        type: array
      FilePathInRepository:
        default: docker-compose.yml
        description: Path to the Stack file inside the Git repository
        example: docker-compose.yml
        type: string
      FilesystemPath:
        description: Local filesystem path
        example: /mnt
        type: string
      HelmConfig:
        allOf:
        - $ref: '#/definitions/portainer.HelmConfig'
        description: HelmConfig is the configuration for the Helm chart
      Name:
        description: |-
          Name of the stack
          Max length: 255
          Name must only contains lowercase characters, numbers, hyphens, or underscores
          Name must start with a lowercase character or number
          Example: stack-name or stack_123 or stackName
        example: stack-name
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
      PrePullImage:
        description: Pre Pull image
        example: false
        type: boolean
      Registries:
        description: List of Registries to use for this stack
        items:
          type: integer
        type: array
      RepositoryAuthentication:
        description: Use basic authentication to clone the Git repository
        example: true
        type: boolean
      RepositoryAuthorizationType:
        allOf:
        - $ref: '#/definitions/gittypes.GitCredentialAuthType'
        description: RepositoryAuthorizationType is the authorization type to use
        example: 0
      RepositoryGitCredentialID:
        description: GitCredentialID used to identify the binded git credential
        example: 0
        type: integer
      RepositoryPassword:
        description: Password used in basic authentication. Required when RepositoryAuthentication
          is true.
        example: myGitPassword
        type: string
      RepositoryReferenceName:
        description: Reference name of a Git repository hosting the Stack file
        example: refs/heads/master
        type: string
      RepositoryURL:
        description: URL of a Git repository hosting the Stack file
        example: https://github.com/openfaas/faas
        type: string
      RepositoryUsername:
        description: Username used in basic authentication. Required when RepositoryAuthentication
          is true.
        example: myGitUsername
        type: string
      RetryDeploy:
        description: Retry deploy
        example: false
        type: boolean
      RetryPeriod:
        description: Retry period specifies the duration, in seconds, for which the
          agent should continue attempting to deploy the stack after a failure
        type: integer
      StaggerConfig:
        allOf:
        - $ref: '#/definitions/portaineree.EdgeStaggerConfig'
        description: Configuration for stagger updates
      SupportPerDeviceConfigs:
        description: Whether the edge stack supports per device configs
        example: false
        type: boolean
      SupportRelativePath:
        description: Whether the stack supports relative path volume
        example: false
        type: boolean
      TLSSkipVerify:
        description: TLSSkipVerify skips SSL verification when cloning the Git repository
        example: false
        type: boolean
      UseManifestNamespaces:
        description: Uses the manifest's namespaces instead of the default one
        type: boolean
    required:
    - EdgeGroups
    - Name
    - RepositoryURL
    type: object
  github_com_portainer_portainer-ee_api_http_handler_edgestacks.edgeStackFromStringPayload:
    properties:
      DeploymentType:
        allOf:
        - $ref: '#/definitions/portainer.EdgeStackDeploymentType'
        description: |-
          Deployment type to deploy this stack
          Valid values are: 0 - 'compose', 1 - 'kubernetes'
          compose is enabled only for docker environments
          kubernetes is enabled only for kubernetes environments
        enum:
        - 0
        - 1
        example: 0
      EdgeGroups:
        description: List of identifiers of EdgeGroups
        example:
        - 1
        items:
          type: integer
        type: array
      EnvVars:
        description: List of environment variables
        items:
          $ref: '#/definitions/portainer.Pair'
        type: array
      Name:
        description: |-
          Name of the stack
          Max length: 255
          Name must only contains lowercase characters, numbers, hyphens, or underscores
          Name must start with a lowercase character or number
          Example: stack-name or stack_123 or stackName
        example: stack-name
        type: string
      PrePullImage:
        description: Pre Pull image
        example: false
        type: boolean
      Registries:
        description: List of Registries to use for this stack
        items:
          type: integer
        type: array
      RetryDeploy:
        description: Retry deploy
        example: false
        type: boolean
      RetryPeriod:
        description: Retry period specifies the duration, in seconds, for which the
          agent should continue attempting to deploy the stack after a failure
        type: integer
      StackFileContent:
        description: Content of the Stack file
        example: |-
          version: 3
           services:
           web:
           image:nginx
        type: string
      StaggerConfig:
        allOf:
        - $ref: '#/definitions/portaineree.EdgeStaggerConfig'
        description: Configuration for stagger updates
      UseManifestNamespaces:
        description: Uses the manifest's namespaces instead of the default one
        type: boolean
      Webhook:
        description: Optional webhook configuration
        example: c11fdf23-183e-428a-9bb6-16db01032174
        type: string
    required:
    - Name
    - StackFileContent
    type: object
  github_com_portainer_portainer-ee_api_http_handler_edgestacks.edgeStackListResponseItem:
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
      StatusSummary:
        $ref: '#/definitions/github_com_portainer_portainer-ee_api_http_handler_edgestacks.edgeStackStatusSummary'
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
  github_com_portainer_portainer-ee_api_http_handler_edgestacks.edgeStackStatusSummary:
    properties:
      AggregatedStatus:
        $ref: '#/definitions/github_com_portainer_portainer-ee_api_http_handler_edgestacks.aggregatedStatusesMap'
      Reason:
        type: string
      Status:
        $ref: '#/definitions/edgestacks.SummarizedStatus'
    type: object
  github_com_portainer_portainer-ee_api_http_handler_edgestacks.stackFileResponse:
    properties:
      StackFileContent:
        type: string
    type: object
  github_com_portainer_portainer-ee_api_http_handler_edgestacks.updateEdgeStackPayload:
    properties:
      DeployerOptions:
        allOf:
        - $ref: '#/definitions/edgestacks.deployerOptionsPayload'
        description: Options to control the deployer behaviour
      DeploymentType:
        $ref: '#/definitions/portainer.EdgeStackDeploymentType'
      EdgeGroups:
        items:
          type: integer
        type: array
      EnvVars:
        description: Environment variables to inject into the stack
        items:
          $ref: '#/definitions/portainer.Pair'
        type: array
      PrePullImage:
        type: boolean
      RePullImage:
        description: 'Deprecated(2.36): use RepullImageAndRedeploy instead'
        type: boolean
      Registries:
        items:
          type: integer
        type: array
      RepullImageAndRedeploy:
        description: RepullImageAndRedeploy indicates whether the edge stack is manually
          forced to redeploy
        type: boolean
      RetryDeploy:
        type: boolean
      RetryPeriod:
        description: RetryPeriod specifies the duration, in seconds, for which the
          agent should continue attempting to deploy the stack after a failure
        type: integer
      RollbackTo:
        description: RollbackTo specifies the stack file version to rollback to (only
          support to rollback to the last version currently)
        type: integer
      StackFileContent:
        type: string
      StaggerConfig:
        allOf:
        - $ref: '#/definitions/portaineree.EdgeStaggerConfig'
        description: Configuration for stagger updates
      UpdateVersion:
        type: boolean
      UseManifestNamespaces:
        description: Uses the manifest's namespaces instead of the default one
        type: boolean
      Webhook:
        description: Optional webhook configuration
        example: c11fdf23-183e-428a-9bb6-16db01032174
        type: string
    type: object
  github_com_portainer_portainer-ee_api_http_handler_edgestacks.updateStatusPayload:
    properties:
      EndpointID:
        type: integer
      Error:
        type: string
      RollbackTo:
        description: RollbackTo specifies the stack file version to rollback to (only
          support to rollback to the last version currently)
        type: integer
      Status:
        $ref: '#/definitions/portainer.EdgeStackStatusType'
      Time:
        type: integer
      Version:
        type: integer
    type: object
  github_com_portainer_portainer-ee_api_http_handler_kubernetes.describeResourceResponse:
    properties:
      describe:
        type: string
    type: object
  github_com_portainer_portainer-ee_api_http_handler_kubernetes.namespacesToggleSystemPayload:
    properties:
      System:
        description: Toggle the system state of this namespace to true or false
        example: true
        type: boolean
    type: object
  github_com_portainer_portainer-ee_api_http_handler_system.nodesCountResponse:
    properties:
      nodes:
        type: integer
    type: object
  github_com_portainer_portainer-ee_api_http_handler_system.status:
    properties:
      InstanceID:
        description: Server Instance ID
        example: 299ab403-70a8-4c05-92f7-bf7a994d50df
        type: string
      Version:
        description: Portainer API version
        example: 2.0.0
        type: string
    type: object
  github_com_portainer_portainer-ee_api_http_handler_system.systemInfoResponse:
    properties:
      agents:
        type: integer
      edgeAgents:
        type: integer
      edgeDevices:
        type: integer
      platform:
        $ref: '#/definitions/platform.ContainerPlatform'
    type: object
  github_com_portainer_portainer-ee_api_http_handler_system.versionResponse:
    properties:
      Build:
        $ref: '#/definitions/build.BuildInfo'
      DatabaseVersion:
        type: string
      Dependencies:
        $ref: '#/definitions/build.DependenciesInfo'
      LatestVersion:
        description: The latest version available
        example: 2.0.0
        type: string
      Runtime:
        $ref: '#/definitions/build.RuntimeInfo'
      ServerEdition:
        example: CE/EE
        type: string
      ServerVersion:
        type: string
      UpdateAvailable:
        description: Whether portainer has an update available
        example: false
        type: boolean
      VersionSupport:
        example: STS/LTS
        type: string
    type: object
  github_com_portainer_portainer_pkg_libhelm_release.Hook:
    properties:
      delete_policies:
        description: DeletePolicies are the policies that indicate when to delete
          the hook
        items:
          type: string
        type: array
      events:
        description: Events are the events that this hook fires on.
        items:
          type: string
        type: array
      kind:
        description: Kind is the Kubernetes kind.
        type: string
      last_run:
        allOf:
        - $ref: '#/definitions/github_com_portainer_portainer_pkg_libhelm_release.HookExecution'
        description: LastRun indicates the date/time this was last run.
      manifest:
        description: Manifest is the manifest contents.
        type: string
      name:
        type: string
      path:
        description: Path is the chart-relative path to the template.
        type: string
      weight:
        description: Weight indicates the sort order for execution among similar Hook
          type
        type: integer
    type: object
  github_com_portainer_portainer_pkg_libhelm_release.HookExecution:
    properties:
      completed_at:
        description: CompletedAt indicates the date/time this hook was completed.
        type: string
      phase:
        description: Phase indicates whether the hook completed successfully
        type: string
      started_at:
        description: StartedAt indicates the date/time this hook was started
        type: string
    type: object
  github_com_portainer_portainer_pkg_libhelm_release.Info:
    properties:
      deleted:
        description: Deleted tracks when this object was deleted.
        type: string
      description:
        description: Description is human-friendly "log entry" about this release.
        type: string
      first_deployed:
        description: FirstDeployed is when the release was first deployed.
        type: string
      last_deployed:
        description: LastDeployed is when the release was last deployed.
        type: string
      notes:
        description: Contains the rendered templates/NOTES.txt if available
        type: string
      resources:
        description: Resources is the list of resources that are part of the release
        items:
          $ref: '#/definitions/unstructured.Unstructured'
        type: array
      status:
        description: Status is the current state of the release
        type: string
    type: object
  github_com_portainer_portainer_pkg_libhelm_release.Release:
    properties:
      appVersion:
        description: AppVersion is the app version of the release.
        type: string
      chart:
        allOf:
        - $ref: '#/definitions/release.Chart'
        description: Chart is the chart that was released.
      chartReference:
        allOf:
        - $ref: '#/definitions/release.ChartReference'
        description: ChartReference are the labels that are used to identify the chart
          source.
      config:
        additionalProperties: {}
        description: |-
          Config is the set of extra Values added to the chart.
          These values override the default values inside of the chart.
        type: object
      hooks:
        description: Hooks are all of the hooks declared for this release.
        items:
          $ref: '#/definitions/github_com_portainer_portainer_pkg_libhelm_release.Hook'
        type: array
      info:
        allOf:
        - $ref: '#/definitions/github_com_portainer_portainer_pkg_libhelm_release.Info'
        description: Info provides information about a release
      manifest:
        description: Manifest is the string representation of the rendered template.
        type: string
      name:
        description: Name is the name of the release
        type: string
      namespace:
        description: Namespace is the kubernetes namespace of the release.
        type: string
      stackID:
        description: StackID is the ID of the Portainer stack associated with this
          release (if using GitOps)
        type: integer
      values:
        allOf:
        - $ref: '#/definitions/release.Values'
        description: Values are the values used to deploy the chart.
      version:
        description: Version is an int which represents the revision of the release.
        type: integer
    type: object
  gitops.fileResponse:
    properties:
      FileContent:
        type: string
    type: object
  gitops.helmValuesPreviewPayload:
    properties:
      authorizationType:
        allOf:
        - $ref: '#/definitions/gittypes.GitCredentialAuthType'
        example: 0
      gitCredentialID:
        example: 0
        type: integer
      password:
        example: myGitPassword
        type: string
      reference:
        example: refs/heads/main
        type: string
      repository:
        example: https://github.com/example/charts
        type: string
      tlsSkipVerify:
        example: false
        type: boolean
      username:
        example: myGitUsername
        type: string
      valuesFiles:
        description: ValuesFiles is an array of paths to Helm values files (matches
