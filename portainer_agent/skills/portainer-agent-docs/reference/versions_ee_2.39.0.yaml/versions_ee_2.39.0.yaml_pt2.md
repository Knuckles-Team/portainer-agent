    properties:
      FileContent:
        type: string
    type: object
  edgejobs.edgeJobUpdatePayload:
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
  edgejobs.fileResponse:
    properties:
      FileContent:
        type: string
    type: object
  edgejobs.taskContainer:
    properties:
      EndpointId:
        type: integer
      EndpointName:
        type: string
      Id:
        type: string
      LogsStatus:
        $ref: '#/definitions/portainer.EdgeJobLogsStatus'
    type: object
  edgestacks.SummarizedStatus:
    enum:
    - Unavailable
    - Deploying
    - Failed
    - Paused
    - PartiallyRunning
    - Completed
    - Running
    type: string
    x-enum-varnames:
    - sumStatusUnavailable
    - sumStatusDeploying
    - sumStatusFailed
    - sumStatusPaused
    - sumStatusPartiallyRunning
    - sumStatusCompleted
    - sumStatusRunning
  edgestacks.deployerOptionsPayload:
    properties:
      Prune:
        type: boolean
      RemoveVolumes:
        type: boolean
    type: object
  edgestacks.edgeStackStaggerStatusResponse:
    properties:
      status:
        type: string
    type: object
  edgestacks.stackGitUpdatePayload:
    properties:
      Atomic:
        description: Enable automatic rollback on deployment failure (equivalent to
          helm --atomic flag)
        example: true
        type: boolean
      Authentication:
        $ref: '#/definitions/gittypes.GitAuthentication'
      AutoUpdate:
        $ref: '#/definitions/portainer.AutoUpdateSettings'
      DeployerOptions:
        allOf:
        - $ref: '#/definitions/edgestacks.deployerOptionsPayload'
        description: Options to control the deployer behaviour
      DeploymentType:
        $ref: '#/definitions/portainer.EdgeStackDeploymentType'
      EnvVars:
        items:
          $ref: '#/definitions/portainer.Pair'
        type: array
      GroupIds:
        items:
          type: integer
        type: array
      PrePullImage:
        type: boolean
      RePullImage:
        description: |-
          Deprecated(2.36): to be removed in future versions (2.44+)
          Use RepullImageAndRedeploy instead
        type: boolean
      RefName:
        type: string
      Registries:
        description: List of Registries to use for this stack
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
      StaggerConfig:
        allOf:
        - $ref: '#/definitions/portaineree.EdgeStaggerConfig'
        description: Configuration for stagger updates
      Timeout:
        description: Timeout for Helm operations (equivalent to helm --timeout flag)
        example: 5m0s
        type: string
      UpdateVersion:
        description: |-
          Update the stack file content from the git repository
          If this is set to true, it indicates that the stack is being redeployed (Pull and update stack),
          if it is false, it indicates that the stack is being updated (Update settings)
        type: boolean
      ValuesFiles:
        description: Array of paths to Helm values YAML files for Helm git deployments
        example:
        - '[''values/prod.yaml'''
        - ' ''values/secrets.yaml'']'
        items:
          type: string
        type: array
    type: object
  edgeupdateschedules.activeSchedulePayload:
    properties:
      EnvironmentIDs:
        items:
          type: integer
        type: array
    type: object
  edgeupdateschedules.createPayload:
    properties:
      AgentImage:
        description: default to "" == portainer/agent:<current_server_version>
        type: string
      GroupIDs:
        items:
          type: integer
        type: array
      Name:
        type: string
      RegistryID:
        description: default to 0 = dockerhub
        type: integer
      ScheduledTime:
        type: string
      Type:
        $ref: '#/definitions/types.UpdateScheduleType'
      UpdaterImage:
        description: default to "" == portainer/portainer-updater:<current_server_version>
        type: string
    type: object
  edgeupdateschedules.decoratedUpdateSchedule:
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
      scheduledTime:
        type: string
      status:
        $ref: '#/definitions/types.UpdateScheduleStatusType'
      statusMessage:
        type: string
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
  edgeupdateschedules.infoResponse:
    properties:
      HasLocalTimeZone:
        type: boolean
      HasNoLocalTimeZone:
        type: boolean
      MinAgentVersion:
        type: string
      OutdatedCount:
        type: integer
      UpToDateCount:
        type: integer
    type: object
  edgeupdateschedules.inspectResponse:
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
      environmentIds:
        items:
          type: integer
        type: array
      environmentsPreviousVersions:
        additionalProperties:
          type: string
        description: Deprecated - use Environment.Agent.PreviousVersion instead
        type: object
      id:
        description: EdgeUpdateSchedule Identifier
        example: 1
        type: integer
      isActive:
        type: boolean
      name:
        description: Name of the schedule
        example: Update Schedule
        type: string
      registryId:
        description: ID of registry
        example: 1
        type: integer
      scheduledTime:
        type: string
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
  edgeupdateschedules.updatePayload:
    properties:
      AgentImage:
        description: default to "" == portainer/agent:<current_server_version>
        type: string
      GroupIDs:
        items:
          type: integer
        type: array
      Name:
        type: string
      RegistryID:
        description: default to 0 = dockerhub
        type: integer
      ScheduledTime:
        type: string
      Type:
        $ref: '#/definitions/types.UpdateScheduleType'
      UpdaterImage:
        description: default to "" == portainer/portainer-updater:latest
        type: string
    type: object
  endpointedge.EdgeAsyncResponse:
    properties:
      commandInterval:
        type: integer
      commands:
        items:
          $ref: '#/definitions/portaineree.EdgeAsyncCommand'
        type: array
      endpointID:
        type: integer
      needFullSnapshot:
        type: boolean
      pingInterval:
        type: integer
      snapshotInterval:
        type: integer
    type: object
  endpointedge.edgeJobResponse:
    properties:
      CollectLogs:
        description: Whether to collect logs
        example: true
        type: boolean
      CronExpression:
        description: A cron expression to schedule this job
        example: '* * * * *'
        type: string
      Id:
        description: EdgeJob Identifier
        example: 2
        type: integer
      Script:
        description: Script to run
        example: echo hello
        type: string
      Version:
        description: Version of this EdgeJob
        example: 2
        type: integer
    type: object
  endpointedge.endpointEdgeStatusInspectResponse:
    properties:
      checkin:
        description: The current value of CheckinInterval
        example: 5
        type: integer
      credentials:
        type: string
      edge_configurations:
        additionalProperties:
          $ref: '#/definitions/portaineree.EdgeConfigStateType'
        description: Edge configurations associated to this environment(endpoint)
        type: object
      policy_chart_summaries:
        description: Helm charts to be installed on the environment(endpoint)
        items:
          $ref: '#/definitions/portainer.PolicyChartSummary'
        type: array
      port:
        description: The tunnel port
        example: 8732
        type: integer
      schedules:
        description: List of requests for jobs to run on the environment(endpoint)
        items:
          $ref: '#/definitions/endpointedge.edgeJobResponse'
        type: array
      stacks:
        description: List of stacks to be deployed on the environments(endpoints)
        items:
          $ref: '#/definitions/endpointedge.stackStatusResponse'
        type: array
      status:
        description: Status represents the environment(endpoint) status
        example: REQUIRED
        type: string
    type: object
  endpointedge.endpointGetChartsResponse:
    properties:
      policyChartBundles:
        items:
          $ref: '#/definitions/portainer.PolicyChartBundle'
        type: array
      restoreSettingsBundle:
        $ref: '#/definitions/portainer.RestoreSettingsBundle'
    type: object
  endpointedge.endpointTrustUpdateRelation:
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
  endpointedge.endpointsTrustPayload:
    properties:
      EndpointIDs:
        items:
          type: integer
        type: array
      Relations:
        additionalProperties:
          $ref: '#/definitions/endpointedge.endpointTrustUpdateRelation'
        type: object
    type: object
  endpointedge.generateKeyResponse:
    properties:
      edgeKey:
        type: string
    type: object
  endpointedge.stackStatusResponse:
    properties:
      ForceRedeploy:
        description: ForceRedeploy indicates whether the stack is force redeployed
        example: true
        type: boolean
      ID:
        description: EdgeStack Identifier
        example: 1
        type: integer
      ReadyRePullImage:
        description: |-
          Deprecated(2.36): use ForceRedeploy and RepullImage instead for cleaner responsibility
          But keep it for backward compatibility. To remove in future versions (2.44+)
          ReadyRePullImage indicates whether the stack is ready to re-pull image
        example: true
        type: boolean
      RepullImage:
        description: RepullImage indicates whether the stack's images should be repulled
        example: true
        type: boolean
      Version:
        description: Version of this stack
        example: 3
        type: integer
    type: object
  endpointgroups.decoratedEndpointGroup:
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
      Policies:
        items:
          $ref: '#/definitions/policies.GenericPolicy'
        type: array
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
  endpointgroups.endpointGroupCreatePayload:
    properties:
      AssociatedEndpoints:
        description: List of environment(endpoint) identifiers that will be part of
          this group
        example:
        - 1
        - 3
        items:
          type: integer
        type: array
      Description:
        description: Environment(Endpoint) group description
        example: description
        type: string
      Name:
        description: Environment(Endpoint) group name
        example: my-Environment-group
        type: string
      TagIDs:
        description: List of tag identifiers to which this environment(endpoint) group
          is associated
        example:
        - 1
        - 2
        items:
          type: integer
        type: array
    required:
    - Name
    type: object
  endpointgroups.endpointGroupResponse:
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
      Policies:
        items:
          $ref: '#/definitions/policies.GenericPolicy'
        type: array
      Size:
        type: integer
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
  endpointgroups.endpointGroupUpdatePayload:
    properties:
      AssociatedEndpoints:
        description: List of environment(endpoint) identifiers that will be part of
          this group
        example:
        - 1
        - 3
        items:
          type: integer
        type: array
      Description:
        description: Environment(Endpoint) group description
        example: description
        type: string
      Name:
        description: Environment(Endpoint) group name
        example: my-environment-group
        type: string
      TagIDs:
        description: List of tag identifiers associated to the environment(endpoint)
          group
        example:
        - 3
        - 4
        items:
          type: integer
        type: array
      TeamAccessPolicies:
        $ref: '#/definitions/portainer.TeamAccessPolicies'
      UserAccessPolicies:
        $ref: '#/definitions/portainer.UserAccessPolicies'
    type: object
  endpoints.dockerhubStatusResponse:
    properties:
      limit:
        description: Daily limit
        type: integer
      remaining:
        description: Remaiming images to pull
        type: integer
    type: object
  endpoints.endpointCreateGlobalKeyResponse:
    properties:
      endpointID:
        type: integer
    type: object
  endpoints.endpointDeleteBatchPartialResponse:
    properties:
      deleted:
        items:
          type: integer
        type: array
      errors:
        items:
          type: integer
        type: array
    type: object
  endpoints.endpointDeleteBatchPayload:
    properties:
      endpoints:
        items:
          $ref: '#/definitions/endpoints.endpointDeleteRequest'
        type: array
    type: object
  endpoints.endpointDeleteRequest:
    properties:
      deleteCluster:
        type: boolean
      id:
        type: integer
    type: object
  endpoints.endpointMTLSCertResponse:
    properties:
      MTLSCertificate:
        allOf:
        - $ref: '#/definitions/ssl.Certificate'
        description: MTLSCertificate is the X.509 Certificate of the MTLS Certificate
    type: object
  endpoints.endpointSettingsUpdatePayload:
    properties:
      changeWindow:
        allOf:
        - $ref: '#/definitions/portaineree.EndpointChangeWindow'
        description: Whether GitOps update time restrictions are enabled
      deploymentOptions:
        allOf:
        - $ref: '#/definitions/portaineree.DeploymentOptions'
        description: Hide manual deployment forms for an environment
      enableGPUManagement:
        example: false
        type: boolean
      enableImageNotification:
        example: true
        type: boolean
      gpus:
        items:
          $ref: '#/definitions/portainer.Pair'
        type: array
      securitySettings:
        description: Security settings updates
        properties:
          allowBindMountsForRegularUsers:
            description: Whether non-administrator should be able to use bind mounts
              when creating containers
            example: false
            type: boolean
          allowContainerCapabilitiesForRegularUsers:
            description: Whether non-administrator should be able to use container
              capabilities
            example: true
            type: boolean
          allowDeviceMappingForRegularUsers:
            description: Whether non-administrator should be able to use device mapping
            example: true
            type: boolean
          allowHostNamespaceForRegularUsers:
            description: Whether non-administrator should be able to use the host
              pid
            example: true
            type: boolean
          allowPrivilegedModeForRegularUsers:
            description: Whether non-administrator should be able to use privileged
              mode when creating containers
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
    type: object
  endpoints.endpointUpdatePayload:
    properties:
      AzureApplicationID:
        description: Azure application ID
        example: eag7cdo9-o09l-9i83-9dO9-f0b23oe78db4
        type: string
      AzureAuthenticationKey:
        description: Azure authentication key
        example: cOrXoK/1D35w8YQ8nH1/8ZGwzz45JIYD5jxHKXEQknk=
        type: string
      AzureTenantID:
        description: Azure tenant ID
        example: 34ddc78d-4fel-2358-8cc1-df84c8o839f5
        type: string
      ChangeWindow:
        allOf:
        - $ref: '#/definitions/portaineree.EndpointChangeWindow'
        description: Whether GitOps update time restrictions are enabled
      DeploymentOptions:
        allOf:
        - $ref: '#/definitions/portaineree.DeploymentOptions'
        description: Hide manual deployment forms for an environment
      Edge:
        properties:
          CommandInterval:
            description: The command list interval for edge agent - used in edge async
              mode (in seconds)
            example: 5
            type: integer
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
        type: object
      EdgeCheckinInterval:
        description: The check in interval for edge agent (in seconds)
        example: 5
        type: integer
      Gpus:
        description: GPUs information
        items:
          $ref: '#/definitions/portainer.Pair'
        type: array
      GroupID:
        description: Group identifier
        example: 1
        type: integer
      IsSetStatusMessage:
        type: boolean
      Kubernetes:
        allOf:
        - $ref: '#/definitions/portaineree.KubernetesData'
        description: Associated Kubernetes data
      Name:
        description: Name that will be used to identify this environment(endpoint)
        example: my-environment
        type: string
      PublicURL:
        description: |-
          URL or IP address where exposed containers will be reachable.\
          Defaults to URL if not specified
        example: docker.mydomain.tld:2375
        type: string
      Status:
        description: The status of the environment(endpoint) (1 - up, 2 - down)
        example: 1
        type: integer
      StatusMessage:
        properties:
          Detail:
            example: Error message
            type: string
          Summary:
            example: Error
            type: string
          operation:
            description: '''scale'', ''upgrade'', ''addons'''
            example: scale
            type: string
          operationStatus:
            allOf:
            - $ref: '#/definitions/portaineree.EndpointOperationStatus'
            description: ''''', ''error'', ''processing'''
            example: error
        type: object
      TLS:
        description: Require TLS to connect against this environment(endpoint)
        example: true
        type: boolean
      TLSSkipClientVerify:
        description: Skip client verification when using TLS
        example: false
        type: boolean
      TLSSkipVerify:
        description: Skip server verification when using TLS
        example: false
        type: boolean
      TagIDs:
        description: List of tag identifiers to which this environment(endpoint) is
          associated
        example:
