```
basePath: /api
definitions:
  auth.authenticatePayload:
    properties:
      apiKey:
        description: API Key
        example: "1234567890"
        type: string
      password:
        description: Password
        example: mypassword
        type: string
      username:
        description: Username
        example: admin
        type: string
    required:
    - apiKey
    - password
    - username
    type: object
  auth.authenticateResponse:
    properties:
      jwt:
        description: JWT token used to authenticate against the API
        example: abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyzAB
        type: string
    type: object
  auth.oauthPayload:
    properties:
      Code:
        description: OAuth code returned from OAuth Provided
        type: string
    type: object
  autoupdates.autoUpdateResponseItem:
    properties:
      doneAtUnix:
        type: integer
      startedAtUnix:
        type: integer
      status:
        $ref: '#/definitions/portaineree.AutoUpdateStatus'
      version:
        type: string
    type: object
  autoupdates.listResponse:
    properties:
      autoUpdates:
        items:
          $ref: '#/definitions/autoupdates.autoUpdateResponseItem'
        type: array
    type: object
  backup.backupPayload:
    properties:
      Password:
        type: string
    type: object
  backup.backupStatus:
    properties:
      Failed:
        type: boolean
      TimestampUTC:
        type: string
    type: object
  backup.restorePayload:
    properties:
      FileContent:
        description: Content of the backup
        items:
          type: integer
        type: array
      FileName:
        description: File name
        type: string
      Password:
        description: Password to decrypt the backup with
        type: string
    required:
    - FileContent
    - FileName
    type: object
  backup.restoreS3Settings:
    properties:
      AccessKeyID:
        description: AWS access key id
        type: string
      BucketName:
        description: AWS S3 bucket name
        type: string
      Filename:
        description: AWS S3 filename in the bucket
        type: string
      Password:
        type: string
      Region:
        description: AWS S3 region. Default to "us-east-1"
        example: us-east-1
        type: string
      S3CompatibleHost:
        description: S3 compatible host
        type: string
      SecretAccessKey:
        description: AWS secret access key
        type: string
    type: object
  backup.s3BackupPayload:
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
  build.BuildInfo:
    properties:
      BuildNumber:
        type: string
      GitCommit:
        type: string
      GoVersion:
        type: string
      ImageTag:
        type: string
      NodejsVersion:
        type: string
      PnpmVersion:
        type: string
      WebpackVersion:
        type: string
    type: object
  build.DependenciesInfo:
    properties:
      ComposeVersion:
        type: string
      DockerVersion:
        type: string
      HelmVersion:
        type: string
      KubectlVersion:
        type: string
    type: object
  build.RuntimeInfo:
    properties:
      Env:
        items:
          type: string
        type: array
    type: object
  container.ContainerState:
    enum:
    - created
    - running
    - paused
    - restarting
    - removing
    - exited
    - dead
    type: string
    x-enum-comments:
      StateCreated: StateCreated indicates the container is created, but not (yet)
        started.
      StateDead: StateDead indicates that the container failed to be deleted. Containers
        in this state are attempted to be cleaned up when the daemon restarts.
      StateExited: StateExited indicates that the container exited.
      StatePaused: StatePaused indicates that the container's current state is paused.
      StateRemoving: StateRemoving indicates that the container is being removed.
      StateRestarting: StateRestarting indicates that the container is currently restarting.
      StateRunning: StateRunning indicates that the container is running.
    x-enum-varnames:
    - StateCreated
    - StateRunning
    - StatePaused
    - StateRestarting
    - StateRemoving
    - StateExited
    - StateDead
  container.MountPoint:
    properties:
      Destination:
        description: |-
          Destination is the path relative to the container root (`/`) where the
          Source is mounted inside the container.
        type: string
      Driver:
        description: Driver is the volume driver used to create the volume (if it
          is a volume).
        type: string
      Mode:
        description: |-
          Mode is a comma separated list of options supplied by the user when
          creating the bind/volume mount.

          The default is platform-specific (`"z"` on Linux, empty on Windows).
        type: string
      Name:
        description: |-
          Name is the name reference to the underlying data defined by `Source`
          e.g., the volume name.
        type: string
      Propagation:
        allOf:
        - $ref: '#/definitions/mount.Propagation'
        description: |-
          Propagation describes how mounts are propagated from the host into the
          mount point, and vice-versa. Refer to the Linux kernel documentation
          for details:
          https://www.kernel.org/doc/Documentation/filesystems/sharedsubtree.txt

          This field is not used on Windows.
      RW:
        description: RW indicates whether the mount is mounted writable (read-write).
        type: boolean
      Source:
        description: |-
          Source is the source location of the mount.

          For volumes, this contains the storage location of the volume (within
          `/var/lib/docker/volumes/`). For bind-mounts, and `npipe`, this contains
          the source (host) part of the bind-mount. For `tmpfs` mount points, this
          field is empty.
        type: string
      Type:
        allOf:
        - $ref: '#/definitions/mount.Type'
        description: |-
          Type is the type of mount, see `Type<foo>` definitions in
          github.com/docker/docker/api/types/mount.Type
    type: object
  container.NetworkSettingsSummary:
    properties:
      Networks:
        additionalProperties:
          $ref: '#/definitions/network.EndpointSettings'
        type: object
    type: object
  container.Port:
    properties:
      IP:
        description: Host IP address that the container's port is mapped to
        type: string
      PrivatePort:
        description: |-
          Port on the container
          Required: true
        type: integer
      PublicPort:
        description: Port exposed on the host
        type: integer
      Type:
        description: |-
          type
          Required: true
        type: string
    type: object
  containers.containerGpusResponse:
    properties:
      gpus:
        type: string
    type: object
  customtemplates.customTemplateFromFileContentPayload:
    properties:
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
      FileContent:
        description: Content of stack file
        type: string
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
          Required for Docker stacks
        enum:
        - 1
        - 2
        example: 1
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
        description: Definitions of variables in the stack file
        items:
          $ref: '#/definitions/portainer.CustomTemplateVariableDefinition'
        type: array
    required:
    - Description
    - FileContent
    - Title
    - Type
    type: object
  customtemplates.customTemplateFromGitRepositoryPayload:
    properties:
      ComposeFilePathInRepository:
        default: docker-compose.yml
        description: Path to the Stack file inside the Git repository
        example: docker-compose.yml
        type: string
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
      IsComposeFormat:
        description: IsComposeFormat indicates if the Kubernetes template is created
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
          Required for Docker stacks
        enum:
        - 1
        - 2
        example: 1
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
      TLSSkipVerify:
        description: TLSSkipVerify skips SSL verification when cloning the Git repository
        example: false
        type: boolean
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
        example: 1
      Variables:
        description: Definitions of variables in the stack file
        items:
          $ref: '#/definitions/portainer.CustomTemplateVariableDefinition'
        type: array
    required:
    - Description
    - RepositoryURL
    - Title
    - Type
    type: object
  customtemplates.customTemplateUpdatePayload:
    properties:
      ComposeFilePathInRepository:
        default: docker-compose.yml
        description: Path to the Stack file inside the Git repository
        example: docker-compose.yml
        type: string
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
      FileContent:
        description: Content of stack file
        type: string
      IsComposeFormat:
        description: IsComposeFormat indicates if the Kubernetes template is created
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
          Required for Docker stacks
        enum:
        - 1
        - 2
        example: 1
      RepositoryAuthentication:
        description: Use authentication to clone the Git repository
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
          Password used in basic authentication or token used in token authentication.
          Required when RepositoryAuthentication is true and RepositoryGitCredentialID is 0
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
          and RepositoryGitCredentialID is 0. Ignored if RepositoryAuthType is token
        example: myGitUsername
        type: string
      TLSSkipVerify:
        description: TLSSkipVerify skips SSL verification when cloning the Git repository
        example: false
        type: boolean
      Title:
        description: Title of the template
        example: Nginx
        type: string
      Type:
        allOf:
        - $ref: '#/definitions/portainer.StackType'
        description: Type of created stack (1 - swarm, 2 - compose, 3 - kubernetes)
        enum:
        - 1
        - 2
        - 3
        example: 1
      Variables:
        description: Definitions of variables in the stack file
        items:
          $ref: '#/definitions/portainer.CustomTemplateVariableDefinition'
        type: array
    required:
    - Description
    - FileContent
    - RepositoryURL
    - Title
    - Type
    type: object
  customtemplates.fileResponse:
    properties:
      FileContent:
        type: string
    type: object
  docker.dashboardResponse:
    properties:
      containers:
        $ref: '#/definitions/stats.ContainerStats'
      images:
        $ref: '#/definitions/docker.imagesCounters'
      networks:
        type: integer
      services:
        type: integer
      stacks:
        type: integer
      volumes:
        type: integer
    type: object
  docker.imagesCounters:
    properties:
      size:
        type: integer
      total:
        type: integer
    type: object
  edge.DeployerOptionsPayload:
    properties:
      ForceRecreate:
        description: |-
          ForceRecreate is a flag indicating if the agent must force the redeployment of the stack.
          This field is only used when the Force Redeployment is triggered.
          Once the stack is redeployed, this field will be reset to false.
          For standard edge agent, this field is used in agent side
          For async edge agent, this field is used in both agent side and server side.
          This flag drives `docker compose up --force-recreate` option
        type: boolean
      Prune:
        description: |-
          Prune is a flag indicating if the agent must prune the containers or not when creating/updating an edge stack
          This flag drives `docker compose up --remove-orphans` and `docker stack up --prune` options
          Used only for EE
        type: boolean
      RemoveVolumes:
        description: |-
          RemoveVolumes is a flag indicating if the agent must remove the named volumes declared
          in the compose file and anonymouse volumes attached to containers
          This flag drives `docker compose down --volumes` option
          Used only for EE
        type: boolean
    type: object
  edge.RegistryCredentials:
    properties:
      Secret:
        type: string
      ServerURL:
        type: string
      Username:
        type: string
    type: object
  edge.StackPayload:
    properties:
      AlwaysCloneGitRepoForRelativePath:
        description: |-
          AlwaysCloneGitRepoForRelativePath is a flag indicating if the agent must always clone the git repository for relative path.
          This field is only valid when SupportRelativePath is true.
          Used only for EE
        type: boolean
      CreatedBy:
        description: |-
          CreatedBy is the username that created this stack
          Used for adding labels to Kubernetes manifests
        type: string
      CreatedByUserId:
        description: |-
          CreatedByUserId is the user ID that created this stack
          Used for adding labels to Kubernetes manifests
        type: string
      DeployerOptionsPayload:
        $ref: '#/definitions/edge.DeployerOptionsPayload'
      DirEntries:
        description: Content of stack folder
        items:
          $ref: '#/definitions/filesystem.DirEntry'
        type: array
      EdgeUpdateID:
        description: |-
          EdgeUpdateID is the ID of the edge update related to this stack.
          Used only for EE
        type: integer
      EntryFileName:
        description: Name of the stack entry file
        type: string
      EnvVars:
        description: |-
          Used only for EE
          EnvVars is a list of environment variables to inject into the stack
        items:
          $ref: '#/definitions/portainer.Pair'
        type: array
      FilesystemPath:
        description: Mount point for relative path
        type: string
      ForceUpdate:
        description: |-
          ForceUpdate is a flag indicating if the agent must force the update of the stack.
          Used only for EE
        type: boolean
      HelmConfig:
        allOf:
        - $ref: '#/definitions/portainer.HelmConfig'
        description: HelmConfig represents the Helm configuration for an edge stack
      ID:
        description: ID of the stack
        type: integer
      Name:
        description: Name of the stack
        type: string
      Namespace:
        description: Namespace to use for kubernetes stack. Keep empty to use the
          manifest namespace.
        type: string
      PrePullImage:
        description: |-
          PrePullImage is a flag indicating if the agent must pull the image before deploying the stack.
          Used only for EE
        type: boolean
      RePullImage:
        description: |-
          RePullImage is a flag indicating if the agent must pull the image if it is already present on the node.
          Used only for EE
        type: boolean
      ReadyRePullImage:
        description: |-
          Used only for EE async edge agent
          ReadyRePullImage is a flag to indicate whether the auto update is trigger to re-pull image
          Deprecated(2.36): use DeployerOptionsPayload.ForceRecreate instead
        type: boolean
      RegistryCredentials:
        description: |-
          RegistryCredentials holds the credentials for a Docker registry.
          Used only for EE
        items:
          $ref: '#/definitions/edge.RegistryCredentials'
        type: array
      RetryDeploy:
        description: |-
          RetryDeploy is a flag indicating if the agent must retry to deploy the stack if it fails.
          Used only for EE
        type: boolean
      RetryPeriod:
        description: |-
          RetryPeriod specifies the duration, in seconds, for which the agent should continue attempting to deploy the stack after a failure
          Used only for EE
        type: integer
      RollbackTo:
        description: RollbackTo specifies the stack file version to rollback to (only
          support to rollback to the last version currently)
        type: integer
      StackFileContent:
        description: Content of the stack file (for compatibility to agent version
          less than 2.19.0)
        type: string
      SupportRelativePath:
        description: Is relative path supported
        type: boolean
      Version:
        description: Version of the stack file
        type: integer
    type: object
  edgeconfigs.edgeConfigCreatePayload:
    properties:
      BaseDir:
        type: string
      Category:
        $ref: '#/definitions/portaineree.EdgeConfigCategory'
      EdgeGroupIDs:
        items:
          type: integer
        type: array
      Name:
        type: string
      Type:
        type: string
    type: object
  edgegroups.decoratedEdgeGroup:
    properties:
      Dynamic:
        type: boolean
      EdgeUpdateID:
        type: integer
      EndpointIds:
        description: Shadow to avoid exposing in the API
        type: integer
      EndpointTypes:
        items:
          $ref: '#/definitions/portainer.EndpointType'
        type: array
      Endpoints:
        description: 'Deprecated: only used for API responses'
        items:
          type: integer
        type: array
      EndpointsCount:
        type: integer
      HasEdgeConfig:
        type: boolean
      HasEdgeJob:
        type: boolean
      HasEdgeStack:
        type: boolean
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
      TrustedEndpoints:
        items:
          type: integer
        type: array
      TrustedEndpointsCount:
        type: integer
    type: object
  edgegroups.edgeGroupCreatePayload:
    properties:
      Dynamic:
        type: boolean
      Endpoints:
        items:
          type: integer
        type: array
      Name:
        type: string
      PartialMatch:
        type: boolean
      TagIDs:
        items:
          type: integer
        type: array
    type: object
  edgegroups.edgeGroupUpdatePayload:
    properties:
      Dynamic:
        type: boolean
      Endpoints:
        items:
          type: integer
        type: array
      Name:
        type: string
      PartialMatch:
        type: boolean
      TagIDs:
        items:
          type: integer
        type: array
    type: object
  edgejobs.edgeJobCreateFromFileContentPayload:
    properties:
      CronExpression:
        type: string
      EdgeGroups:
        items:
          type: integer
        type: array
      Endpoints:
        items:
          type: integer
        type: array
      FileContent:
        type: string
      Name:
        type: string
      Recurring:
        type: boolean
    type: object
  edgejobs.edgeJobFileResponse:
