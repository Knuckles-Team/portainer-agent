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
          description: Unable to find an environment with the specified identifier
            or release name.
        "500":
          description: Server error occurred while attempting to rollback the release.
      security:
      - ApiKeyAuth: []
        jwt: []
      summary: Rollback a helm release
      tags:
      - helm
  /endpoints/{id}/kubernetes/helm/git/dryrun:
    post:
      consumes:
      - application/json
      description: '**Access policy**: authenticated'
      operationId: HelmGitDryRun
      parameters:
      - description: Environment(Endpoint) identifier
        in: path
        name: id
        required: true
        type: integer
      - description: Git Helm dry run details
        in: body
        name: payload
        required: true
        schema:
          $ref: '#/definitions/helm.gitHelmDryRunPayload'
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            $ref: '#/definitions/github_com_portainer_portainer_pkg_libhelm_release.Release'
        "400":
          description: Bad request
        "401":
          description: Unauthorized
        "404":
          description: Environment(Endpoint) not found
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
        jwt: []
      summary: Helm Git Dry Run
      tags:
      - helm
  /endpoints/{id}/mtls_certificate:
    get:
      description: |-
        Retrieve the mTLS certificate of an environment(endpoint).
        **Access policy**: administrator
      operationId: EndpointMTLSCertificate
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
            $ref: '#/definitions/endpoints.endpointMTLSCertResponse'
        "400":
          description: Invalid request
        "404":
          description: Environment(Endpoint) not found
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Get an environment(endpoint) mTLS certificate
      tags:
      - endpoints
  /endpoints/{id}/mtls_certificate_error:
    get:
      description: |-
        Retrieve the mTLS certificate of an environment(endpoint).
        **Access policy**: administrator
      operationId: EndpointMTLSAgentCertificateError
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
            $ref: '#/definitions/endpoints.endpointMTLSCertResponse'
        "400":
          description: Invalid request
        "404":
          description: Environment(Endpoint) not found
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Get an agent(endpoint) mTLS certificate
      tags:
      - endpoints
  /endpoints/{id}/pools/{rpn}/access:
    put:
      consumes:
      - application/json
      description: |-
        Update the access permissions on a namespace in the given environment. This endpoint allows adding or removing users and teams that can access the specified namespace. Please note that users or teams must be added to the environment before they can be added to the namespace.
        **Access policy**: Restricted. User must be an administrator or have appropriate permissions to modify namespace access.
      operationId: namespacesAccessUpdate
      parameters:
      - description: Environment identifier
        in: path
        name: id
        required: true
        type: integer
      - description: Namespace identifier
        in: path
        name: rpn
        required: true
        type: integer
      - description: Payload containing lists of users and teams to add or remove
          access for
        in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/endpoints.resourcePoolUpdatePayload'
      responses:
        "204":
          description: Success - Access permissions were successfully updated
        "400":
          description: Invalid request payload, such as missing required fields or
            fields not meeting validation criteria.
        "403":
          description: Permission denied - the user is authenticated but does not
            have the necessary permissions to access the requested resource or perform
            the specified operation. Check your user roles and permissions.
        "404":
          description: Unable to find an environment with the specified identifier.
        "500":
          description: Server error occurred while attempting to update namespace
            access permissions.
      security:
      - ApiKeyAuth: []
        jwt: []
      summary: Update namespace access for a given namespace
      tags:
      - endpoints
  /endpoints/{id}/registries:
    get:
      description: |-
        List all registries based on the current user authorizations in current environment.
        **Access policy**: authenticated
      operationId: endpointRegistriesList
      parameters:
      - description: required if kubernetes environment, will show registries by namespace
        in: query
        name: namespace
        type: string
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
            items:
              $ref: '#/definitions/portaineree.Registry'
            type: array
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: List Registries on environment
      tags:
      - endpoints
  /endpoints/{id}/registries/{registryId}:
    put:
      consumes:
      - application/json
      description: '**Access policy**: authenticated'
      operationId: endpointRegistryAccess
      parameters:
      - description: Environment(Endpoint) identifier
        in: path
        name: id
        required: true
        type: integer
      - description: Registry identifier
        in: path
        name: registryId
        required: true
        type: integer
      - description: details
        in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/endpoints.registryAccessPayload'
      produces:
      - application/json
      responses:
        "204":
          description: Success
        "400":
          description: Invalid request
        "403":
          description: Permission denied
        "404":
          description: Endpoint not found
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: update registry access for environment
      tags:
      - endpoints
  /endpoints/{id}/settings:
    put:
      consumes:
      - application/json
      description: |-
        Update settings for an environment(endpoint).
        **Access policy**: authenticated
      operationId: EndpointSettingsUpdate
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
          $ref: '#/definitions/endpoints.endpointSettingsUpdatePayload'
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
      summary: Update settings for an environment(endpoint)
      tags:
      - endpoints
  /endpoints/{id}/snapshot:
    post:
      description: |-
        Snapshots an environment(endpoint)
        **Access policy**: authenticated
      operationId: EndpointSnapshot
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
        "404":
          description: Environment(Endpoint) not found
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Snapshots an environment(endpoint)
      tags:
      - endpoints
  /endpoints/agent_versions:
    get:
      description: |-
        List all agent versions based on the current user authorizations and query parameters.
        **Access policy**: restricted
      operationId: AgentVersions
      produces:
      - application/json
      responses:
        "200":
          description: List of available agent versions
          schema:
            items:
              type: string
            type: array
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: List agent versions
      tags:
      - endpoints
  /endpoints/delete:
    post:
      consumes:
      - application/json
      description: |-
        Remove multiple environments and optionally clean-up associated resources.
        **Access policy**: Administrator only.
      operationId: EndpointDeleteBatch
      parameters:
      - description: List of environments to delete, with optional deleteCluster flag
          to clean-up associated resources (cloud environments only)
        in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/endpoints.endpointDeleteBatchPayload'
      produces:
      - application/json
      responses:
        "204":
          description: Environment(s) successfully deleted.
        "207":
          description: Partial success. Some environments were deleted successfully,
            while others failed.
          schema:
            $ref: '#/definitions/endpoints.endpointDeleteBatchPartialResponse'
        "400":
          description: Invalid request payload, such as missing required fields or
            fields not meeting validation criteria.
        "403":
          description: Unauthorized access or operation not allowed.
        "500":
          description: Server error occurred while attempting to delete the specified
            environments.
      security:
      - ApiKeyAuth: []
        jwt: []
      summary: Remove multiple environments
      tags:
      - endpoints
  /endpoints/edge/async:
    post:
      description: |-
        Environment(Endpoint) for edge agent to check status of environment(endpoint)
        **Access policy**: restricted only to Edge environments(endpoints)
      operationId: endpointEdgeAsync
      responses:
        "200":
          description: Success
          schema:
            $ref: '#/definitions/endpointedge.EdgeAsyncResponse'
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
  /endpoints/edge/generate-key:
    post:
      consumes:
      - application/json
      description: |-
        Generates a general edge key
        **Access policy**: admin
      parameters:
      - description: Generate Key Info
        in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/endpointedge.generateKeyResponse'
      produces:
      - application/json
      responses:
        "200":
          description: OK
        "400":
          description: Bad Request
        "500":
          description: Internal Server Error
      summary: Generate an EdgeKey
      tags:
      - edge
      - endpoints
  /endpoints/edge/trust:
    post:
      consumes:
      - application/json
      description: |-
        Associate one or more Edge environments, currently in the waiting room, with Portainer environments. This action effectively grants trust to these environments.
        **Access policy**: Administrator only.
      operationId: TrustEdgeEndpoints
      parameters:
      - description: Information about the environments to trust
        in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/endpointedge.endpointsTrustPayload'
      responses:
        "204":
          description: Environment(s) successfully associated.
        "400":
          description: Invalid request payload, such as missing required fields or
            fields not meeting validation criteria.
        "500":
          description: Server error occurred while attempting to associate the environments.
      security:
      - ApiKeyAuth: []
        jwt: []
      summary: Associate one or more Edge environments in the waiting room to environments
      tags:
      - endpoints
  /endpoints/global-key:
    post:
      operationId: EndpointCreateGlobalKey
      responses:
        "200":
          description: Success
          schema:
            $ref: '#/definitions/endpoints.endpointCreateGlobalKeyResponse'
        "400":
          description: Invalid request
        "500":
          description: Server error
      summary: Create or retrieve the endpoint for an EdgeID
      tags:
      - endpoints
  /endpoints/relations:
    put:
      consumes:
      - application/json
      description: |-
        Update relations for a list of environments
        Edge groups, tags and environment group can be updated.

        **Access policy**: administrator
      operationId: EndpointUpdateRelations
      parameters:
      - description: Environment relations data
        in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/endpoints.endpointUpdateRelationsPayload'
      responses:
        "204":
          description: Success
        "400":
          description: Invalid request
        "401":
          description: Unauthorized
        "404":
          description: Not found
        "500":
          description: Server error
      security:
      - jwt: []
      summary: Update relations for a list of environments
      tags:
      - endpoints
  /endpoints/snapshot:
    post:
      description: |-
        Snapshot all environments(endpoints)
        **Access policy**: administrator
      operationId: EndpointSnapshots
      responses:
        "204":
          description: Success
        "500":
          description: Server Error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Snapshot all environment(endpoint)
      tags:
      - endpoints
  /gitops/repo/file/preview:
    post:
      description: |-
        Retrieve the compose file content based on git repository configuration
        **Access policy**: authenticated
      operationId: GitOperationRepoFilePreview
      parameters:
      - description: Template details
        in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/gitops.repositoryFilePreviewPayload'
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            $ref: '#/definitions/gitops.fileResponse'
        "400":
          description: Invalid request
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: preview the content of target file in the git repository
      tags:
      - gitops
  /gitops/repo/files/search:
    post:
      description: |-
        Search the file path from the git repository based on partial or completed filename
        **Access policy**: authenticated
      operationId: GitOperationRepoFilesSearch
      parameters:
      - description: list the results without using cache
        in: query
        name: force
        type: boolean
      - description: details
        in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/gitops.repositoryFileSearchPayload'
      responses:
        "200":
          description: Success
          schema:
            items:
              type: string
            type: array
        "400":
          description: Invalid request
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Search the file path from a git repository files with specified extensions
      tags:
      - gitops
  /gitops/repo/helm/values:
    post:
      description: |-
        Load and merge multiple Helm values files from a Git repository, mimicking Helm CLI behavior
        **Access policy**: authenticated
      operationId: GitOperationRepoHelmValues
      parameters:
      - description: Helm values preview request
        in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/gitops.helmValuesPreviewPayload'
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            $ref: '#/definitions/gitops.helmValuesPreviewResponse'
        "400":
          description: Invalid request
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Preview merged Helm values files from git repository
      tags:
      - gitops
  /gitops/repo/refs:
    post:
      description: |-
        List all the refs of a git repository
        Will return all refs of a git repository
        **Access policy**: authenticated
      operationId: GitOperationRepoRefs
      parameters:
      - description: list the results without using cache
        in: query
        name: force
        type: boolean
      - description: details
        in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/gitops.repositoryReferenceListPayload'
      responses:
        "200":
          description: Success
          schema:
            items:
              type: string
            type: array
        "400":
          description: Invalid request
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: List the refs of a git repository
      tags:
      - gitops
  /kubernetes/{environmentId}/opa:
    get:
      consumes:
      - application/json
      description: |-
        Get Pod Security Rule within k8s cluster
        **Access policy**: authenticated
      operationId: getKubernetesPodSecurityRule
      parameters:
      - description: Environment identifier
        in: path
        name: environmentId
        required: true
        type: integer
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            $ref: '#/definitions/podsecurity.PodSecurityRule'
        "400":
          description: Invalid request
        "404":
          description: Endpoint not found
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Get Pod Security Rule within k8s cluster, if not found, the frontend
        will create a default
      tags:
      - kubernetes
    put:
      consumes:
      - application/json
      description: |-
        Update Pod Security Rule within k8s cluster
        **Access policy**: authenticated
      operationId: updateK8sPodSecurityRule
      parameters:
      - description: Environment(Endpoint) identifier
        in: path
        name: environmentId
        required: true
        type: integer
      produces:
      - application/json
      responses:
        "200":
          description: Success
        "400":
          description: Invalid request
        "404":
          description: Pod Security Rule not found
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Update Pod Security Rule within k8s cluster
      tags:
      - kubernetes
  /kubernetes/{id}/applications:
    get:
      consumes:
      - application/json
      description: |-
        Get a list of applications across all namespaces in the cluster. If the nodeName is provided, it will return the applications running on that node.
        **Access policy**: authenticated
      operationId: GetAllKubernetesApplications
      parameters:
      - description: Environment(Endpoint) identifier
        in: path
        name: id
        required: true
        type: integer
      - description: Namespace name
        in: query
        name: namespace
        required: true
        type: string
      - description: Node name
        in: query
        name: nodeName
        required: true
        type: string
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            items:
              $ref: '#/definitions/models.K8sApplication'
            type: array
        "400":
          description: Invalid request
        "401":
          description: Unauthorized
        "403":
          description: Permission denied
        "404":
          description: Environment(Endpoint) not found
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
        jwt: []
      summary: Get a list of applications across all namespaces in the cluster. If
        the nodeName is provided, it will return the applications running on that
        node.
      tags:
      - kubernetes
  /kubernetes/{id}/applications/count:
    get:
      description: |-
        Get the count of Applications across all namespaces in the cluster. If the nodeName is provided, it will return the count of applications running on that node.
        **Access policy**: Authenticated user.
      operationId: getAllKubernetesApplicationsCount
      parameters:
      - description: Environment identifier
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
            type: integer
        "400":
          description: Invalid request payload, such as missing required fields or
            fields not meeting validation criteria.
        "403":
          description: Unauthorized access or operation not allowed.
        "500":
          description: Server error occurred while attempting to retrieve the count
            of all applications from the cluster.
      security:
      - ApiKeyAuth: []
        jwt: []
      summary: Get Applications count
      tags:
      - kubernetes
  /kubernetes/{id}/cluster_role_bindings/delete:
    post:
      consumes:
      - application/json
      description: |-
        Delete the provided list of cluster role bindings.
        **Access policy**: Authenticated user.
      operationId: DeleteClusterRoleBindings
      parameters:
      - description: Environment identifier
        in: path
        name: id
        required: true
        type: integer
      - description: A list of cluster role bindings to delete
        in: body
        name: payload
        required: true
        schema:
          items:
            type: string
          type: array
      responses:
        "204":
          description: Success
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
          description: Unable to find an environment with the specified identifier
            or unable to find a specific cluster role binding.
        "500":
          description: Server error occurred while attempting to delete cluster role
