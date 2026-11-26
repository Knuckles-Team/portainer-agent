        **Access policy**: administrator
      operationId: PolicyMetadata
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            $ref: '#/definitions/policies.policyMetadataResponse'
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Get policy metadata
      tags:
      - policies
  /policies/templates:
    get:
      description: |-
        List all built-in policy templates. Templates can be filtered by category or type.
        **Access policy**: administrator
      operationId: PolicyTemplateList
      parameters:
      - description: Filter by category (rbac, security, setup, registry)
        in: query
        name: category
        type: string
      - description: Filter by policy type (e.g., security-k8s, security-docker)
        in: query
        name: type
        type: string
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            $ref: '#/definitions/policies.templateListResponse'
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: List policy templates
      tags:
      - policies
  /policies/templates/{id}:
    get:
      description: |-
        Retrieve a specific policy template by ID.
        **Access policy**: administrator
      operationId: PolicyTemplateInspect
      parameters:
      - description: Template ID
        in: path
        name: id
        required: true
        type: string
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            $ref: '#/definitions/policies.PolicyTemplate'
        "404":
          description: Template not found
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Inspect a policy template
      tags:
      - policies
  /registries:
    get:
      description: |-
        List all registries.
        Administrators and edge-admins receive the full registry record (minus passwords).
        All other authenticated users receive a scrubbed record containing only ID, Name, and Type.
        **Access policy**: authenticated
      operationId: RegistryList
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
      summary: List Registries
      tags:
      - registries
    post:
      consumes:
      - application/json
      description: |-
        Create a new registry.
        **Access policy**: restricted
      operationId: RegistryCreate
      parameters:
      - description: Registry details
        in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/registries.registryCreatePayload'
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            $ref: '#/definitions/portaineree.Registry'
        "400":
          description: Invalid request
        "409":
          description: Another registry with either the same name or same URL & credeintials
            already exists
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Create a new registry
      tags:
      - registries
  /registries/{id}:
    delete:
      description: |-
        Remove a registry
        **Access policy**: restricted
      operationId: RegistryDelete
      parameters:
      - description: Registry identifier
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
          description: Registry not found
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Remove a registry
      tags:
      - registries
    get:
      description: |-
        Retrieve details about a registry. If endpointId is provided, applies policy overrides for that environment.
        **Access policy**: restricted
      operationId: RegistryInspect
      parameters:
      - description: Registry identifier
        in: path
        name: id
        required: true
        type: integer
      - description: Environment identifier (applies policy overrides if provided)
        in: query
        name: endpointId
        type: integer
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            $ref: '#/definitions/portaineree.Registry'
        "400":
          description: Invalid request
        "403":
          description: Permission denied to access registry
        "404":
          description: Registry not found
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Inspect a registry
      tags:
      - registries
    put:
      consumes:
      - application/json
      description: |-
        Update a registry
        **Access policy**: restricted
      operationId: RegistryUpdate
      parameters:
      - description: Registry identifier
        in: path
        name: id
        required: true
        type: integer
      - description: Registry details
        in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/registries.registryUpdatePayload'
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            $ref: '#/definitions/portaineree.Registry'
        "400":
          description: Invalid request
        "404":
          description: Registry not found
        "409":
          description: Another registry with either the same name or same URL & credentials
            already exists
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Update a registry
      tags:
      - registries
  /registries/{id}/configure:
    post:
      consumes:
      - application/json
      description: |-
        Configures a registry.
        **Access policy**: restricted
      operationId: RegistryConfigure
      parameters:
      - description: Registry identifier
        in: path
        name: id
        required: true
        type: integer
      - description: Registry configuration
        in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/registries.registryConfigurePayload'
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
          description: Registry not found
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Configures a registry
      tags:
      - registries
  /registries/{id}/ecr/repositories/{repositoryName}:
    delete:
      description: |-
        Delete ECR repository.
        **Access policy**: restricted
      operationId: ecrDeleteRepository
      parameters:
      - description: Registry identifier
        in: path
        name: id
        required: true
        type: integer
      - description: Repository name
        in: path
        name: repositoryName
        required: true
        type: string
      produces:
      - application/json
      responses:
        "200":
          description: Success
        "400":
          description: Invalid request
        "403":
          description: Permission denied to access registry
        "404":
          description: Registry not found
        "500":
          description: Server error
      security:
      - jwt: []
      summary: Delete ECR repository
      tags:
      - registries
  /registries/{id}/ecr/repositories/{repositoryName}/tags:
    delete:
      description: |-
        Delete tags for a given ECR repository
        **Access policy**: restricted
      operationId: ecrDeleteTags
      parameters:
      - description: Registry identifier
        in: path
        name: id
        required: true
        type: integer
      - description: Repository name
        in: path
        name: repositoryName
        required: true
        type: integer
      - description: Tag Array
        in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/registries.deleteTagsPayload'
      responses:
        "204":
          description: Success
        "400":
          description: Invalid request
        "403":
          description: Permission denied to access registry
        "404":
          description: Registry not found
        "500":
          description: Server error
      security:
      - jwt: []
      summary: Delete tags
      tags:
      - registries
  /registries/{id}/repositories/{repositoryName}/tags:
    delete:
      consumes:
      - application/json
      description: |-
        Delete tags for a given repository
        **Access policy**: restricted
      operationId: RepositoryTagsDelete
      parameters:
      - description: Registry identifier
        in: path
        name: id
        required: true
        type: integer
      - description: Repository name
        in: path
        name: repositoryName
        required: true
        type: string
      - description: Tags to delete
        in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/registries.repositoryTagsDeletePayload'
      responses:
        "204":
          description: Success
        "400":
          description: Invalid request
        "403":
          description: Permission denied to access registry
        "404":
          description: Registry not found
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
        jwt: []
      summary: Delete repository tags
      tags:
      - registries
  /registries/ping:
    post:
      consumes:
      - application/json
      description: |-
        Test connection to a registry with provided credentials
        **Access policy**: authenticated
      operationId: RegistryPing
      parameters:
      - description: Registry credentials to test
        in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/registries.registryPingPayload'
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            $ref: '#/definitions/registries.registryPingResponse'
        "400":
          description: Invalid request
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Test registry connection
      tags:
      - registries
  /resource_controls:
    post:
      consumes:
      - application/json
      description: |-
        Create a new resource control to restrict access to a Docker resource.
        **Access policy**: administrator
      operationId: ResourceControlCreate
      parameters:
      - description: Resource control details
        in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/resourcecontrols.resourceControlCreatePayload'
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            $ref: '#/definitions/portainer.ResourceControl'
        "400":
          description: Invalid request
        "409":
          description: A resource control is already associated to this resource
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Create a new resource control
      tags:
      - resource_controls
  /resource_controls/{id}:
    delete:
      description: |-
        Remove a resource control.
        **Access policy**: administrator
      operationId: ResourceControlDelete
      parameters:
      - description: Resource control identifier
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
          description: Resource control not found
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Remove a resource control
      tags:
      - resource_controls
    put:
      consumes:
      - application/json
      description: |-
        Update a resource control
        **Access policy**: authenticated
      operationId: ResourceControlUpdate
      parameters:
      - description: Resource control identifier
        in: path
        name: id
        required: true
        type: integer
      - description: Resource control details
        in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/resourcecontrols.resourceControlUpdatePayload'
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            $ref: '#/definitions/portainer.ResourceControl'
        "400":
          description: Invalid request
        "403":
          description: Unauthorized
        "404":
          description: Resource control not found
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Update a resource control
      tags:
      - resource_controls
  /restore:
    post:
      consumes:
      - application/json
      description: |-
        Triggers a system restore using provided backup file
        **Access policy**: public
      operationId: Restore
      parameters:
      - description: Restore request payload
        in: body
        name: restorePayload
        required: true
        schema:
          $ref: '#/definitions/backup.restorePayload'
      responses:
        "200":
          description: Success
        "400":
          description: Invalid request
        "500":
          description: Server error
      summary: Triggers a system restore using provided backup file
      tags:
      - backup
  /roles:
    get:
      description: |-
        List all roles available for use
        **Access policy**: authenticated
      operationId: RoleList
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            items:
              $ref: '#/definitions/portaineree.Role'
            type: array
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: List roles
      tags:
      - roles
  /settings:
    get:
      description: |-
        Retrieve Portainer settings.
        **Access policy**: administrator
      operationId: SettingsInspect
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            $ref: '#/definitions/portaineree.Settings'
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Retrieve Portainer settings
      tags:
      - settings
    put:
      consumes:
      - application/json
      description: |-
        Update Portainer settings.
        **Access policy**: administrator
      operationId: SettingsUpdate
      parameters:
      - description: New settings
        in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/settings.settingsUpdatePayload'
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            $ref: '#/definitions/portaineree.Settings'
        "400":
          description: Invalid request
        "409":
          description: Edge Compute features cannot be disabled while they are in
            use
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Update Portainer settings
      tags:
      - settings
  /settings/additional_functionality:
    get:
      description: |-
        Retrieve Portainer additional functionality settings.
        **Access policy**: authenticated
      operationId: SettingsAdditionalFunctionalityInspect
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            $ref: '#/definitions/settings.settingsAdditionalFunctionalityInspectResponse'
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Retrieve Portainer additional functionality settings
      tags:
      - settings
    put:
      consumes:
      - application/json
      description: |-
        Update Portainer additional functionality settings.
        **Access policy**: administrator
      operationId: SettingsAdditionalFunctionalityUpdate
      parameters:
      - description: New settings
        in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/settings.settingsAdditionalFunctionalityUpdatePayload'
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
      summary: Update Portainer additional functionality settings
      tags:
      - settings
  /settings/default_registry:
    put:
      consumes:
      - application/json
      description: |-
        Update Portainer default registry settings.
        **Access policy**: administrator
      operationId: DefaultRegistryUpdate
      parameters:
      - description: Update default registry
        in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/settings.defaultRegistryUpdatePayload'
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            $ref: '#/definitions/portaineree.Settings'
        "400":
          description: Invalid request
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Update Portainer default registry settings
      tags:
      - settings
  /settings/edge/mtls_ca_certificate:
    get:
      description: |-
        Retrieve Portainer Edge MTLS CA Certificates.
        **Access policy**: administrator
      operationId: SettingsEdgeMTLSCACertificates
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            $ref: '#/definitions/settings.settingsCACertResponse'
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Retrieve Portainer Edge MTLS CA Certificates
      tags:
      - settings
  /settings/edge/mtls_certificate:
    get:
      description: |-
        Retrieve Portainer Edge MTLS Certificates.
        **Access policy**: administrator
      operationId: SettingsEdgeMTLSCertificates
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            $ref: '#/definitions/settings.settingsCertResponse'
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Retrieve Portainer Edge MTLS Certificates
      tags:
      - settings
  /settings/experimental:
    get:
      description: |-
        Retrieve Portainer experimental settings.
        **Access policy**: authenticated
      operationId: SettingsExperimentalInspect
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            $ref: '#/definitions/settings.settingsExperimentalInspectResponse'
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Retrieve Portainer experimental settings
      tags:
      - settings
    put:
      consumes:
      - application/json
      description: |-
        Update Portainer experimental settings.
        **Access policy**: administrator
      operationId: SettingsExperimentalUpdate
      parameters:
      - description: New settings
        in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/settings.settingsExperimentalUpdatePayload'
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
      summary: Update Portainer experimental settings
      tags:
      - settings
  /settings/public:
    get:
      description: |-
        Retrieve public settings. Returns a small set of settings that are not reserved to administrators only.
        **Access policy**: public
      operationId: SettingsPublic
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            $ref: '#/definitions/settings.publicSettingsResponse'
        "500":
          description: Server error
      summary: Retrieve Portainer public settings
      tags:
      - settings
  /sshkeygen:
    post:
      consumes:
      - application/json
      - multipart/form-data
      description: |-
        Generate an ssh public / private keypair
        **Access policy**: authenticated
      operationId: Generate
      produces:
      - application/json
      responses:
        "200":
          description: OK
          schema:
            $ref: '#/definitions/models.SSHKeyPair'
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Generate ssh keypair
      tags:
      - cloud_credentials
  /ssl:
    get:
      description: |-
        Retrieve the ssl settings.
        **Access policy**: administrator
      operationId: SSLInspect
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            $ref: '#/definitions/portaineree.SSLSettings'
        "400":
          description: Invalid request
        "403":
          description: Permission denied to access settings
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Inspect the ssl settings
      tags:
      - ssl
    put:
      consumes:
      - application/json
      description: |-
        Update the ssl settings.
        **Access policy**: administrator
      operationId: SSLUpdate
      parameters:
      - description: SSL Settings
        in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/ssl.sslUpdatePayload'
      produces:
      - application/json
      responses:
        "204":
          description: Success
        "400":
          description: Invalid request
        "403":
          description: Permission denied to access settings
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Update the ssl settings
      tags:
      - ssl
  /stacks:
    get:
      description: |-
        List all stacks based on the current user authorizations.
        Will return all stacks if using an administrator account otherwise it
        will only return the list of stacks the user have access to.
        Limited stacks will not be returned by this endpoint.
        **Access policy**: authenticated
      operationId: StackList
      parameters:
      - description: 'Filters to process on the stack list. Encoded as JSON (a map[string]string).
          For example, {''SwarmID'': ''jpofkc0i9uo9wtx1zesuk649w''} will only return
          stacks that are part of the specified Swarm cluster. Available filters:
          EndpointID, SwarmID.'
        in: query
        name: filters
        type: string
      responses:
        "200":
          description: Success
          schema:
            items:
              $ref: '#/definitions/portaineree.Stack'
            type: array
        "204":
          description: Success
        "400":
          description: Invalid request
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: List stacks
      tags:
      - stacks
  /stacks/{id}:
    delete:
      description: |-
        Remove a stack.
        **Access policy**: restricted
      operationId: StackDelete
      parameters:
      - description: Stack identifier
        in: path
        name: id
        required: true
        type: integer
      - description: Set to true to delete an external stack. Only external Swarm
          stacks are supported
        in: query
        name: external
        type: boolean
      - description: Set to true to delete named volumes declared in the stack file
