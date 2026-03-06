          Unconfined - no profile should be applied.
          +unionDiscriminator
    type: object
  v1.SeccompProfileType:
    enum:
    - Unconfined
    - RuntimeDefault
    - Localhost
    type: string
    x-enum-varnames:
    - SeccompProfileTypeUnconfined
    - SeccompProfileTypeRuntimeDefault
    - SeccompProfileTypeLocalhost
  v1.SecretEnvSource:
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
          Specify whether the Secret must be defined
          +optional
        type: boolean
    type: object
  v1.SecretKeySelector:
    properties:
      key:
        description: The key of the secret to select from.  Must be a valid secret
          key.
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
          Specify whether the Secret or its key must be defined
          +optional
        type: boolean
    type: object
  v1.SecretReference:
    properties:
      name:
        description: |-
          name is unique within a namespace to reference a secret resource.
          +optional
        type: string
      namespace:
        description: |-
          namespace defines the space within which the secret name must be unique.
          +optional
        type: string
    type: object
  v1.SecurityContext:
    properties:
      allowPrivilegeEscalation:
        description: |-
          AllowPrivilegeEscalation controls whether a process can gain more
          privileges than its parent process. This bool directly controls if
          the no_new_privs flag will be set on the container process.
          AllowPrivilegeEscalation is true always when the container is:
          1) run as Privileged
          2) has CAP_SYS_ADMIN
          Note that this field cannot be set when spec.os.name is windows.
          +optional
        type: boolean
      appArmorProfile:
        allOf:
        - $ref: '#/definitions/v1.AppArmorProfile'
        description: |-
          appArmorProfile is the AppArmor options to use by this container. If set, this profile
          overrides the pod's appArmorProfile.
          Note that this field cannot be set when spec.os.name is windows.
          +optional
      capabilities:
        allOf:
        - $ref: '#/definitions/v1.Capabilities'
        description: |-
          The capabilities to add/drop when running containers.
          Defaults to the default set of capabilities granted by the container runtime.
          Note that this field cannot be set when spec.os.name is windows.
          +optional
      privileged:
        description: |-
          Run container in privileged mode.
          Processes in privileged containers are essentially equivalent to root on the host.
          Defaults to false.
          Note that this field cannot be set when spec.os.name is windows.
          +optional
        type: boolean
      procMount:
        allOf:
        - $ref: '#/definitions/v1.ProcMountType'
        description: |-
          procMount denotes the type of proc mount to use for the containers.
          The default value is Default which uses the container runtime defaults for
          readonly paths and masked paths.
          This requires the ProcMountType feature flag to be enabled.
          Note that this field cannot be set when spec.os.name is windows.
          +optional
      readOnlyRootFilesystem:
        description: |-
          Whether this container has a read-only root filesystem.
          Default is false.
          Note that this field cannot be set when spec.os.name is windows.
          +optional
        type: boolean
      runAsGroup:
        description: |-
          The GID to run the entrypoint of the container process.
          Uses runtime default if unset.
          May also be set in PodSecurityContext.  If set in both SecurityContext and
          PodSecurityContext, the value specified in SecurityContext takes precedence.
          Note that this field cannot be set when spec.os.name is windows.
          +optional
        type: integer
      runAsNonRoot:
        description: |-
          Indicates that the container must run as a non-root user.
          If true, the Kubelet will validate the image at runtime to ensure that it
          does not run as UID 0 (root) and fail to start the container if it does.
          If unset or false, no such validation will be performed.
          May also be set in PodSecurityContext.  If set in both SecurityContext and
          PodSecurityContext, the value specified in SecurityContext takes precedence.
          +optional
        type: boolean
      runAsUser:
        description: |-
          The UID to run the entrypoint of the container process.
          Defaults to user specified in image metadata if unspecified.
          May also be set in PodSecurityContext.  If set in both SecurityContext and
          PodSecurityContext, the value specified in SecurityContext takes precedence.
          Note that this field cannot be set when spec.os.name is windows.
          +optional
        type: integer
      seLinuxOptions:
        allOf:
        - $ref: '#/definitions/v1.SELinuxOptions'
        description: |-
          The SELinux context to be applied to the container.
          If unspecified, the container runtime will allocate a random SELinux context for each
          container.  May also be set in PodSecurityContext.  If set in both SecurityContext and
          PodSecurityContext, the value specified in SecurityContext takes precedence.
          Note that this field cannot be set when spec.os.name is windows.
          +optional
      seccompProfile:
        allOf:
        - $ref: '#/definitions/v1.SeccompProfile'
        description: |-
          The seccomp options to use by this container. If seccomp options are
          provided at both the pod & container level, the container options
          override the pod options.
          Note that this field cannot be set when spec.os.name is windows.
          +optional
      windowsOptions:
        allOf:
        - $ref: '#/definitions/v1.WindowsSecurityContextOptions'
        description: |-
          The Windows specific settings applied to all containers.
          If unspecified, the options from the PodSecurityContext will be used.
          If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.
          Note that this field cannot be set when spec.os.name is linux.
          +optional
    type: object
  v1.Signal:
    enum:
    - SIGABRT
    - SIGALRM
    - SIGBUS
    - SIGCHLD
    - SIGCLD
    - SIGCONT
    - SIGFPE
    - SIGHUP
    - SIGILL
    - SIGINT
    - SIGIO
    - SIGIOT
    - SIGKILL
    - SIGPIPE
    - SIGPOLL
    - SIGPROF
    - SIGPWR
    - SIGQUIT
    - SIGSEGV
    - SIGSTKFLT
    - SIGSTOP
    - SIGSYS
    - SIGTERM
    - SIGTRAP
    - SIGTSTP
    - SIGTTIN
    - SIGTTOU
    - SIGURG
    - SIGUSR1
    - SIGUSR2
    - SIGVTALRM
    - SIGWINCH
    - SIGXCPU
    - SIGXFSZ
    - SIGRTMIN
    - SIGRTMIN+1
    - SIGRTMIN+2
    - SIGRTMIN+3
    - SIGRTMIN+4
    - SIGRTMIN+5
    - SIGRTMIN+6
    - SIGRTMIN+7
    - SIGRTMIN+8
    - SIGRTMIN+9
    - SIGRTMIN+10
    - SIGRTMIN+11
    - SIGRTMIN+12
    - SIGRTMIN+13
    - SIGRTMIN+14
    - SIGRTMIN+15
    - SIGRTMAX-14
    - SIGRTMAX-13
    - SIGRTMAX-12
    - SIGRTMAX-11
    - SIGRTMAX-10
    - SIGRTMAX-9
    - SIGRTMAX-8
    - SIGRTMAX-7
    - SIGRTMAX-6
    - SIGRTMAX-5
    - SIGRTMAX-4
    - SIGRTMAX-3
    - SIGRTMAX-2
    - SIGRTMAX-1
    - SIGRTMAX
    type: string
    x-enum-varnames:
    - SIGABRT
    - SIGALRM
    - SIGBUS
    - SIGCHLD
    - SIGCLD
    - SIGCONT
    - SIGFPE
    - SIGHUP
    - SIGILL
    - SIGINT
    - SIGIO
    - SIGIOT
    - SIGKILL
    - SIGPIPE
    - SIGPOLL
    - SIGPROF
    - SIGPWR
    - SIGQUIT
    - SIGSEGV
    - SIGSTKFLT
    - SIGSTOP
    - SIGSYS
    - SIGTERM
    - SIGTRAP
    - SIGTSTP
    - SIGTTIN
    - SIGTTOU
    - SIGURG
    - SIGUSR1
    - SIGUSR2
    - SIGVTALRM
    - SIGWINCH
    - SIGXCPU
    - SIGXFSZ
    - SIGRTMIN
    - SIGRTMINPLUS1
    - SIGRTMINPLUS2
    - SIGRTMINPLUS3
    - SIGRTMINPLUS4
    - SIGRTMINPLUS5
    - SIGRTMINPLUS6
    - SIGRTMINPLUS7
    - SIGRTMINPLUS8
    - SIGRTMINPLUS9
    - SIGRTMINPLUS10
    - SIGRTMINPLUS11
    - SIGRTMINPLUS12
    - SIGRTMINPLUS13
    - SIGRTMINPLUS14
    - SIGRTMINPLUS15
    - SIGRTMAXMINUS14
    - SIGRTMAXMINUS13
    - SIGRTMAXMINUS12
    - SIGRTMAXMINUS11
    - SIGRTMAXMINUS10
    - SIGRTMAXMINUS9
    - SIGRTMAXMINUS8
    - SIGRTMAXMINUS7
    - SIGRTMAXMINUS6
    - SIGRTMAXMINUS5
    - SIGRTMAXMINUS4
    - SIGRTMAXMINUS3
    - SIGRTMAXMINUS2
    - SIGRTMAXMINUS1
    - SIGRTMAX
  v1.SleepAction:
    properties:
      seconds:
        description: Seconds is the number of seconds to sleep.
        type: integer
    type: object
  v1.TCPSocketAction:
    properties:
      host:
        description: |-
          Optional: Host name to connect to, defaults to the pod IP.
          +optional
        type: string
      port:
        allOf:
        - $ref: '#/definitions/intstr.IntOrString'
        description: |-
          Number or name of the port to access on the container.
          Number must be in the range 1 to 65535.
          Name must be an IANA_SVC_NAME.
    type: object
  v1.TerminationMessagePolicy:
    enum:
    - File
    - FallbackToLogsOnError
    type: string
    x-enum-varnames:
    - TerminationMessageReadFile
    - TerminationMessageFallbackToLogsOnError
  v1.URIScheme:
    enum:
    - HTTP
    - HTTPS
    type: string
    x-enum-varnames:
    - URISchemeHTTP
    - URISchemeHTTPS
  v1.VolumeDevice:
    properties:
      devicePath:
        description: devicePath is the path inside of the container that the device
          will be mapped to.
        type: string
      name:
        description: name must match the name of a persistentVolumeClaim in the pod
        type: string
    type: object
  v1.VolumeMount:
    properties:
      mountPath:
        description: |-
          Path within the container at which the volume should be mounted.  Must
          not contain ':'.
        type: string
      mountPropagation:
        allOf:
        - $ref: '#/definitions/v1.MountPropagationMode'
        description: |-
          mountPropagation determines how mounts are propagated from the host
          to container and the other way around.
          When not set, MountPropagationNone is used.
          This field is beta in 1.10.
          When RecursiveReadOnly is set to IfPossible or to Enabled, MountPropagation must be None or unspecified
          (which defaults to None).
          +optional
      name:
        description: This must match the Name of a Volume.
        type: string
      readOnly:
        description: |-
          Mounted read-only if true, read-write otherwise (false or unspecified).
          Defaults to false.
          +optional
        type: boolean
      recursiveReadOnly:
        allOf:
        - $ref: '#/definitions/v1.RecursiveReadOnlyMode'
        description: |-
          RecursiveReadOnly specifies whether read-only mounts should be handled
          recursively.

          If ReadOnly is false, this field has no meaning and must be unspecified.

          If ReadOnly is true, and this field is set to Disabled, the mount is not made
          recursively read-only.  If this field is set to IfPossible, the mount is made
          recursively read-only, if it is supported by the container runtime.  If this
          field is set to Enabled, the mount is made recursively read-only if it is
          supported by the container runtime, otherwise the pod will not be started and
          an error will be generated to indicate the reason.

          If this field is set to IfPossible or Enabled, MountPropagation must be set to
          None (or be unspecified, which defaults to None).

          If this field is not specified, it is treated as an equivalent of Disabled.

          +featureGate=RecursiveReadOnlyMounts
          +optional
      subPath:
        description: |-
          Path within the volume from which the container's volume should be mounted.
          Defaults to "" (volume's root).
          +optional
        type: string
      subPathExpr:
        description: |-
          Expanded path within the volume from which the container's volume should be mounted.
          Behaves similarly to SubPath but environment variable references $(VAR_NAME) are expanded using the container's environment.
          Defaults to "" (volume's root).
          SubPathExpr and SubPath are mutually exclusive.
          +optional
        type: string
    type: object
  v1.WindowsSecurityContextOptions:
    properties:
      gmsaCredentialSpec:
        description: |-
          GMSACredentialSpec is where the GMSA admission webhook
          (https://github.com/kubernetes-sigs/windows-gmsa) inlines the contents of the
          GMSA credential spec named by the GMSACredentialSpecName field.
          +optional
        type: string
      gmsaCredentialSpecName:
        description: |-
          GMSACredentialSpecName is the name of the GMSA credential spec to use.
          +optional
        type: string
      hostProcess:
        description: |-
          HostProcess determines if a container should be run as a 'Host Process' container.
          All of a Pod's containers must have the same effective HostProcess value
          (it is not allowed to have a mix of HostProcess containers and non-HostProcess containers).
          In addition, if HostProcess is true then HostNetwork must also be set to true.
          +optional
        type: boolean
      runAsUserName:
        description: |-
          The UserName in Windows to run the entrypoint of the container process.
          Defaults to the user specified in image metadata if unspecified.
          May also be set in PodSecurityContext. If set in both SecurityContext and
          PodSecurityContext, the value specified in SecurityContext takes precedence.
          +optional
        type: string
    type: object
  v1beta1.ContainerMetrics:
    properties:
      name:
        description: Container name corresponding to the one from pod.spec.containers.
        type: string
      usage:
        allOf:
        - $ref: '#/definitions/v1.ResourceList'
        description: The memory usage is the memory working set.
    type: object
  v1beta1.NodeMetrics:
    properties:
      apiVersion:
        description: |-
          APIVersion defines the versioned schema of this representation of an object.
          Servers should convert recognized schemas to the latest internal value, and
          may reject unrecognized values.
          More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
          +optional
        type: string
      kind:
        description: |-
          Kind is a string value representing the REST resource this object represents.
          Servers may infer this from the endpoint the client submits requests to.
          Cannot be updated.
          In CamelCase.
          More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
          +optional
        type: string
      metadata:
        allOf:
        - $ref: '#/definitions/v1.ObjectMeta'
        description: |-
          Standard object's metadata.
          More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
          +optional
      timestamp:
        description: |-
          The following fields define time interval from which metrics were
          collected from the interval [Timestamp-Window, Timestamp].
        type: string
      usage:
        allOf:
        - $ref: '#/definitions/v1.ResourceList'
        description: The memory usage is the memory working set.
      window:
        $ref: '#/definitions/v1.Duration'
    type: object
  v1beta1.NodeMetricsList:
    properties:
      apiVersion:
        description: |-
          APIVersion defines the versioned schema of this representation of an object.
          Servers should convert recognized schemas to the latest internal value, and
          may reject unrecognized values.
          More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
          +optional
        type: string
      items:
        description: List of node metrics.
        items:
          $ref: '#/definitions/v1beta1.NodeMetrics'
        type: array
      kind:
        description: |-
          Kind is a string value representing the REST resource this object represents.
          Servers may infer this from the endpoint the client submits requests to.
          Cannot be updated.
          In CamelCase.
          More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
          +optional
        type: string
      metadata:
        allOf:
        - $ref: '#/definitions/v1.ListMeta'
        description: |-
          Standard list metadata.
          More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    type: object
  v1beta1.PodMetrics:
    properties:
      apiVersion:
        description: |-
          APIVersion defines the versioned schema of this representation of an object.
          Servers should convert recognized schemas to the latest internal value, and
          may reject unrecognized values.
          More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
          +optional
        type: string
      containers:
        description: |-
          Metrics for all containers are collected within the same time window.
          +listType=atomic
        items:
          $ref: '#/definitions/v1beta1.ContainerMetrics'
        type: array
      kind:
        description: |-
          Kind is a string value representing the REST resource this object represents.
          Servers may infer this from the endpoint the client submits requests to.
          Cannot be updated.
          In CamelCase.
          More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
          +optional
        type: string
      metadata:
        allOf:
        - $ref: '#/definitions/v1.ObjectMeta'
        description: |-
          Standard object's metadata.
          More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
          +optional
      timestamp:
        description: |-
          The following fields define time interval from which metrics were
          collected from the interval [Timestamp-Window, Timestamp].
        type: string
      window:
        $ref: '#/definitions/v1.Duration'
    type: object
  v1beta1.PodMetricsList:
    properties:
      apiVersion:
        description: |-
          APIVersion defines the versioned schema of this representation of an object.
          Servers should convert recognized schemas to the latest internal value, and
          may reject unrecognized values.
          More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
          +optional
        type: string
      items:
        description: List of pod metrics.
        items:
          $ref: '#/definitions/v1beta1.PodMetrics'
        type: array
      kind:
        description: |-
          Kind is a string value representing the REST resource this object represents.
          Servers may infer this from the endpoint the client submits requests to.
          Cannot be updated.
          In CamelCase.
          More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
          +optional
        type: string
      metadata:
        allOf:
        - $ref: '#/definitions/v1.ListMeta'
        description: |-
          Standard list metadata.
          More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    type: object
  webhooks.webhookCreatePayload:
    properties:
      EndpointID:
        type: integer
      RegistryID:
        type: integer
      ResourceID:
        type: string
      WebhookType:
        allOf:
        - $ref: '#/definitions/portainer.WebhookType'
        description: Type of webhook (1 - service, 2 - container)
    type: object
  webhooks.webhookReassignPayload:
    properties:
      ResourceID:
        type: string
      WebhookType:
        allOf:
        - $ref: '#/definitions/portainer.WebhookType'
        description: Type of webhook (1 - service, 2 - container)
    type: object
  webhooks.webhookUpdatePayload:
    properties:
      RegistryID:
        type: integer
    type: object
info:
  contact:
    email: info@portainer.io
  description: |
    Portainer API is an HTTP API served by Portainer. It is used by the Portainer UI and everything you can do with the UI can be done using the HTTP API.
    Examples are available at https://documentation.portainer.io/api/api-examples/
    You can find out more about Portainer at [http://portainer.io](http://portainer.io) and get some support on [Slack](http://portainer.io/slack/).

    # Authentication

    Most of the API environments(endpoints) require to be authenticated as well as some level of authorization to be used.
    Portainer API uses JSON Web Token to manage authentication and thus requires you to provide a token in the **Authorization** header of each request
    with the **Bearer** authentication mechanism.

    Example:

```
    Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwidXNlcm5hbWUiOiJhZG1pbiIsInJvbGUiOjEsImV4cCI6MTQ5OTM3NjE1NH0.NJ6vE8FY1WG6jsRQzfMqeatJ4vh2TWAeeYfDhP71YEE
```

    # Security

    Each API environment(endpoint) has an associated access policy, it is documented in the description of each environment(endpoint).

    Different access policies are available:

    - Public access
    - Authenticated access
    - Restricted access
    - Administrator access

    ### Public access

    No authentication is required to access the environments(endpoints) with this access policy.

    ### Authenticated access

    Authentication is required to access the environments(endpoints) with this access policy.

    ### Restricted access

    Authentication is required to access the environments(endpoints) with this access policy.
    Extra-checks might be added to ensure access to the resource is granted. Returned data might also be filtered.

    ### Administrator access

    Authentication as well as an administrator role are required to access the environments(endpoints) with this access policy.

    # Execute Docker requests

    Portainer **DO NOT** expose specific environments(endpoints) to manage your Docker resources (create a container, remove a volume, etc...).

    Instead, it acts as a reverse-proxy to the Docker HTTP API. This means that you can execute Docker requests **via** the Portainer HTTP API.

    To do so, you can use the `/endpoints/{id}/docker` Portainer API environment(endpoint) (which is not documented below due to Swagger limitations). This environment(endpoint) has a restricted access policy so you still need to be authenticated to be able to query this environment(endpoint). Any query on this environment(endpoint) will be proxied to the Docker API of the associated environment(endpoint) (requests and responses objects are the same as documented in the Docker API).

    # Private Registry

    Using private registry, you will need to pass a based64 encoded JSON string â€˜{"registryId":\<registryID value\>}â€™ inside the Request Header. The parameter name is "X-Registry-Auth".
    \<registryID value\> - The registry ID where the repository was created.

    Example:

```
    eyJyZWdpc3RyeUlkIjoxfQ==
```

    **NOTE**: You can find more information on how to query the Docker API in the [Docker official documentation](https://docs.docker.com/engine/api/v1.30/) as well as in [this Portainer example](https://documentation.portainer.io/api/api-examples/).
  title: PortainerEE API
  version: 2.39.0
paths:
  /auth:
    post:
      consumes:
      - application/json
      description: |-
        **Access policy**: public
