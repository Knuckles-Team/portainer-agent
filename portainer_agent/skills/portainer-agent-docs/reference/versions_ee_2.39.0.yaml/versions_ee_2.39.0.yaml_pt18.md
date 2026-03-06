      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: list EdgeGroups
      tags:
      - edge_groups
    post:
      consumes:
      - application/json
      description: '**Access policy**: administrator'
      operationId: EdgeGroupCreate
      parameters:
      - description: EdgeGroup data
        in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/edgegroups.edgeGroupCreatePayload'
      produces:
      - application/json
      responses:
        "200":
          description: OK
          schema:
            $ref: '#/definitions/portaineree.EdgeGroup'
        "500":
          description: Internal Server Error
        "503":
          description: Edge compute features are disabled
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Create an EdgeGroup
      tags:
      - edge_groups
  /edge_groups/{id}:
    delete:
      description: '**Access policy**: administrator'
      operationId: EdgeGroupDelete
      parameters:
      - description: EdgeGroup Id
        in: path
        name: id
        required: true
        type: integer
      responses:
        "204":
          description: No Content
        "409":
          description: Edge group is in use by an Edge stack, Edge job or Edge config
        "500":
          description: Server error
        "503":
          description: Edge compute features are disabled
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Deletes an EdgeGroup
      tags:
      - edge_groups
    get:
      description: '**Access policy**: administrator'
      operationId: EdgeGroupInspect
      parameters:
      - description: EdgeGroup Id
        in: path
        name: id
        required: true
        type: integer
      produces:
      - application/json
      responses:
        "200":
          description: OK
          schema:
            $ref: '#/definitions/portaineree.EdgeGroup'
        "500":
          description: Internal Server Error
        "503":
          description: Edge compute features are disabled
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Inspects an EdgeGroup
      tags:
      - edge_groups
    put:
      consumes:
      - application/json
      description: '**Access policy**: administrator'
      operationId: EdgeGroupUpdate
      parameters:
      - description: EdgeGroup Id
        in: path
        name: id
        required: true
        type: integer
      - description: EdgeGroup data
        in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/edgegroups.edgeGroupUpdatePayload'
      produces:
      - application/json
      responses:
        "200":
          description: OK
          schema:
            $ref: '#/definitions/portaineree.EdgeGroup'
        "500":
          description: Internal Server Error
        "503":
          description: Edge compute features are disabled
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Updates an EdgeGroup
      tags:
      - edge_groups
  /edge_jobs:
    get:
      description: '**Access policy**: administrator'
      operationId: EdgeJobList
      produces:
      - application/json
      responses:
        "200":
          description: OK
          schema:
            items:
              $ref: '#/definitions/portainer.EdgeJob'
            type: array
        "400":
          description: Bad Request
        "500":
          description: Internal Server Error
        "503":
          description: Edge compute features are disabled
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Fetch EdgeJobs list
      tags:
      - edge_jobs
  /edge_jobs/{id}:
    delete:
      description: '**Access policy**: administrator'
      operationId: EdgeJobDelete
      parameters:
      - description: EdgeJob Id
        in: path
        name: id
        required: true
        type: integer
      responses:
        "204":
          description: No Content
        "400":
          description: Bad Request
        "500":
          description: Internal Server Error
        "503":
          description: Edge compute features are disabled
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Delete an EdgeJob
      tags:
      - edge_jobs
    get:
      description: '**Access policy**: administrator'
      operationId: EdgeJobInspect
      parameters:
      - description: EdgeJob Id
        in: path
        name: id
        required: true
        type: integer
      produces:
      - application/json
      responses:
        "200":
          description: OK
          schema:
            $ref: '#/definitions/portainer.EdgeJob'
        "400":
          description: Bad Request
        "500":
          description: Internal Server Error
        "503":
          description: Edge compute features are disabled
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Inspect an EdgeJob
      tags:
      - edge_jobs
    put:
      consumes:
      - application/json
      description: '**Access policy**: administrator'
      operationId: EdgeJobUpdate
      parameters:
      - description: EdgeJob Id
        in: path
        name: id
        required: true
        type: integer
      - description: EdgeGroup data
        in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/edgejobs.edgeJobUpdatePayload'
      produces:
      - application/json
      responses:
        "200":
          description: OK
          schema:
            $ref: '#/definitions/portainer.EdgeJob'
        "400":
          description: Bad Request
        "500":
          description: Internal Server Error
        "503":
          description: Edge compute features are disabled
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Update an EdgeJob
      tags:
      - edge_jobs
  /edge_jobs/{id}/file:
    get:
      description: '**Access policy**: administrator'
      operationId: EdgeJobFile
      parameters:
      - description: EdgeJob Id
        in: path
        name: id
        required: true
        type: integer
      produces:
      - application/json
      responses:
        "200":
          description: OK
          schema:
            $ref: '#/definitions/edgejobs.edgeJobFileResponse'
        "400":
          description: Bad Request
        "500":
          description: Internal Server Error
        "503":
          description: Edge compute features are disabled
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Fetch a file of an EdgeJob
      tags:
      - edge_jobs
  /edge_jobs/{id}/tasks:
    get:
      description: '**Access policy**: administrator'
      operationId: EdgeJobTasksList
      parameters:
      - description: EdgeJob Id
        in: path
        name: id
        required: true
        type: integer
      produces:
      - application/json
      responses:
        "200":
          description: OK
          schema:
            items:
              $ref: '#/definitions/edgejobs.taskContainer'
            type: array
        "400":
          description: Bad Request
        "500":
          description: Internal Server Error
        "503":
          description: Edge compute features are disabled
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Fetch the list of tasks on an EdgeJob
      tags:
      - edge_jobs
  /edge_jobs/{id}/tasks/{taskID}/logs:
    delete:
      description: '**Access policy**: administrator'
      operationId: EdgeJobTasksClear
      parameters:
      - description: EdgeJob Id
        in: path
        name: id
        required: true
        type: integer
      - description: Task Id
        in: path
        name: taskID
        required: true
        type: integer
      produces:
      - application/json
      responses:
        "204":
          description: No Content
        "400":
          description: Bad Request
        "500":
          description: Internal Server Error
        "503":
          description: Edge compute features are disabled
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Clear the log for a specifc task on an EdgeJob
      tags:
      - edge_jobs
    get:
      description: '**Access policy**: administrator'
      operationId: EdgeJobTaskLogsInspect
      parameters:
      - description: EdgeJob Id
        in: path
        name: id
        required: true
        type: integer
      - description: Task Id
        in: path
        name: taskID
        required: true
        type: integer
      produces:
      - application/json
      responses:
        "200":
          description: OK
          schema:
            $ref: '#/definitions/edgejobs.fileResponse'
        "400":
          description: Bad Request
        "500":
          description: Internal Server Error
        "503":
          description: Edge compute features are disabled
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Fetch the log for a specifc task on an EdgeJob
      tags:
      - edge_jobs
    post:
      description: '**Access policy**: administrator'
      operationId: EdgeJobTasksCollect
      parameters:
      - description: EdgeJob Id
        in: path
        name: id
        required: true
        type: integer
      - description: Task Id
        in: path
        name: taskID
        required: true
        type: integer
      produces:
      - application/json
      responses:
        "204":
          description: No Content
        "400":
          description: Bad Request
        "500":
          description: Internal Server Error
        "503":
          description: Edge compute features are disabled
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Collect the log for a specifc task on an EdgeJob
      tags:
      - edge_jobs
  /edge_jobs/create/file:
    post:
      consumes:
      - multipart/form-data
      description: '**Access policy**: administrator'
      operationId: EdgeJobCreateFile
      parameters:
      - description: Content of the Stack file
        in: formData
        name: file
        required: true
        type: file
      - description: Name of the stack
        in: formData
        name: Name
        required: true
        type: string
      - description: A cron expression to schedule this job
        in: formData
        name: CronExpression
        required: true
        type: string
      - description: JSON stringified array of Edge Groups ids
        in: formData
        name: EdgeGroups
        required: true
        type: string
      - description: JSON stringified array of Environment ids
        in: formData
        name: Endpoints
        required: true
        type: string
      - description: If recurring
        in: formData
        name: Recurring
        type: boolean
      produces:
      - application/json
      responses:
        "200":
          description: OK
          schema:
            $ref: '#/definitions/portaineree.EdgeGroup'
        "500":
          description: Internal Server Error
        "503":
          description: Edge compute features are disabled
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Create an EdgeJob from a file
      tags:
      - edge_jobs
  /edge_jobs/create/string:
    post:
      description: '**Access policy**: administrator'
      operationId: EdgeJobCreateString
      parameters:
      - description: EdgeGroup data when method is string
        in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/edgejobs.edgeJobCreateFromFileContentPayload'
      produces:
      - application/json
      responses:
        "200":
          description: OK
          schema:
            $ref: '#/definitions/portaineree.EdgeGroup'
        "500":
          description: Internal Server Error
        "503":
          description: Edge compute features are disabled
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Create an EdgeJob from a text
      tags:
      - edge_jobs
  /edge_stacks:
    get:
      description: '**Access policy**: administrator'
      operationId: EdgeStackList
      parameters:
      - description: when true summarize the edge stack statuses in the StatusSummary
          field and void the Status field.
        in: query
        name: summarizeStatuses
        type: boolean
      produces:
      - application/json
      responses:
        "200":
          description: OK
          schema:
            items:
              $ref: '#/definitions/github_com_portainer_portainer-ee_api_http_handler_edgestacks.edgeStackListResponseItem'
            type: array
        "400":
          description: Bad Request
        "500":
          description: Internal Server Error
        "503":
          description: Edge compute features are disabled
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Fetches the list of EdgeStacks
      tags:
      - edge_stacks
  /edge_stacks/{id}:
    delete:
      description: '**Access policy**: administrator'
      operationId: EdgeStackDelete
      parameters:
      - description: EdgeStack Id
        in: path
        name: id
        required: true
        type: integer
      responses:
        "204":
          description: No Content
        "400":
          description: Bad Request
        "500":
          description: Internal Server Error
        "503":
          description: Edge compute features are disabled
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Delete an EdgeStack
      tags:
      - edge_stacks
    get:
      description: '**Access policy**: administrator'
      operationId: EdgeStackInspect
      parameters:
      - description: EdgeStack Id
        in: path
        name: id
        required: true
        type: integer
      produces:
      - application/json
      responses:
        "200":
          description: OK
          schema:
            $ref: '#/definitions/portaineree.EdgeStack'
        "400":
          description: Bad Request
        "500":
          description: Internal Server Error
        "503":
          description: Edge compute features are disabled
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Inspect an EdgeStack
      tags:
      - edge_stacks
    put:
      consumes:
      - application/json
      description: '**Access policy**: administrator'
      operationId: EdgeStackUpdate
      parameters:
      - description: EdgeStack Id
        in: path
        name: id
        required: true
        type: integer
      - description: EdgeStack data
        in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/github_com_portainer_portainer-ee_api_http_handler_edgestacks.updateEdgeStackPayload'
      produces:
      - application/json
      responses:
        "200":
          description: OK
          schema:
            $ref: '#/definitions/portaineree.EdgeStack'
        "400":
          description: Bad Request
        "500":
          description: Internal Server Error
        "503":
          description: Edge compute features are disabled
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Update an EdgeStack
      tags:
      - edge_stacks
  /edge_stacks/{id}/file:
    get:
      description: '**Access policy**: administrator'
      operationId: EdgeStackFile
      parameters:
      - description: EdgeStack Id
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
          description: OK
          schema:
            $ref: '#/definitions/github_com_portainer_portainer-ee_api_http_handler_edgestacks.stackFileResponse'
        "400":
          description: Bad Request
        "500":
          description: Internal Server Error
        "503":
          description: Edge compute features are disabled
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Fetches the stack file for an EdgeStack
      tags:
      - edge_stacks
  /edge_stacks/{id}/git:
    put:
      consumes:
      - application/json
      description: '**Access policy**: authenticated'
      operationId: edgeStackUpdateFromGit
      parameters:
      - description: Stack identifier
        in: path
        name: id
        required: true
        type: integer
      - description: Git configurations
        in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/edgestacks.stackGitUpdatePayload'
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
          description: Not found
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Update git configuration and pulls the repository
      tags:
      - edge_stacks
  /edge_stacks/{id}/logs/{endpoint_id}:
    delete:
      description: '**Access policy**: administrator'
      operationId: EdgeStackLogsDelete
      parameters:
      - description: EdgeStack Id
        in: path
        name: id
        required: true
        type: integer
      - description: Endpoint Id
        in: path
        name: endpoint_id
        required: true
        type: integer
      responses:
        "204":
          description: No Content
        "400":
          description: Bad Request
        "503":
          description: Edge compute features are disabled
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Deletes the available logs for a given edge stack and endpoint
      tags:
      - edge_stacks
    get:
      description: '**Access policy**: administrator'
      operationId: EdgeStackLogsStatusGet
      parameters:
      - description: EdgeStack Id
        in: path
        name: id
        required: true
        type: integer
      - description: Environment Id
        in: path
        name: endpoint_id
        required: true
        type: integer
      responses:
        "200":
          description: OK
        "400":
          description: Bad Request
        "500":
          description: Internal Server Error
        "503":
          description: Edge compute features are disabled
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Gets the status of the log collection for a given edgestack and environment
      tags:
      - edge_stacks
    put:
      description: '**Access policy**: administrator'
      operationId: EdgeStackLogsCollect
      parameters:
      - description: EdgeStack Id
        in: path
        name: id
        required: true
        type: integer
      - description: Environment Id
        in: path
        name: endpoint_id
        required: true
        type: integer
      - description: Number of lines to request for the logs
        in: query
        name: tail
        type: integer
      - description: Container Id
        in: query
        name: container_id
        type: string
      - description: Start time to request for the logs
        in: query
        name: since
        type: string
      - description: End time to request for the logs
        in: query
        name: until
        type: string
      responses:
        "204":
          description: No Content
        "400":
          description: Bad Request
        "404":
          description: Not Found
        "500":
          description: Internal Server Error
        "503":
          description: Edge compute features are disabled
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Schedule the collection of logs for a given endpoint and edge stack
      tags:
      - edge_stacks
  /edge_stacks/{id}/logs/{endpoint_id}/file:
    get:
      description: '**Access policy**: administrator'
      operationId: EdgeStackLogsDownload
      parameters:
      - description: EdgeStack Id
        in: path
        name: id
        required: true
        type: integer
      - description: Endpoint Id
        in: path
        name: endpoint_id
        required: true
        type: integer
      responses:
        "200":
          description: OK
        "400":
          description: Bad Request
        "404":
          description: Not Found
        "500":
          description: Internal Server Error
        "503":
          description: Edge compute features are disabled
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Downloads the available logs for a given edge stack and endpoint
      tags:
      - edge_stacks
  /edge_stacks/{id}/stagger/status:
    get:
      description: '**Access policy**: administrator'
      operationId: EdgeStackStaggerStatusInspect
      parameters:
      - description: EdgeStack Id
        in: path
        name: id
        required: true
        type: integer
      produces:
      - application/json
      responses:
        "200":
          description: OK
          schema:
            $ref: '#/definitions/edgestacks.edgeStackStaggerStatusResponse'
        "400":
          description: Bad Request
        "500":
          description: Internal Server Error
        "503":
          description: Edge compute features are disabled
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Inspect an EdgeStack's parallel update status
      tags:
      - edge_stacks
  /edge_stacks/{id}/status:
    put:
      consumes:
      - application/json
      description: Authorized only if the request is done by an Edge Environment(Endpoint)
      operationId: EdgeStackStatusUpdate
      parameters:
      - description: EdgeStack Id
        in: path
        name: id
        required: true
        type: integer
      - description: EdgeStack status payload
        in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/github_com_portainer_portainer-ee_api_http_handler_edgestacks.updateStatusPayload'
      produces:
      - application/json
      responses:
        "200":
          description: OK
          schema:
            $ref: '#/definitions/portaineree.EdgeStack'
        "400":
          description: Bad Request
        "403":
          description: Forbidden
        "404":
          description: Not Found
        "500":
          description: Internal Server Error
      summary: Update an EdgeStack status
      tags:
      - edge_stacks
  /edge_stacks/create/file:
    post:
      consumes:
      - multipart/form-data
      description: '**Access policy**: administrator'
      operationId: EdgeStackCreateFile
      parameters:
      - description: Name of the stack. it must only consist of lowercase alphanumeric
          characters, hyphens, or underscores as well as start with a letter or number
        in: formData
        name: Name
        required: true
        type: string
      - description: Content of the Stack file
        in: formData
        name: file
        required: true
        type: file
      - description: JSON stringified array of Edge Groups ids
        in: formData
        name: EdgeGroups
        required: true
        type: string
      - description: deploy type 0 - 'compose', 1 - 'kubernetes'
        in: formData
        name: DeploymentType
        required: true
        type: integer
      - description: JSON stringified array of Registry ids to use for this stack
        in: formData
        name: Registries
        type: string
      - description: Uses the manifest's namespaces instead of the default one, relevant
          only for kube environments
        in: formData
        name: UseManifestNamespaces
        type: boolean
      - description: Pre Pull image
        in: formData
        name: PrePullImage
        type: boolean
      - description: Retry deploy
        in: formData
        name: RetryDeploy
        type: boolean
      - description: Duration, in seconds, for which the agent should continue attempting
          to deploy the stack after a failure
        in: formData
        name: RetryPeriod
        type: integer
      - description: if true, will not create an edge stack, but just will check the
          settings and return a non-persisted edge stack object
        in: query
        name: dryrun
        type: string
      - description: unique webhook id
        in: formData
        name: Webhook
        required: true
        type: string
      - description: JSON stringified array of environment variables {name, value}
        in: formData
        name: EnvVars
        type: string
      - description: JSON stringified object of stagger config
        in: formData
        name: StaggerConfig
        type: string
      produces:
      - application/json
      responses:
        "200":
          description: OK
          schema:
            $ref: '#/definitions/portaineree.EdgeStack'
        "400":
          description: Bad request
        "500":
          description: Internal server error
