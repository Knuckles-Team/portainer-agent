  models.K8sCustomResourceDefinition:
    properties:
      creationDate:
        type: string
      group:
        type: string
      name:
        type: string
      releaseName:
        type: string
      releaseNamespace:
        type: string
      releaseVersion:
        type: string
      scope:
        type: string
    type: object
  models.K8sDashboard:
    properties:
      applicationsCount:
        type: integer
      configMapsCount:
        type: integer
      ingressesCount:
        type: integer
      namespacesCount:
        type: integer
      secretsCount:
        type: integer
      servicesCount:
        type: integer
      volumesCount:
        type: integer
    type: object
  models.K8sIngressController:
    properties:
      Availability:
        type: boolean
      ClassName:
        type: string
      Name:
        type: string
      New:
        type: boolean
      Type:
        type: string
      Used:
        type: boolean
    type: object
  models.K8sIngressDeleteRequests:
    additionalProperties:
      items:
        type: string
      type: array
    type: object
  models.K8sIngressInfo:
    properties:
      Annotations:
        additionalProperties:
          type: string
        type: object
      ClassName:
        type: string
      CreationDate:
        type: string
      Hosts:
        items:
          type: string
        type: array
      Labels:
        additionalProperties:
          type: string
        type: object
      Name:
        type: string
      Namespace:
        type: string
      Paths:
        items:
          $ref: '#/definitions/models.K8sIngressPath'
        type: array
      TLS:
        items:
          $ref: '#/definitions/models.K8sIngressTLS'
        type: array
      Type:
        type: string
      UID:
        type: string
    type: object
  models.K8sIngressPath:
    properties:
      HasService:
        type: boolean
      Host:
        type: string
      IngressName:
        type: string
      Path:
        type: string
      PathType:
        type: string
      Port:
        type: integer
      ServiceName:
        type: string
    type: object
  models.K8sIngressTLS:
    properties:
      Hosts:
        items:
          type: string
        type: array
      SecretName:
        type: string
    type: object
  models.K8sLoadBalancerQuota:
    properties:
      enabled:
        type: boolean
      limit:
        type: integer
    type: object
  models.K8sNamespaceDetails:
    properties:
      Annotations:
        additionalProperties:
          type: string
        type: object
      LoadBalancerQuota:
        $ref: '#/definitions/models.K8sLoadBalancerQuota'
      Name:
        type: string
      Owner:
        type: string
      ResourceQuota:
        $ref: '#/definitions/models.K8sResourceQuota'
      StorageQuotas:
        additionalProperties:
          $ref: '#/definitions/models.K8sStorageQuota'
        type: object
    type: object
  models.K8sResourceQuota:
    properties:
      cpuLimit:
        type: string
      cpuRequest:
        type: string
      enabled:
        type: boolean
      memoryLimit:
        type: string
      memoryRequest:
        type: string
    type: object
  models.K8sRole:
    properties:
      annotations:
        additionalProperties:
          type: string
        type: object
      creationDate:
        type: string
      isSystem:
        description: |-
          isSystem is true if prefixed with "system:" or exists in the kube-system namespace
          or is one of the portainer roles
        type: boolean
      isUnused:
        description: Unused is true if the role is not bound to any subject.
        type: boolean
      name:
        type: string
      namespace:
        type: string
      resourceVersion:
        type: string
      rules:
        items:
          $ref: '#/definitions/v1.PolicyRule'
        type: array
      uid:
        type: string
    type: object
  models.K8sRoleBinding:
    properties:
      annotations:
        additionalProperties:
          type: string
        type: object
      creationDate:
        type: string
      isSystem:
        type: boolean
      isUnused:
        type: boolean
      name:
        type: string
      namespace:
        type: string
      resourceVersion:
        type: string
      roleRef:
        $ref: '#/definitions/v1.RoleRef'
      subjects:
        items:
          $ref: '#/definitions/k8s_io_api_rbac_v1.Subject'
        type: array
      uid:
        type: string
    type: object
  models.K8sRoleBindingDeleteRequests:
    additionalProperties:
      items:
        type: string
      type: array
    type: object
  models.K8sRoleDeleteRequests:
    additionalProperties:
      items:
        type: string
      type: array
    type: object
  models.K8sSecret:
    properties:
      Annotations:
        additionalProperties:
          type: string
        type: object
      ConfigurationOwner:
        type: string
      ConfigurationOwnerId:
        type: string
      ConfigurationOwners:
        items:
          $ref: '#/definitions/models.K8sConfigurationOwnerResource'
        type: array
      CreationDate:
        type: string
      Data:
        additionalProperties:
          type: string
        type: object
      IsUsed:
        type: boolean
      Labels:
        additionalProperties:
          type: string
        type: object
      Name:
        type: string
      Namespace:
        type: string
      SecretType:
        type: string
      UID:
        type: string
    type: object
  models.K8sServiceDeleteRequests:
    additionalProperties:
      items:
        type: string
      type: array
    type: object
  models.K8sServiceInfo:
    properties:
      AllocateLoadBalancerNodePorts:
        type: boolean
      Annotations:
        additionalProperties:
          type: string
        type: object
      Applications:
        description: serviceList screen
        items:
          $ref: '#/definitions/models.K8sApplication'
        type: array
      ClusterIPs:
        items:
          type: string
        type: array
      CreationDate:
        type: string
      ExternalIPs:
        items:
          type: string
        type: array
      ExternalName:
        type: string
      IngressStatus:
        items:
          $ref: '#/definitions/models.K8sServiceIngress'
        type: array
      Labels:
        additionalProperties:
          type: string
        type: object
      Name:
        type: string
      Namespace:
        type: string
      Ports:
        items:
          $ref: '#/definitions/models.K8sServicePort'
        type: array
      Selector:
        additionalProperties:
          type: string
        type: object
      Type:
        type: string
      UID:
        type: string
    type: object
  models.K8sServiceIngress:
    properties:
      Host:
        type: string
      IP:
        type: string
    type: object
  models.K8sServicePort:
    properties:
      Name:
        type: string
      NodePort:
        type: integer
      Port:
        type: integer
      Protocol:
        type: string
      TargetPort:
        type: string
    type: object
  models.K8sStorageQuota:
    properties:
      enabled:
        type: boolean
      limit:
        type: string
    type: object
  models.Matcher:
    properties:
      isEqual:
        description: is equal
        type: boolean
      isRegex:
        description: |-
          is regex
          Required: true
        type: boolean
      name:
        description: |-
          name
          Required: true
        type: string
      value:
        description: |-
          value
          Required: true
        type: string
    type: object
  models.Metadata:
    properties:
      annotations:
        additionalProperties:
          type: string
        type: object
      labels:
        additionalProperties:
          type: string
        type: object
    type: object
  models.Pod:
    properties:
      ContainerName:
        type: string
      CreationDate:
        type: string
      Image:
        type: string
      ImagePullPolicy:
        type: string
      Name:
        type: string
      NodeName:
        type: string
      PodIP:
        type: string
      Status:
        type: string
      Uid:
        type: string
    type: object
  models.PostableSilence:
    properties:
      comment:
        description: |-
          comment
          Required: true
        type: string
      createdBy:
        description: |-
          created by
          Required: true
        type: string
      endsAt:
        description: |-
          ends at
          Required: true
          Format: date-time
        type: string
      id:
        description: id
        type: string
      matchers:
        description: |-
          matchers
          Required: true
        items:
          $ref: '#/definitions/models.Matcher'
        type: array
      startsAt:
        description: |-
          starts at
          Required: true
          Format: date-time
        type: string
    type: object
  models.PublishedPort:
    properties:
      IngressRules:
        items:
          $ref: '#/definitions/models.IngressRule'
        type: array
      Port:
        type: integer
    type: object
  models.SSHKeyPair:
    properties:
      private:
        type: string
      public:
        type: string
    type: object
  models.TLSInfo:
    properties:
      hosts:
        items:
          type: string
        type: array
    type: object
  motd.motdResponse:
    properties:
      ContentLayout:
        additionalProperties:
          type: string
        type: object
      Hash:
        items:
          type: integer
        type: array
      Message:
        type: string
      Style:
        type: string
      Title:
        type: string
    type: object
  mount.Propagation:
    enum:
    - rprivate
    - private
    - rshared
    - shared
    - rslave
    - slave
    type: string
    x-enum-varnames:
    - PropagationRPrivate
    - PropagationPrivate
    - PropagationRShared
    - PropagationShared
    - PropagationRSlave
    - PropagationSlave
  mount.Type:
    enum:
    - bind
    - volume
    - tmpfs
    - npipe
    - cluster
    - image
    type: string
    x-enum-varnames:
    - TypeBind
    - TypeVolume
    - TypeTmpfs
    - TypeNamedPipe
    - TypeCluster
    - TypeImage
  network.EndpointIPAMConfig:
    properties:
      IPv4Address:
        type: string
      IPv6Address:
        type: string
      LinkLocalIPs:
        items:
          type: string
        type: array
    type: object
  network.EndpointSettings:
    properties:
      Aliases:
        description: Aliases holds the list of extra, user-specified DNS names for
          this endpoint.
        items:
          type: string
        type: array
      DNSNames:
        description: |-
          DNSNames holds all the (non fully qualified) DNS names associated to this endpoint. First entry is used to
          generate PTR records.
        items:
          type: string
        type: array
      DriverOpts:
        additionalProperties:
          type: string
        type: object
      EndpointID:
        type: string
      Gateway:
        type: string
      GlobalIPv6Address:
        type: string
      GlobalIPv6PrefixLen:
        type: integer
      GwPriority:
        description: |-
          GwPriority determines which endpoint will provide the default gateway
          for the container. The endpoint with the highest priority will be used.
          If multiple endpoints have the same priority, they are lexicographically
          sorted based on their network name, and the one that sorts first is picked.
        type: integer
      IPAMConfig:
        allOf:
        - $ref: '#/definitions/network.EndpointIPAMConfig'
        description: Configurations
      IPAddress:
        type: string
      IPPrefixLen:
        type: integer
      IPv6Gateway:
        type: string
      Links:
        items:
          type: string
        type: array
      MacAddress:
        description: |-
          MacAddress may be used to specify a MAC address when the container is created.
          Once the container is running, it becomes operational data (it may contain a
          generated address).
        type: string
      NetworkID:
        description: Operational data
        type: string
    type: object
  oauth2.AuthStyle:
    enum:
    - 0
    - 1
    - 2
    type: integer
    x-enum-varnames:
    - AuthStyleAutoDetect
    - AuthStyleInParams
    - AuthStyleInHeader
  observability.alertRuleUpdatePayload:
    properties:
      AlertingRule:
        $ref: '#/definitions/portaineree.AlertingRule'
    type: object
  observability.alertingUpdatePayload:
    properties:
      AlertingSettings:
        $ref: '#/definitions/portaineree.AlertingSettings'
    type: object
  observability.createSilencePayload:
    properties:
      alertManagerURL:
        type: string
      silence:
        $ref: '#/definitions/models.PostableSilence'
    required:
    - alertManagerURL
    - silence
    type: object
  openamt.deviceActionPayload:
    properties:
      Action:
        type: string
    type: object
  openamt.deviceFeaturesPayload:
    properties:
      Features:
        $ref: '#/definitions/portainer.OpenAMTDeviceEnabledFeatures'
    type: object
  openamt.openAMTConfigurePayload:
    properties:
      CertFileContent:
        type: string
      CertFileName:
        type: string
      CertFilePassword:
        type: string
      DomainName:
        type: string
      Enabled:
        type: boolean
      MPSPassword:
        type: string
      MPSServer:
        type: string
      MPSUser:
        type: string
    type: object
  os.FileMode:
    enum:
    - 2147483648
    - 1073741824
    - 536870912
    - 268435456
    - 134217728
    - 67108864
    - 33554432
    - 16777216
    - 8388608
    - 4194304
    - 2097152
    - 1048576
    - 524288
    - 2401763328
    - 511
    - 2147483648
    - 1073741824
    - 536870912
    - 268435456
    - 134217728
    - 67108864
    - 33554432
    - 16777216
    - 8388608
    - 4194304
    - 2097152
    - 1048576
    - 524288
    - 2401763328
    - 511
    type: integer
    x-enum-comments:
      ModeAppend: 'a: append-only'
      ModeCharDevice: 'c: Unix character device, when ModeDevice is set'
      ModeDevice: 'D: device file'
      ModeDir: 'd: is a directory'
      ModeExclusive: 'l: exclusive use'
      ModeIrregular: '?: non-regular file; nothing else is known about this file'
      ModeNamedPipe: 'p: named pipe (FIFO)'
      ModePerm: Unix permission bits, 0o777
      ModeSetgid: 'g: setgid'
      ModeSetuid: 'u: setuid'
      ModeSocket: 'S: Unix domain socket'
      ModeSticky: 't: sticky'
      ModeSymlink: 'L: symbolic link'
      ModeTemporary: 'T: temporary file; Plan 9 only'
    x-enum-varnames:
    - ModeDir
    - ModeAppend
    - ModeExclusive
    - ModeTemporary
    - ModeSymlink
    - ModeDevice
    - ModeNamedPipe
    - ModeSocket
    - ModeSetuid
    - ModeSetgid
    - ModeCharDevice
    - ModeSticky
    - ModeIrregular
    - ModeType
    - ModePerm
  platform.ContainerPlatform:
    enum:
    - Docker
    - Docker Standalone
    - Docker Swarm
    - Kubernetes
    - Podman
    type: string
    x-enum-varnames:
    - PlatformDocker
    - PlatformDockerStandalone
    - PlatformDockerSwarm
    - PlatformKubernetes
    - PlatformPodman
  podsecurity.FSGroupStrategyType:
    enum:
    - MayRunAs
    - MustRunAs
    - RunAsAny
    type: string
    x-enum-varnames:
    - FSGroupStrategyMayRunAs
    - FSGroupStrategyMustRunAs
    - FSGroupStrategyRunAsAny
  podsecurity.FSType:
    enum:
    - azureFile
    - flocker
    - flexVolume
    - hostPath
    - emptyDir
    - gcePersistentDisk
    - awsElasticBlockStore
    - gitRepo
    - secret
    - nfs
    - iscsi
    - glusterfs
    - persistentVolumeClaim
    - rbd
    - cinder
    - cephFS
    - downwardAPI
    - fc
    - configMap
    - vsphereVolume
    - quobyte
    - azureDisk
    - photonPersistentDisk
    - storageos
    - projected
    - portworxVolume
    - scaleIO
    - csi
    - ephemeral
    - '*'
    type: string
    x-enum-varnames:
    - AzureFile
    - Flocker
    - FlexVolume
    - HostPath
    - EmptyDir
    - GCEPersistentDisk
    - AWSElasticBlockStore
    - GitRepo
    - Secret
    - NFS
    - ISCSI
    - Glusterfs
    - PersistentVolumeClaim
    - RBD
    - Cinder
    - CephFS
    - DownwardAPI
    - FC
    - ConfigMap
    - VsphereVolume
    - Quobyte
    - AzureDisk
    - PhotonPersistentDisk
    - StorageOS
    - Projected
    - PortworxVolume
    - ScaleIO
    - CSI
    - Ephemeral
    - All
  podsecurity.PodSecurityAllowFlexVolumes:
    properties:
      allowedVolumes:
        items:
          type: string
        type: array
      enabled:
        type: boolean
    type: object
  podsecurity.PodSecurityAllowPrivilegeEscalation:
    properties:
      enabled:
        type: boolean
    type: object
  podsecurity.PodSecurityAllowProcMount:
    properties:
      enabled:
        type: boolean
      procMountType:
        type: string
    type: object
  podsecurity.PodSecurityAllowedCapabilities:
    properties:
      level:
        type: string
      role:
        type: string
      type:
        type: string
      user:
        type: string
    type: object
  podsecurity.PodSecurityAllowedPaths:
    properties:
      pathPrefix:
        type: string
      readonly:
        type: boolean
    type: object
  podsecurity.PodSecurityAppArmour:
    properties:
      AppArmorType:
        items:
          type: string
        type: array
      enabled:
        type: boolean
    type: object
  podsecurity.PodSecurityCapabilities:
    properties:
      allowedCapabilities:
        items:
          type: string
        type: array
      enabled:
        type: boolean
      requiredDropCapabilities:
        items:
          type: string
        type: array
    type: object
  podsecurity.PodSecurityForbiddenSysctlsList:
    properties:
      enabled:
        type: boolean
      requiredDropCapabilities:
        items:
          type: string
        type: array
    type: object
  podsecurity.PodSecurityFsGroups:
    properties:
      idrange:
        items:
          $ref: '#/definitions/podsecurity.PodSecurityIdrange'
        type: array
      type:
        $ref: '#/definitions/podsecurity.FSGroupStrategyType'
    type: object
  podsecurity.PodSecurityHostFilesystem:
    properties:
      allowedPaths:
        items:
          $ref: '#/definitions/podsecurity.PodSecurityAllowedPaths'
        type: array
      enabled:
        type: boolean
    type: object
  podsecurity.PodSecurityHostNamespaces:
    properties:
      enabled:
        type: boolean
    type: object
  podsecurity.PodSecurityHostNetworkingPorts:
    properties:
      enabled:
        type: boolean
      hostNetwork:
        type: boolean
      max:
        type: integer
      min:
        type: integer
    type: object
  podsecurity.PodSecurityIdrange:
    properties:
      max:
        type: integer
      min:
        type: integer
    type: object
  podsecurity.PodSecurityPrivilegedContainers:
    properties:
      enabled:
        type: boolean
    type: object
  podsecurity.PodSecurityReadOnlyRootFileSystem:
    properties:
      enabled:
        type: boolean
    type: object
  podsecurity.PodSecurityRule:
    properties:
      allowFlexVolumes:
        $ref: '#/definitions/podsecurity.PodSecurityAllowFlexVolumes'
      allowPrivilegeEscalation:
        $ref: '#/definitions/podsecurity.PodSecurityAllowPrivilegeEscalation'
      allowProcMount:
        $ref: '#/definitions/podsecurity.PodSecurityAllowProcMount'
      appArmor:
        $ref: '#/definitions/podsecurity.PodSecurityAppArmour'
      capabilities:
        $ref: '#/definitions/podsecurity.PodSecurityCapabilities'
      enabled:
        type: boolean
      endPointID:
        type: integer
      forbiddenSysctlsList:
        $ref: '#/definitions/podsecurity.PodSecurityForbiddenSysctlsList'
      hostFilesystem:
        $ref: '#/definitions/podsecurity.PodSecurityHostFilesystem'
      hostNamespaces:
        $ref: '#/definitions/podsecurity.PodSecurityHostNamespaces'
      hostPorts:
        $ref: '#/definitions/podsecurity.PodSecurityHostNetworkingPorts'
      id:
        type: integer
      privilegedContainers:
        $ref: '#/definitions/podsecurity.PodSecurityPrivilegedContainers'
      readOnlyRootFileSystem:
        $ref: '#/definitions/podsecurity.PodSecurityReadOnlyRootFileSystem'
      restrictDefaultNamespace:
        type: boolean
      restrictSecrets:
        type: boolean
      secComp:
        $ref: '#/definitions/podsecurity.PodSecuritySecComp'
      selinux:
        $ref: '#/definitions/podsecurity.PodSecuritySelinux'
      users:
        $ref: '#/definitions/podsecurity.PodSecurityUsers'
      volumeTypes:
        $ref: '#/definitions/podsecurity.PodSecurityVolumeTypes'
    type: object
  podsecurity.PodSecurityRunAsGroup:
    properties:
      idrange:
        items:
          $ref: '#/definitions/podsecurity.PodSecurityIdrange'
        type: array
      type:
        $ref: '#/definitions/podsecurity.RunAsGroupStrategy'
    type: object
  podsecurity.PodSecurityRunAsUser:
    properties:
      idrange:
        items:
          $ref: '#/definitions/podsecurity.PodSecurityIdrange'
        type: array
      type:
        $ref: '#/definitions/podsecurity.RunAsUserStrategy'
    type: object
  podsecurity.PodSecuritySecComp:
    properties:
      enabled:
        type: boolean
      secCompType:
        items:
          type: string
        type: array
    type: object
  podsecurity.PodSecuritySelinux:
    properties:
      allowedCapabilities:
        items:
          $ref: '#/definitions/podsecurity.PodSecurityAllowedCapabilities'
        type: array
      enabled:
        type: boolean
    type: object
  podsecurity.PodSecuritySupplementalGroups:
    properties:
      idrange:
        items:
          $ref: '#/definitions/podsecurity.PodSecurityIdrange'
        type: array
      type:
        $ref: '#/definitions/podsecurity.SupplementalGroupsStrategyType'
    type: object
  podsecurity.PodSecurityUsers:
    properties:
      enabled:
        type: boolean
      fsGroups:
        $ref: '#/definitions/podsecurity.PodSecurityFsGroups'
      runAsGroup:
        $ref: '#/definitions/podsecurity.PodSecurityRunAsGroup'
      runAsUser:
        $ref: '#/definitions/podsecurity.PodSecurityRunAsUser'
      supplementalGroups:
        $ref: '#/definitions/podsecurity.PodSecuritySupplementalGroups'
    type: object
  podsecurity.PodSecurityVolumeTypes:
    properties:
      allowedTypes:
        items:
          $ref: '#/definitions/podsecurity.FSType'
        type: array
      enabled:
        type: boolean
    type: object
  podsecurity.RunAsGroupStrategy:
    enum:
    - MayRunAs
    - MustRunAs
    - RunAsAny
    type: string
    x-enum-varnames:
    - RunAsGroupStrategyMayRunAs
    - RunAsGroupStrategyMustRunAs
    - RunAsGroupStrategyRunAsAny
  podsecurity.RunAsUserStrategy:
    enum:
    - MustRunAs
    - MustRunAsNonRoot
    - RunAsAny
    type: string
    x-enum-varnames:
    - RunAsUserStrategyMustRunAs
    - RunAsUserStrategyMustRunAsNonRoot
    - RunAsUserStrategyRunAsAny
  podsecurity.SupplementalGroupsStrategyType:
    enum:
    - MayRunAs
    - MustRunAs
    - RunAsAny
    type: string
    x-enum-varnames:
    - SupplementalGroupsStrategyMayRunAs
    - SupplementalGroupsStrategyMustRunAs
    - SupplementalGroupsStrategyRunAsAny
  policies.GenericPolicy:
    properties:
      CreatedAt:
        type: string
      Data:
        additionalProperties: {}
        type: object
      EnvironmentGroups:
        items:
          type: integer
        type: array
      EnvironmentType:
        enum:
        - kubernetes
        - docker
        - podman
        - swarm
        type: string
      Id:
        type: integer
      Name:
        type: string
      StatusBreakdown:
        allOf:
        - $ref: '#/definitions/policies.PolicyStatusBreakdown'
        description: |-
          StatusBreakdown is computed on-demand and returned in API responses.
          It is not persisted to the database.
      Type:
        allOf:
        - $ref: '#/definitions/policies.PolicyType'
        enum:
        - rbac-k8s
        - rbac-docker
        - security-k8s
        - security-docker
        - setup-k8s
        - setup-docker
        - registry-k8s
        - registry-docker
      UpdatedAt:
        type: string
    type: object
  policies.Policy:
    properties:
      CreatedAt:
        type: string
      EnvironmentGroups:
        items:
          type: integer
        type: array
      EnvironmentType:
        enum:
        - kubernetes
        - docker
        - podman
        - swarm
        type: string
      Id:
        type: integer
      Name:
        type: string
      StatusBreakdown:
        allOf:
        - $ref: '#/definitions/policies.PolicyStatusBreakdown'
        description: |-
          StatusBreakdown is computed on-demand and returned in API responses.
          It is not persisted to the database.
      Type:
        allOf:
        - $ref: '#/definitions/policies.PolicyType'
        enum:
        - rbac-k8s
        - rbac-docker
        - security-k8s
        - security-docker
        - setup-k8s
        - setup-docker
        - registry-k8s
        - registry-docker
      UpdatedAt:
        type: string
    type: object
  policies.PolicyCategory:
    enum:
