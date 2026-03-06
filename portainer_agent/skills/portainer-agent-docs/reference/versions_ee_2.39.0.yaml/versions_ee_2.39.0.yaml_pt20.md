        **Access policy**: administrator
      operationId: EndpointCreate
      parameters:
      - description: 'Name that will be used to identify this environment(endpoint)
          (example: my-environment)'
        in: formData
        name: Name
        required: true
        type: string
      - description: 'Environment(Endpoint) type. Value must be one of: 1 (Local Docker
          environment), 2 (Agent environment), 3 (Azure environment), 4 (Edge agent
          environment) or 5 (Local Kubernetes Environment)'
        in: formData
        name: EndpointCreationType
        required: true
        type: integer
      - description: 'Container engine used by the environment(endpoint). Value must
          be one of: ''docker'' or ''podman'''
        in: formData
        name: ContainerEngine
        type: string
      - description: 'URL or IP address of a Docker host (example: docker.mydomain.tld:2375).
          Defaults to local if not specified (Linux: /var/run/docker.sock, Windows:
          //./pipe/docker_engine). Cannot be empty if EndpointCreationType is set
          to 4 (Edge agent environment)'
        in: formData
        name: URL
        type: string
      - description: 'URL or IP address where exposed containers will be reachable.
          Defaults to URL if not specified (example: docker.mydomain.tld:2375)'
        in: formData
        name: PublicURL
        type: string
      - description: Environment(Endpoint) group identifier. If not specified will
          default to 1 (unassigned).
        in: formData
        name: GroupID
        type: integer
      - description: Require TLS to connect against this environment(endpoint). Must
          be true if EndpointCreationType is set to 2 (Agent environment)
        in: formData
        name: TLS
        type: boolean
      - description: Skip server verification when using TLS. Must be true if EndpointCreationType
          is set to 2 (Agent environment)
        in: formData
        name: TLSSkipVerify
        type: boolean
      - description: Skip client verification when using TLS. Must be true if EndpointCreationType
          is set to 2 (Agent environment)
        in: formData
        name: TLSSkipClientVerify
        type: boolean
      - description: TLS CA certificate file
        in: formData
        name: TLSCACertFile
        type: file
      - description: TLS client certificate file
        in: formData
        name: TLSCertFile
        type: file
      - description: TLS client key file
        in: formData
        name: TLSKeyFile
        type: file
      - description: Azure application ID. Required if environment(endpoint) type
          is set to 3
        in: formData
        name: AzureApplicationID
        type: string
      - description: Azure tenant ID. Required if environment(endpoint) type is set
          to 3
        in: formData
        name: AzureTenantID
        type: string
      - description: Azure authentication key. Required if environment(endpoint) type
          is set to 3
        in: formData
        name: AzureAuthenticationKey
        type: string
      - collectionFormat: csv
        description: List of tag identifiers to which this environment(endpoint) is
          associated
        in: formData
        items:
          type: integer
        name: TagIds
        type: array
      - description: The check in interval for edge agent (in seconds)
        in: formData
        name: EdgeCheckinInterval
        type: integer
      - description: URL or IP address that will be used to establish a reverse tunnel.
          Required when settings.EnableEdgeComputeFeatures is set to false or when
          settings.Edge.TunnelServerAddress is not set
        in: formData
        name: EdgeTunnelServerAddress
        type: string
      - description: Enable async mode for edge agent
        in: formData
        name: EdgeAsyncMode
        type: boolean
      - description: List of GPUs - json stringified array of {name, value} structs
        in: formData
        name: Gpus
        type: string
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            $ref: '#/definitions/portaineree.Endpoint'
        "400":
          description: Invalid request
        "409":
          description: Name is not unique
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Create a new environment(endpoint)
      tags:
      - endpoints
  /endpoints/{id}:
    delete:
      description: |-
        Remove the environment associated to the specified identifier and optionally clean-up associated resources.
        **Access policy**: Administrator only.
      operationId: EndpointDelete
      parameters:
      - description: Environment(Endpoint) identifier
        in: path
        name: id
        required: true
        type: integer
      responses:
        "204":
          description: Environment successfully deleted.
        "400":
          description: Invalid request payload, such as missing required fields or
            fields not meeting validation criteria.
        "403":
          description: Unauthorized access or operation not allowed.
        "404":
          description: Unable to find the environment with the specified identifier
            inside the database.
        "500":
          description: Server error occurred while attempting to delete the environment.
      security:
      - ApiKeyAuth: []
        jwt: []
      summary: Remove an environment
      tags:
      - endpoints
    get:
      description: |-
        Retrieve details about an environment(endpoint).
        **Access policy**: restricted
      operationId: EndpointInspect
      parameters:
      - description: Environment(Endpoint) identifier
        in: path
        name: id
        required: true
        type: integer
      - description: if true, the snapshot data won't be retrieved
        in: query
        name: excludeSnapshot
        type: boolean
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            $ref: '#/definitions/portaineree.Endpoint'
        "400":
          description: Invalid request
        "404":
          description: Environment(Endpoint) not found
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Inspect an environment(endpoint)
      tags:
      - endpoints
    put:
      consumes:
      - application/json
      description: |-
        Update an environment(endpoint).
        **Access policy**: authenticated
      operationId: EndpointUpdate
      parameters:
      - description: Environment(Endpoint) identifier
        in: path
        name: id
        required: true
        type: integer
      - description: Environment(Endpoint) details
        in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/endpoints.endpointUpdatePayload'
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            $ref: '#/definitions/portaineree.Endpoint'
        "400":
          description: Invalid request
        "404":
          description: Environment(Endpoint) not found
        "409":
          description: Name is not unique
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Update an environment(endpoint)
      tags:
      - endpoints
  /endpoints/{id}/association:
    put:
      description: |-
        De-association an edge environment(endpoint).
        **Access policy**: administrator
      operationId: EndpointAssociationDelete
      parameters:
      - description: Environment(Endpoint) identifier
        in: path
        name: id
        required: true
        type: integer
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            $ref: '#/definitions/portaineree.Endpoint'
        "400":
          description: Invalid request
        "404":
          description: Environment(Endpoint) not found
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: De-association an edge environment(endpoint)
      tags:
      - endpoints
  /endpoints/{id}/docker/v2/browse/put:
    post:
      consumes:
      - multipart/form-data
      description: |-
        Use this environment(endpoint) to upload TLS files.
        **Access policy**: administrator
      parameters:
      - description: Environment(Endpoint) identifier
        in: path
        name: id
        required: true
        type: integer
      - description: Optional volume identifier to upload the file
        in: query
        name: volumeID
        type: string
      - description: The destination path to upload the file to
        in: formData
        name: Path
        required: true
        type: string
      - description: The file to upload
        in: formData
        name: file
        required: true
        type: file
      produces:
      - application/json
      responses:
        "204":
          description: Success
        "400":
          description: Invalid request
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Upload a file under a specific path on the file system of an environment
        (endpoint)
      tags:
      - endpoints
  /endpoints/{id}/dockerhub/{registryId}:
    get:
      description: |-
        get docker pull limits for a docker hub registry in the environment
        **Access policy**:
      operationId: endpointDockerhubStatus
      parameters:
      - description: endpoint ID
        in: path
        name: id
        required: true
        type: integer
      - description: registry ID
        in: path
        name: registryId
        required: true
        type: integer
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            $ref: '#/definitions/endpoints.dockerhubStatusResponse'
        "400":
          description: Invalid request
        "403":
          description: Permission denied
        "404":
          description: registry or endpoint not found
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: fetch docker pull limits
      tags:
      - endpoints
  /endpoints/{id}/edge/charts:
    get:
      description: |-
        environment(endpoint) for edge agent to get contents of requested Helm charts environment(endpoint)
        **Access policy**: restricted only to Edge environments(endpoints)
      operationId: EndpointGetCharts
      parameters:
      - description: Environment(Endpoint) identifier
        in: path
        name: id
        required: true
        type: integer
      - description: JSON encoded list of charts to install
        in: query
        name: chartNames
        type: string
      responses:
        "200":
          description: Success
          schema:
            $ref: '#/definitions/endpointedge.endpointGetChartsResponse'
        "400":
          description: Invalid request
        "403":
          description: Permission denied to access environment(endpoint)
        "404":
          description: Environment(Endpoint) not found
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Get environment(endpoint) charts to install
      tags:
      - endpoints
  /endpoints/{id}/edge/charts/statuses:
    put:
      description: |-
        environment(endpoint) for edge agent to report back installation statuses of Helm charts
        **Access policy**: restricted only to Edge environments(endpoints)
      operationId: EndpointUpdateChartStatuses
      parameters:
      - description: Environment(Endpoint) identifier
        in: path
        name: id
        required: true
        type: integer
      responses:
        "204":
          description: Success
        "400":
          description: Invalid request
        "403":
          description: Permission denied to access environment(endpoint)
        "404":
          description: Environment(Endpoint) not found
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Update environment(endpoint) policy chart installation statuses
      tags:
      - endpoints
  /endpoints/{id}/edge/jobs/{jobID}/logs:
    post:
      consumes:
      - application/json
      description: Authorized only if the request is done by an Edge Environment(Endpoint)
      parameters:
      - description: Environment(Endpoint) Id
        in: path
        name: id
        required: true
        type: integer
      - description: Job Id
        in: path
        name: jobID
        required: true
        type: integer
      produces:
      - application/json
      responses:
        "200":
          description: OK
        "400":
          description: Bad Request
        "403":
          description: Forbidden
        "500":
          description: Internal Server Error
      summary: Update the logs collected from an Edge Job
      tags:
      - edge
      - endpoints
  /endpoints/{id}/edge/stacks/{stackId}:
    get:
      consumes:
      - application/json
      description: '**Access policy**: public'
      parameters:
      - description: Environment(Endpoint) Id
        in: path
        name: id
        required: true
        type: integer
      - description: EdgeStack Id
        in: path
        name: stackId
        required: true
        type: integer
      - description: Stack file version maintained by Portainer
        in: query
        name: version
        type: integer
      produces:
      - application/json
      responses:
        "200":
          description: OK
          schema:
            $ref: '#/definitions/edge.StackPayload'
        "400":
          description: Bad Request
        "404":
          description: Not Found
        "500":
          description: Internal Server Error
      summary: Inspect an Edge Stack for an Environment(Endpoint)
      tags:
      - edge
      - endpoints
      - edge_stacks
  /endpoints/{id}/edge/status:
    get:
      description: |-
        environment(endpoint) for edge agent to check status of environment(endpoint)
        **Access policy**: restricted only to Edge environments(endpoints)
      operationId: EndpointEdgeStatusInspect
      parameters:
      - description: Environment(Endpoint) identifier
        in: path
        name: id
        required: true
        type: integer
      responses:
        "200":
          description: Success
          schema:
            $ref: '#/definitions/endpointedge.endpointEdgeStatusInspectResponse'
        "400":
          description: Invalid request
        "403":
          description: Permission denied to access environment(endpoint)
        "404":
          description: Environment(Endpoint) not found
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Get environment(endpoint) status
      tags:
      - endpoints
  /endpoints/{id}/forceupdateservice:
    put:
      consumes:
      - application/json
      description: |-
        force update a docker service
        **Access policy**: authenticated
      operationId: endpointForceUpdateService
      parameters:
      - description: endpoint identifier
        in: path
        name: id
        required: true
        type: integer
      - description: details
        in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/endpoints.forceUpdateServicePayload'
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            $ref: '#/definitions/swarm.ServiceUpdateResponse'
        "400":
          description: Invalid request
        "403":
          description: Permission denied
        "404":
          description: endpoint not found
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: force update a docker service
      tags:
      - endpoints
  /endpoints/{id}/kubernetes/helm:
    get:
      consumes:
      - application/json
      description: '**Access policy**: authenticated'
      operationId: HelmList
      parameters:
      - description: Environment(Endpoint) identifier
        in: path
        name: id
        required: true
        type: integer
      - description: specify an optional namespace
        in: query
        name: namespace
        type: string
      - description: specify an optional filter
        in: query
        name: filter
        type: string
      - description: specify an optional selector
        in: query
        name: selector
        type: string
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            items:
              $ref: '#/definitions/release.ReleaseElement'
            type: array
        "400":
          description: Invalid environment(endpoint) identifier
        "401":
          description: Unauthorized
        "404":
          description: Environment(Endpoint) or ServiceAccount not found
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: List Helm Releases
      tags:
      - helm
    post:
      consumes:
      - application/json
      description: '**Access policy**: authenticated'
      operationId: HelmInstall
      parameters:
      - description: Environment(Endpoint) identifier
        in: path
        name: id
        required: true
        type: integer
      - description: Chart details
        in: body
        name: payload
        required: true
        schema:
          $ref: '#/definitions/helm.installChartPayload'
      - description: Dry run
        in: query
        name: dryRun
        type: boolean
      produces:
      - application/json
      responses:
        "201":
          description: Created
          schema:
            $ref: '#/definitions/github_com_portainer_portainer_pkg_libhelm_release.Release'
        "401":
          description: Unauthorized
        "404":
          description: Environment(Endpoint) or ServiceAccount not found
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Install Helm Chart
      tags:
      - helm
  /endpoints/{id}/kubernetes/helm/{name}:
    get:
      description: |-
        Get details of a helm release by release name
        **Access policy**: authenticated
      operationId: HelmGet
      parameters:
      - description: Environment(Endpoint) identifier
        in: path
        name: id
        required: true
        type: integer
      - description: Helm release name
        in: path
        name: name
        required: true
        type: string
      - description: specify an optional namespace
        in: query
        name: namespace
        type: string
      - description: show resources of the release
        in: query
        name: showResources
        type: boolean
      - description: specify an optional revision
        in: query
        name: revision
        type: integer
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            $ref: '#/definitions/github_com_portainer_portainer_pkg_libhelm_release.Release'
        "400":
          description: Invalid request payload, such as missing required fields or
            fields not meeting validation criteria.
        "401":
          description: Unauthorized access - the user is not authenticated or does
            not have the necessary permissions. Ensure that you have provided a valid
            API key or JWT token, and that you have the required permissions.
        "403":
          description: Permission denied - the user is authenticated but does not
            have the necessary permissions to access the requested resource or perform
            the specified operation. Check your user roles and permissions.
        "404":
          description: Unable to find an environment with the specified identifier.
        "500":
          description: Server error occurred while attempting to retrieve the release.
      security:
      - ApiKeyAuth: []
        jwt: []
      summary: Get a helm release
      tags:
      - helm
  /endpoints/{id}/kubernetes/helm/{release}:
    delete:
      description: '**Access policy**: authenticated'
      operationId: HelmDelete
      parameters:
      - description: Environment(Endpoint) identifier
        in: path
        name: id
        required: true
        type: integer
      - description: The name of the release/application to uninstall
        in: path
        name: release
        required: true
        type: string
      - description: An optional namespace
        in: query
        name: namespace
        type: string
      responses:
        "204":
          description: Success
        "400":
          description: Invalid environment(endpoint) id or bad request
        "401":
          description: Unauthorized
        "404":
          description: Environment(Endpoint) or ServiceAccount not found
        "500":
          description: Server error or helm error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Delete Helm Release
      tags:
      - helm
  /endpoints/{id}/kubernetes/helm/{release}/history:
    get:
      description: |-
        Get a historical list of releases by release name
        **Access policy**: authenticated
      operationId: HelmGetHistory
      parameters:
      - description: Environment(Endpoint) identifier
        in: path
        name: id
        required: true
        type: integer
      - description: Helm release name
        in: path
        name: name
        required: true
        type: string
      - description: specify an optional namespace
        in: query
        name: namespace
        type: string
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            items:
              $ref: '#/definitions/github_com_portainer_portainer_pkg_libhelm_release.Release'
            type: array
        "400":
          description: Invalid request payload, such as missing required fields or
            fields not meeting validation criteria.
        "401":
          description: Unauthorized access - the user is not authenticated or does
            not have the necessary permissions. Ensure that you have provided a valid
            API key or JWT token, and that you have the required permissions.
        "403":
          description: Permission denied - the user is authenticated but does not
            have the necessary permissions to access the requested resource or perform
            the specified operation. Check your user roles and permissions.
        "404":
          description: Unable to find an environment with the specified identifier.
        "500":
          description: Server error occurred while attempting to retrieve the historical
            list of releases.
      security:
      - ApiKeyAuth: []
        jwt: []
      summary: Get a historical list of releases
      tags:
      - helm
  /endpoints/{id}/kubernetes/helm/{release}/rollback:
    post:
      description: |-
        Rollback a helm release to a previous revision
        **Access policy**: authenticated
      operationId: HelmRollback
      parameters:
      - description: Environment(Endpoint) identifier
        in: path
        name: id
        required: true
        type: integer
      - description: Helm release name
        in: path
        name: release
        required: true
        type: string
      - description: specify an optional namespace
        in: query
        name: namespace
        type: string
      - description: specify the revision to rollback to (defaults to previous revision
          if not specified)
        in: query
        name: revision
        type: integer
      - description: 'wait for resources to be ready (default: false)'
        in: query
        name: wait
        type: boolean
      - description: 'wait for jobs to complete before marking the release as successful
          (default: false)'
        in: query
        name: waitForJobs
        type: boolean
      - description: 'performs pods restart for the resource if applicable (default:
          true)'
        in: query
        name: recreate
        type: boolean
      - description: 'force resource update through delete/recreate if needed (default:
          false)'
        in: query
        name: force
        type: boolean
      - description: 'time to wait for any individual Kubernetes operation in seconds
          (default: 300)'
        in: query
        name: timeout
        type: integer
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            $ref: '#/definitions/github_com_portainer_portainer_pkg_libhelm_release.Release'
