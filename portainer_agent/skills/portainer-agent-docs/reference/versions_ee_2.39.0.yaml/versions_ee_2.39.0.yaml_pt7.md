  portainer.MembershipRole:
    enum:
    - 0
    - 1
    - 2
    type: integer
    x-enum-varnames:
    - _
    - TeamLeader
    - TeamMember
  portainer.OAuthSettings:
    properties:
      AccessTokenURI:
        type: string
      AuthStyle:
        $ref: '#/definitions/oauth2.AuthStyle'
      AuthorizationURI:
        type: string
      ClientID:
        type: string
      ClientSecret:
        type: string
      DefaultTeamID:
        type: integer
      KubeSecretKey:
        items:
          type: integer
        type: array
      LogoutURI:
        type: string
      OAuthAutoCreateUsers:
        type: boolean
      RedirectURI:
        type: string
      ResourceURI:
        type: string
      SSO:
        type: boolean
      Scopes:
        type: string
      UserIdentifier:
        type: string
    type: object
  portainer.OpenAMTConfiguration:
    properties:
      certFileContent:
        type: string
      certFileName:
        type: string
      certFilePassword:
        type: string
      domainName:
        type: string
      enabled:
        type: boolean
      mpsPassword:
        type: string
      mpsServer:
        type: string
      mpsToken:
        description: retrieved from API
        type: string
      mpsUser:
        type: string
    type: object
  portainer.OpenAMTDeviceEnabledFeatures:
    properties:
      IDER:
        type: boolean
      KVM:
        type: boolean
      SOL:
        type: boolean
      redirection:
        type: boolean
      userConsent:
        type: string
    type: object
  portainer.Pair:
    properties:
      name:
        example: name
        type: string
      value:
        example: value
        type: string
    type: object
  portainer.PerDevConfigsFilterType:
    enum:
    - file
    - dir
    type: string
    x-enum-varnames:
    - PerDevConfigsTypeFile
    - PerDevConfigsTypeDir
  portainer.PerformanceMetrics:
    properties:
      CPUUsage:
        type: number
      MemoryUsage:
        type: number
      NetworkUsage:
        type: number
    type: object
  portainer.PolicyChartBundle:
    properties:
      ChartName:
        type: string
      EncodedTgz:
        type: string
      EncodedValues:
        type: string
      Fingerprint:
        type: string
      Namespace:
        type: string
      PreInstallAdoptions:
        items:
          $ref: '#/definitions/portainer.ResourceAdoption'
        type: array
      PreInstallDeletions:
        items:
          $ref: '#/definitions/portainer.ResourceDeletion'
        type: array
      PreReleaseManifest:
        type: string
    type: object
  portainer.PolicyChartSummary:
    properties:
      ChartName:
        type: string
      Fingerprint:
        type: string
    type: object
  portainer.QuayRegistryData:
    properties:
      OrganisationName:
        type: string
      UseOrganisation:
        type: boolean
    type: object
  portainer.RegistryAccessPolicies:
    properties:
      Namespaces:
        description: Kubernetes specific fields (with kubernetes, namespaces have
          access to a registry, if users/teams have access to the same namespace,
          they have access to the registry)
        items:
          type: string
        type: array
      TeamAccessPolicies:
        $ref: '#/definitions/portainer.TeamAccessPolicies'
      UserAccessPolicies:
        allOf:
        - $ref: '#/definitions/portainer.UserAccessPolicies'
        description: Docker specific fields (with docker, users/teams have access
          to a registry)
    type: object
  portainer.RegistryAccesses:
    additionalProperties:
      $ref: '#/definitions/portainer.RegistryAccessPolicies'
    type: object
  portainer.RegistryManagementConfiguration:
    properties:
      AccessToken:
        type: string
      AccessTokenExpiry:
        type: integer
      Authentication:
        type: boolean
      Ecr:
        $ref: '#/definitions/portainer.EcrData'
      Password:
        type: string
      TLSConfig:
        $ref: '#/definitions/portainer.TLSConfiguration'
      Type:
        $ref: '#/definitions/portainer.RegistryType'
      Username:
        type: string
    type: object
  portainer.RegistryType:
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
    type: integer
    x-enum-varnames:
    - _
    - QuayRegistry
    - AzureRegistry
    - CustomRegistry
    - GitlabRegistry
    - ProGetRegistry
    - DockerHubRegistry
    - EcrRegistry
    - GithubRegistry
  portainer.ResourceAccessLevel:
    enum:
    - 0
    - 1
    type: integer
    x-enum-varnames:
    - _
    - ReadWriteAccessLevel
  portainer.ResourceAdoption:
    properties:
      apiVersion:
        example: v1
        type: string
      kind:
        example: Secret
        type: string
      name:
        example: registry-1
        type: string
      namespace:
        example: default
        type: string
    type: object
  portainer.ResourceControl:
    properties:
      AccessLevel:
        $ref: '#/definitions/portainer.ResourceAccessLevel'
      AdministratorsOnly:
        description: Permit access to resource only to admins
        example: true
        type: boolean
      Id:
        description: ResourceControl Identifier
        example: 1
        type: integer
      OwnerId:
        description: |-
          Deprecated fields
          Deprecated in DBVersion == 2
        type: integer
      Public:
        description: Permit access to the associated resource to any user
        example: true
        type: boolean
      ResourceId:
        description: |-
          Docker resource identifier on which access control will be applied.\
          In the case of a resource control applied to a stack, use the stack name as identifier
        example: 617c5f22bb9b023d6daab7cba43a57576f83492867bc767d1c59416b065e5f08
        type: string
      SubResourceIds:
        description: List of Docker resources that will inherit this access control
        example:
        - 617c5f22bb9b023d6daab7cba43a57576f83492867bc767d1c59416b065e5f08
        items:
          type: string
        type: array
      System:
        type: boolean
      TeamAccesses:
        items:
          $ref: '#/definitions/portainer.TeamResourceAccess'
        type: array
      Type:
        allOf:
        - $ref: '#/definitions/portainer.ResourceControlType'
        description: |-
          Type of Docker resource. Valid values are: 1- container, 2 -service
          3 - volume, 4 - secret, 5 - stack, 6 - config or 7 - custom template
        example: 1
      UserAccesses:
        items:
          $ref: '#/definitions/portainer.UserResourceAccess'
        type: array
    type: object
  portainer.ResourceControlType:
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
    type: integer
    x-enum-varnames:
    - _
    - ContainerResourceControl
    - ServiceResourceControl
    - VolumeResourceControl
    - NetworkResourceControl
    - SecretResourceControl
    - StackResourceControl
    - ConfigResourceControl
    - CustomTemplateResourceControl
    - ContainerGroupResourceControl
  portainer.ResourceDeletion:
    properties:
      apiVersion:
        example: v1
        type: string
      kind:
        example: Secret
        type: string
      name:
        example: registry-1
        type: string
      namespace:
        example: default
        type: string
    type: object
  portainer.RestoreSettings:
    properties:
      manifest:
        description: Base64-encoded Kubernetes YAML manifest
        type: string
    type: object
  portainer.RestoreSettingsBundle:
    additionalProperties:
      $ref: '#/definitions/portainer.RestoreSettings'
    type: object
  portainer.StackDeploymentInfo:
    properties:
      ConfigHash:
        description: ConfigHash is the commit hash of the git repository used for
          deploying the stack
        type: string
      FileVersion:
        description: FileVersion is the version of the stack file, used to detect
          changes
        type: integer
      Version:
        description: Version is the version of the stack and also is the deployed
          version in edge agent
        type: integer
    type: object
  portainer.StackOption:
    properties:
      HelmAtomic:
        description: Enable atomic rollback on failure (Helm --atomic flag for Kubernetes
          Helm stacks)
        example: false
        type: boolean
      Prune:
        description: Prune services that are no longer referenced
        example: false
        type: boolean
    type: object
  portainer.StackStatus:
    enum:
    - 0
    - 1
    - 2
    type: integer
    x-enum-varnames:
    - _
    - StackStatusActive
    - StackStatusInactive
  portainer.StackType:
    enum:
    - 0
    - 1
    - 2
    - 3
    type: integer
    x-enum-varnames:
    - _
    - DockerSwarmStack
    - DockerComposeStack
    - KubernetesStack
  portainer.TLSConfiguration:
    properties:
      TLS:
        description: Use TLS
        example: true
        type: boolean
      TLSCACert:
        description: Path to the TLS CA certificate file
        example: /data/tls/ca.pem
        type: string
      TLSCert:
        description: Path to the TLS client certificate file
        example: /data/tls/cert.pem
        type: string
      TLSKey:
        description: Path to the TLS client key file
        example: /data/tls/key.pem
        type: string
      TLSSkipVerify:
        description: Skip the verification of the server TLS certificate
        example: false
        type: boolean
    type: object
  portainer.Tag:
    properties:
      EndpointGroups:
        additionalProperties:
          type: boolean
        description: A set of environment(endpoint) group ids that have this tag
        type: object
      Endpoints:
        additionalProperties:
          type: boolean
        description: A set of environment(endpoint) ids that have this tag
        type: object
      ID:
        description: Tag identifier
        example: 1
        type: integer
      Name:
        description: Tag name
        example: org/acme
        type: string
    type: object
  portainer.Team:
    properties:
      Id:
        description: Team Identifier
        example: 1
        type: integer
      Name:
        description: Team name
        example: developers
        type: string
    type: object
  portainer.TeamAccessPolicies:
    additionalProperties:
      $ref: '#/definitions/portainer.AccessPolicy'
    type: object
  portainer.TeamMembership:
    properties:
      Id:
        description: Membership Identifier
        example: 1
        type: integer
      Role:
        allOf:
        - $ref: '#/definitions/portainer.MembershipRole'
        description: Team role (1 for team leader and 2 for team member)
        example: 1
      TeamID:
        description: Team identifier
        example: 1
        type: integer
      UserID:
        description: User identifier
        example: 1
        type: integer
    type: object
  portainer.TeamResourceAccess:
    properties:
      AccessLevel:
        $ref: '#/definitions/portainer.ResourceAccessLevel'
      TeamId:
        type: integer
    type: object
  portainer.Template:
    properties:
      administrator_only:
        description: Whether the template should be available to administrators only
        example: true
        type: boolean
      categories:
        description: A list of categories associated to the template
        example:
        - database
        items:
          type: string
        type: array
      command:
        description: The command that will be executed in a container template
        example: ls -lah
        type: string
      description:
        description: Description of the template
        example: High performance web server
        type: string
      env:
        description: A list of environment(endpoint) variables used during the template
          deployment
        items:
          $ref: '#/definitions/portainer.TemplateEnv'
        type: array
      hostname:
        description: Container hostname
        example: mycontainer
        type: string
      id:
        description: |-
          Mandatory container/stack fields
          Template Identifier
        example: 1
        type: integer
      image:
        description: |-
          Mandatory container fields
          Image associated to a container template. Mandatory for a container template
        example: nginx:latest
        type: string
      interactive:
        description: |-
          Whether the container should be started in
          interactive mode (-i -t equivalent on the CLI)
        example: true
        type: boolean
      labels:
        description: Container labels
        items:
          $ref: '#/definitions/portainer.Pair'
        type: array
      logo:
        description: URL of the template's logo
        example: https://portainer.io/img/logo.svg
        type: string
      name:
        description: |-
          Optional stack/container fields
          Default name for the stack/container to be used on deployment
        example: mystackname
        type: string
      network:
        description: Name of a network that will be used on container deployment if
          it exists inside the environment(endpoint)
        example: mynet
        type: string
      note:
        description: A note that will be displayed in the UI. Supports HTML content
        example: This is my <b>custom</b> template
        type: string
      platform:
        description: |-
          Platform associated to the template.
          Valid values are: 'linux', 'windows' or leave empty for multi-platform
        example: linux
        type: string
      ports:
        description: A list of ports exposed by the container
        example:
        - 8080:80/tcp
        items:
          type: string
        type: array
      privileged:
        description: Whether the container should be started in privileged mode
        example: true
        type: boolean
      registry:
        description: |-
          Optional container fields
          The URL of a registry associated to the image for a container template
        example: quay.io
        type: string
      repository:
        allOf:
        - $ref: '#/definitions/portainer.TemplateRepository'
        description: Mandatory stack fields
      restart_policy:
        description: Container restart policy
        example: on-failure
        type: string
      stackFile:
        description: |-
          Mandatory Edge stack fields
          Stack file used for this template
        type: string
      title:
        description: Title of the template
        example: Nginx
        type: string
      type:
        allOf:
        - $ref: '#/definitions/portainer.TemplateType'
        description: 'Template type. Valid values are: 1 (container), 2 (Swarm stack),
          3 (Compose stack), 4 (Compose edge stack)'
        example: 1
      volumes:
        description: A list of volumes used during the container template deployment
        items:
          $ref: '#/definitions/portainer.TemplateVolume'
        type: array
    type: object
  portainer.TemplateEnv:
    properties:
      default:
        description: Default value that will be set for the variable
        example: default_value
        type: string
      description:
        description: Content of the tooltip that will be generated in the UI
        example: MySQL root account password
        type: string
      label:
        description: Text for the label that will be generated in the UI
        example: Root password
        type: string
      name:
        description: name of the environment(endpoint) variable
        example: MYSQL_ROOT_PASSWORD
        type: string
      preset:
        description: If set to true, will not generate any input for this variable
          in the UI
        example: false
        type: boolean
      select:
        description: A list of name/value that will be used to generate a dropdown
          in the UI
        items:
          $ref: '#/definitions/portainer.TemplateEnvSelect'
        type: array
    type: object
  portainer.TemplateEnvSelect:
    properties:
      default:
        description: Will set this choice as the default choice
        example: false
        type: boolean
      text:
        description: Some text that will displayed as a choice
        example: text value
        type: string
      value:
        description: A value that will be associated to the choice
        example: value
        type: string
    type: object
  portainer.TemplateRepository:
    properties:
      stackfile:
        description: Path to the stack file inside the git repository
        example: ./subfolder/docker-compose.yml
        type: string
      url:
        description: URL of a git repository used to deploy a stack template. Mandatory
          for a Swarm/Compose stack template
        example: https://github.com/portainer/portainer-compose
        type: string
    type: object
  portainer.TemplateType:
    enum:
    - 0
    - 1
    - 2
    - 3
    type: integer
    x-enum-varnames:
    - _
    - ContainerTemplate
    - SwarmStackTemplate
    - ComposeStackTemplate
  portainer.TemplateVolume:
    properties:
      bind:
        description: Path on the host
        example: /tmp
        type: string
      container:
        description: Path inside the container
        example: /data
        type: string
      readonly:
        description: Whether the volume used should be readonly
        example: true
        type: boolean
    type: object
  portainer.UserAccessPolicies:
    additionalProperties:
      $ref: '#/definitions/portainer.AccessPolicy'
    type: object
  portainer.UserResourceAccess:
    properties:
      AccessLevel:
        $ref: '#/definitions/portainer.ResourceAccessLevel'
      UserId:
        type: integer
    type: object
  portainer.UserRole:
    enum:
    - 0
    - 1
    - 2
    type: integer
    x-enum-varnames:
    - _
    - AdministratorRole
    - StandardUserRole
  portainer.Webhook:
    properties:
      EndpointId:
        type: integer
      Id:
        description: Webhook Identifier
        example: 1
        type: integer
      RegistryId:
        type: integer
      ResourceId:
        type: string
      Token:
        type: string
      Type:
        allOf:
        - $ref: '#/definitions/portainer.WebhookType'
        description: Type of webhook (1 - service)
    type: object
  portainer.WebhookType:
    enum:
    - 0
    - 1
    type: integer
    x-enum-varnames:
    - _
    - ServiceWebhook
  portaineree.AdditionalFunctionality:
    properties:
      Observability:
        type: boolean
    type: object
  portaineree.AlertingNotificationChannel:
    properties:
      config:
        additionalProperties: {}
        type: object
      enabled:
        type: boolean
      id:
        type: integer
      name:
        type: string
      type:
        enum:
        - slack
        - webhook
        - teams
        - discord
        - email
        - pagerduty
        - opsgenie
        type: string
    type: object
  portaineree.AlertingRule:
    properties:
      alertManagerID:
        type: integer
      conditionOperator:
        allOf:
        - $ref: '#/definitions/portaineree.ConditionOperator'
        enum:
        - '>'
        - <
        - =
        - '>='
        - <=
      createdAt:
        type: string
      createdBy:
        type: string
      description:
        type: string
      duration:
        type: integer
      enabled:
        type: boolean
      id:
        type: integer
      isEditable:
        type: boolean
      isInternal:
        type: boolean
      labels:
        additionalProperties:
          type: string
        type: object
      metricType:
        enum:
        - percentage
        - bytes
        - raw
        type: string
      name:
        type: string
      severity:
        enum:
        - critical
        - warning
        - info
        type: string
      summary:
        type: string
      supportedAgentVersion:
        type: string
      supportedEnvironmentTypes:
        enum:
        - docker
        - kubernetes
        - podman
        - all
        type: string
      threshold:
        type: number
      updatedAt:
        type: string
    type: object
  portaineree.AlertingSettings:
    properties:
      createdAt:
        type: string
      createdBy:
        type: string
      enabled:
        type: boolean
      id:
        type: integer
      isInternal:
        type: boolean
      name:
        type: string
      notificationChannels:
        items:
          $ref: '#/definitions/portaineree.AlertingNotificationChannel'
        type: array
      portainerURL:
        type: string
      status:
        enum:
        - disabled
        - connected
        - disconnected
        - error
        type: string
      uptime:
        type: string
      url:
        type: string
    type: object
  portaineree.AppliedPolicy:
    properties:
      policyID:
        type: integer
      policyName:
        type: string
      policyStatus:
        $ref: '#/definitions/portaineree.PolicyStatus'
    type: object
  portaineree.AuthActivityLog:
    properties:
      context:
        $ref: '#/definitions/portainer.AuthenticationMethod'
      id:
        type: integer
      origin:
        type: string
      timestamp:
        type: integer
      type:
        $ref: '#/definitions/portaineree.AuthenticationActivityType'
      username:
        type: string
    type: object
  portaineree.AuthenticationActivityType:
    enum:
    - 0
    - 1
    - 2
    - 3
    type: integer
    x-enum-varnames:
    - _
    - AuthenticationActivitySuccess
    - AuthenticationActivityFailure
    - AuthenticationActivityLogOut
  portaineree.AutoPatchSettings:
    properties:
      Enabled:
        example: false
        type: boolean
      PatchCron:
        example: 0 4 * * *
        type: string
      PortainerRepository:
        example: portainer/portainer-ee
        type: string
      RegistryID:
        example: 0
        type: integer
      UpdaterRepository:
        example: portainer/portainer-updater
        type: string
    type: object
  portaineree.AutoUpdateStatus:
    enum:
    - inProgress
    - completed
    - failed
    type: string
    x-enum-varnames:
    - AutoUpdateStatusInProgress
    - AutoUpdateStatusCompleted
    - AutoUpdateStatusFailed
  portaineree.CloudApiKeys:
    properties:
      CivoApiKey:
        example: DgJ33kwIhnHumQFyc8ihGwWJql9cC8UJDiBhN8YImKqiX
        type: string
      DigitalOceanToken:
        example: dop_v1_n9rq7dkcbg3zb3bewtk9nnvmfkyfnr94d42n28lym22vhqu23rtkllsldygqm22v
        type: string
      GKEApiKey:
        example: an entire base64ed key file
        type: string
      LinodeToken:
        example: 92gsh9r9u5helgs4eibcuvlo403vm45hrmc6mzbslotnrqmkwc1ovqgmolcyq0wc
        type: string
    type: object
  portaineree.CloudProvider:
    properties:
      AddonWithArgs:
        description: MicroK8S specific fields
        items:
          $ref: '#/definitions/portaineree.MicroK8sAddon'
        type: array
      AmiType:
        description: Amazon specific fields
        type: string
      CPU:
        type: integer
      CredentialID:
        description: CredentialID holds an ID of the credential used to create the
          cluster
        type: integer
      DNSPrefix:
        type: string
      HDD:
        type: integer
      InstanceType:
        type: string
      KubernetesVersion:
        type: string
      Name:
        type: string
      NetworkID:
        description: |-
          Pointer will hide this field for providers other than civo which do
          not use this field.
        type: string
      NodeCount:
        type: integer
      NodeIPs:
        type: string
      NodeVolumeSize:
        type: integer
      OfflineInstall:
        type: boolean
      PoolName:
        type: string
      Provider:
        type: string
      RAM:
        type: number
      Region:
        type: string
      ResourceGroup:
        description: Azure specific fields
        type: string
      Size:
        type: string
      Tier:
        type: string
      URL:
        type: string
    type: object
  portaineree.ConditionOperator:
    enum:
    - '>'
    - <
    - =
    - '>='
    - <=
    type: string
    x-enum-varnames:
    - OperatorGreaterThan
    - OperatorLessThan
    - OperatorEqual
    - OperatorGreaterThanOrEqual
    - OperatorLessThanOrEqual
  portaineree.CustomTemplate:
    properties:
      CreatedByUserId:
        description: User identifier who created this template
        example: 3
        type: integer
      Description:
        description: Description of the template
        example: High performance web server
        type: string
      EdgeSettings:
        $ref: '#/definitions/portaineree.CustomTemplateEdgeSettings'
      EdgeTemplate:
        description: EdgeTemplate indicates if this template purpose for Edge Stack
        example: false
        type: boolean
      EntryPoint:
        description: Path to the Stack file
        example: docker-compose.yml
        type: string
      GitConfig:
        $ref: '#/definitions/gittypes.RepoConfig'
      Id:
        description: CustomTemplate Identifier
        example: 1
        type: integer
      IsComposeFormat:
        description: IsComposeFormat indicates if the Kubernetes template is created
