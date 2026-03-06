          Stack.HelmValuesFiles)
        example:
        - '["values/base.yaml"'
        - '"values/prod.yaml"]'
        items:
          type: string
        type: array
    required:
    - repository
    - valuesFiles
    type: object
  gitops.helmValuesPreviewResponse:
    properties:
      commitHash:
        type: string
      filesProcessed:
        items:
          type: string
        type: array
      mergedValues:
        type: string
    type: object
  gitops.repositoryFilePreviewPayload:
    properties:
      TLSSkipVerify:
        description: TLSSkipVerify skips SSL verification when cloning the Git repository
        example: false
        type: boolean
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
        example: refs/heads/master
        type: string
      repository:
        example: https://github.com/openfaas/faas
        type: string
      targetFile:
        description: Path to file whose content will be read
        example: docker-compose.yml
        type: string
      username:
        example: myGitUsername
        type: string
    required:
    - repository
    type: object
  gitops.repositoryFileSearchPayload:
    properties:
      TLSSkipVerify:
        description: TLSSkipVerify skips SSL verification when cloning the Git repository
        example: false
        type: boolean
      authorizationType:
        allOf:
        - $ref: '#/definitions/gittypes.GitCredentialAuthType'
        example: 0
      createdFromCustomTemplateID:
        type: integer
      dirOnly:
        description: DirOnly List directories only
        example: false
        type: boolean
      gitCredentialID:
        type: integer
      include:
        description: Allow to provide specific file extension as the search result.
          If empty, the file extensions yml,yaml,hcl,json will be set by default
        example: json,yml
        type: string
      keyword:
        description: Partial or completed file name. If empty, all filenames with
          included extensions will be returned
        example: docker-compose
        type: string
      password:
        type: string
      reference:
        description: Specific Git repository reference. If empty, the reference ref/heads/main
          will be set by default
        example: refs/heads/develop
        type: string
      repository:
        type: string
      username:
        type: string
    required:
    - repository
    type: object
  gitops.repositoryReferenceListPayload:
    properties:
      TLSSkipVerify:
        description: TLSSkipVerify skips SSL verification when cloning the Git repository
        example: false
        type: boolean
      authorizationType:
        allOf:
        - $ref: '#/definitions/gittypes.GitCredentialAuthType'
        example: 0
      createdFromCustomTemplateID:
        type: integer
      gitCredentialID:
        type: integer
      password:
        type: string
      repository:
        type: string
      stackID:
        type: integer
      username:
        type: string
    required:
    - repository
    type: object
  gittypes.GitAuthentication:
    properties:
      AuthorizationType:
        $ref: '#/definitions/gittypes.GitCredentialAuthType'
      GitCredentialID:
        description: |-
          Git credentials identifier when the value is not 0
          When the value is 0, Username, Password, and Authtype are set without using saved credential
          This is introduced since 2.15.0
        example: 0
        type: integer
      Password:
        type: string
      Username:
        type: string
    type: object
  gittypes.GitCredentialAuthType:
    enum:
    - 0
    - 1
    type: integer
    x-enum-varnames:
    - GitCredentialAuthType_Basic
    - GitCredentialAuthType_Token
  gittypes.RepoConfig:
    properties:
      Authentication:
        allOf:
        - $ref: '#/definitions/gittypes.GitAuthentication'
        description: Git credentials
      ConfigFilePath:
        description: Path to where the config file is in this url/refName
        example: docker-compose.yml
        type: string
      ConfigHash:
        description: Repository hash
        example: bc4c183d756879ea4d173315338110b31004b8e0
        type: string
      ReferenceName:
        description: The reference name
        example: refs/heads/branch_name
        type: string
      TLSSkipVerify:
        description: TLSSkipVerify skips SSL verification when cloning the Git repository
        example: false
        type: boolean
      URL:
        description: The repo url
        example: https://github.com/portainer/portainer.git
        type: string
    type: object
  helm.gitHelmDryRunPayload:
    properties:
      helmChartPath:
        type: string
      helmValuesFiles:
        items:
          type: string
        type: array
      name:
        type: string
      namespace:
        type: string
      repositoryAuthentication:
        type: boolean
      repositoryAuthorizationType:
        $ref: '#/definitions/gittypes.GitCredentialAuthType'
      repositoryGitCredentialID:
        type: integer
      repositoryPassword:
        type: string
      repositoryReferenceName:
        type: string
      repositoryURL:
        type: string
      repositoryUsername:
        type: string
      tlsSkipVerify:
        type: boolean
    type: object
  helm.installChartPayload:
    properties:
      atomic:
        type: boolean
      chart:
        type: string
      name:
        type: string
      namespace:
        type: string
      registryId:
        type: integer
      repo:
        type: string
      values:
        type: string
      version:
        type: string
    type: object
  images.ImageResponse:
    properties:
      created:
        type: integer
      id:
        type: string
      nodeName:
        type: string
      size:
        type: integer
      tags:
        items:
          type: string
        type: array
      used:
        description: |-
          Used is true if the image is used by at least one container
          supplied only when withUsage is true
        type: boolean
    type: object
  images.StatusResponse:
    properties:
      Message:
        type: string
      Status:
        $ref: '#/definitions/github_com_portainer_portainer-ee_api_docker_images.Status'
    type: object
  intstr.IntOrString:
    properties:
      IntVal:
        type: integer
      StrVal:
        type: string
      Type:
        $ref: '#/definitions/intstr.Type'
    type: object
  intstr.Type:
    enum:
    - 0
    - 1
    type: integer
    x-enum-comments:
      Int: The IntOrString holds an int.
      String: The IntOrString holds a string.
    x-enum-varnames:
    - Int
    - String
  k8s_io_api_core_v1.ConditionStatus:
    enum:
    - "True"
    - "False"
    - Unknown
    type: string
    x-enum-varnames:
    - ConditionTrue
    - ConditionFalse
    - ConditionUnknown
  k8s_io_api_core_v1.ResourceClaim:
    properties:
      name:
        description: |-
          Name must match the name of one entry in pod.spec.resourceClaims of
          the Pod where this field is used. It makes that resource available
          inside a container.
        type: string
      request:
        description: |-
          Request is the name chosen for a request in the referenced claim.
          If empty, everything from the claim is made available, otherwise
          only the result of this request.

          +optional
        type: string
    type: object
  k8s_io_api_rbac_v1.Subject:
    properties:
      apiGroup:
        description: |-
          APIGroup holds the API group of the referenced subject.
          Defaults to "" for ServiceAccount subjects.
          Defaults to "rbac.authorization.k8s.io" for User and Group subjects.
          +optional
        type: string
      kind:
        description: |-
          Kind of object being referenced. Values defined by this API group are "User", "Group", and "ServiceAccount".
          If the Authorizer does not recognized the kind value, the Authorizer should report an error.
        type: string
      name:
        description: Name of the object being referenced.
        type: string
      namespace:
        description: |-
          Namespace of the referenced object.  If the object kind is non-namespace, such as "User" or "Group", and this value is not empty
          the Authorizer should report an error.
          +optional
        type: string
    type: object
  kubernetes.Configuration:
    properties:
      ConfigurationOwner:
        type: string
      Data:
        additionalProperties: {}
        type: object
      Kind:
        type: string
    type: object
  kubernetes.CustomResourceMetadata:
    properties:
      apiVersion:
        type: string
      kind:
        type: string
      name:
        type: string
      plural:
        type: string
      scope:
        type: string
    type: object
  kubernetes.IngressRule:
    properties:
      Host:
        type: string
      IP:
        type: string
      Path:
        type: string
      TLS:
        items:
          $ref: '#/definitions/kubernetes.TLSInfo'
        type: array
    type: object
  kubernetes.K8sApplication:
    properties:
      Annotations:
        additionalProperties:
          type: string
        type: object
      ApplicationOwner:
        type: string
      ApplicationType:
        type: string
      Configurations:
        items:
          $ref: '#/definitions/kubernetes.Configuration'
        type: array
      Containers:
        items: {}
        type: array
      CreationDate:
        type: string
      CustomResourceMetadata:
        $ref: '#/definitions/kubernetes.CustomResourceMetadata'
      DeploymentType:
        type: string
      Id:
        type: string
      Image:
        type: string
      Kind:
        type: string
      Labels:
        additionalProperties:
          type: string
        type: object
      LoadBalancerIPAddress:
        type: string
      MatchLabels:
        additionalProperties:
          type: string
        type: object
      Metadata:
        $ref: '#/definitions/kubernetes.Metadata'
      Name:
        type: string
      Namespace:
        type: string
      Pods:
        items:
          $ref: '#/definitions/kubernetes.Pod'
        type: array
      PublishedPorts:
        items:
          $ref: '#/definitions/kubernetes.PublishedPort'
        type: array
      Resource:
        $ref: '#/definitions/kubernetes.K8sApplicationResource'
      ResourcePool:
        type: string
      RunningPodsCount:
        type: integer
      ServiceId:
        type: string
      ServiceName:
        type: string
      ServiceType:
        type: string
      StackId:
        type: string
      StackKind:
        type: string
      StackName:
        type: string
      Status:
        type: string
      TotalPodsCount:
        type: integer
      Uid:
        type: string
    type: object
  kubernetes.K8sApplicationResource:
    properties:
      CpuLimit:
        type: number
      CpuRequest:
        type: number
      MemoryLimit:
        type: integer
      MemoryRequest:
        type: integer
    type: object
  kubernetes.K8sClusterRole:
    properties:
      creationDate:
        type: string
      isSystem:
        type: boolean
      name:
        type: string
      uid:
        type: string
    type: object
  kubernetes.K8sClusterRoleBinding:
    properties:
      creationDate:
        type: string
      isSystem:
        type: boolean
      name:
        type: string
      namespace:
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
  kubernetes.K8sCronJob:
    properties:
      Command:
        type: string
      Id:
        type: string
      IsSystem:
        type: boolean
      Jobs:
        items:
          $ref: '#/definitions/kubernetes.K8sJob'
        type: array
      Name:
        type: string
      Namespace:
        type: string
      Schedule:
        type: string
      Suspend:
        type: boolean
      Timezone:
        type: string
    type: object
  kubernetes.K8sCronJobDeleteRequests:
    additionalProperties:
      items:
        type: string
      type: array
    type: object
  kubernetes.K8sEvent:
    properties:
      count:
        type: integer
      eventTime:
        type: string
      firstTimestamp:
        type: string
      involvedObject:
        $ref: '#/definitions/kubernetes.K8sEventInvolvedObject'
      kind:
        type: string
      lastTimestamp:
        type: string
      message:
        type: string
      name:
        type: string
      namespace:
        type: string
      reason:
        type: string
      type:
        type: string
      uid:
        type: string
    type: object
  kubernetes.K8sEventInvolvedObject:
    properties:
      kind:
        type: string
      name:
        type: string
      namespace:
        type: string
      uid:
        type: string
    type: object
  kubernetes.K8sJob:
    properties:
      BackoffLimit:
        type: integer
      Command:
        type: string
      Completions:
        type: integer
      Container:
        $ref: '#/definitions/v1.Container'
      Duration:
        type: string
      FailedReason:
        type: string
      FinishTime:
        type: string
      Id:
        type: string
      IsSystem:
        type: boolean
      Name:
        type: string
      Namespace:
        type: string
      PodName:
        type: string
      StartTime:
        type: string
      Status:
        type: string
    type: object
  kubernetes.K8sJobDeleteRequests:
    additionalProperties:
      items:
        type: string
      type: array
    type: object
  kubernetes.K8sPersistentVolume:
    properties:
      accessModes:
        items:
          $ref: '#/definitions/v1.PersistentVolumeAccessMode'
        type: array
      annotations:
        additionalProperties:
          type: string
        type: object
      capacity:
        $ref: '#/definitions/v1.ResourceList'
      claimRef:
        $ref: '#/definitions/v1.ObjectReference'
      csi:
        $ref: '#/definitions/v1.CSIPersistentVolumeSource'
      name:
        type: string
      persistentVolumeReclaimPolicy:
        $ref: '#/definitions/v1.PersistentVolumeReclaimPolicy'
      storageClassName:
        type: string
      volumeMode:
        $ref: '#/definitions/v1.PersistentVolumeMode'
    type: object
  kubernetes.K8sPersistentVolumeClaim:
    properties:
      accessModes:
        items:
          $ref: '#/definitions/v1.PersistentVolumeAccessMode'
        type: array
      creationDate:
        type: string
      id:
        type: string
      labels:
        additionalProperties:
          type: string
        type: object
      name:
        type: string
      namespace:
        type: string
      owningApplications:
        items:
          $ref: '#/definitions/kubernetes.K8sApplication'
        type: array
      phase:
        $ref: '#/definitions/v1.PersistentVolumeClaimPhase'
      resourcesRequests:
        $ref: '#/definitions/v1.ResourceList'
      storage:
        type: integer
      storageClass:
        type: string
      volumeMode:
        $ref: '#/definitions/v1.PersistentVolumeMode'
      volumeName:
        type: string
    type: object
  kubernetes.K8sServiceAccount:
    properties:
      creationDate:
        type: string
      isSystem:
        type: boolean
      name:
        type: string
      namespace:
        type: string
      uid:
        type: string
    type: object
  kubernetes.K8sServiceAccountDeleteRequests:
    additionalProperties:
      items:
        type: string
      type: array
    type: object
  kubernetes.K8sStorageClass:
    properties:
      allowVolumeExpansion:
        type: boolean
      name:
        type: string
      provisioner:
        type: string
      reclaimPolicy:
        $ref: '#/definitions/v1.PersistentVolumeReclaimPolicy'
    type: object
  kubernetes.K8sVolumeInfo:
    properties:
      persistentVolume:
        $ref: '#/definitions/kubernetes.K8sPersistentVolume'
      persistentVolumeClaim:
        $ref: '#/definitions/kubernetes.K8sPersistentVolumeClaim'
      storageClass:
        $ref: '#/definitions/kubernetes.K8sStorageClass'
    type: object
  kubernetes.Metadata:
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
  kubernetes.Pod:
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
      Resource:
        $ref: '#/definitions/kubernetes.K8sApplicationResource'
      Status:
        type: string
      Uid:
        type: string
    type: object
  kubernetes.PublishedPort:
    properties:
      IngressRules:
        items:
          $ref: '#/definitions/kubernetes.IngressRule'
        type: array
      Port:
        type: integer
    type: object
  kubernetes.TLSInfo:
    properties:
      hosts:
        items:
          type: string
        type: array
    type: object
  ldap.adminGroupsPayload:
    properties:
      LDAPSettings:
        $ref: '#/definitions/portaineree.LDAPSettings'
    type: object
  ldap.checkPayload:
    properties:
      LDAPSettings:
        $ref: '#/definitions/portaineree.LDAPSettings'
    type: object
  ldap.groupsPayload:
    properties:
      LDAPSettings:
        $ref: '#/definitions/portaineree.LDAPSettings'
    type: object
  ldap.testLoginPayload:
    properties:
      LDAPSettings:
        $ref: '#/definitions/portaineree.LDAPSettings'
      Password:
        type: string
      Username:
        type: string
    type: object
  ldap.testLoginResponse:
    properties:
      valid:
        type: boolean
    type: object
  ldap.usersPayload:
    properties:
      LDAPSettings:
        $ref: '#/definitions/portaineree.LDAPSettings'
    type: object
  liblicense.PortainerLicense:
    properties:
      company:
        type: string
      created:
        type: integer
      email:
        type: string
      expiresAfter:
        type: integer
      expiresAt:
        type: integer
      firstCheckin:
        type: integer
      id:
        type: string
      lastCheckin:
        type: integer
      licenseKey:
        type: string
      multiCheckinCount:
        type: integer
      multiuseInstancesCount:
        type: integer
      nodes:
        type: integer
      productEdition:
        allOf:
        - $ref: '#/definitions/liblicense.ProductEdition'
        description: |-
          ProductEdition was created originally with plans on having a
          seperate portainer product for Enterprise users and Business users
          with differing features. This didn't wind up coming about, but may
          still serve useful in the future if we need to issue keys for a
          different product entirely.
          Originally, the ProductEdition was used as the prefix for generating
          license keys, but in practice most people thought it was the
          "version" due to us having the original extension licenses which can
          be thought of as the true version 1 licenses.
      redisRef:
        type: string
      reference:
        type: string
      revoked:
        type: boolean
      revokedAt:
        type: integer
      type:
        allOf:
        - $ref: '#/definitions/liblicense.PortainerLicenseType'
        description: |-
          Type is used to distinguish different kinds of licenses, trial
          licenses, enterprise subscriptions
      uniqueId:
        type: string
      version:
        description: |-
          Version indicates which key should be used to encode/decode the
          license string.
        type: integer
    type: object
  liblicense.PortainerLicenseType:
    enum:
    - 0
    - 1
    - 2
    - 3
    - 4
    - 5
    type: integer
    x-enum-varnames:
    - _
    - PortainerLicenseTrial
    - PortainerLicenseSubscription
    - PortainerLicenseFree
    - PortainerLicensePersonal
    - PortainerLicenseStarter
  liblicense.ProductEdition:
    enum:
    - 0
    - 1
    - 2
    - 3
    type: integer
    x-enum-varnames:
    - _
    - PortainerCE
    - PortainerBE
    - PortainerEE
  licenses.LicenseInfo:
    properties:
      company:
        type: string
      enforcedAt:
        type: integer
      expiresAt:
        type: integer
      nodes:
        type: integer
      overuseStartedTimestamp:
        description: unix timestamp when node usage exceeded available license limit
        type: integer
      type:
        $ref: '#/definitions/liblicense.PortainerLicenseType'
      valid:
        type: boolean
    type: object
  licenses.attachPayload:
    properties:
      key:
        type: string
    type: object
  licenses.attachResponse:
    properties:
      conflictingKeys:
        items:
          type: string
        type: array
    type: object
  licenses.deletePayload:
    properties:
      LicenseKeys:
        description: List of license keys to remove
        items:
          type: string
        type: array
    type: object
  models.CloudCredential:
    properties:
      created:
        example: 1650000000
        type: integer
      credentials:
        $ref: '#/definitions/models.CloudCredentialMap'
      id:
        example: 1
        type: integer
      name:
        example: test-env
        type: string
      provider:
        example: aws
        type: string
    type: object
  models.CloudCredentialMap:
    additionalProperties:
      type: string
    type: object
  models.Configuration:
    properties:
      ConfigurationOwner:
        type: string
      Data:
        additionalProperties: {}
        type: object
      Kind:
        type: string
    type: object
  models.IngressRule:
    properties:
      Host:
        type: string
      IP:
        type: string
      Path:
        type: string
      TLS:
        items:
          $ref: '#/definitions/models.TLSInfo'
        type: array
    type: object
  models.K8sApplication:
    properties:
      Annotations:
        additionalProperties:
          type: string
        type: object
      ApplicationOwner:
        type: string
      ApplicationType:
        type: string
      Configurations:
        items:
          $ref: '#/definitions/models.Configuration'
        type: array
      Containers:
        items: {}
        type: array
      CreationDate:
        type: string
      DeploymentType:
        type: string
      Id:
        type: string
      Image:
        type: string
      Kind:
        type: string
      Labels:
        additionalProperties:
          type: string
        type: object
      LoadBalancerIPAddress:
        type: string
      MatchLabels:
        additionalProperties:
          type: string
        type: object
      Metadata:
        $ref: '#/definitions/models.Metadata'
      Name:
        type: string
      Namespace:
        type: string
      Pods:
        items:
          $ref: '#/definitions/models.Pod'
        type: array
      PublishedPorts:
        items:
          $ref: '#/definitions/models.PublishedPort'
        type: array
      Resource:
        $ref: '#/definitions/models.K8sApplicationResource'
      ResourcePool:
        type: string
      RunningPodsCount:
        type: integer
      ServiceId:
        type: string
      ServiceName:
        type: string
      ServiceType:
        type: string
      StackId:
        type: string
      StackName:
        type: string
      Status:
        type: string
      TotalPodsCount:
        type: integer
      Uid:
        type: string
    type: object
  models.K8sApplicationResource:
    properties:
      CpuLimit:
        type: number
      CpuRequest:
        type: number
      MemoryLimit:
        type: integer
      MemoryRequest:
        type: integer
    type: object
  models.K8sConfigMap:
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
      UID:
        type: string
    type: object
  models.K8sConfigurationOwnerResource:
    properties:
      Id:
        type: string
      Name:
        type: string
      ResourceKind:
        type: string
    type: object
  models.K8sCustomResource:
    properties:
      creationDate:
        type: string
      definitionName:
        type: string
      name:
        type: string
      namespace:
        type: string
      uid:
        type: string
    type: object
