        "503":
          description: Edge compute features are disabled
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Create an EdgeStack from file
      tags:
      - edge_stacks
  /edge_stacks/create/repository:
    post:
      description: '**Access policy**: administrator'
      operationId: EdgeStackCreateRepository
      parameters:
      - description: stack config
        in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/github_com_portainer_portainer-ee_api_http_handler_edgestacks.edgeStackFromGitRepositoryPayload'
      - description: if true, will not create an edge stack, but just will check the
          settings and return a non-persisted edge stack object
        in: query
        name: dryrun
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
        "409":
          description: Webhook ID already exists
        "500":
          description: Internal server error
        "503":
          description: Edge compute features are disabled
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Create an EdgeStack from a git repository
      tags:
      - edge_stacks
  /edge_stacks/create/string:
    post:
      description: '**Access policy**: administrator'
      operationId: EdgeStackCreateString
      parameters:
      - description: stack config
        in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/github_com_portainer_portainer-ee_api_http_handler_edgestacks.edgeStackFromStringPayload'
      - description: if true, will not create an edge stack, but just will check the
          settings and return a non-persisted edge stack object
        in: query
        name: dryrun
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
        "503":
          description: Edge compute features are disabled
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Create an EdgeStack from a text
      tags:
      - edge_stacks
  /edge_stacks/parse_registries:
    post:
      consumes:
      - multipart/form-data
      description: '**Access policy**: authenticated'
      operationId: EdgeStackParseRegistries
      parameters:
      - description: stack file
        in: formData
        name: file
        required: true
        type: file
      produces:
      - application/json
      responses:
        "200":
          description: List of registries IDs
          schema:
            items:
              type: integer
            type: array
        "400":
          description: Invalid request payload
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Parse registries from a stack file
      tags:
      - edge_stacks
  /edge_stacks/webhooks/{webhookID}:
    post:
      description: '**Access policy**: public'
      operationId: EdgeStackWebhookInvoke
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
          description: Conflict
        "500":
          description: Server error
      summary: Webhook for triggering edge stack updates from git
      tags:
      - stacks
  /edge_update_schedules:
    get:
      description: '**Access policy**: administrator'
      operationId: EdgeUpdateScheduleList
      parameters:
      - description: Include Edge Stacks in the response
        in: query
        name: includeEdgeStacks
        type: boolean
      produces:
      - application/json
      responses:
        "200":
          description: OK
          schema:
            items:
              $ref: '#/definitions/edgeupdateschedules.decoratedUpdateSchedule'
            type: array
        "500":
          description: Internal Server Error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Fetches the list of Edge Update Schedules
      tags:
      - edge_update_schedules
    post:
      consumes:
      - application/json
      description: |-
        Creates a scheduled remote update process that will update or rollback the Edge agents in the specified Edge groups.
        **Access policy**: Administrator only.
      operationId: EdgeUpdateScheduleCreate
      parameters:
      - description: Schedule details
        in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/edgeupdateschedules.createPayload'
      produces:
      - application/json
      responses:
        "200":
          description: Remote update procedure successfully created
          schema:
            $ref: '#/definitions/types.UpdateSchedule'
        "400":
          description: Invalid request payload, such as missing required fields or
            fields not meeting validation criteria.
        "403":
          description: Unauthorized access or operation not allowed.
        "409":
          description: Edge update schedule name already in use.
        "500":
          description: Server error occurred while attempting to create the remote
            update procedure.
      security:
      - ApiKeyAuth: []
        jwt: []
      summary: Creates a scheduled remote update procedure for Edge agents
      tags:
      - edge_update_schedules
  /edge_update_schedules/{id}:
    delete:
      description: '**Access policy**: administrator'
      operationId: EdgeUpdateScheduleDelete
      parameters:
      - description: EdgeUpdate Id
        in: path
        name: id
        required: true
        type: integer
      responses:
        "204":
          description: No Content
        "500":
          description: Internal Server Error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Deletes an Edge Update Schedule
      tags:
      - edge_update_schedules
    get:
      description: '**Access policy**: administrator'
      operationId: EdgeUpdateScheduleInspect
      parameters:
      - description: EdgeUpdate Id
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
            $ref: '#/definitions/edgeupdateschedules.inspectResponse'
        "500":
          description: Internal Server Error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Returns the Edge Update Schedule with the given ID
      tags:
      - edge_update_schedules
    post:
      consumes:
      - application/json
      description: |-
        Creates a scheduled remote update process that will update or rollback the Edge agents in the specified Edge groups.
        **Access policy**: Administrator only.
      operationId: EdgeUpdateScheduleUpdate
      parameters:
      - description: EdgeUpdate Id
        in: path
        name: id
        required: true
        type: integer
      - description: Schedule details
        in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/edgeupdateschedules.updatePayload'
      produces:
      - application/json
      responses:
        "204":
          description: Remote update procedure successfully updated
          schema:
            $ref: '#/definitions/types.UpdateSchedule'
        "400":
          description: Invalid request payload, such as missing required fields or
            fields not meeting validation criteria.
        "403":
          description: Unauthorized access or operation not allowed.
        "404":
          description: Unable to find an Edge Update with the specified identifier
            inside the database
        "409":
          description: Edge update schedule name already in use.
        "500":
          description: Server error occurred while attempting to update the remote
            update procedure.
      security:
      - ApiKeyAuth: []
        jwt: []
      summary: Update a scheduled remote update procedure for Edge agents
      tags:
      - edge_update_schedules
  /edge_update_schedules/active:
    post:
      consumes:
      - application/json
      description: '**Access policy**: administrator'
      operationId: EdgeUpdateScheduleActiveSchedulesList
      parameters:
      - description: Active schedule query
        in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/edgeupdateschedules.activeSchedulePayload'
      produces:
      - application/json
      responses:
        "200":
          description: OK
          schema:
            items:
              $ref: '#/definitions/types.EndpointUpdateScheduleRelation'
            type: array
        "500":
          description: Internal Server Error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Fetches the list of Active Edge Update Schedules
      tags:
      - edge_update_schedules
  /edge_update_schedules/agent_versions:
    get:
      description: '**Access policy**: authenticated'
      operationId: RemoteUpdatesAgentVersions
      produces:
      - application/json
      responses:
        "200":
          description: OK
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
      summary: Fetches the supported versions of the agent to update/rollback
      tags:
      - edge_update_schedules
  /edge_update_schedules/info:
    get:
      description: '**Access policy**: administrator'
      operationId: EdgeUpdateScheduleInfo
      produces:
      - application/json
      responses:
        "200":
          description: OK
          schema:
            $ref: '#/definitions/edgeupdateschedules.infoResponse'
        "500":
          description: Internal Server Error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Returns informations the help create edge update schedules
      tags:
      - edge_update_schedules
  /edge_update_schedules/previous_versions:
    get:
      description: '**Access policy**: administrator'
      operationId: EdgeUpdatePreviousVersions
      parameters:
      - collectionFormat: csv
        description: Environment IDs
        in: query
        items:
          type: integer
        name: environmentIds
        type: array
      - collectionFormat: csv
        description: Edge Group IDs
        in: query
        items:
          type: integer
        name: edgeGroupIds
        type: array
      produces:
      - application/json
      responses:
        "200":
          description: OK
          schema:
            additionalProperties:
              type: string
            type: object
        "400":
          description: Invalid request
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Fetches the previous versions of updated agents
      tags:
      - edge_update_schedules
  /endpoint_groups:
    get:
      description: |-
        List all environment(endpoint) groups based on the current user authorizations. Will
        return all environment(endpoint) groups if using an administrator account otherwise it will
        only return authorized environment(endpoint) groups.
        **Access policy**: restricted
      operationId: EndpointGroupList
      parameters:
      - description: If true, each environment(endpoint) group will include the number
          of environments(endpoints) associated to it
        in: query
        name: size
        type: boolean
      produces:
      - application/json
      responses:
        "200":
          description: Environment(Endpoint) group
          schema:
            items:
              $ref: '#/definitions/endpointgroups.endpointGroupResponse'
            type: array
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: List Environment(Endpoint) groups
      tags:
      - endpoint_groups
    post:
      consumes:
      - application/json
      description: |-
        Create a new environment(endpoint) group.
        **Access policy**: administrator
      parameters:
      - description: Environment(Endpoint) Group details
        in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/endpointgroups.endpointGroupCreatePayload'
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            $ref: '#/definitions/portainer.EndpointGroup'
        "400":
          description: Invalid request
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Create an Environment(Endpoint) Group
      tags:
      - endpoint_groups
  /endpoint_groups/{id}:
    delete:
      description: |-
        Remove an environment(endpoint) group.
        **Access policy**: administrator
      operationId: EndpointGroupDelete
      parameters:
      - description: EndpointGroup identifier
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
          description: EndpointGroup not found
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Remove an environment(endpoint) group
      tags:
      - endpoint_groups
    get:
      consumes:
      - application/json
      description: |-
        Retrieve details abont an environment(endpoint) group.
        **Access policy**: administrator
      parameters:
      - description: Environment(Endpoint) group identifier
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
            $ref: '#/definitions/endpointgroups.decoratedEndpointGroup'
        "400":
          description: Invalid request
        "404":
          description: EndpointGroup not found
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Inspect an Environment(Endpoint) group
      tags:
      - endpoint_groups
    put:
      consumes:
      - application/json
      description: |-
        Update an environment(endpoint) group.
        **Access policy**: administrator
      operationId: EndpointGroupUpdate
      parameters:
      - description: EndpointGroup identifier
        in: path
        name: id
        required: true
        type: integer
      - description: EndpointGroup details
        in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/endpointgroups.endpointGroupUpdatePayload'
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            $ref: '#/definitions/portainer.EndpointGroup'
        "400":
          description: Invalid request
        "404":
          description: EndpointGroup not found
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Update an environment(endpoint) group
      tags:
      - endpoint_groups
  /endpoint_groups/{id}/endpoints/{endpointId}:
    delete:
      description: '**Access policy**: administrator'
      operationId: EndpointGroupDeleteEndpoint
      parameters:
      - description: EndpointGroup identifier
        in: path
        name: id
        required: true
        type: integer
      - description: Environment(Endpoint) identifier
        in: path
        name: endpointId
        required: true
        type: integer
      responses:
        "204":
          description: Success
        "400":
          description: Invalid request
        "404":
          description: EndpointGroup not found
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Removes environment(endpoint) from an environment(endpoint) group
      tags:
      - endpoint_groups
    put:
      description: |-
        Add an environment(endpoint) to an environment(endpoint) group
        **Access policy**: administrator
      operationId: EndpointGroupAddEndpoint
      parameters:
      - description: EndpointGroup identifier
        in: path
        name: id
        required: true
        type: integer
      - description: Environment(Endpoint) identifier
        in: path
        name: endpointId
        required: true
        type: integer
      responses:
        "204":
          description: Success
        "400":
          description: Invalid request
        "404":
          description: EndpointGroup not found
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Add an environment(endpoint) to an environment(endpoint) group
      tags:
      - endpoint_groups
  /endpoints:
    delete:
      consumes:
      - application/json
      deprecated: true
      description: |-
        Deprecated: use the `POST` endpoint instead.
        Remove multiple environments and optionally clean-up associated resources.
        **Access policy**: Administrator only.
      operationId: EndpointDeleteBatchDeprecated
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
    get:
      description: |-
        List all environments(endpoints) based on the current user authorizations. Will
        return all environments(endpoints) if using an administrator or team leader account otherwise it will
        only return authorized environments(endpoints).
        **Access policy**: restricted
      operationId: EndpointList
      parameters:
      - description: Start searching from
        in: query
        name: start
        type: integer
      - description: Limit results to this value
        in: query
        name: limit
        type: integer
      - description: Sort results by this value
        enum:
        - Name
        - Group
        - Status
        - LastCheckIn
        - EdgeID
        in: query
        name: sort
        type: string
      - description: Order sorted results by desc/asc
        in: query
        name: order
        type: integer
      - description: If true, an `X-Update-Available` header will be added to the
          response to indicate if an update is available
        in: query
        name: updateInformation
        type: boolean
      - description: If true, an `X-K8S-Env-Admin` header will be added to the response
          to indicate if the user is a K8S environment admin for any of the returned
          environments
        in: query
        name: k8sEnvAdmin
        type: boolean
      - description: Search query
        in: query
        name: search
        type: string
      - collectionFormat: csv
        description: List environments(endpoints) of these groups
        in: query
        items:
          type: integer
        name: groupIds
        type: array
      - collectionFormat: csv
        description: List environments(endpoints) by this status
        in: query
        items:
          type: integer
        name: status
        type: array
      - collectionFormat: csv
        description: List environments(endpoints) of this type
        in: query
        items:
          type: integer
        name: types
        type: array
      - collectionFormat: csv
        description: search environments(endpoints) with these tags (depends on tagsPartialMatch)
        in: query
        items:
          type: integer
        name: tagIds
        type: array
      - description: If true, will return environment(endpoint) which has one of tagIds,
          if false (or missing) will return only environments(endpoints) that has
          all the tags
        in: query
        name: tagsPartialMatch
        type: boolean
      - collectionFormat: csv
        description: will return only these environments(endpoints)
        in: query
        items:
          type: integer
        name: endpointIds
        type: array
      - collectionFormat: csv
        description: will exclude these environments(endpoints)
        in: query
        items:
          type: integer
        name: excludeIds
        type: array
      - description: If true, will return environment(endpoint) that were provisioned
        in: query
        name: provisioned
        type: boolean
      - collectionFormat: csv
        description: will return only environments with on of these agent versions
        in: query
        items:
          type: string
        name: agentVersions
        type: array
      - description: if exists true show only edge async agents, false show only standard
          edge agents. if missing, will show both types (relevant only for edge agents)
        in: query
        name: edgeAsync
        type: boolean
      - description: if true, show only untrusted edge agents, if false show only
          trusted edge agents (relevant only for edge agents)
        in: query
        name: edgeDeviceUntrusted
        type: boolean
      - description: if bigger then zero, show only edge agents that checked-in in
          the last provided seconds (relevant only for edge agents)
        in: query
        name: edgeCheckInPassedSeconds
        type: number
      - description: if true, the snapshot data won't be retrieved
        in: query
        name: excludeSnapshots
        type: boolean
      - description: will return only environments(endpoints) with this name
        in: query
        name: name
        type: string
      - description: Filter environments by partial name match (case-insensitive,
          searches name only)
        in: query
        name: nameFilter
        type: string
      - description: only applied when edgeStackId exists. Filter the returned environments
          based on their deployment status in the stack (not the environment status!)
        in: query
        name: edgeStackStatus
        type: string
      - collectionFormat: csv
        description: List environments(endpoints) of these edge groups
        in: query
        items:
          type: integer
        name: edgeGroupIds
        type: array
      - collectionFormat: csv
        description: Exclude environments(endpoints) of these edge groups
        in: query
        items:
          type: integer
        name: excludeEdgeGroupIds
        type: array
      - description: If true, will apply policy data to the returned environments(endpoints)
        in: query
        name: policy
        type: boolean
      - collectionFormat: csv
        description: List environments(endpoints) associated with these policies
        in: query
        items:
          type: integer
        name: policyIds
        type: array
      - collectionFormat: csv
        description: Filter environments by policy status (applied, failed, in_progress,
          warning, not_supported). Only applies when policyIds is specified.
        in: query
        items:
          type: string
        name: policyStatus
        type: array
      produces:
      - application/json
      responses:
        "200":
          description: Endpoints
          schema:
            items:
              $ref: '#/definitions/portaineree.Endpoint'
            type: array
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: List environments(endpoints)
      tags:
      - endpoints
    post:
      consumes:
      - multipart/form-data
      description: |-
        Create a new environment(endpoint) that will be used to manage an environment(endpoint).
