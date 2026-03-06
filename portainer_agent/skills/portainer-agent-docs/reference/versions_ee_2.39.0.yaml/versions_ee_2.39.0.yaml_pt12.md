        description: Shadow to include the AuthType even if it's empty
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
  users.themePayload:
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
        example: false
        type: boolean
    type: object
  users.userAccessTokenCreatePayload:
    properties:
      description:
        example: github-api-key
        type: string
      password:
        example: password
        type: string
    required:
    - description
    - password
    type: object
  users.userCreatePayload:
    properties:
      Password:
        example: cg9Wgky3
        type: string
      Role:
        allOf:
        - $ref: '#/definitions/portainer.UserRole'
        description: |-
          User role
          1 = administrator account
          2 = regular account
        enum:
        - 1
        - 2
        example: 1
      Username:
        example: bob
        type: string
    required:
    - Password
    - Role
    - Username
    type: object
  users.userGitCredentialCreatePayload:
    properties:
      authorizationType:
        $ref: '#/definitions/gittypes.GitCredentialAuthType'
      name:
        example: my-credential
        type: string
      password:
        type: string
      username:
        type: string
    required:
    - authorizationType
    - name
    - password
    - username
    type: object
  users.userUpdatePasswordPayload:
    properties:
      NewPassword:
        description: New Password
        example: new_passwd
        type: string
      Password:
        description: Current Password
        example: passwd
        type: string
    required:
    - NewPassword
    - Password
    type: object
  users.userUpdatePayload:
    properties:
      NewPassword:
        example: asfj2emv
        type: string
      Password:
        example: cg9Wgky3
        type: string
      Role:
        allOf:
        - $ref: '#/definitions/portainer.UserRole'
        description: |-
          User role
          1 = administrator account
          2 = regular account
          3 = edge administrator account
        enum:
        - 1
        - 2
        - 3
        example: 2
      Theme:
        $ref: '#/definitions/users.themePayload'
      UseCache:
        example: true
        type: boolean
      Username:
        example: bob
        type: string
    required:
    - NewPassword
    - Password
    - Role
    - UseCache
    - Username
    type: object
  v1.AppArmorProfile:
    properties:
      localhostProfile:
        description: |-
          localhostProfile indicates a profile loaded on the node that should be used.
          The profile must be preconfigured on the node to work.
          Must match the loaded name of the profile.
          Must be set if and only if type is "Localhost".
          +optional
        type: string
      type:
        allOf:
        - $ref: '#/definitions/v1.AppArmorProfileType'
        description: |-
          type indicates which kind of AppArmor profile will be applied.
          Valid options are:
            Localhost - a profile pre-loaded on the node.
            RuntimeDefault - the container runtime's default profile.
            Unconfined - no AppArmor enforcement.
          +unionDiscriminator
    type: object
  v1.AppArmorProfileType:
    enum:
    - Unconfined
    - RuntimeDefault
    - Localhost
    type: string
    x-enum-varnames:
    - AppArmorProfileTypeUnconfined
    - AppArmorProfileTypeRuntimeDefault
    - AppArmorProfileTypeLocalhost
  v1.CSIPersistentVolumeSource:
    properties:
      controllerExpandSecretRef:
        allOf:
        - $ref: '#/definitions/v1.SecretReference'
        description: |-
          controllerExpandSecretRef is a reference to the secret object containing
          sensitive information to pass to the CSI driver to complete the CSI
          ControllerExpandVolume call.
          This field is optional, and may be empty if no secret is required. If the
          secret object contains more than one secret, all secrets are passed.
          +optional
      controllerPublishSecretRef:
        allOf:
        - $ref: '#/definitions/v1.SecretReference'
        description: |-
          controllerPublishSecretRef is a reference to the secret object containing
          sensitive information to pass to the CSI driver to complete the CSI
          ControllerPublishVolume and ControllerUnpublishVolume calls.
          This field is optional, and may be empty if no secret is required. If the
          secret object contains more than one secret, all secrets are passed.
          +optional
      driver:
        description: |-
          driver is the name of the driver to use for this volume.
          Required.
        type: string
      fsType:
        description: |-
          fsType to mount. Must be a filesystem type supported by the host operating system.
          Ex. "ext4", "xfs", "ntfs".
          +optional
        type: string
      nodeExpandSecretRef:
        allOf:
        - $ref: '#/definitions/v1.SecretReference'
        description: |-
          nodeExpandSecretRef is a reference to the secret object containing
          sensitive information to pass to the CSI driver to complete the CSI
          NodeExpandVolume call.
          This field is optional, may be omitted if no secret is required. If the
          secret object contains more than one secret, all secrets are passed.
          +optional
      nodePublishSecretRef:
        allOf:
        - $ref: '#/definitions/v1.SecretReference'
        description: |-
          nodePublishSecretRef is a reference to the secret object containing
          sensitive information to pass to the CSI driver to complete the CSI
          NodePublishVolume and NodeUnpublishVolume calls.
          This field is optional, and may be empty if no secret is required. If the
          secret object contains more than one secret, all secrets are passed.
          +optional
      nodeStageSecretRef:
        allOf:
        - $ref: '#/definitions/v1.SecretReference'
        description: |-
          nodeStageSecretRef is a reference to the secret object containing sensitive
          information to pass to the CSI driver to complete the CSI NodeStageVolume
          and NodeStageVolume and NodeUnstageVolume calls.
          This field is optional, and may be empty if no secret is required. If the
          secret object contains more than one secret, all secrets are passed.
          +optional
      readOnly:
        description: |-
          readOnly value to pass to ControllerPublishVolumeRequest.
          Defaults to false (read/write).
          +optional
        type: boolean
      volumeAttributes:
        additionalProperties:
          type: string
        description: |-
          volumeAttributes of the volume to publish.
          +optional
        type: object
      volumeHandle:
        description: |-
          volumeHandle is the unique volume name returned by the CSI volume
          pluginâ€™s CreateVolume to refer to the volume on all subsequent calls.
          Required.
        type: string
    type: object
  v1.Capabilities:
    properties:
      add:
        description: |-
          Added capabilities
          +optional
          +listType=atomic
        items:
          type: string
        type: array
      drop:
        description: |-
          Removed capabilities
          +optional
          +listType=atomic
        items:
          type: string
        type: array
    type: object
  v1.ConfigMapEnvSource:
    properties:
      name:
        description: |-
          Name of the referent.
          This field is effectively required, but due to backwards compatibility is
          allowed to be empty. Instances of this type with an empty value here are
          almost certainly wrong.
          More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names
          +optional
          +default=""
          +kubebuilder:default=""
          TODO: Drop `kubebuilder:default` when controller-gen doesn't need it https://github.com/kubernetes-sigs/kubebuilder/issues/3896.
        type: string
      optional:
        description: |-
          Specify whether the ConfigMap must be defined
          +optional
        type: boolean
    type: object
  v1.ConfigMapKeySelector:
    properties:
      key:
        description: The key to select.
        type: string
      name:
        description: |-
          Name of the referent.
          This field is effectively required, but due to backwards compatibility is
          allowed to be empty. Instances of this type with an empty value here are
          almost certainly wrong.
          More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names
          +optional
          +default=""
          +kubebuilder:default=""
          TODO: Drop `kubebuilder:default` when controller-gen doesn't need it https://github.com/kubernetes-sigs/kubebuilder/issues/3896.
        type: string
      optional:
        description: |-
          Specify whether the ConfigMap or its key must be defined
          +optional
        type: boolean
    type: object
  v1.Container:
    properties:
      args:
        description: |-
          Arguments to the entrypoint.
          The container image's CMD is used if this is not provided.
          Variable references $(VAR_NAME) are expanded using the container's environment. If a variable
          cannot be resolved, the reference in the input string will be unchanged. Double $$ are reduced
          to a single $, which allows for escaping the $(VAR_NAME) syntax: i.e. "$$(VAR_NAME)" will
          produce the string literal "$(VAR_NAME)". Escaped references will never be expanded, regardless
          of whether the variable exists or not. Cannot be updated.
          More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell
          +optional
          +listType=atomic
        items:
          type: string
        type: array
      command:
        description: |-
          Entrypoint array. Not executed within a shell.
          The container image's ENTRYPOINT is used if this is not provided.
          Variable references $(VAR_NAME) are expanded using the container's environment. If a variable
          cannot be resolved, the reference in the input string will be unchanged. Double $$ are reduced
          to a single $, which allows for escaping the $(VAR_NAME) syntax: i.e. "$$(VAR_NAME)" will
          produce the string literal "$(VAR_NAME)". Escaped references will never be expanded, regardless
          of whether the variable exists or not. Cannot be updated.
          More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell
          +optional
          +listType=atomic
        items:
          type: string
        type: array
      env:
        description: |-
          List of environment variables to set in the container.
          Cannot be updated.
          +optional
          +patchMergeKey=name
          +patchStrategy=merge
          +listType=map
          +listMapKey=name
        items:
          $ref: '#/definitions/v1.EnvVar'
        type: array
      envFrom:
        description: |-
          List of sources to populate environment variables in the container.
          The keys defined within a source may consist of any printable ASCII characters except '='.
          When a key exists in multiple
          sources, the value associated with the last source will take precedence.
          Values defined by an Env with a duplicate key will take precedence.
          Cannot be updated.
          +optional
          +listType=atomic
        items:
          $ref: '#/definitions/v1.EnvFromSource'
        type: array
      image:
        description: |-
          Container image name.
          More info: https://kubernetes.io/docs/concepts/containers/images
          This field is optional to allow higher level config management to default or override
          container images in workload controllers like Deployments and StatefulSets.
          +optional
        type: string
      imagePullPolicy:
        allOf:
        - $ref: '#/definitions/v1.PullPolicy'
        description: |-
          Image pull policy.
          One of Always, Never, IfNotPresent.
          Defaults to Always if :latest tag is specified, or IfNotPresent otherwise.
          Cannot be updated.
          More info: https://kubernetes.io/docs/concepts/containers/images#updating-images
          +optional
      lifecycle:
        allOf:
        - $ref: '#/definitions/v1.Lifecycle'
        description: |-
          Actions that the management system should take in response to container lifecycle events.
          Cannot be updated.
          +optional
      livenessProbe:
        allOf:
        - $ref: '#/definitions/v1.Probe'
        description: |-
          Periodic probe of container liveness.
          Container will be restarted if the probe fails.
          Cannot be updated.
          More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes
          +optional
      name:
        description: |-
          Name of the container specified as a DNS_LABEL.
          Each container in a pod must have a unique name (DNS_LABEL).
          Cannot be updated.
        type: string
      ports:
        description: |-
          List of ports to expose from the container. Not specifying a port here
          DOES NOT prevent that port from being exposed. Any port which is
          listening on the default "0.0.0.0" address inside a container will be
          accessible from the network.
          Modifying this array with strategic merge patch may corrupt the data.
          For more information See https://github.com/kubernetes/kubernetes/issues/108255.
          Cannot be updated.
          +optional
          +patchMergeKey=containerPort
          +patchStrategy=merge
          +listType=map
          +listMapKey=containerPort
          +listMapKey=protocol
        items:
          $ref: '#/definitions/v1.ContainerPort'
        type: array
      readinessProbe:
        allOf:
        - $ref: '#/definitions/v1.Probe'
        description: |-
          Periodic probe of container service readiness.
          Container will be removed from service endpoints if the probe fails.
          Cannot be updated.
          More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes
          +optional
      resizePolicy:
        description: |-
          Resources resize policy for the container.
          +featureGate=InPlacePodVerticalScaling
          +optional
          +listType=atomic
        items:
          $ref: '#/definitions/v1.ContainerResizePolicy'
        type: array
      resources:
        allOf:
        - $ref: '#/definitions/v1.ResourceRequirements'
        description: |-
          Compute Resources required by this container.
          Cannot be updated.
          More info: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/
          +optional
      restartPolicy:
        allOf:
        - $ref: '#/definitions/v1.ContainerRestartPolicy'
        description: |-
          RestartPolicy defines the restart behavior of individual containers in a pod.
          This overrides the pod-level restart policy. When this field is not specified,
          the restart behavior is defined by the Pod's restart policy and the container type.
          Additionally, setting the RestartPolicy as "Always" for the init container will
          have the following effect:
          this init container will be continually restarted on
          exit until all regular containers have terminated. Once all regular
          containers have completed, all init containers with restartPolicy "Always"
          will be shut down. This lifecycle differs from normal init containers and
          is often referred to as a "sidecar" container. Although this init
          container still starts in the init container sequence, it does not wait
          for the container to complete before proceeding to the next init
          container. Instead, the next init container starts immediately after this
          init container is started, or after any startupProbe has successfully
          completed.
          +featureGate=SidecarContainers
          +optional
      restartPolicyRules:
        description: |-
          Represents a list of rules to be checked to determine if the
          container should be restarted on exit. The rules are evaluated in
          order. Once a rule matches a container exit condition, the remaining
          rules are ignored. If no rule matches the container exit condition,
          the Container-level restart policy determines the whether the container
          is restarted or not. Constraints on the rules:
          - At most 20 rules are allowed.
          - Rules can have the same action.
          - Identical rules are not forbidden in validations.
          When rules are specified, container MUST set RestartPolicy explicitly
          even it if matches the Pod's RestartPolicy.
          +featureGate=ContainerRestartRules
          +optional
          +listType=atomic
        items:
          $ref: '#/definitions/v1.ContainerRestartRule'
        type: array
      securityContext:
        allOf:
        - $ref: '#/definitions/v1.SecurityContext'
        description: |-
          SecurityContext defines the security options the container should be run with.
          If set, the fields of SecurityContext override the equivalent fields of PodSecurityContext.
          More info: https://kubernetes.io/docs/tasks/configure-pod-container/security-context/
          +optional
      startupProbe:
        allOf:
        - $ref: '#/definitions/v1.Probe'
        description: |-
          StartupProbe indicates that the Pod has successfully initialized.
          If specified, no other probes are executed until this completes successfully.
          If this probe fails, the Pod will be restarted, just as if the livenessProbe failed.
          This can be used to provide different probe parameters at the beginning of a Pod's lifecycle,
          when it might take a long time to load data or warm a cache, than during steady-state operation.
          This cannot be updated.
          More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes
          +optional
      stdin:
        description: |-
          Whether this container should allocate a buffer for stdin in the container runtime. If this
          is not set, reads from stdin in the container will always result in EOF.
          Default is false.
          +optional
        type: boolean
      stdinOnce:
        description: |-
          Whether the container runtime should close the stdin channel after it has been opened by
          a single attach. When stdin is true the stdin stream will remain open across multiple attach
          sessions. If stdinOnce is set to true, stdin is opened on container start, is empty until the
          first client attaches to stdin, and then remains open and accepts data until the client disconnects,
          at which time stdin is closed and remains closed until the container is restarted. If this
          flag is false, a container processes that reads from stdin will never receive an EOF.
          Default is false
          +optional
        type: boolean
      terminationMessagePath:
        description: |-
          Optional: Path at which the file to which the container's termination message
          will be written is mounted into the container's filesystem.
          Message written is intended to be brief final status, such as an assertion failure message.
          Will be truncated by the node if greater than 4096 bytes. The total message length across
          all containers will be limited to 12kb.
          Defaults to /dev/termination-log.
          Cannot be updated.
          +optional
        type: string
      terminationMessagePolicy:
        allOf:
        - $ref: '#/definitions/v1.TerminationMessagePolicy'
        description: |-
          Indicate how the termination message should be populated. File will use the contents of
          terminationMessagePath to populate the container status message on both success and failure.
          FallbackToLogsOnError will use the last chunk of container log output if the termination
          message file is empty and the container exited with an error.
          The log output is limited to 2048 bytes or 80 lines, whichever is smaller.
          Defaults to File.
          Cannot be updated.
          +optional
      tty:
        description: |-
          Whether this container should allocate a TTY for itself, also requires 'stdin' to be true.
          Default is false.
          +optional
        type: boolean
      volumeDevices:
        description: |-
          volumeDevices is the list of block devices to be used by the container.
          +patchMergeKey=devicePath
          +patchStrategy=merge
          +listType=map
          +listMapKey=devicePath
          +optional
        items:
          $ref: '#/definitions/v1.VolumeDevice'
        type: array
      volumeMounts:
        description: |-
          Pod volumes to mount into the container's filesystem.
          Cannot be updated.
          +optional
          +patchMergeKey=mountPath
          +patchStrategy=merge
          +listType=map
          +listMapKey=mountPath
        items:
          $ref: '#/definitions/v1.VolumeMount'
        type: array
      workingDir:
        description: |-
          Container's working directory.
          If not specified, the container runtime's default will be used, which
          might be configured in the container image.
          Cannot be updated.
          +optional
        type: string
    type: object
  v1.ContainerPort:
    properties:
      containerPort:
        description: |-
          Number of port to expose on the pod's IP address.
          This must be a valid port number, 0 < x < 65536.
        type: integer
      hostIP:
        description: |-
          What host IP to bind the external port to.
          +optional
        type: string
      hostPort:
        description: |-
          Number of port to expose on the host.
          If specified, this must be a valid port number, 0 < x < 65536.
          If HostNetwork is specified, this must match ContainerPort.
          Most containers do not need this.
          +optional
        type: integer
      name:
        description: |-
          If specified, this must be an IANA_SVC_NAME and unique within the pod. Each
          named port in a pod must have a unique name. Name for the port that can be
          referred to by services.
          +optional
        type: string
      protocol:
        allOf:
        - $ref: '#/definitions/v1.Protocol'
        description: |-
          Protocol for port. Must be UDP, TCP, or SCTP.
          Defaults to "TCP".
          +optional
          +default="TCP"
    type: object
  v1.ContainerResizePolicy:
    properties:
      resourceName:
        allOf:
        - $ref: '#/definitions/v1.ResourceName'
        description: |-
          Name of the resource to which this resource resize policy applies.
          Supported values: cpu, memory.
      restartPolicy:
        allOf:
        - $ref: '#/definitions/v1.ResourceResizeRestartPolicy'
        description: |-
          Restart policy to apply when specified resource is resized.
          If not specified, it defaults to NotRequired.
    type: object
  v1.ContainerRestartPolicy:
    enum:
    - Always
    - Never
    - OnFailure
    type: string
    x-enum-varnames:
    - ContainerRestartPolicyAlways
    - ContainerRestartPolicyNever
    - ContainerRestartPolicyOnFailure
  v1.ContainerRestartRule:
    properties:
      action:
        allOf:
        - $ref: '#/definitions/v1.ContainerRestartRuleAction'
        description: |-
          Specifies the action taken on a container exit if the requirements
          are satisfied. The only possible value is "Restart" to restart the
          container.
          +required
      exitCodes:
        allOf:
        - $ref: '#/definitions/v1.ContainerRestartRuleOnExitCodes'
        description: |-
          Represents the exit codes to check on container exits.
          +optional
          +oneOf=when
    type: object
  v1.ContainerRestartRuleAction:
    enum:
    - Restart
    type: string
    x-enum-varnames:
    - ContainerRestartRuleActionRestart
  v1.ContainerRestartRuleOnExitCodes:
    properties:
      operator:
        allOf:
        - $ref: '#/definitions/v1.ContainerRestartRuleOnExitCodesOperator'
