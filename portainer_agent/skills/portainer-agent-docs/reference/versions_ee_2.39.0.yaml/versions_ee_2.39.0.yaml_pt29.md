          and anonymous volumes attached to containers. Only affects Docker Standalone
          stacks.
        in: query
        name: removeVolumes
        type: boolean
      - description: Environment identifier
        in: query
        name: endpointId
        required: true
        type: integer
      responses:
        "204":
          description: Success
        "400":
          description: Invalid request
        "403":
          description: Permission denied
        "404":
          description: Not found
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Remove a stack
      tags:
      - stacks
    get:
      description: |-
        Retrieve details about a stack.
        **Access policy**: restricted
      operationId: StackInspect
      parameters:
      - description: Stack identifier
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
            $ref: '#/definitions/portaineree.Stack'
        "400":
          description: Invalid request
        "403":
          description: Permission denied
        "404":
          description: Stack not found
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Inspect a stack
      tags:
      - stacks
    put:
      consumes:
      - application/json
      description: |-
        Update a stack, only for file based stacks.
        **Access policy**: authenticated
      operationId: StackUpdate
      parameters:
      - description: Stack identifier
        in: path
        name: id
        required: true
        type: integer
      - description: Environment identifier
        in: query
        name: endpointId
        required: true
        type: integer
      - description: Stack details
        in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/stacks.updateStackPayload'
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            $ref: '#/definitions/portaineree.Stack'
        "400":
          description: Invalid request
        "403":
          description: Permission denied
        "404":
          description: Not found
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Update a stack
      tags:
      - stacks
  /stacks/{id}/associate:
    put:
      description: '**Access policy**: administrator'
      operationId: StackAssociate
      parameters:
      - description: Stack identifier
        in: path
        name: id
        required: true
        type: integer
      - description: Environment identifier
        in: query
        name: endpointId
        required: true
        type: integer
      - description: Swarm identifier
        in: query
        name: swarmId
        required: true
        type: integer
      - description: Indicates whether the stack is orphaned
        in: query
        name: orphanedRunning
        required: true
        type: boolean
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            $ref: '#/definitions/portaineree.Stack'
        "400":
          description: Invalid request
        "403":
          description: Permission denied
        "404":
          description: Stack not found
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Associate an orphaned stack to a new environment(endpoint)
      tags:
      - stacks
  /stacks/{id}/file:
    get:
      description: |-
        Get Stack file content.
        **Access policy**: restricted
      operationId: StackFileInspect
      parameters:
      - description: Stack identifier
        in: path
        name: id
        required: true
        type: integer
      - description: Stack file version maintained by Portainer. If both version and
          commitHash are provided, the commitHash will be used
        in: query
        name: version
        type: integer
      - description: Git repository commit hash. If both version and commitHash are
          provided, the commitHash will be used
        in: query
        name: commitHash
        type: string
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            $ref: '#/definitions/stacks.stackFileResponse'
        "400":
          description: Invalid request
        "403":
          description: Permission denied
        "404":
          description: Stack not found
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Retrieve the content of the Stack file for the specified stack
      tags:
      - stacks
  /stacks/{id}/git:
    post:
      consumes:
      - application/json
      description: |-
        Update the Git settings in a stack, e.g., RepositoryReferenceName and AutoUpdate
        **Access policy**: authenticated
      operationId: StackUpdateGit
      parameters:
      - description: Stack identifier
        in: path
        name: id
        required: true
        type: integer
      - description: Stacks created before version 1.18.0 might not have an associated
          environment(endpoint) identifier. Use this optional parameter to set the
          environment(endpoint) identifier used by the stack.
        in: query
        name: endpointId
        type: integer
      - description: Git configs for pull and redeploy a stack
        in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/stacks.stackGitUpdatePayload'
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            $ref: '#/definitions/portaineree.Stack'
        "400":
          description: Invalid request
        "403":
          description: Permission denied
        "404":
          description: Not found
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Update a stack's Git configs
      tags:
      - stacks
  /stacks/{id}/git/redeploy:
    put:
      consumes:
      - application/json
      description: |-
        Pull and redeploy a stack via Git
        **Access policy**: authenticated
      operationId: StackGitRedeploy
      parameters:
      - description: Stack identifier
        in: path
        name: id
        required: true
        type: integer
      - description: Stacks created before version 1.18.0 might not have an associated
          environment(endpoint) identifier. Use this optional parameter to set the
          environment(endpoint) identifier used by the stack.
        in: query
        name: endpointId
        type: integer
      - description: Git configs for pull and redeploy of a stack. **StackName** may
          only be populated for Kuberenetes stacks, and if specified with a blank
          string, it will be set to blank
        in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/stacks.stackGitRedployPayload'
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            $ref: '#/definitions/portaineree.Stack'
        "400":
          description: Invalid request
        "403":
          description: Permission denied
        "404":
          description: Not found
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Redeploy a stack
      tags:
      - stacks
  /stacks/{id}/images_status:
    get:
      consumes:
      - application/json
      description: '**Access policy**:'
      operationId: stackImagesStatus
      parameters:
      - description: Stack identifier
        in: path
        name: id
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
      summary: Fetch image status for stack
      tags:
      - stacks
  /stacks/{id}/migrate:
    post:
      description: |-
        Migrate a stack from an environment(endpoint) to another environment(endpoint). It will re-create the stack inside the target environment(endpoint) before removing the original stack.
        **Access policy**: authenticated
      operationId: StackMigrate
      parameters:
      - description: Stack identifier
        in: path
        name: id
        required: true
        type: integer
      - description: Stacks created before version 1.18.0 might not have an associated
          environment(endpoint) identifier. Use this optional parameter to set the
          environment(endpoint) identifier used by the stack.
        in: query
        name: endpointId
        type: integer
      - description: Stack migration details
        in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/stacks.stackMigratePayload'
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            $ref: '#/definitions/portaineree.Stack'
        "400":
          description: Invalid request
        "403":
          description: Permission denied
        "404":
          description: Stack not found
        "409":
          description: A stack with the same name is already running on the target
            environment(endpoint)
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Migrate a stack to another environment(endpoint)
      tags:
      - stacks
  /stacks/{id}/start:
    post:
      description: |-
        Starts a stopped Stack.
        **Access policy**: authenticated
      operationId: StackStart
      parameters:
      - description: Stack identifier
        in: path
        name: id
        required: true
        type: integer
      - description: Environment identifier
        in: query
        name: endpointId
        required: true
        type: integer
      responses:
        "200":
          description: Success
          schema:
            $ref: '#/definitions/portaineree.Stack'
        "400":
          description: Invalid request
        "403":
          description: Permission denied
        "404":
          description: Not found
        "409":
          description: Stack name is not unique
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Starts a stopped Stack
      tags:
      - stacks
  /stacks/{id}/stop:
    post:
      description: |-
        Stops a stopped Stack.
        **Access policy**: authenticated
      operationId: StackStop
      parameters:
      - description: Stack identifier
        in: path
        name: id
        required: true
        type: integer
      - description: Environment identifier
        in: query
        name: endpointId
        required: true
        type: integer
      responses:
        "200":
          description: Success
          schema:
            $ref: '#/definitions/portaineree.Stack'
        "400":
          description: Invalid request
        "403":
          description: Permission denied
        "404":
          description: Not found
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Stops a stopped Stack
      tags:
      - stacks
  /stacks/create/kubernetes/repository:
    post:
      description: |-
        Deploy a new stack into a Docker environment specified via the environment identifier.
        **Access policy**: authenticated
      operationId: StackCreateKubernetesGit
      parameters:
      - description: stack config
        in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/stacks.kubernetesGitDeploymentPayload'
      - description: Identifier of the environment that will be used to deploy the
          stack
        in: query
        name: endpointId
        required: true
        type: integer
      produces:
      - application/json
      responses:
        "200":
          description: OK
          schema:
            $ref: '#/definitions/portaineree.Stack'
        "400":
          description: Invalid request
        "409":
          description: Webhook ID already exists
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Deploy a new kubernetes stack from a git repository
      tags:
      - stacks
  /stacks/create/kubernetes/string:
    post:
      description: |-
        Deploy a new stack into a Docker environment specified via the environment identifier.
        **Access policy**: authenticated
      operationId: StackCreateKubernetesFile
      parameters:
      - description: stack config
        in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/stacks.kubernetesStringDeploymentPayload'
      - description: Identifier of the environment that will be used to deploy the
          stack
        in: query
        name: endpointId
        required: true
        type: integer
      produces:
      - application/json
      responses:
        "200":
          description: OK
          schema:
            $ref: '#/definitions/portaineree.Stack'
        "400":
          description: Invalid request
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Deploy a new kubernetes stack from a file
      tags:
      - stacks
  /stacks/create/kubernetes/url:
    post:
      description: |-
        Deploy a new stack into a Docker environment specified via the environment identifier.
        **Access policy**: authenticated
      operationId: StackCreateKubernetesUrl
      parameters:
      - description: stack config
        in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/stacks.kubernetesManifestURLDeploymentPayload'
      - description: Identifier of the environment that will be used to deploy the
          stack
        in: query
        name: endpointId
        required: true
        type: integer
      produces:
      - application/json
      responses:
        "200":
          description: OK
          schema:
            $ref: '#/definitions/portaineree.Stack'
        "400":
          description: Invalid request
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Deploy a new kubernetes stack from a url
      tags:
      - stacks
  /stacks/create/standalone/file:
    post:
      consumes:
      - multipart/form-data
      description: |-
        Deploy a new stack into a Docker environment specified via the environment identifier.
        **Access policy**: authenticated
      operationId: StackCreateDockerStandaloneFile
      parameters:
      - description: Name of the stack
        in: formData
        name: Name
        required: true
        type: string
      - description: 'Environment variables passed during deployment, represented
          as a JSON array [{''name'': ''name'', ''value'': ''value''}].'
        in: formData
        name: Env
        type: string
      - description: Stack file
        in: formData
        name: file
        type: file
      - description: Identifier of the environment that will be used to deploy the
          stack
        in: query
        name: endpointId
        required: true
        type: integer
      produces:
      - application/json
      responses:
        "200":
          description: OK
          schema:
            $ref: '#/definitions/portaineree.Stack'
        "400":
          description: Invalid request
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Deploy a new compose stack from a file
      tags:
      - stacks
  /stacks/create/standalone/repository:
    post:
      consumes:
      - application/json
      description: |-
        Deploy a new stack into a Docker environment specified via the environment identifier.
        **Access policy**: authenticated
      operationId: StackCreateDockerStandaloneRepository
      parameters:
      - description: Identifier of the environment that will be used to deploy the
          stack
        in: query
        name: endpointId
        required: true
        type: integer
      - description: stack config
        in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/stacks.composeStackFromGitRepositoryPayload'
      produces:
      - application/json
      responses:
        "200":
          description: OK
          schema:
            $ref: '#/definitions/portaineree.Stack'
        "400":
          description: Invalid request
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Deploy a new compose stack from repository
      tags:
      - stacks
  /stacks/create/standalone/string:
    post:
      consumes:
      - application/json
      description: |-
        Deploy a new stack into a Docker environment specified via the environment identifier.
        **Access policy**: authenticated
      operationId: StackCreateDockerStandaloneString
      parameters:
      - description: stack config
        in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/stacks.composeStackFromFileContentPayload'
      - description: Identifier of the environment that will be used to deploy the
          stack
        in: query
        name: endpointId
        required: true
        type: integer
      produces:
      - application/json
      responses:
        "200":
          description: OK
          schema:
            $ref: '#/definitions/portaineree.Stack'
        "400":
          description: Invalid request
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Deploy a new compose stack from a text
      tags:
      - stacks
  /stacks/create/swarm/file:
    post:
      consumes:
      - multipart/form-data
      description: |-
        Deploy a new stack into a Docker environment specified via the environment identifier.
        **Access policy**: authenticated
      operationId: StackCreateDockerSwarmFile
      parameters:
      - description: Name of the stack
        in: formData
        name: Name
        type: string
      - description: Swarm cluster identifier.
        in: formData
        name: SwarmID
        type: string
      - description: 'Environment variables passed during deployment, represented
          as a JSON array [{''name'': ''name'', ''value'': ''value''}]. Optional'
        in: formData
        name: Env
        type: string
      - description: Stack file
        in: formData
        name: file
        type: file
      - description: Identifier of the environment that will be used to deploy the
          stack
        in: query
        name: endpointId
        required: true
        type: integer
      produces:
      - application/json
      responses:
        "200":
          description: OK
          schema:
            $ref: '#/definitions/portaineree.Stack'
        "400":
          description: Invalid request
        "409":
          description: Stack name or webhook id is not unique
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Deploy a new swarm stack from a file
      tags:
      - stacks
  /stacks/create/swarm/repository:
    post:
      consumes:
      - application/json
      description: |-
        Deploy a new stack into a Docker environment specified via the environment identifier.
        **Access policy**: authenticated
      operationId: StackCreateDockerSwarmRepository
      parameters:
      - description: Identifier of the environment that will be used to deploy the
          stack
        in: query
        name: endpointId
        required: true
        type: integer
      - description: stack config
        in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/stacks.swarmStackFromGitRepositoryPayload'
      produces:
      - application/json
      responses:
        "200":
          description: OK
          schema:
            $ref: '#/definitions/portaineree.Stack'
        "400":
          description: Invalid request
        "409":
          description: Stack name or webhook id is not unique
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Deploy a new swarm stack from a git repository
      tags:
      - stacks
  /stacks/create/swarm/string:
    post:
      consumes:
      - application/json
      description: |-
        Deploy a new stack into a Docker environment specified via the environment identifier.
        **Access policy**: authenticated
      operationId: StackCreateDockerSwarmString
      parameters:
      - description: stack config
        in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/stacks.swarmStackFromFileContentPayload'
      - description: Identifier of the environment that will be used to deploy the
          stack
        in: query
        name: endpointId
        required: true
        type: integer
      produces:
      - application/json
      responses:
        "200":
          description: OK
          schema:
            $ref: '#/definitions/portaineree.Stack'
        "400":
          description: Invalid request
        "409":
          description: Stack name or webhook id is not unique
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Deploy a new swarm stack from a text
      tags:
      - stacks
  /stacks/image_status/clear:
    post:
      consumes:
      - application/json
      description: |-
        Clear the image status cache for all stacks in the environment
        **Access policy**:
      operationId: stacksImageStatusClear
      parameters:
      - description: Identifier of the environment(endpoint) that will be used to
          filter the stacks to clear the image status cache for
        in: query
        name: environmentId
        type: integer
      - description: Identifier of the swarm cluster that will be used to filter the
          stacks to clear the image status cache for
        in: query
        name: swarmId
        type: string
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
      summary: Clear stack image status cache
      tags:
      - docker
  /stacks/name/{name}:
    delete:
      description: |-
        Remove a stack.
        **Access policy**: restricted
      operationId: StackDeleteKubernetesByName
      parameters:
      - description: Stack name
        in: path
        name: name
        required: true
        type: string
      - description: Set to true to delete an external stack. Only external Swarm
          stacks are supported
        in: query
        name: external
        type: boolean
      - description: Environment identifier
        in: query
        name: endpointId
        required: true
        type: integer
      responses:
        "204":
          description: Success
        "400":
          description: Invalid request
        "403":
          description: Permission denied
        "404":
          description: Not found
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Remove Kubernetes stacks by name
      tags:
      - stacks
  /stacks/webhooks/{webhookID}:
    post:
      description: '**Access policy**: public'
      operationId: StacksWebhookInvoke
      parameters:
      - description: Stack identifier
        in: path
        name: webhookID
        required: true
        type: string
      responses:
        "200":
          description: Success
        "400":
          description: Invalid request
        "409":
          description: Autoupdate for the stack isn't available
        "500":
          description: Server error
      summary: Webhook for triggering stack updates from git
      tags:
      - stacks
  /status:
    get:
      deprecated: true
      description: |-
        Deprecated: use the `/system/status` endpoint instead.
        Retrieve Portainer status
        **Access policy**: public
