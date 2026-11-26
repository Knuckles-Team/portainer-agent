      responses:
        "200":
          description: Success
          schema:
            items:
              $ref: '#/definitions/sshtest.SSHTestResult'
            type: array
        "400":
          description: Invalid request
        "500":
          description: Server error
        "503":
          description: Missing configuration
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Test SSH connection to nodes
      tags:
      - kaas
  /custom_templates:
    get:
      description: |-
        List available custom templates.
        **Access policy**: authenticated
      operationId: CustomTemplateList
      parameters:
      - collectionFormat: csv
        description: Template types
        in: query
        items:
          enum:
          - 1
          - 2
          - 3
          type: integer
        name: type
        required: true
        type: array
      - description: Filter by edge templates
        in: query
        name: edge
        type: boolean
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            items:
              $ref: '#/definitions/portaineree.CustomTemplate'
            type: array
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: List available custom templates
      tags:
      - custom_templates
    post:
      consumes:
      - application/json
      - multipart/form-data
      deprecated: true
      description: |-
        Create a custom template.
        **Access policy**: authenticated
      operationId: CustomTemplateCreate
      parameters:
      - description: method for creating template
        enum:
        - string
        - file
        - repository
        in: query
        name: method
        required: true
        type: string
      - description: for body documentation see the relevant /custom_templates/{method}
          endpoint
        in: body
        name: body
        required: true
        schema:
          type: object
      produces:
      - application/json
      responses:
        "200":
          description: OK
          schema:
            $ref: '#/definitions/portaineree.CustomTemplate'
        "400":
          description: Invalid request
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Create a custom template
      tags:
      - custom_templates
  /custom_templates/{id}:
    delete:
      description: |-
        Remove a template.
        **Access policy**: authenticated
      operationId: CustomTemplateDelete
      parameters:
      - description: Template identifier
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
          description: Access denied to resource
        "404":
          description: Template not found
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Remove a template
      tags:
      - custom_templates
    get:
      description: |-
        Retrieve details about a template.
        **Access policy**: authenticated
      operationId: CustomTemplateInspect
      parameters:
      - description: Template identifier
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
            $ref: '#/definitions/portaineree.CustomTemplate'
        "400":
          description: Invalid request
        "404":
          description: Template not found
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Inspect a custom template
      tags:
      - custom_templates
    put:
      consumes:
      - application/json
      description: |-
        Update a template.
        **Access policy**: authenticated
      operationId: CustomTemplateUpdate
      parameters:
      - description: Template identifier
        in: path
        name: id
        required: true
        type: integer
      - description: Template details
        in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/customtemplates.customTemplateUpdatePayload'
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            $ref: '#/definitions/portaineree.CustomTemplate'
        "400":
          description: Invalid request
        "403":
          description: Permission denied to access template
        "404":
          description: Template not found
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Update a template
      tags:
      - custom_templates
  /custom_templates/{id}/file:
    get:
      description: |-
        Retrieve the content of the Stack file for the specified custom template
        **Access policy**: authenticated
      operationId: CustomTemplateFile
      parameters:
      - description: Template identifier
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
            $ref: '#/definitions/customtemplates.fileResponse'
        "400":
          description: Invalid request
        "404":
          description: Custom template not found
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Get Template stack file content.
      tags:
      - custom_templates
  /custom_templates/{id}/git_fetch:
    put:
      description: |-
        Retrieve details about a template created from git repository method.
        **Access policy**: authenticated
      operationId: CustomTemplateGitFetch
      parameters:
      - description: Template identifier
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
            $ref: '#/definitions/customtemplates.fileResponse'
        "400":
          description: Invalid request
        "404":
          description: Custom template not found
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Fetch the latest config file content based on custom template's git
        repository configuration
      tags:
      - custom_templates
  /custom_templates/create/file:
    post:
      consumes:
      - multipart/form-data
      description: |-
        Create a custom template.
        **Access policy**: authenticated
      operationId: CustomTemplateCreateFile
      parameters:
      - description: Title of the template
        in: formData
        name: Title
        required: true
        type: string
      - description: Description of the template
        in: formData
        name: Description
        required: true
        type: string
      - description: A note that will be displayed in the UI. Supports HTML content
        in: formData
        name: Note
        required: true
        type: string
      - description: Platform associated to the template (1 - 'linux', 2 - 'windows')
        enum:
        - 1
        - 2
        in: formData
        name: Platform
        required: true
        type: integer
      - description: Type of created stack (1 - swarm, 2 - compose, 3 - kubernetes)
        enum:
        - 1
        - 2
        - 3
        in: formData
        name: Type
        required: true
        type: integer
      - description: File
        in: formData
        name: File
        required: true
        type: file
      - description: URL of the template's logo
        in: formData
        name: Logo
        type: string
      - description: A json array of variables definitions
        in: formData
        name: Variables
        type: string
      - description: Indicates if this template purpose for Edge Stack
        in: formData
        name: EdgeTemplate
        type: boolean
      - description: A json object of edge config
        in: formData
        name: EdgeSettings
        type: string
      produces:
      - application/json
      responses:
        "200":
          description: OK
          schema:
            $ref: '#/definitions/portaineree.CustomTemplate'
        "400":
          description: Invalid request
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Create a custom template
      tags:
      - custom_templates
  /custom_templates/create/repository:
    post:
      consumes:
      - application/json
      description: |-
        Create a custom template.
        **Access policy**: authenticated
      operationId: CustomTemplateCreateRepository
      parameters:
      - description: Required when using method=repository
        in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/customtemplates.customTemplateFromGitRepositoryPayload'
      produces:
      - application/json
      responses:
        "200":
          description: OK
          schema:
            $ref: '#/definitions/portaineree.CustomTemplate'
        "400":
          description: Invalid request
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Create a custom template
      tags:
      - custom_templates
  /custom_templates/create/string:
    post:
      consumes:
      - application/json
      description: |-
        Create a custom template.
        **Access policy**: authenticated
      operationId: CustomTemplateCreateString
      parameters:
      - description: body
        in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/customtemplates.customTemplateFromFileContentPayload'
      produces:
      - application/json
      responses:
        "200":
          description: OK
          schema:
            $ref: '#/definitions/portaineree.CustomTemplate'
        "400":
          description: Invalid request
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Create a custom template
      tags:
      - custom_templates
  /docker/{environmentId}/containers/{containerId}/gpus:
    get:
      consumes:
      - application/json
      description: '**Access policy**:'
      operationId: dockerContainerGpusInspect
      parameters:
      - description: Environment identifier
        in: path
        name: environmentId
        required: true
        type: integer
      - description: Container identifier
        in: path
        name: containerId
        required: true
        type: integer
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            $ref: '#/definitions/containers.containerGpusResponse'
        "400":
          description: Bad request
        "404":
          description: Environment or container not found
        "500":
          description: Internal server error
      security:
      - jwt: []
      summary: Fetch container gpus data
      tags:
      - docker
  /docker/{environmentId}/containers/{containerId}/image_status:
    get:
      consumes:
      - application/json
      description: '**Access policy**:'
      operationId: containerImageStatus
      parameters:
      - description: Environment identifier
        in: path
        name: environmentId
        required: true
        type: integer
      - description: Container identifier
        in: path
        name: containerId
        required: true
        type: integer
      - description: Refresh will force a refresh of the image status cache
        in: query
        name: refresh
        type: boolean
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            $ref: '#/definitions/images.StatusResponse'
        "400":
          description: Bad request
        "500":
          description: Internal server error
      security:
      - jwt: []
      summary: Fetch image status for container
      tags:
      - docker
  /docker/{environmentId}/containers/image_status/clear:
    post:
      consumes:
      - application/json
      description: |-
        Clear the image status cache for all containers in the environment
        **Access policy**:
      operationId: containersImageStatusClear
      parameters:
      - description: Environment identifier
        in: path
        name: environmentId
        required: true
        type: integer
      produces:
      - application/json
      responses:
        "204":
          description: Success
        "400":
          description: Bad request
        "500":
          description: Internal server error
      security:
      - jwt: []
      summary: Clear container image status cache
      tags:
      - docker
  /docker/{environmentId}/dashboard:
    get:
      consumes:
      - application/json
      description: '**Access policy**: restricted'
      operationId: dockerDashboard
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
            $ref: '#/definitions/docker.dashboardResponse'
        "400":
          description: Bad request
        "500":
          description: Internal server error
      security:
      - jwt: []
      summary: Get counters for the dashboard
      tags:
      - docker
  /docker/{environmentId}/images:
    get:
      description: '**Access policy**:'
      operationId: dockerImagesList
      parameters:
      - description: Environment identifier
        in: path
        name: environmentId
        required: true
        type: integer
      - description: Include image usage information
        in: query
        name: withUsage
        type: boolean
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            items:
              $ref: '#/definitions/images.ImageResponse'
            type: array
        "400":
          description: Bad request
        "500":
          description: Internal server error
      security:
      - jwt: []
      summary: Fetch images
      tags:
      - docker
  /docker/{environmentId}/services/{serviceId}/image_status:
    get:
      consumes:
      - application/json
      description: '**Access policy**:'
      operationId: ServiceImageStatus
      parameters:
      - description: Environment identifier
        in: path
        name: environmentId
        required: true
        type: integer
      - description: Service identifier
        in: path
        name: serviceId
        required: true
        type: integer
      - description: Refresh will force a refresh of the image status cache
        in: query
        name: refresh
        type: boolean
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            $ref: '#/definitions/images.StatusResponse'
        "400":
          description: Bad request
        "500":
          description: Internal server error
      security:
      - jwt: []
      summary: Fetch image status for service
      tags:
      - docker
  /docker/{environmentId}/services/image_status/clear:
    post:
      consumes:
      - application/json
      description: |-
        Clear the image status cache for all services in the environment
        **Access policy**:
      operationId: serviceImageStatusClear
      parameters:
      - description: Environment identifier
        in: path
        name: environmentId
        required: true
        type: integer
      produces:
      - application/json
      responses:
        "204":
          description: Success
        "400":
          description: Bad request
        "500":
          description: Internal server error
      security:
      - jwt: []
      summary: Clear service image status cache
      tags:
      - docker
  /docker/{environmentId}/snapshot:
    get:
      consumes:
      - application/json
      description: '**Access policy**:'
      operationId: snapshotInspect
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
            $ref: '#/definitions/portainer.DockerSnapshotRaw'
        "404":
          description: Environment not found
      security:
      - jwt: []
      summary: Fetch latest snapshot of environment
      tags:
      - endpoints
      - docker
  /docker/{environmentId}/snapshot/containers:
    get:
      consumes:
      - application/json
      description: '**Access policy**:'
      operationId: snapshotContainersList
      parameters:
      - description: Environment identifier
        in: path
        name: environmentId
        required: true
        type: integer
      - description: Edge stack identifier, will return only containers for this edge
          stack
        in: query
        name: edgeStackId
        type: integer
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            $ref: '#/definitions/portainer.DockerContainerSnapshot'
        "404":
          description: Environment not found
      security:
      - jwt: []
      summary: Fetch containers list from a snapshot
      tags:
      - endpoints
      - docker
  /docker/{environmentId}/snapshot/containers/{containerId}:
    get:
      consumes:
      - application/json
      description: '**Access policy**:'
      operationId: snapshotContainerInspect
      parameters:
      - description: Environment identifier
        in: path
        name: environmentId
        required: true
        type: integer
      - description: Container identifier
        in: path
        name: containerId
        required: true
        type: integer
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            $ref: '#/definitions/portainer.DockerContainerSnapshot'
        "404":
          description: Environment not found
      security:
      - jwt: []
      summary: Fetch container from a snapshot
      tags:
      - endpoints
      - docker
  /edge_configurations:
    get:
      consumes:
      - application/json
      description: '**Access policy**: authenticated'
      operationId: EdgeConfigList
      parameters:
      - description: body
        in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/edgeconfigs.edgeConfigCreatePayload'
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            items:
              $ref: '#/definitions/portaineree.EdgeConfig'
            type: array
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: List available Edge Configurations
      tags:
      - edge_configs
    post:
      consumes:
      - multipart/form-data
      description: |-
        Create an Edge Configuration.
        **Access policy**: authenticated
      operationId: EdgeConfigCreate
      parameters:
      - in: formData
        name: BaseDir
        type: string
      - enum:
        - configuration
        - secret
        in: formData
        name: Category
        type: string
        x-enum-varnames:
        - EdgeConfigCategoryConfig
        - EdgeConfigCategorySecret
      - collectionFormat: csv
        in: formData
        items:
          type: integer
        name: EdgeGroupIDs
        type: array
      - in: formData
        name: Name
        type: string
      - in: formData
        name: Type
        type: string
      - description: File
        in: formData
        name: File
        required: true
        type: file
      responses:
        "204":
          description: No Content
        "400":
          description: Invalid request
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Create an Edge Configuration
      tags:
      - edge_configs
  /edge_configurations/{id}:
    delete:
      description: |-
        Delete an Edge configuration.
        **Access policy**: authenticated
      operationId: EdgeConfigDelete
      parameters:
      - description: Edge configuration identifier
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
          description: Edge configuration not found
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Delete an Edge configuration
      tags:
      - edge_configs
    get:
      description: |-
        Retrieve details about an Edge configuration.
        **Access policy**: authenticated
      operationId: EdgeConfigInspect
      parameters:
      - description: Edge configuration identifier
        in: path
        name: id
        required: true
        type: integer
      responses:
        "200":
          description: Success
          schema:
            $ref: '#/definitions/portaineree.EdgeConfig'
        "400":
          description: Invalid request
        "404":
          description: Edge configuration not found
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Inspect an Edge configuration
      tags:
      - edge_configs
    put:
      consumes:
      - multipart/form-data
      description: |-
        Update an Edge Configuration.
        **Access policy**: authenticated
      operationId: EdgeConfigUpdate
      parameters:
      - description: Edge configuration identifier
        in: path
        name: id
        required: true
        type: integer
      - collectionFormat: csv
        in: formData
        items:
          type: integer
        name: EdgeGroupIDs
        type: array
      - in: formData
        name: Type
        type: string
      - description: File
        in: formData
        name: File
        required: true
        type: file
      produces:
      - application/json
      responses:
        "204":
          description: No Content
        "400":
          description: Invalid request
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Update an Edge Configuration
      tags:
      - edge_configs
  /edge_configurations/{id}/{state}:
    put:
      description: Used by the standard edge agent to update the state of an Edge
        configuration.
      operationId: EdgeConfigState
      parameters:
      - description: Edge configuration identifier
        in: path
        name: id
        required: true
        type: integer
      - description: Edge configuration state
        in: path
        name: state
        required: true
        type: integer
      responses:
        "204":
          description: Success
        "400":
          description: Invalid request
        "403":
          description: Permission denied to access environment
        "404":
          description: Edge configuration not found
        "500":
          description: Server error
      summary: Update the state of an Edge configuration
      tags:
      - edge_configs
  /edge_configurations/{id}/files:
    get:
      description: Used by the standard edge agent to retrieve the files for an Edge
        configuration.
      operationId: EdgeConfigFiles
      parameters:
      - description: Edge configuration identifier
        in: path
        name: id
        required: true
        type: integer
      responses:
        "200":
          description: Success
          schema:
            type: string
        "400":
          description: Invalid request
        "403":
          description: Permission denied to access environment
        "404":
          description: Edge configuration not found
        "500":
          description: Server error
      summary: Get the files for an Edge configuration
      tags:
      - edge_configs
  /edge_groups:
    get:
      description: '**Access policy**: administrator'
      operationId: EdgeGroupList
      parameters:
      - description: will summarize the env count
        in: query
        name: summarize
        type: boolean
      produces:
      - application/json
      responses:
        "200":
          description: EdgeGroups
          schema:
            items:
              $ref: '#/definitions/edgegroups.decoratedEdgeGroup'
            type: array
        "500":
          description: Internal Server Error
        "503":
          description: Edge compute features are disabled
