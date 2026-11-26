      Service:
        type: string
      Username:
        type: string
    type: object
  portaineree.LDAPServerType:
    enum:
    - 0
    - 1
    - 2
    type: integer
    x-enum-varnames:
    - LDAPServerCustom
    - LDAPServerOpenLDAP
    - LDAPServerAD
  portaineree.LDAPSettings:
    properties:
      AdminAutoPopulate:
        description: Whether auto admin population is switched on or not
        example: true
        type: boolean
      AdminGroupSearchSettings:
        items:
          $ref: '#/definitions/portainer.LDAPGroupSearchSettings'
        type: array
      AdminGroups:
        description: Saved admin group list, the user will be populated as an admin
          role if any user group matches the record in the list
        example:
        - '[''manager'''
        - '''operator'']'
        items:
          type: string
        type: array
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
      Kerberos:
        allOf:
        - $ref: '#/definitions/portaineree.LDAPKerberosSettings'
        description: Kerberos settings
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
      ServerType:
        allOf:
        - $ref: '#/definitions/portaineree.LDAPServerType'
        example: 1
      StartTLS:
        description: Whether LDAP connection should use StartTLS
        example: true
        type: boolean
      TLSConfig:
        $ref: '#/definitions/portainer.TLSConfiguration'
      URL:
        description: Deprecated
        type: string
      URLs:
        description: URLs or IP addresses of the LDAP server
        items:
          type: string
        type: array
    type: object
  portaineree.MTLSSettings:
    properties:
      CaCertFile:
        description: CaCertFile is the path to the mTLS CA certificate file
        type: string
      CertFile:
        description: CertFile is the path to the mTLS certificate file
        type: string
      KeyFile:
        description: KeyFile is the path to the mTLS key file
        type: string
      UseSeparateCert:
        type: boolean
    type: object
  portaineree.MTLSStatus:
    properties:
      enabled:
        type: boolean
      ok:
        type: boolean
    type: object
  portaineree.MicroK8sAddon:
    properties:
      arguments:
        type: string
      name:
        type: string
      repository:
        type: string
    type: object
  portaineree.OAuthClaimMappings:
    properties:
      ClaimValRegex:
        type: string
      Team:
        type: integer
    type: object
  portaineree.OAuthSettings:
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
      HideInternalAuth:
        type: boolean
      KubeSecretKey:
        items:
          type: integer
        type: array
      LogoutURI:
        type: string
      MicrosoftTenantID:
        type: string
      OAuthAutoCreateUsers:
        type: boolean
      OAuthAutoMapTeamMemberships:
        type: boolean
      RedirectURI:
        type: string
      ResourceURI:
        type: string
      SSO:
        type: boolean
      Scopes:
        type: string
      TeamMemberships:
        $ref: '#/definitions/portaineree.TeamMemberships'
      UserIdentifier:
        type: string
    type: object
  portaineree.PolicyStatus:
    properties:
      LastAttemptTime:
        description: Unix timestamp
        type: integer
      Message:
        type: string
      Status:
        $ref: '#/definitions/portaineree.PolicyStatusType'
    type: object
  portaineree.PolicyStatusType:
    enum:
    - applied
    - failed
    - in_progress
    - warning
    - not_supported
    type: string
    x-enum-varnames:
    - PolicyStatusTypeApplied
    - PolicyStatusTypeFailed
    - PolicyStatusTypeInProgress
    - PolicyStatusTypeWarning
    - PolicyStatusTypeNotSupported
  portaineree.Registry:
    properties:
      AccessToken:
        description: Stores temporary access token
        type: string
      AccessTokenExpiry:
        type: integer
      Authentication:
        description: Is authentication against this registry enabled
        example: true
        type: boolean
      AuthorizedTeams:
        description: Deprecated in DBVersion == 18
        items:
          type: integer
        type: array
      AuthorizedUsers:
        description: Deprecated in DBVersion == 18
        items:
          type: integer
        type: array
      BaseURL:
        description: Base URL, introduced for ProGet registry
        example: registry.mydomain.tld:2375
        type: string
      Ecr:
        $ref: '#/definitions/portainer.EcrData'
      Github:
        allOf:
        - $ref: '#/definitions/portaineree.GithubRegistryData'
        description: |-
          TODO: remove this in 2.34.0 https://linear.app/portainer/issue/R8S-399/
          this data is migrated in migrateGithubRegistry_2_32_0
      Gitlab:
        $ref: '#/definitions/portainer.GitlabRegistryData'
      Id:
        description: Registry Identifier
        example: 1
        type: integer
      ManagementConfiguration:
        $ref: '#/definitions/portainer.RegistryManagementConfiguration'
      Name:
        description: Registry Name
        example: my-registry
        type: string
      Password:
        description: Password or SecretAccessKey used to authenticate against this
          registry
        example: registry_password
        type: string
      Quay:
        $ref: '#/definitions/portainer.QuayRegistryData'
      RegistryAccesses:
        $ref: '#/definitions/portainer.RegistryAccesses'
      TeamAccessPolicies:
        allOf:
        - $ref: '#/definitions/portainer.TeamAccessPolicies'
        description: Deprecated in DBVersion == 31
      Type:
        allOf:
        - $ref: '#/definitions/portainer.RegistryType'
        description: Registry Type (1 - Quay, 2 - Azure, 3 - Custom, 4 - Gitlab, 5
          - ProGet, 6 - DockerHub, 7 - ECR)
        enum:
        - 1
        - 2
        - 3
        - 4
        - 5
        - 6
        - 7
      URL:
        description: URL or IP address of the Docker registry
        example: registry.mydomain.tld:2375
        type: string
      UserAccessPolicies:
        allOf:
        - $ref: '#/definitions/portainer.UserAccessPolicies'
        description: |-
          Deprecated fields
          Deprecated in DBVersion == 31
      Username:
        description: Username or AccessKeyID used to authenticate against this registry
        example: registry user
        type: string
    type: object
  portaineree.Role:
    properties:
      Authorizations:
        allOf:
        - $ref: '#/definitions/portainer.Authorizations'
        description: Authorizations associated to a role
      Description:
        description: Role description
        example: Read-only access of all resources in an environment(endpoint)
        type: string
      Id:
        description: Role Identifier
        example: 1
        type: integer
      Name:
        description: Role name
        example: HelpDesk
        type: string
      Priority:
        type: integer
      Scope:
        additionalProperties:
          items:
            type: string
          type: array
        type: object
    required:
    - Authorizations
    - Description
    - Id
    - Name
    - Priority
    - Scope
    type: object
  portaineree.S3BackupSettings:
    properties:
      accessKeyID:
        description: AWS access key id
        type: string
      bucketName:
        description: AWS S3 bucket name
        type: string
      cronRule:
        description: Crontab rule to make periodical backups
        type: string
      password:
        description: Password to encrypt the backup with
        type: string
      region:
        description: AWS S3 region. Default to "us-east-1"
        example: us-east-1
        type: string
      s3CompatibleHost:
        description: S3 compatible host
        type: string
      secretAccessKey:
        description: AWS secret access key
        type: string
    type: object
  portaineree.SSLSettings:
    properties:
      caCertPath:
        type: string
      certPath:
        type: string
      httpEnabled:
        type: boolean
      keyPath:
        type: string
      selfSigned:
        type: boolean
    type: object
  portaineree.Settings:
    properties:
      AdditionalFunctionality:
        allOf:
        - $ref: '#/definitions/portaineree.AdditionalFunctionality'
        description: Additional Functionality
      AgentSecret:
        description: Container environment parameter AGENT_SECRET
        type: string
      AllowBindMountsForRegularUsers:
        type: boolean
      AllowContainerCapabilitiesForRegularUsers:
        type: boolean
      AllowDeviceMappingForRegularUsers:
        type: boolean
      AllowHostNamespaceForRegularUsers:
        type: boolean
      AllowPrivilegedModeForRegularUsers:
        type: boolean
      AllowStackManagementForRegularUsers:
        type: boolean
      AllowVolumeBrowserForRegularUsers:
        type: boolean
      AuthenticationMethod:
        allOf:
        - $ref: '#/definitions/portainer.AuthenticationMethod'
        description: 'Active authentication method for the Portainer instance. Valid
          values are: 1 for internal, 2 for LDAP, or 3 for oauth'
        example: 1
      AutoPatchSettings:
        $ref: '#/definitions/portaineree.AutoPatchSettings'
      BlackListedLabels:
        description: A list of label name & value that will be used to hide containers
          when querying containers
        items:
          $ref: '#/definitions/portainer.Pair'
        type: array
      CloudApiKeys:
        allOf:
        - $ref: '#/definitions/portaineree.CloudApiKeys'
        description: CloudAPIKeys
      CustomLoginBanner:
        description: The content in plaintext used to display in the login page. Will
          hide when value is empty string
        type: string
      DefaultRegistry:
        description: The default builtin registry now is anonymous docker hub registry
        properties:
          Hide:
            example: false
            type: boolean
        type: object
      DisableKubeRolesSync:
        description: DisableKubeRolesSync will disable the sync of kube roles for
          all built-in roles
        example: false
        type: boolean
      DisableKubeShell:
        description: DisableKubeShell will disable the kube shell feature for non-admin
          users
        example: false
        type: boolean
      DisableKubeconfigDownload:
        description: DisableKubeconfigDownload will disable the download of kubeconfig
          files for non-admin users
        example: false
        type: boolean
      DisplayDonationHeader:
        description: Deprecated fields
        type: boolean
      DisplayExternalContributors:
        type: boolean
      Edge:
        $ref: '#/definitions/portaineree.Edge'
      EdgeAgentCheckinInterval:
        description: The default check in interval for edge agent (in seconds)
        example: 5
        type: integer
      EdgePortainerUrl:
        description: EdgePortainerURL is the URL that is exposed to edge agents
        type: string
      EnableEdgeComputeFeatures:
        description: Whether edge compute features are enabled
        type: boolean
      EnableHostManagementFeatures:
        description: Deprecated fields v26
        type: boolean
      EnforceEdgeID:
        description: EnforceEdgeID makes Portainer store the Edge ID instead of accepting
          anyone
        example: false
        type: boolean
      ExperimentalFeatures:
        allOf:
        - $ref: '#/definitions/portaineree.ExperimentalFeatures'
        description: Experimental features
      FeatureFlagSettings:
        additionalProperties:
          type: boolean
        type: object
      GlobalDeploymentOptions:
        allOf:
        - $ref: '#/definitions/portaineree.GlobalDeploymentOptions'
        description: Deployment options for encouraging git ops workflows
      HelmRepositoryURL:
        description: Helm repository URL, defaults to "https://charts.bitnami.com/bitnami"
        example: https://charts.bitnami.com/bitnami
        type: string
      InternalAuthSettings:
        $ref: '#/definitions/portainer.InternalAuthSettings'
      IsDockerDesktopExtension:
        type: boolean
      KubeconfigExpiry:
        description: The expiry of a Kubeconfig
        example: 24h
        type: string
      KubectlShellImage:
        description: KubectlImage, defaults to portainer/kubectl-shell
        example: portainer/kubectl-shell
        type: string
      LDAPSettings:
        $ref: '#/definitions/portaineree.LDAPSettings'
      LogoURL:
        description: URL to a logo that will be displayed on the login page as well
          as on top of the sidebar. Will use default Portainer logo when value is
          empty string
        example: https://mycompany.mydomain.tld/logo.png
        type: string
      OAuthSettings:
        $ref: '#/definitions/portaineree.OAuthSettings'
      SnapshotInterval:
        description: The interval in which environment(endpoint) snapshots are created
        example: 5m
        type: string
      TemplatesURL:
        description: URL to the templates that will be displayed in the UI when navigating
          to App Templates
        example: https://raw.githubusercontent.com/portainer/templates/master/templates.json
        type: string
      TrustOnFirstConnect:
        description: TrustOnFirstConnect makes Portainer accepting edge agent connection
          by default
        example: false
        type: boolean
      UserSessionTimeout:
        description: The duration of a user session
        example: 5m
        type: string
      openAMTConfiguration:
        $ref: '#/definitions/portainer.OpenAMTConfiguration'
    type: object
  portaineree.Stack:
    properties:
      AdditionalFiles:
        description: Only applies when deploying stack with multiple files
        items:
          type: string
        type: array
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
        description: The date in unix time when stack was created
        example: 1587399600
        type: integer
      EndpointId:
        description: Environment(Endpoint) identifier. Reference the environment(endpoint)
          that will be used for deployment
        example: 1
        type: integer
      EntryPoint:
        description: Path to the Stack file
        example: docker-compose.yml
        type: string
      Env:
        description: A list of environment(endpoint) variables used during stack deployment
        items:
          $ref: '#/definitions/portainer.Pair'
        type: array
      FilesystemPath:
        description: Network(Swarm) or local(Standalone) filesystem path
        example: /tmp
        type: string
      FromAppTemplate:
        description: Whether the stack is from a app template
        example: false
        type: boolean
      GitConfig:
        allOf:
        - $ref: '#/definitions/gittypes.RepoConfig'
        description: The git config of this stack
      HelmChartPath:
        description: Path to a Helm chart folder for Helm git deployments
        example: charts/my-app
        type: string
      HelmValuesFiles:
        description: Array of paths to Helm values YAML files for Helm git deployments
        example:
        - '[''values/prod.yaml'''
        - ' ''values/secrets.yaml'']'
        items:
          type: string
        type: array
      Id:
        description: Stack Identifier
        example: 1
        type: integer
      IsDetachedFromGit:
        description: Whether the stack is detached from git
        example: false
        type: boolean
      Name:
        description: Stack name
        example: myStack
        type: string
      Namespace:
        description: Kubernetes namespace if stack is a kube application
        example: default
        type: string
      Option:
        allOf:
        - $ref: '#/definitions/portainer.StackOption'
        description: The stack deployment option
      PreviousDeploymentInfo:
        allOf:
        - $ref: '#/definitions/portainer.StackDeploymentInfo'
        description: The previous deployment info of the stack
      ProjectPath:
        description: Path on disk to the repository hosting the Stack file
        example: /data/compose/myStack_jpofkc0i9uo9wtx1zesuk649w
        type: string
      Registries:
        description: List of Registries to use for this stack
        items:
          type: integer
        type: array
      ResourceControl:
        $ref: '#/definitions/portainer.ResourceControl'
      StackFileVersion:
        description: StackFileVersion indicates the stack file version, such as yaml,
          hcl, and manifest
        example: 1
        type: integer
      Status:
        allOf:
        - $ref: '#/definitions/portainer.StackStatus'
        description: Stack status (1 - active, 2 - inactive)
        example: 1
      SupportRelativePath:
        description: If stack support relative path volume
        example: false
        type: boolean
      SwarmId:
        description: Cluster identifier of the Swarm cluster where the stack is deployed
        example: jpofkc0i9uo9wtx1zesuk649w
        type: string
      Type:
        allOf:
        - $ref: '#/definitions/portainer.StackType'
        description: Stack type. 1 for a Swarm stack, 2 for a Compose stack
        example: 2
      UpdateDate:
        description: The date in unix time when stack was last updated
        example: 1587399600
        type: integer
      UpdatedBy:
        description: The username which last updated this stack
        example: bob
        type: string
      Webhook:
        description: A UUID to identify a webhook. The stack will be force updated
          and pull the latest image when the webhook was invoked.
        example: c11fdf23-183e-428a-9bb6-16db01032174
        type: string
    type: object
  portaineree.TeamMemberships:
    properties:
      AdminAutoPopulate:
        type: boolean
      AdminGroupClaimsRegexList:
        items:
          type: string
        type: array
      OAuthClaimMappings:
        items:
          $ref: '#/definitions/portaineree.OAuthClaimMappings'
        type: array
      OAuthClaimName:
        type: string
    type: object
  portaineree.User:
    properties:
      EndpointAuthorizations:
        allOf:
        - $ref: '#/definitions/portainer.EndpointAuthorizations'
        description: 'Deprecated: in 2.32, no longer populated - see separate dataservice
          for UserEndpointAuthorizations'
      Id:
        description: User Identifier
        example: 1
        type: integer
      PortainerAuthorizations:
        $ref: '#/definitions/portainer.Authorizations'
      Role:
        allOf:
        - $ref: '#/definitions/portainer.UserRole'
        description: User role (1 for administrator account and 2 for regular account)
        example: 1
      ThemeSettings:
        $ref: '#/definitions/portaineree.UserThemeSettings'
      TokenIssueAt:
        example: 1639408208
        type: integer
      UseCache:
        example: true
        type: boolean
      UserTheme:
        description: 'Deprecated: xxxx'
        example: dark
        type: string
      Username:
        example: bob
        type: string
    type: object
  portaineree.UserActivityLog:
    properties:
      action:
        type: string
      context:
        type: string
      id:
        type: integer
      payload:
        items:
          type: integer
        type: array
      timestamp:
        type: integer
      username:
        type: string
    type: object
  portaineree.UserThemeSettings:
    properties:
      color:
        description: Color represents the color theme of the UI
        enum:
        - dark
        - light
        - highcontrast
        - auto
        example: dark
        type: string
      subtleUpgradeButton:
        description: SubtleUpgradeButton indicates if the upgrade banner should be
          displayed in a subtle way
        type: boolean
    type: object
  providers.AmazonProvisionPayload:
    properties:
      AmiType:
        example: BOTTLEROCKET_x86_64
        type: string
      CredentialID:
        example: 1
        type: integer
      InstanceType:
        example: m5.large
        type: string
      KubernetesVersion:
        example: "1.23"
        type: string
      Name:
        example: myDevCluster
        type: string
      NetworkID:
        example: 8465fb26-632e-4fa3-bb9b-21c449629026
        type: string
      NodeCount:
        example: 3
        type: integer
      NodeSize:
        example: g3.small
        type: string
      NodeVolumeSize:
        example: 20
        type: integer
      Region:
        example: NYC1
        type: string
      meta:
        $ref: '#/definitions/types.EnvironmentMetadata'
    required:
    - AmiType
    - CredentialID
    - InstanceType
    - KubernetesVersion
    - Name
    - NodeCount
    - NodeSize
    - Region
    type: object
  providers.AzureProvisionPayload:
    properties:
      CredentialID:
        example: 1
        type: integer
      KubernetesVersion:
        example: "1.23"
        type: string
      Name:
        example: myDevCluster
        type: string
      NetworkID:
        example: 8465fb26-632e-4fa3-bb9b-21c449629026
        type: string
      NodeCount:
        example: 3
        type: integer
      NodeSize:
        example: g3.small
        type: string
      Region:
        example: NYC1
        type: string
      availabilityZones:
        items:
          type: string
        type: array
      dnsPrefix:
        type: string
      meta:
        $ref: '#/definitions/types.EnvironmentMetadata'
      poolName:
        type: string
      resourceGroup:
        description: Azure specific fields
        type: string
      resourceGroupName:
        type: string
      tier:
        type: string
    required:
    - CredentialID
    - KubernetesVersion
    - Name
    - NodeCount
    - NodeSize
    - Region
    type: object
  providers.DefaultProvisionPayload:
    properties:
      CredentialID:
        example: 1
        type: integer
      KubernetesVersion:
        example: "1.23"
        type: string
      Name:
        example: myDevCluster
        type: string
      NetworkID:
        example: 8465fb26-632e-4fa3-bb9b-21c449629026
        type: string
      NodeCount:
        example: 3
        type: integer
      NodeSize:
        example: g3.small
        type: string
      Region:
        example: NYC1
        type: string
      meta:
        $ref: '#/definitions/types.EnvironmentMetadata'
    required:
    - CredentialID
    - KubernetesVersion
    - Name
    - NodeCount
    - NodeSize
    - Region
    type: object
  providers.GKEProvisionPayload:
    properties:
      CPU:
        example: 2
        type: integer
      CredentialID:
        example: 1
        type: integer
      HDD:
        example: 100
        type: integer
      KubernetesVersion:
        example: "1.23"
        type: string
      Name:
        example: myDevCluster
        type: string
      NetworkID:
        example: 8465fb26-632e-4fa3-bb9b-21c449629026
        type: string
      NodeCount:
        example: 3
        type: integer
      NodeSize:
        example: g3.small
        type: string
      RAM:
        example: 4
        type: number
      Region:
        example: NYC1
        type: string
      meta:
        $ref: '#/definitions/types.EnvironmentMetadata'
    required:
    - CredentialID
    - KubernetesVersion
    - Name
    - NodeCount
    - NodeSize
    - Region
    type: object
  providers.Microk8sTestSSHPayload:
    properties:
      credentialID:
        example: 1
        type: integer
      nodeIPs:
        items:
          type: string
        type: array
    required:
    - credentialID
    - nodeIPs
    type: object
  providers.Microk8sUpdateAddonsPayload:
    properties:
      addons:
        items:
          $ref: '#/definitions/portaineree.MicroK8sAddon'
        type: array
    type: object
  registries.deleteTagsPayload:
    properties:
      Tags:
