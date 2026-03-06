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
    type: object
  sshtest.SSHTestResult:
    properties:
      address:
        type: string
      error:
        type: string
    type: object
  ssl.Certificate:
    properties:
      AuthorityKeyId:
        type: string
      CRLDistributionPoints:
        items:
          type: string
        type: array
      ExtendedKeyUsages:
        items:
          type: string
        type: array
      IsCertificateAuthority:
        type: boolean
      Issuer:
        $ref: '#/definitions/ssl.Name'
      IssuingCertificateURLs:
        items:
          type: string
        type: array
      KeyUsages:
        items:
          type: string
        type: array
      OCSPServers:
        items:
          type: string
        type: array
      Policies:
        items:
          type: string
        type: array
      PublicKey:
        $ref: '#/definitions/ssl.PublicKey'
      SHA256Fingerprint:
        type: string
      SerialNumber:
        type: string
      SignatureAlgorithm:
        type: string
      Subject:
        $ref: '#/definitions/ssl.Name'
      SubjectAltDNSNames:
        items:
          type: string
        type: array
      SubjectAltEmailAddresses:
        items:
          type: string
        type: array
      SubjectAltIpAddresses:
        items:
          type: string
        type: array
      SubjectAltURIs:
        items:
          type: string
        type: array
      SubjectKeyId:
        type: string
      ValidNotAfter:
        type: string
      ValidNotBefore:
        type: string
      Version:
        type: integer
    type: object
  ssl.Name:
    properties:
      Country:
        items:
          type: string
        type: array
      Locality:
        items:
          type: string
        type: array
      SerialNumber:
        type: string
      StreetAddress:
        items:
          type: string
        type: array
    type: object
  ssl.PublicKey:
    properties:
      Algorithm:
        type: string
      Exponent:
        type: string
      Modulus:
        type: string
      Size:
        type: integer
      Value:
        type: string
    type: object
  ssl.sslUpdatePayload:
    properties:
      Cert:
        description: SSL Certificates
        type: string
      HTTPEnabled:
        type: boolean
      Key:
        type: string
      clientCert:
        description: SSL Client Certificates
        type: string
    type: object
  stacks.composeStackFromFileContentPayload:
    properties:
      Env:
        description: A list of environment variables used during stack deployment
        items:
          $ref: '#/definitions/portainer.Pair'
        type: array
      FromAppTemplate:
        description: Whether the stack is from a app template
        example: false
        type: boolean
      Name:
        description: Name of the stack
        example: myStack
        type: string
      Registries:
        description: List of Registries to use for this stack
        items:
          type: integer
        type: array
      StackFileContent:
        description: Content of the Stack file
        example: |-
          version: 3
           services:
           web:
           image:nginx
        type: string
      Webhook:
        description: A UUID to identify a webhook. The stack will be force updated
          and pull the latest image when the webhook was invoked.
        example: c11fdf23-183e-428a-9bb6-16db01032174
        type: string
    required:
    - Name
    - StackFileContent
    type: object
  stacks.composeStackFromGitRepositoryPayload:
    properties:
      AdditionalFiles:
        description: Applicable when deploying with multiple stack files
        example:
        - '[nz.compose.yml'
        - ' uat.compose.yml]'
        items:
          type: string
        type: array
      AutoUpdate:
        allOf:
        - $ref: '#/definitions/portainer.AutoUpdateSettings'
        description: Optional GitOps update configuration
      ComposeFile:
        default: docker-compose.yml
        description: Path to the Stack file inside the Git repository
        example: docker-compose.yml
        type: string
      Env:
        description: A list of environment variables used during stack deployment
        items:
          $ref: '#/definitions/portainer.Pair'
        type: array
      FilesystemPath:
        description: Local filesystem path
        example: /tmp
        type: string
      FromAppTemplate:
        description: Whether the stack is from a app template
        example: false
        type: boolean
      Name:
        description: Name of the stack
        example: myStack
        type: string
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
        description: |-
          GitCredentialID used to identify the bound git credential. Required when RepositoryAuthentication
          is true and RepositoryUsername/RepositoryPassword are not provided
        example: 0
        type: integer
      RepositoryPassword:
        description: |-
          Password used in basic authentication. Required when RepositoryAuthentication is true
          and RepositoryGitCredentialID is 0
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
        description: |-
          Username used in basic authentication. Required when RepositoryAuthentication is true
          and RepositoryGitCredentialID is 0
        example: myGitUsername
        type: string
      SupportRelativePath:
        description: Whether the stack supports relative path volume
        example: false
        type: boolean
      TLSSkipVerify:
        description: TLSSkipVerify skips SSL verification when cloning the Git repository
        example: false
        type: boolean
    required:
    - Name
    - RepositoryURL
    type: object
  stacks.kubernetesGitDeploymentPayload:
    properties:
      AdditionalFiles:
        items:
          type: string
        type: array
      AutoUpdate:
        $ref: '#/definitions/portainer.AutoUpdateSettings'
      ComposeFormat:
        type: boolean
      HelmChartPath:
        description: Helm-specific fields
        type: string
      HelmValuesFiles:
        description: Array of paths to values YAML files in Git repo
        items:
          type: string
        type: array
      ManifestFile:
        type: string
      Namespace:
        type: string
      RepositoryAuthentication:
        type: boolean
      RepositoryAuthorizationType:
        $ref: '#/definitions/gittypes.GitCredentialAuthType'
      RepositoryGitCredentialID:
        type: integer
      RepositoryPassword:
        type: string
      RepositoryReferenceName:
        type: string
      RepositoryURL:
        type: string
      RepositoryUsername:
        type: string
      StackName:
        type: string
      TLSSkipVerify:
        description: TLSSkipVerify skips SSL verification when cloning the Git repository
        example: false
        type: boolean
    type: object
  stacks.kubernetesManifestURLDeploymentPayload:
    properties:
      ComposeFormat:
        type: boolean
      ManifestURL:
        type: string
      Namespace:
        type: string
      StackName:
        type: string
    type: object
  stacks.kubernetesStringDeploymentPayload:
    properties:
      ComposeFormat:
        type: boolean
      FromAppTemplate:
        description: Whether the stack is from a app template
        example: false
        type: boolean
      Namespace:
        type: string
      StackFileContent:
        type: string
      StackName:
        type: string
    type: object
  stacks.stackFileResponse:
    properties:
      StackFileContent:
        description: Content of the Stack file
        example: |-
          version: 3
           services:
           web:
           image:nginx
        type: string
    type: object
  stacks.stackGitRedployPayload:
    properties:
      Env:
        items:
          $ref: '#/definitions/portainer.Pair'
        type: array
      Prune:
        example: false
        type: boolean
      PullImage:
        description: |-
          Deprecated(2.36): use RepullImageAndRedeploy instead for cleaner responsibility
          Force a pulling to current image with the original tag though the image is already the latest
        example: false
        type: boolean
      RepositoryAuthentication:
        type: boolean
      RepositoryAuthorizationType:
        $ref: '#/definitions/gittypes.GitCredentialAuthType'
      RepositoryGitCredentialID:
        type: integer
      RepositoryPassword:
        type: string
      RepositoryReferenceName:
        type: string
      RepositoryUsername:
        type: string
      RepullImageAndRedeploy:
        description: RepullImageAndRedeploy indicates whether to force repulling images
          and redeploying the stack
        type: boolean
      StackName:
        type: string
    type: object
  stacks.stackGitUpdatePayload:
    properties:
      Atomic:
        description: Enable atomic rollback on failure (Helm --atomic flag)
        type: boolean
      AutoUpdate:
        $ref: '#/definitions/portainer.AutoUpdateSettings'
      Env:
        items:
          $ref: '#/definitions/portainer.Pair'
        type: array
      HelmChartPath:
        description: Helm chart folder path in Git repo (for Helm stacks)
        type: string
      HelmValuesFiles:
        description: Helm values files paths in Git repo (for Helm stacks)
        items:
          type: string
        type: array
      Prune:
        type: boolean
      Registries:
        items:
          type: integer
        type: array
      RepositoryAuthentication:
        type: boolean
      RepositoryAuthorizationType:
        $ref: '#/definitions/gittypes.GitCredentialAuthType'
      RepositoryGitCredentialID:
        type: integer
      RepositoryPassword:
        type: string
      RepositoryReferenceName:
        type: string
      RepositoryUsername:
        type: string
      TLSSkipVerify:
        type: boolean
    type: object
  stacks.stackMigratePayload:
    properties:
      EndpointID:
        example: 2
        type: integer
      Name:
        example: new-stack
        type: string
      SwarmID:
        example: jpofkc0i9uo9wtx1zesuk649w
        type: string
    required:
    - EndpointID
    type: object
  stacks.swarmStackFromFileContentPayload:
    properties:
      Env:
        description: A list of environment variables used during stack deployment
        items:
          $ref: '#/definitions/portainer.Pair'
        type: array
      FromAppTemplate:
        description: Whether the stack is from a app template
        example: false
        type: boolean
      Name:
        description: Name of the stack
        example: myStack
        type: string
      Registries:
        description: List of Registries to use for this stack
        items:
          type: integer
        type: array
      StackFileContent:
        description: Content of the Stack file
        example: |-
          version: 3
           services:
           web:
           image:nginx
        type: string
      SwarmID:
        description: Swarm cluster identifier
        example: jpofkc0i9uo9wtx1zesuk649w
        type: string
      Webhook:
        description: A UUID to identify a webhook. The stack will be force updated
          and pull the latest image when the webhook was invoked.
        example: c11fdf23-183e-428a-9bb6-16db01032174
        type: string
    required:
    - Name
    - StackFileContent
    - SwarmID
    type: object
  stacks.swarmStackFromGitRepositoryPayload:
    properties:
      AdditionalFiles:
        description: Applicable when deploying with multiple stack files
        example:
        - '[nz.compose.yml'
        - ' uat.compose.yml]'
        items:
          type: string
        type: array
      AutoUpdate:
        allOf:
        - $ref: '#/definitions/portainer.AutoUpdateSettings'
        description: Optional GitOps update configuration
      ComposeFile:
        default: docker-compose.yml
        description: Path to the Stack file inside the Git repository
        example: docker-compose.yml
        type: string
      Env:
        description: A list of environment variables used during stack deployment
        items:
          $ref: '#/definitions/portainer.Pair'
        type: array
      FilesystemPath:
        description: Network filesystem path
        example: /tmp
        type: string
      FromAppTemplate:
        description: Whether the stack is from a app template
        example: false
        type: boolean
      Name:
        description: Name of the stack
        example: myStack
        type: string
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
        description: |-
          GitCredentialID used to identify the bound git credential. Required when RepositoryAuthentication
          is true and RepositoryUsername/RepositoryPassword are not provided
        example: 0
        type: integer
      RepositoryPassword:
        description: |-
          Password used in basic authentication. Required when RepositoryAuthentication is true
          and RepositoryGitCredentialID is 0
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
        description: |-
          Username used in basic authentication. Required when RepositoryAuthentication is true
          and RepositoryGitCredentialID is 0
        example: myGitUsername
        type: string
      SupportRelativePath:
        description: Whether the stack suppors relative path volume
        example: false
        type: boolean
      SwarmID:
        description: Swarm cluster identifier
        example: jpofkc0i9uo9wtx1zesuk649w
        type: string
      TLSSkipVerify:
        description: TLSSkipVerify skips SSL verification when cloning the Git repository
        example: false
        type: boolean
    required:
    - Name
    - RepositoryURL
    - SwarmID
    type: object
  stacks.updateStackPayload:
    properties:
      Env:
        description: A list of environment(endpoint) variables used during stack deployment
        items:
          $ref: '#/definitions/portainer.Pair'
        type: array
      Prune:
        description: Prune services that are no longer referenced (only available
          for Swarm stacks)
        example: true
        type: boolean
      PullImage:
        description: |-
          Deprecated(2.36): use RepullImageAndRedeploy instead for cleaner responsibility
          Force a pulling to current image with the original tag though the image is already the latest
        example: false
        type: boolean
      Registries:
        description: List of Registries to use for this stack
        items:
          type: integer
        type: array
      RepullImageAndRedeploy:
        description: RepullImageAndRedeploy indicates whether to force repulling images
          and redeploying the stack
        type: boolean
      RollbackTo:
        description: RollbackTo specifies the stack file version to rollback to (only
          support to rollback to the last version currently)
        type: integer
      StackFileContent:
        description: New content of the Stack file
        example: |-
          version: 3
           services:
           web:
           image:nginx
        type: string
      Webhook:
        description: A UUID to identify a webhook. The stack will be force updated
          and pull the latest image when the webhook was invoked.
        example: c11fdf23-183e-428a-9bb6-16db01032174
        type: string
    type: object
  stats.ContainerStats:
    properties:
      healthy:
        type: integer
      running:
        type: integer
      stopped:
        type: integer
      total:
        type: integer
      unhealthy:
        type: integer
    type: object
  support.debugLogPayload:
    properties:
      debugLogEnabled:
        type: boolean
    type: object
  swarm.ServiceUpdateResponse:
    properties:
      Warnings:
        description: Optional warning messages
        items:
          type: string
        type: array
    type: object
  tags.tagCreatePayload:
    properties:
      Name:
        example: org/acme
        type: string
    required:
    - Name
    type: object
  teammemberships.teamMembershipCreatePayload:
    properties:
      Role:
        description: Role for the user inside the team (1 for leader and 2 for regular
          member)
        enum:
        - 1
        - 2
        example: 1
        type: integer
      TeamID:
        description: Team identifier
        example: 1
        type: integer
      UserID:
        description: User identifier
        example: 1
        type: integer
    required:
    - Role
    - TeamID
    - UserID
    type: object
  teammemberships.teamMembershipUpdatePayload:
    properties:
      Role:
        description: Role for the user inside the team (1 for leader and 2 for regular
          member)
        enum:
        - 1
        - 2
        example: 1
        type: integer
      TeamID:
        description: Team identifier
        example: 1
        type: integer
      UserID:
        description: User identifier
        example: 1
        type: integer
    required:
    - Role
    - TeamID
    - UserID
    type: object
  teams.teamCreatePayload:
    properties:
      Name:
        description: Name
        example: developers
        type: string
      TeamLeaders:
        description: TeamLeaders
        example:
        - 3
        - 5
        items:
          type: integer
        type: array
    required:
    - Name
    type: object
  teams.teamUpdatePayload:
    properties:
      Name:
        description: Name
        example: developers
        type: string
    type: object
  templates.fileResponse:
    properties:
      FileContent:
        description: The requested file content
        example: version:2
        type: string
    type: object
  templates.listResponse:
    properties:
      templates:
        items:
          $ref: '#/definitions/portainer.Template'
        type: array
      version:
        type: string
    type: object
  types.EndpointUpdateScheduleRelation:
    properties:
      edgeStackId:
        type: integer
      environmentId:
        type: integer
      scheduleId:
        type: integer
      targetVersion:
        type: string
    type: object
  types.EnvironmentMetadata:
    properties:
      customTemplateContent:
        type: string
      customTemplateID:
        type: integer
      groupId:
        type: integer
      stackName:
        type: string
      tagIds:
        items:
          type: integer
        type: array
    type: object
  types.UpdateSchedule:
    properties:
      agentImage:
        description: Name of the agent image, does not include the registry
        example: portainer/agent:latest
        type: string
      created:
        description: Created timestamp
        example: 1564897200
        type: integer
      createdBy:
        description: Created by user id
        example: 1
        type: integer
      edgeGroupIds:
        description: |-
          EdgeGroups to be updated

          There is some duplication here with EdgeStack.EdgeGroups
          EdgeStack.EdgeGroup should have only one group which a temporary group, used only for the update
          This field is saved only to show which groups the user chose when creating the schedule
        example:
        - 1
        items:
          type: integer
        type: array
      edgeStackId:
        example: 1
        type: integer
      environmentsPreviousVersions:
        additionalProperties:
          type: string
        description: Deprecated - use Environment.Agent.PreviousVersion instead
        type: object
      id:
        description: EdgeUpdateSchedule Identifier
        example: 1
        type: integer
      name:
        description: Name of the schedule
        example: Update Schedule
        type: string
      registryId:
        description: ID of registry
        example: 1
        type: integer
      type:
        allOf:
        - $ref: '#/definitions/types.UpdateScheduleType'
        description: Type of the update (1 - update, 2 - rollback)
        enum:
        - 1
        - 2
        example: 1
      updated:
        description: Updated timestamp
        example: 1564897200
        type: integer
      updaterImage:
        description: Name of the updater image, does not include the registry but
          must include a tag
        example: portainer/portainer-updater:latest
        type: string
      version:
        description: Deprecated
        example: 1.0.0
        type: string
    type: object
  types.UpdateScheduleStatusType:
    enum:
    - 0
    - 1
    - 2
    - 3
    - 4
    type: integer
    x-enum-varnames:
    - UpdateScheduleStatusPending
    - UpdateScheduleStatusError
    - UpdateScheduleStatusSuccess
    - UpdateScheduleStatusSent
    - UpdateScheduleStatusInProgress
  types.UpdateScheduleType:
    enum:
    - 0
    - 1
    - 2
    type: integer
    x-enum-varnames:
    - _
    - UpdateScheduleUpdate
    - UpdateScheduleRollback
  unstructured.Unstructured:
    properties:
      Object:
        additionalProperties: true
        description: |-
          Object is a JSON compatible map with string, float, int, bool, []interface{}, or
          map[string]interface{}
          children.
        type: object
    type: object
  useractivity.logsListResponse:
    properties:
      logs:
        items:
          $ref: '#/definitions/portaineree.UserActivityLog'
        type: array
      totalCount:
        type: integer
    type: object
  users.CurrentUserEndpointAuthResponse:
    properties:
      Authorizations:
        $ref: '#/definitions/portainer.Authorizations'
    type: object
  users.User:
    properties:
      Id:
        example: 1
        type: integer
      Role:
        allOf:
        - $ref: '#/definitions/portainer.UserRole'
        description: User role (1 for administrator account and 2 for regular account)
        example: 1
      Username:
        example: bob
        type: string
    type: object
  users.accessTokenResponse:
    properties:
      apiKey:
        $ref: '#/definitions/portainer.APIKey'
      rawAPIKey:
        type: string
    type: object
  users.addHelmRepoUrlPayload:
    properties:
      url:
        type: string
    type: object
  users.adminInitPayload:
    properties:
      Password:
        description: Password for the admin user
        example: admin-password
        type: string
      Username:
        description: Username for the admin user
        example: admin
        type: string
    required:
    - Password
    - Username
    type: object
  users.gitCredentialResponse:
    properties:
      gitCredential:
        $ref: '#/definitions/users.shadowedGitCredential'
    type: object
  users.helmUserRepositoryResponse:
    properties:
      GlobalRepository:
        type: string
      UserRepositories:
        items:
          $ref: '#/definitions/portainer.HelmUserRepository'
        type: array
    type: object
  users.namespaceMapping:
    additionalProperties:
      additionalProperties:
        $ref: '#/definitions/portainer.Authorizations'
      type: object
    type: object
  users.shadowedGitCredential:
    properties:
      authorizationType:
        allOf:
        - $ref: '#/definitions/gittypes.GitCredentialAuthType'
