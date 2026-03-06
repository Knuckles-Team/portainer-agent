        items:
          type: string
        type: array
    type: object
  registries.registryConfigurePayload:
    properties:
      Authentication:
        description: Is authentication against this registry enabled
        example: false
        type: boolean
      Password:
        description: Password used to authenticate against this registry. required
          when Authentication is true
        example: registry_password
        type: string
      Region:
        description: ECR region
        type: string
      TLS:
        description: Use TLS
        example: true
        type: boolean
      TLSCACertFile:
        description: The TLS CA certificate file
        items:
          type: integer
        type: array
      TLSCertFile:
        description: The TLS client certificate file
        items:
          type: integer
        type: array
      TLSKeyFile:
        description: The TLS client key file
        items:
          type: integer
        type: array
      TLSSkipVerify:
        description: Skip the verification of the server TLS certificate
        example: false
        type: boolean
      Username:
        description: Username used to authenticate against this registry. Required
          when Authentication is true
        example: registry_user
        type: string
    required:
    - Authentication
    type: object
  registries.registryCreatePayload:
    properties:
      Authentication:
        description: Is authentication against this registry enabled
        example: false
        type: boolean
      BaseURL:
        description: BaseURL required for ProGet registry
        example: registry.mydomain.tld:2375
        type: string
      Ecr:
        allOf:
        - $ref: '#/definitions/portainer.EcrData'
        description: ECR specific details, required when type = 7
      Github:
        allOf:
        - $ref: '#/definitions/portaineree.GithubRegistryData'
        description: Github specific details, required when type = 8
      Gitlab:
        allOf:
        - $ref: '#/definitions/portainer.GitlabRegistryData'
        description: Gitlab specific details, required when type = 4
      Name:
        description: Name that will be used to identify this registry
        example: my-registry
        type: string
      Password:
        description: Password used to authenticate against this registry. required
          when Authentication is true
        example: registry_password
        type: string
      Quay:
        allOf:
        - $ref: '#/definitions/portainer.QuayRegistryData'
        description: Quay specific details, required when type = 1
      TLS:
        description: Use TLS
        example: true
        type: boolean
      Type:
        allOf:
        - $ref: '#/definitions/portainer.RegistryType'
        description: "Registry Type. Valid values are:\n\t1 (Quay.io),\n\t2 (Azure
          container registry),\n\t3 (custom registry),\n\t4 (Gitlab registry),\n\t5
          (ProGet registry),\n\t6 (DockerHub)\n\t7 (ECR)\n\t8 (Github registry)"
        enum:
        - 1
        - 2
        - 3
        - 4
        - 5
        - 6
        - 7
        - 8
        example: 1
      URL:
        description: URL or IP address of the Docker registry
        example: registry.mydomain.tld:2375/feed
        type: string
      Username:
        description: Username used to authenticate against this registry. Required
          when Authentication is true
        example: registry_user
        type: string
    required:
    - Authentication
    - Name
    - Type
    - URL
    type: object
  registries.registryPingPayload:
    properties:
      Password:
        description: Password used to authenticate against this registry
        example: registry_password
        type: string
      TLS:
        description: Use TLS
        example: true
        type: boolean
      Type:
        allOf:
        - $ref: '#/definitions/portainer.RegistryType'
        description: "Registry Type. Valid values are:\n\t1 (Quay.io),\n\t2 (Azure
          container registry),\n\t3 (custom registry),\n\t4 (Gitlab registry),\n\t5
          (ProGet registry),\n\t6 (DockerHub)\n\t7 (ECR)\n\t8 (Github registry)"
        enum:
        - 1
        - 2
        - 3
        - 4
        - 5
        - 6
        - 7
        - 8
        example: 6
      URL:
        description: URL or IP address of the Docker registry
        example: registry-1.docker.io
        type: string
      Username:
        description: Username used to authenticate against this registry
        example: registry_user
        type: string
    required:
    - Type
    - URL
    type: object
  registries.registryPingResponse:
    properties:
      message:
        description: Message provides details about the connection test result
        example: Registry connection successful
        type: string
      success:
        description: Success indicates if the registry connection was successful
        example: true
        type: boolean
    type: object
  registries.registryUpdatePayload:
    properties:
      Authentication:
        example: false
        type: boolean
      BaseURL:
        example: registry.mydomain.tld:2375
        type: string
      Ecr:
        $ref: '#/definitions/portainer.EcrData'
      Github:
        $ref: '#/definitions/portaineree.GithubRegistryData'
      Name:
        example: my-registry
        type: string
      Password:
        example: registry_password
        type: string
      Quay:
        $ref: '#/definitions/portainer.QuayRegistryData'
      RegistryAccesses:
        $ref: '#/definitions/portainer.RegistryAccesses'
      URL:
        example: registry.mydomain.tld:2375/feed
        type: string
      Username:
        example: registry_user
        type: string
    required:
    - Authentication
    - Name
    - URL
    type: object
  registries.repositoryTagsDeletePayload:
    properties:
      tags:
        items:
          type: string
        type: array
    type: object
  release.Chart:
    properties:
      files:
        description: |-
          Files are miscellaneous files in a chart archive,
          e.g. README, LICENSE, etc.
        items:
          $ref: '#/definitions/release.File'
        type: array
      lock:
        allOf:
        - $ref: '#/definitions/release.Lock'
        description: Lock is the contents of Chart.lock.
      metadata:
        allOf:
        - $ref: '#/definitions/release.Metadata'
        description: Metadata is the contents of the Chartfile.
      schema:
        description: Schema is an optional JSON schema for imposing structure on Values
        items:
          type: integer
        type: array
      templates:
        description: Templates for this chart.
        items:
          $ref: '#/definitions/release.File'
        type: array
      values:
        additionalProperties: {}
        description: Values are default config for this chart.
        type: object
    type: object
  release.ChartReference:
    properties:
      chartPath:
        type: string
      registryID:
        type: integer
      repoURL:
        type: string
    type: object
  release.Dependency:
    properties:
      alias:
        description: Alias usable alias to be used for the chart
        type: string
      condition:
        description: A yaml path that resolves to a boolean, used for enabling/disabling
          charts (e.g. subchart1.enabled )
        type: string
      enabled:
        description: Enabled bool determines if chart should be loaded
        type: boolean
      import-values:
        description: |-
          ImportValues holds the mapping of source values to parent key to be imported. Each item can be a
          string or pair of child/parent sublist items.
        items: {}
        type: array
      name:
        description: |-
          Name is the name of the dependency.

          This must mach the name in the dependency's Chart.yaml.
        type: string
      repository:
        description: |-
          The URL to the repository.

          Appending `index.yaml` to this string should result in a URL that can be
          used to fetch the repository index.
        type: string
      tags:
        description: Tags can be used to group charts for enabling/disabling together
        items:
          type: string
        type: array
      version:
        description: |-
          Version is the version (range) of this chart.

          A lock file will always produce a single version, while a dependency
          may contain a semantic version range.
        type: string
    type: object
  release.File:
    properties:
      data:
        description: Data is the template as byte data.
        items:
          type: integer
        type: array
      name:
        description: Name is the path-like name of the template.
        type: string
    type: object
  release.Lock:
    properties:
      dependencies:
        description: Dependencies is the list of dependencies that this lock file
          has locked.
        items:
          $ref: '#/definitions/release.Dependency'
        type: array
      digest:
        description: Digest is a hash of the dependencies in Chart.yaml.
        type: string
      generated:
        description: Generated is the date the lock file was last generated.
        type: string
    type: object
  release.Maintainer:
    properties:
      email:
        description: Email is an optional email address to contact the named maintainer
        type: string
      name:
        description: Name is a user name or organization name
        type: string
      url:
        description: URL is an optional URL to an address for the named maintainer
        type: string
    type: object
  release.Metadata:
    properties:
      annotations:
        additionalProperties:
          type: string
        description: |-
          Annotations are additional mappings uninterpreted by Helm,
          made available for inspection by other applications.
        type: object
      apiVersion:
        description: The API Version of this chart. Required.
        type: string
      appVersion:
        description: The version of the application enclosed inside of this chart.
        type: string
      condition:
        description: The condition to check to enable chart
        type: string
      dependencies:
        description: Dependencies are a list of dependencies for a chart.
        items:
          $ref: '#/definitions/release.Dependency'
        type: array
      deprecated:
        description: Whether or not this chart is deprecated
        type: boolean
      description:
        description: A one-sentence description of the chart
        type: string
      home:
        description: The URL to a relevant project page, git repo, or contact person
        type: string
      icon:
        description: The URL to an icon file.
        type: string
      keywords:
        description: A list of string keywords
        items:
          type: string
        type: array
      kubeVersion:
        description: KubeVersion is a SemVer constraint specifying the version of
          Kubernetes required.
        type: string
      maintainers:
        description: A list of name and URL/email address combinations for the maintainer(s)
        items:
          $ref: '#/definitions/release.Maintainer'
        type: array
      name:
        description: The name of the chart. Required.
        type: string
      sources:
        description: Source is the URL to the source code of this chart
        items:
          type: string
        type: array
      tags:
        description: The tags to check to enable chart
        type: string
      type:
        description: 'Specifies the chart type: application or library'
        type: string
      version:
        description: A SemVer 2 conformant version string of the chart. Required.
        type: string
    type: object
  release.ReleaseElement:
    properties:
      appVersion:
        type: string
      chart:
        type: string
      name:
        type: string
      namespace:
        type: string
      revision:
        type: string
      status:
        type: string
      updated:
        type: string
    type: object
  release.Values:
    properties:
      computedValues:
        type: string
      userSuppliedValues:
        type: string
    type: object
  resource.Quantity:
    properties:
      Format:
        enum:
        - DecimalExponent
        - BinarySI
        - DecimalSI
        type: string
        x-enum-comments:
          BinarySI: e.g., 12Mi (12 * 2^20)
          DecimalExponent: e.g., 12e6
          DecimalSI: e.g., 12M  (12 * 10^6)
        x-enum-varnames:
        - DecimalExponent
        - BinarySI
        - DecimalSI
    type: object
  resourcecontrols.resourceControlCreatePayload:
    properties:
      AdministratorsOnly:
        description: Permit access to resource only to admins
        example: true
        type: boolean
      Public:
        description: Permit access to the associated resource to any user
        example: true
        type: boolean
      ResourceID:
        example: 617c5f22bb9b023d6daab7cba43a57576f83492867bc767d1c59416b065e5f08
        type: string
      SubResourceIDs:
        description: List of Docker resources that will inherit this access control
        example:
        - 617c5f22bb9b023d6daab7cba43a57576f83492867bc767d1c59416b065e5f08
        items:
          type: string
        type: array
      Teams:
        description: List of team identifiers with access to the associated resource
        example:
        - 56
        - 7
        items:
          type: integer
        type: array
      Type:
        allOf:
        - $ref: '#/definitions/portainer.ResourceControlType'
        description: |-
          Type of Resource. Valid values are: 1 - container, 2 - service
          3 - volume, 4 - network, 5 - secret, 6 - stack, 7 - config, 8 - custom template, 9 - azure-container-group
        enum:
        - 1
        - 2
        - 3
        - 4
        - 5
        - 6
        - 7
        - 8
        - 9
        example: 1
      Users:
        description: List of user identifiers with access to the associated resource
        example:
        - 1
        - 4
        items:
          type: integer
        type: array
    required:
    - ResourceID
    - Type
    type: object
  resourcecontrols.resourceControlUpdatePayload:
    properties:
      AdministratorsOnly:
        description: Permit access to resource only to admins
        example: true
        type: boolean
      Public:
        description: Permit access to the associated resource to any user
        example: true
        type: boolean
      Teams:
        description: List of team identifiers with access to the associated resource
        example:
        - 7
        items:
          type: integer
        type: array
      Users:
        description: List of user identifiers with access to the associated resource
        example:
        - 4
        items:
          type: integer
        type: array
    type: object
  roar.Roar-portainer_EndpointID:
    type: object
  settings.autoPatchResponse:
    properties:
      Enabled:
        type: boolean
      PatchCron:
        example: 0 4 * * *
        type: string
    type: object
  settings.autoPatchSettingsPayload:
    properties:
      Enabled:
        example: false
        type: boolean
      PatchCron:
        example: 0 0 * * *
        type: string
      PortainerRepository:
        example: portainer/portainer-ee
        type: string
      RegistryID:
        example: 1
        type: integer
      UpdaterRepository:
        example: portainer/portainer-updater
        type: string
    type: object
  settings.defaultRegistryUpdatePayload:
    properties:
      Hide:
        example: false
        type: boolean
    type: object
  settings.mTLSPayload:
    properties:
      CaCert:
        type: string
      Cert:
        type: string
      Key:
        type: string
      UseSeparateCert:
        type: boolean
    type: object
  settings.publicSettingsResponse:
    properties:
      AuthenticationMethod:
        allOf:
        - $ref: '#/definitions/portainer.AuthenticationMethod'
        description: 'Active authentication method for the Portainer instance. Valid
          values are: 1 for internal, 2 for LDAP, or 3 for oauth'
        example: 1
      AutoPatchSettings:
        $ref: '#/definitions/settings.autoPatchResponse'
      CustomLoginBanner:
        description: The content in plaintext used to display in the login page. Will
          hide when value is empty string
        example: notice or agreement
        type: string
      DefaultRegistry:
        properties:
          Hide:
            example: false
            type: boolean
        type: object
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
      Edge:
        properties:
          CheckinInterval:
            description: The check in interval for edge agent (in seconds) - used
              in non async mode [seconds]
            example: 60
            type: integer
          CommandInterval:
            description: The command list interval for edge agent - used in edge async
              mode [seconds]
            example: 60
            type: integer
          MTLS:
            $ref: '#/definitions/portaineree.MTLSSettings'
          PingInterval:
            description: The ping interval for edge agent - used in edge async mode
              [seconds]
            example: 60
            type: integer
          SnapshotInterval:
            description: The snapshot interval for edge agent - used in edge async
              mode [seconds]
            example: 60
            type: integer
        type: object
      EnableEdgeComputeFeatures:
        description: Whether edge compute features are enabled
        example: true
        type: boolean
      FIPSMode:
        description: Whether FIPS mode is enabled
        type: boolean
      Features:
        additionalProperties:
          type: boolean
        description: Supported feature flags
        type: object
      GlobalDeploymentOptions:
        allOf:
        - $ref: '#/definitions/portaineree.GlobalDeploymentOptions'
        description: Deployment options for encouraging deployment as code
      IsAMTEnabled:
        description: Whether AMT is enabled
        type: boolean
      IsObservabilityEnabled:
        description: Whether observability is enabled
        type: boolean
      KubeconfigExpiry:
        default: "0"
        description: The expiry of a Kubeconfig
        example: 24h
        type: string
      LogoURL:
        description: URL to a logo that will be displayed on the login page as well
          as on top of the sidebar. Will use default Portainer logo when value is
          empty string
        example: https://mycompany.mydomain.tld/logo.png
        type: string
      OAuthHideInternalAuth:
        description: Whether portainer internal auth view will be hidden
        example: true
        type: boolean
      OAuthLoginURI:
        description: The URL used for oauth login
        example: https://gitlab.com/oauth
        type: string
      OAuthLogoutURI:
        description: The URL used for oauth logout
        example: https://gitlab.com/oauth/logout
        type: string
      RequiredPasswordLength:
        description: The minimum required length for a password of any user when using
          internal auth mode
        example: 1
        type: integer
      TeamSync:
        description: Whether team sync is enabled
        example: true
        type: boolean
      Whitelabel:
        description: The display name of the app
        example: My Company
        type: string
    type: object
  settings.settingsAdditionalFunctionalityInspectResponse:
    properties:
      additionalFunctionality:
        $ref: '#/definitions/portaineree.AdditionalFunctionality'
    type: object
  settings.settingsAdditionalFunctionalityUpdatePayload:
    properties:
      Observability:
        example: true
        type: boolean
      Policies:
        example: true
        type: boolean
    required:
    - Observability
    - Policies
    type: object
  settings.settingsCACertResponse:
    properties:
      MTLSCACertificate:
        allOf:
        - $ref: '#/definitions/ssl.Certificate'
        description: MTLSCACertificate is the X.509 Certificate of the MTLS CA Certificate
    type: object
  settings.settingsCertResponse:
    properties:
      MTLSCertificate:
        allOf:
        - $ref: '#/definitions/ssl.Certificate'
        description: MTLSCertificate is the X.509 Certificate of the MTLS Certificate
    type: object
  settings.settingsExperimentalInspectResponse:
    properties:
      experimentalFeatures:
        $ref: '#/definitions/portaineree.ExperimentalFeatures'
    type: object
  settings.settingsExperimentalUpdatePayload:
    properties:
      fleetManagement:
        example: false
        type: boolean
    type: object
  settings.settingsUpdatePayload:
    properties:
      AuthenticationMethod:
        description: 'Active authentication method for the Portainer instance. Valid
          values are: 1 for internal, 2 for LDAP, or 3 for oauth'
        example: 1
        type: integer
      AutoPatchSettings:
        allOf:
        - $ref: '#/definitions/settings.autoPatchSettingsPayload'
        description: Whether to enable automatic patches
      BlackListedLabels:
        description: A list of label name & value that will be used to hide containers
          when querying containers
        items:
          $ref: '#/definitions/portainer.Pair'
        type: array
      CustomLoginBanner:
        description: The content in plaintext used to display in the login page. Will
          hide when value is empty string
        example: notice or agreement
        type: string
      DisableKubeRolesSync:
        description: Whether to disable kube roles sync for all built-in roles
        example: false
        type: boolean
      DisableKubeShell:
        description: Whether to disable kubeshell access for non-admin users
        example: false
        type: boolean
      DisableKubeconfigDownload:
        description: Whether to disable kubeconfig download for non-admin users
        example: false
        type: boolean
      Edge:
        properties:
          AsyncMode:
            description: AsyncMode enables edge agent to run in async mode by default
            type: boolean
          CommandInterval:
            description: The command list interval for edge agent - used in edge async
              mode (in seconds)
            example: 5
            type: integer
          MTLS:
            $ref: '#/definitions/settings.mTLSPayload'
          PingInterval:
            description: The ping interval for edge agent - used in edge async mode
              (in seconds)
            example: 5
            type: integer
          SnapshotInterval:
            description: The snapshot interval for edge agent - used in edge async
              mode (in seconds)
            example: 5
            type: integer
          TunnelServerAddress:
            description: The address where the tunneling server can be reached by
              Edge agents
            type: string
        type: object
      EdgeAgentCheckinInterval:
        description: The default check in interval for edge agent (in seconds)
        example: 5
        type: integer
      EdgePortainerURL:
        description: EdgePortainerURL is the URL that is exposed to edge agents
        type: string
      EnableEdgeComputeFeatures:
        description: Whether edge compute features are enabled
        example: true
        type: boolean
      EnforceEdgeID:
        description: EnforceEdgeID makes Portainer store the Edge ID instead of accepting
          anyone
        example: false
        type: boolean
      GlobalDeploymentOptions:
        allOf:
        - $ref: '#/definitions/portaineree.GlobalDeploymentOptions'
        description: Deployment options for encouraging deployment as code
      HelmRepositoryURL:
        description: Helm repository URL
        example: https://charts.bitnami.com/bitnami
        type: string
      InternalAuthSettings:
        $ref: '#/definitions/portainer.InternalAuthSettings'
      KubeconfigExpiry:
        default: "0"
        description: The expiry of a Kubeconfig
        example: 24h
        type: string
      KubectlShellImage:
        description: "Kubec\ttl Shell Image Name/Tag"
        example: portainer/kubectl-shell:latest
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
