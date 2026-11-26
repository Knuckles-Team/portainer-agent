        description: |-
          Represents the relationship between the container exit code(s) and the
          specified values. Possible values are:
          - In: the requirement is satisfied if the container exit code is in the
            set of specified values.
          - NotIn: the requirement is satisfied if the container exit code is
            not in the set of specified values.
          +required
      values:
        description: |-
          Specifies the set of values to check for container exit codes.
          At most 255 elements are allowed.
          +optional
          +listType=set
        items:
          type: integer
        type: array
    type: object
  v1.ContainerRestartRuleOnExitCodesOperator:
    enum:
    - In
    - NotIn
    type: string
    x-enum-varnames:
    - ContainerRestartRuleOnExitCodesOpIn
    - ContainerRestartRuleOnExitCodesOpNotIn
  v1.Descriptor:
    properties:
      annotations:
        additionalProperties:
          type: string
        description: Annotations contains arbitrary metadata relating to the targeted
          content.
        type: object
      artifactType:
        description: ArtifactType is the IANA media type of this artifact.
        type: string
      data:
        description: |-
          Data is an embedding of the targeted content. This is encoded as a base64
          string when marshalled to JSON (automatically, by encoding/json). If
          present, Data can be used directly to avoid fetching the targeted content.
        items:
          type: integer
        type: array
      digest:
        description: Digest is the digest of the targeted content.
        type: string
      mediaType:
        description: MediaType is the media type of the object this schema refers
          to.
        type: string
      platform:
        allOf:
        - $ref: '#/definitions/v1.Platform'
        description: |-
          Platform describes the platform which the image in the manifest runs on.

          This should only be used when referring to a manifest.
      size:
        description: Size specifies the size in bytes of the blob.
        type: integer
      urls:
        description: URLs specifies a list of URLs from which this object MAY be downloaded
        items:
          type: string
        type: array
    type: object
  v1.Duration:
    properties:
      time.Duration:
        enum:
        - -9223372036854775808
        - 9223372036854775807
        - 1
        - 1000
        - 1000000
        - 1000000000
        - 60000000000
        - 3600000000000
        type: integer
        x-enum-varnames:
        - minDuration
        - maxDuration
        - Nanosecond
        - Microsecond
        - Millisecond
        - Second
        - Minute
        - Hour
    type: object
  v1.EnvFromSource:
    properties:
      configMapRef:
        allOf:
        - $ref: '#/definitions/v1.ConfigMapEnvSource'
        description: |-
          The ConfigMap to select from
          +optional
      prefix:
        description: |-
          Optional text to prepend to the name of each environment variable.
          May consist of any printable ASCII characters except '='.
          +optional
        type: string
      secretRef:
        allOf:
        - $ref: '#/definitions/v1.SecretEnvSource'
        description: |-
          The Secret to select from
          +optional
    type: object
  v1.EnvVar:
    properties:
      name:
        description: |-
          Name of the environment variable.
          May consist of any printable ASCII characters except '='.
        type: string
      value:
        description: |-
          Variable references $(VAR_NAME) are expanded
          using the previously defined environment variables in the container and
          any service environment variables. If a variable cannot be resolved,
          the reference in the input string will be unchanged. Double $$ are reduced
          to a single $, which allows for escaping the $(VAR_NAME) syntax: i.e.
          "$$(VAR_NAME)" will produce the string literal "$(VAR_NAME)".
          Escaped references will never be expanded, regardless of whether the variable
          exists or not.
          Defaults to "".
          +optional
        type: string
      valueFrom:
        allOf:
        - $ref: '#/definitions/v1.EnvVarSource'
        description: |-
          Source for the environment variable's value. Cannot be used if value is not empty.
          +optional
    type: object
  v1.EnvVarSource:
    properties:
      configMapKeyRef:
        allOf:
        - $ref: '#/definitions/v1.ConfigMapKeySelector'
        description: |-
          Selects a key of a ConfigMap.
          +optional
      fieldRef:
        allOf:
        - $ref: '#/definitions/v1.ObjectFieldSelector'
        description: |-
          Selects a field of the pod: supports metadata.name, metadata.namespace, `metadata.labels['<KEY>']`, `metadata.annotations['<KEY>']`,
          spec.nodeName, spec.serviceAccountName, status.hostIP, status.podIP, status.podIPs.
          +optional
      fileKeyRef:
        allOf:
        - $ref: '#/definitions/v1.FileKeySelector'
        description: |-
          FileKeyRef selects a key of the env file.
          Requires the EnvFiles feature gate to be enabled.

          +featureGate=EnvFiles
          +optional
      resourceFieldRef:
        allOf:
        - $ref: '#/definitions/v1.ResourceFieldSelector'
        description: |-
          Selects a resource of the container: only resources limits and requests
          (limits.cpu, limits.memory, limits.ephemeral-storage, requests.cpu, requests.memory and requests.ephemeral-storage) are currently supported.
          +optional
      secretKeyRef:
        allOf:
        - $ref: '#/definitions/v1.SecretKeySelector'
        description: |-
          Selects a key of a secret in the pod's namespace
          +optional
    type: object
  v1.ExecAction:
    properties:
      command:
        description: |-
          Command is the command line to execute inside the container, the working directory for the
          command  is root ('/') in the container's filesystem. The command is simply exec'd, it is
          not run inside a shell, so traditional shell instructions ('|', etc) won't work. To use
          a shell, you need to explicitly call out to that shell.
          Exit status of 0 is treated as live/healthy and non-zero is unhealthy.
          +optional
          +listType=atomic
        items:
          type: string
        type: array
    type: object
  v1.FieldsV1:
    type: object
  v1.FileKeySelector:
    properties:
      key:
        description: |-
          The key within the env file. An invalid key will prevent the pod from starting.
          The keys defined within a source may consist of any printable ASCII characters except '='.
          During Alpha stage of the EnvFiles feature gate, the key size is limited to 128 characters.
          +required
        type: string
      optional:
        description: |-
          Specify whether the file or its key must be defined. If the file or key
          does not exist, then the env var is not published.
          If optional is set to true and the specified key does not exist,
          the environment variable will not be set in the Pod's containers.

          If optional is set to false and the specified key does not exist,
          an error will be returned during Pod creation.
          +optional
          +default=false
        type: boolean
      path:
        description: |-
          The path within the volume from which to select the file.
          Must be relative and may not contain the '..' path or start with '..'.
          +required
        type: string
      volumeName:
        description: |-
          The name of the volume mount containing the env file.
          +required
        type: string
    type: object
  v1.GRPCAction:
    properties:
      port:
        description: Port number of the gRPC service. Number must be in the range
          1 to 65535.
        type: integer
      service:
        description: |-
          Service is the name of the service to place in the gRPC HealthCheckRequest
          (see https://github.com/grpc/grpc/blob/master/doc/health-checking.md).

          If this is not specified, the default behavior is defined by gRPC.
          +optional
          +default=""
        type: string
    type: object
  v1.HTTPGetAction:
    properties:
      host:
        description: |-
          Host name to connect to, defaults to the pod IP. You probably want to set
          "Host" in httpHeaders instead.
          +optional
        type: string
      httpHeaders:
        description: |-
          Custom headers to set in the request. HTTP allows repeated headers.
          +optional
          +listType=atomic
        items:
          $ref: '#/definitions/v1.HTTPHeader'
        type: array
      path:
        description: |-
          Path to access on the HTTP server.
          +optional
        type: string
      port:
        allOf:
        - $ref: '#/definitions/intstr.IntOrString'
        description: |-
          Name or number of the port to access on the container.
          Number must be in the range 1 to 65535.
          Name must be an IANA_SVC_NAME.
      scheme:
        allOf:
        - $ref: '#/definitions/v1.URIScheme'
        description: |-
          Scheme to use for connecting to the host.
          Defaults to HTTP.
          +optional
    type: object
  v1.HTTPHeader:
    properties:
      name:
        description: |-
          The header field name.
          This will be canonicalized upon output, so case-variant names will be understood as the same header.
        type: string
      value:
        description: The header field value
        type: string
    type: object
  v1.Lifecycle:
    properties:
      postStart:
        allOf:
        - $ref: '#/definitions/v1.LifecycleHandler'
        description: |-
          PostStart is called immediately after a container is created. If the handler fails,
          the container is terminated and restarted according to its restart policy.
          Other management of the container blocks until the hook completes.
          More info: https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/#container-hooks
          +optional
      preStop:
        allOf:
        - $ref: '#/definitions/v1.LifecycleHandler'
        description: |-
          PreStop is called immediately before a container is terminated due to an
          API request or management event such as liveness/startup probe failure,
          preemption, resource contention, etc. The handler is not called if the
          container crashes or exits. The Pod's termination grace period countdown begins before the
          PreStop hook is executed. Regardless of the outcome of the handler, the
          container will eventually terminate within the Pod's termination grace
          period (unless delayed by finalizers). Other management of the container blocks until the hook completes
          or until the termination grace period is reached.
          More info: https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/#container-hooks
          +optional
      stopSignal:
        allOf:
        - $ref: '#/definitions/v1.Signal'
        description: |-
          StopSignal defines which signal will be sent to a container when it is being stopped.
          If not specified, the default is defined by the container runtime in use.
          StopSignal can only be set for Pods with a non-empty .spec.os.name
          +optional
    type: object
  v1.LifecycleHandler:
    properties:
      exec:
        allOf:
        - $ref: '#/definitions/v1.ExecAction'
        description: |-
          Exec specifies a command to execute in the container.
          +optional
      httpGet:
        allOf:
        - $ref: '#/definitions/v1.HTTPGetAction'
        description: |-
          HTTPGet specifies an HTTP GET request to perform.
          +optional
      sleep:
        allOf:
        - $ref: '#/definitions/v1.SleepAction'
        description: |-
          Sleep represents a duration that the container should sleep.
          +featureGate=PodLifecycleSleepAction
          +optional
      tcpSocket:
        allOf:
        - $ref: '#/definitions/v1.TCPSocketAction'
        description: |-
          Deprecated. TCPSocket is NOT supported as a LifecycleHandler and kept
          for backward compatibility. There is no validation of this field and
          lifecycle hooks will fail at runtime when it is specified.
          +optional
    type: object
  v1.ListMeta:
    properties:
      continue:
        description: |-
          continue may be set if the user set a limit on the number of items returned, and indicates that
          the server has more data available. The value is opaque and may be used to issue another request
          to the endpoint that served this list to retrieve the next set of available objects. Continuing a
          consistent list may not be possible if the server configuration has changed or more than a few
          minutes have passed. The resourceVersion field returned when using this continue value will be
          identical to the value in the first response, unless you have received this token from an error
          message.
        type: string
      remainingItemCount:
        description: |-
          remainingItemCount is the number of subsequent items in the list which are not included in this
          list response. If the list request contained label or field selectors, then the number of
          remaining items is unknown and the field will be left unset and omitted during serialization.
          If the list is complete (either because it is not chunking or because this is the last chunk),
          then there are no more remaining items and this field will be left unset and omitted during
          serialization.
          Servers older than v1.15 do not set this field.
          The intended use of the remainingItemCount is *estimating* the size of a collection. Clients
          should not rely on the remainingItemCount to be set or to be exact.
          +optional
        type: integer
      resourceVersion:
        description: |-
          String that identifies the server's internal version of this object that
          can be used by clients to determine when objects have changed.
          Value must be treated as opaque by clients and passed unmodified back to the server.
          Populated by the system.
          Read-only.
          More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency
          +optional
        type: string
      selfLink:
        description: |-
          Deprecated: selfLink is a legacy read-only field that is no longer populated by the system.
          +optional
        type: string
    type: object
  v1.ManagedFieldsEntry:
    properties:
      apiVersion:
        description: |-
          APIVersion defines the version of this resource that this field set
          applies to. The format is "group/version" just like the top-level
          APIVersion field. It is necessary to track the version of a field
          set because it cannot be automatically converted.
        type: string
      fieldsType:
        description: |-
          FieldsType is the discriminator for the different fields format and version.
          There is currently only one possible value: "FieldsV1"
        type: string
      fieldsV1:
        allOf:
        - $ref: '#/definitions/v1.FieldsV1'
        description: |-
          FieldsV1 holds the first JSON version format as described in the "FieldsV1" type.
          +optional
      manager:
        description: Manager is an identifier of the workflow managing these fields.
        type: string
      operation:
        allOf:
        - $ref: '#/definitions/v1.ManagedFieldsOperationType'
        description: |-
          Operation is the type of operation which lead to this ManagedFieldsEntry being created.
          The only valid values for this field are 'Apply' and 'Update'.
      subresource:
        description: |-
          Subresource is the name of the subresource used to update that object, or
          empty string if the object was updated through the main resource. The
          value of this field is used to distinguish between managers, even if they
          share the same name. For example, a status update will be distinct from a
          regular update using the same manager name.
          Note that the APIVersion field is not related to the Subresource field and
          it always corresponds to the version of the main resource.
        type: string
      time:
        description: |-
          Time is the timestamp of when the ManagedFields entry was added. The
          timestamp will also be updated if a field is added, the manager
          changes any of the owned fields value or removes a field. The
          timestamp does not update when a field is removed from the entry
          because another manager took it over.
          +optional
        type: string
    type: object
  v1.ManagedFieldsOperationType:
    enum:
    - Apply
    - Update
    type: string
    x-enum-varnames:
    - ManagedFieldsOperationApply
    - ManagedFieldsOperationUpdate
  v1.MountPropagationMode:
    enum:
    - None
    - HostToContainer
    - Bidirectional
    type: string
    x-enum-varnames:
    - MountPropagationNone
    - MountPropagationHostToContainer
    - MountPropagationBidirectional
  v1.NamespaceCondition:
    properties:
      lastTransitionTime:
        description: |-
          Last time the condition transitioned from one status to another.
          +optional
        type: string
      message:
        description: |-
          Human-readable message indicating details about last transition.
          +optional
        type: string
      reason:
        description: |-
          Unique, one-word, CamelCase reason for the condition's last transition.
          +optional
        type: string
      status:
        allOf:
        - $ref: '#/definitions/k8s_io_api_core_v1.ConditionStatus'
        description: Status of the condition, one of True, False, Unknown.
      type:
        allOf:
        - $ref: '#/definitions/v1.NamespaceConditionType'
        description: Type of namespace controller condition.
    type: object
  v1.NamespaceConditionType:
    enum:
    - NamespaceDeletionDiscoveryFailure
    - NamespaceDeletionContentFailure
    - NamespaceDeletionGroupVersionParsingFailure
    - NamespaceContentRemaining
    - NamespaceFinalizersRemaining
    type: string
    x-enum-varnames:
    - NamespaceDeletionDiscoveryFailure
    - NamespaceDeletionContentFailure
    - NamespaceDeletionGVParsingFailure
    - NamespaceContentRemaining
    - NamespaceFinalizersRemaining
  v1.NamespacePhase:
    enum:
    - Active
    - Terminating
    type: string
    x-enum-varnames:
    - NamespaceActive
    - NamespaceTerminating
  v1.NamespaceStatus:
    properties:
      conditions:
        description: |-
          Represents the latest available observations of a namespace's current state.
          +optional
          +patchMergeKey=type
          +patchStrategy=merge
          +listType=map
          +listMapKey=type
        items:
          $ref: '#/definitions/v1.NamespaceCondition'
        type: array
      phase:
        allOf:
        - $ref: '#/definitions/v1.NamespacePhase'
        description: |-
          Phase is the current lifecycle phase of the namespace.
          More info: https://kubernetes.io/docs/tasks/administer-cluster/namespaces/
          +optional
    type: object
  v1.ObjectFieldSelector:
    properties:
      apiVersion:
        description: |-
          Version of the schema the FieldPath is written in terms of, defaults to "v1".
          +optional
        type: string
      fieldPath:
        description: Path of the field to select in the specified API version.
        type: string
    type: object
  v1.ObjectMeta:
    properties:
      annotations:
        additionalProperties:
          type: string
        description: |-
          Annotations is an unstructured key value map stored with a resource that may be
          set by external tools to store and retrieve arbitrary metadata. They are not
          queryable and should be preserved when modifying objects.
          More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations
          +optional
        type: object
      creationTimestamp:
        description: |-
          CreationTimestamp is a timestamp representing the server time when this object was
          created. It is not guaranteed to be set in happens-before order across separate operations.
          Clients may not set this value. It is represented in RFC3339 form and is in UTC.

          Populated by the system.
          Read-only.
          Null for lists.
          More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
          +optional
        type: string
      deletionGracePeriodSeconds:
        description: |-
          Number of seconds allowed for this object to gracefully terminate before
          it will be removed from the system. Only set when deletionTimestamp is also set.
          May only be shortened.
          Read-only.
          +optional
        type: integer
      deletionTimestamp:
        description: |-
          DeletionTimestamp is RFC 3339 date and time at which this resource will be deleted. This
          field is set by the server when a graceful deletion is requested by the user, and is not
          directly settable by a client. The resource is expected to be deleted (no longer visible
          from resource lists, and not reachable by name) after the time in this field, once the
          finalizers list is empty. As long as the finalizers list contains items, deletion is blocked.
          Once the deletionTimestamp is set, this value may not be unset or be set further into the
          future, although it may be shortened or the resource may be deleted prior to this time.
          For example, a user may request that a pod is deleted in 30 seconds. The Kubelet will react
          by sending a graceful termination signal to the containers in the pod. After that 30 seconds,
          the Kubelet will send a hard termination signal (SIGKILL) to the container and after cleanup,
          remove the pod from the API. In the presence of network partitions, this object may still
          exist after this timestamp, until an administrator or automated process can determine the
          resource is fully terminated.
          If not set, graceful deletion of the object has not been requested.

          Populated by the system when a graceful deletion is requested.
          Read-only.
          More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
          +optional
        type: string
      finalizers:
        description: |-
          Must be empty before the object is deleted from the registry. Each entry
          is an identifier for the responsible component that will remove the entry
          from the list. If the deletionTimestamp of the object is non-nil, entries
          in this list can only be removed.
          Finalizers may be processed and removed in any order.  Order is NOT enforced
          because it introduces significant risk of stuck finalizers.
          finalizers is a shared field, any actor with permission can reorder it.
          If the finalizer list is processed in order, then this can lead to a situation
          in which the component responsible for the first finalizer in the list is
          waiting for a signal (field value, external system, or other) produced by a
          component responsible for a finalizer later in the list, resulting in a deadlock.
          Without enforced ordering finalizers are free to order amongst themselves and
          are not vulnerable to ordering changes in the list.
          +optional
          +patchStrategy=merge
          +listType=set
        items:
          type: string
        type: array
      generateName:
        description: |-
          GenerateName is an optional prefix, used by the server, to generate a unique
          name ONLY IF the Name field has not been provided.
          If this field is used, the name returned to the client will be different
          than the name passed. This value will also be combined with a unique suffix.
          The provided value has the same validation rules as the Name field,
          and may be truncated by the length of the suffix required to make the value
          unique on the server.

          If this field is specified and the generated name exists, the server will return a 409.

          Applied only if Name is not specified.
          More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#idempotency
          +optional
        type: string
      generation:
        description: |-
          A sequence number representing a specific generation of the desired state.
          Populated by the system. Read-only.
          +optional
        type: integer
