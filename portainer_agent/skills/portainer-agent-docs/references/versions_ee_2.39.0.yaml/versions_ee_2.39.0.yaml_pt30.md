      operationId: StatusInspect
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            $ref: '#/definitions/github_com_portainer_portainer-ee_api_http_handler_system.status'
      summary: Check Portainer status
      tags:
      - status
  /support/debug_log:
    get:
      description: |-
        Checks if the global log level is enabled
        **Access policy**: administrator
      operationId: GetDebugLogStatus
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            $ref: '#/definitions/support.debugLogPayload'
        "500":
          description: Server error occurred.
      security:
      - ApiKeyAuth: []
        jwt: []
      summary: Get status of the global debug log
      tags:
      - support
    put:
      description: |-
        Enables the debug log by setting the global log level to debug or info if disabled
        **Access policy**: administrator
      operationId: SetDebugLogStatus
      parameters:
      - description: Debug log should be set to enabled or disabled
        in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/support.debugLogPayload'
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            $ref: '#/definitions/support.debugLogPayload'
        "400":
          description: Invalid request payload
        "500":
          description: Server error occurred.
      security:
      - ApiKeyAuth: []
        jwt: []
      summary: Enables or disables the global debug log
      tags:
      - support
  /support/download:
    post:
      consumes:
      - application/json
      description: '**Access policy**: administrator'
      operationId: SupportBundleDownload
      produces:
      - application/octet-stream
      responses:
        "200":
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
        "500":
          description: Failed to create support archive
      security:
      - ApiKeyAuth: []
        jwt: []
      summary: Download a bundle of files to help support diagnose issues
      tags:
      - support
  /system/info:
    get:
      description: '**Access policy**: authenticated'
      operationId: systemInfo
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            $ref: '#/definitions/github_com_portainer_portainer-ee_api_http_handler_system.systemInfoResponse'
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Retrieve system info
      tags:
      - system
  /system/nodes:
    get:
      description: '**Access policy**: authenticated'
      operationId: systemNodesCount
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            $ref: '#/definitions/github_com_portainer_portainer-ee_api_http_handler_system.nodesCountResponse'
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Retrieve the count of nodes
      tags:
      - system
  /system/status:
    get:
      description: |-
        Retrieve Portainer status
        **Access policy**: public
      operationId: systemStatus
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            $ref: '#/definitions/github_com_portainer_portainer-ee_api_http_handler_system.status'
      summary: Check Portainer status
      tags:
      - system
  /system/update:
    post:
      description: |-
        Update Portainer to latest version
        **Access policy**: administrator
      operationId: systemUpdate
      produces:
      - application/json
      responses:
        "204":
          description: Success
          schema:
            $ref: '#/definitions/github_com_portainer_portainer-ee_api_http_handler_system.status'
        "409":
          description: Conflict, an automatic patch operation is already in progress
        "500":
          description: Server error
      summary: Update Portainer to latest version
      tags:
      - system
  /system/version:
    get:
      description: |-
        Check if portainer has an update available
        **Access policy**: authenticated
      operationId: systemVersion
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            $ref: '#/definitions/github_com_portainer_portainer-ee_api_http_handler_system.versionResponse'
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Check for portainer updates
      tags:
      - system
  /tags:
    get:
      description: |-
        List tags.
        **Access policy**: authenticated
      operationId: TagList
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            items:
              $ref: '#/definitions/portainer.Tag'
            type: array
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: List tags
      tags:
      - tags
    post:
      consumes:
      - application/json
      description: |-
        Create a new tag.
        **Access policy**: administrator
      operationId: TagCreate
      parameters:
      - description: Tag details
        in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/tags.tagCreatePayload'
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            $ref: '#/definitions/portainer.Tag'
        "409":
          description: This name is already associated to a tag
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Create a new tag
      tags:
      - tags
  /tags/{id}:
    delete:
      description: |-
        Remove a tag.
        **Access policy**: administrator
      operationId: TagDelete
      parameters:
      - description: Tag identifier
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
          description: Permission denied
        "404":
          description: Tag not found
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Remove a tag
      tags:
      - tags
  /team_memberships:
    get:
      description: |-
        List team memberships. Access is only available to administrators and team leaders.
        **Access policy**: administrator
      operationId: TeamMembershipList
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            items:
              $ref: '#/definitions/portainer.TeamMembership'
            type: array
        "400":
          description: Invalid request
        "403":
          description: Permission denied
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: List team memberships
      tags:
      - team_memberships
    post:
      consumes:
      - application/json
      description: |-
        Create a new team memberships. Access is only available to administrators leaders of the associated team.
        **Access policy**: administrator
      operationId: TeamMembershipCreate
      parameters:
      - description: Team membership details
        in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/teammemberships.teamMembershipCreatePayload'
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            $ref: '#/definitions/portainer.TeamMembership'
        "400":
          description: Invalid request
        "403":
          description: Permission denied to manage memberships
        "409":
          description: Team membership already registered
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Create a new team membership
      tags:
      - team_memberships
  /team_memberships/{id}:
    delete:
      description: |-
        Remove a team membership. Access is only available to administrators leaders of the associated team.
        **Access policy**: administrator
      operationId: TeamMembershipDelete
      parameters:
      - description: TeamMembership identifier
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
          description: Permission denied
        "404":
          description: TeamMembership not found
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Remove a team membership
      tags:
      - team_memberships
    put:
      consumes:
      - application/json
      description: |-
        Update a team membership. Access is only available to administrators or leaders of the associated team.
        **Access policy**: administrator or leaders of the associated team
      operationId: TeamMembershipUpdate
      parameters:
      - description: Team membership identifier
        in: path
        name: id
        required: true
        type: integer
      - description: Team membership details
        in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/teammemberships.teamMembershipUpdatePayload'
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            $ref: '#/definitions/portainer.TeamMembership'
        "400":
          description: Invalid request
        "403":
          description: Permission denied
        "404":
          description: TeamMembership not found
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Update a team membership
      tags:
      - team_memberships
  /teams:
    get:
      description: |-
        List teams. All authenticated users can list all teams (teams only expose ID and Name).
        **Access policy**: authenticated
      operationId: TeamList
      parameters:
      - description: Only list teams that the user is leader of
        in: query
        name: onlyLedTeams
        type: boolean
      - description: Identifier of the environment(endpoint) that will be used to
          filter the authorized teams
        in: query
        name: environmentId
        type: integer
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            items:
              $ref: '#/definitions/portainer.Team'
            type: array
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: List teams
      tags:
      - teams
    post:
      consumes:
      - application/json
      description: |-
        Create a new team.
        **Access policy**: administrator
      operationId: TeamCreate
      parameters:
      - description: details
        in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/teams.teamCreatePayload'
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            $ref: '#/definitions/portainer.Team'
        "400":
          description: Invalid request
        "409":
          description: A team with the same name already exists
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Create a new team
      tags:
      - teams
  /teams/{id}:
    delete:
      description: |-
        Remove a team.
        **Access policy**: administrator
      operationId: TeamDelete
      parameters:
      - description: Team Id
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
          description: Permission denied
        "404":
          description: Team not found
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Remove a team
      tags:
      - teams
    get:
      description: |-
        Retrieve details about a team. Access is only available for administrator and leaders of that team.
        **Access policy**: administrator or team leader
      operationId: TeamInspect
      parameters:
      - description: Team identifier
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
            $ref: '#/definitions/portainer.Team'
        "400":
          description: Invalid request
        "403":
          description: Permission denied
        "404":
          description: Team not found
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Inspect a team
      tags:
      - teams
    put:
      consumes:
      - application/json
      description: |-
        Update a team.
        **Access policy**: administrator
      operationId: TeamUpdate
      parameters:
      - description: Team identifier
        in: path
        name: id
        required: true
        type: integer
      - description: Team details
        in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/teams.teamUpdatePayload'
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            $ref: '#/definitions/portainer.Team'
        "400":
          description: Invalid request
        "403":
          description: Permission denied
        "404":
          description: Team not found
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Update a team
      tags:
      - teams
  /teams/{id}/memberships:
    get:
      description: |-
        List team memberships. Access is only available to administrators and team leaders.
        **Access policy**: restricted
      operationId: TeamMemberships
      parameters:
      - description: Team Id
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
              $ref: '#/definitions/portainer.TeamMembership'
            type: array
        "400":
          description: Invalid request
        "403":
          description: Permission denied
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: List team memberships
      tags:
      - team_memberships
  /templates:
    get:
      description: |-
        List available templates.
        **Access policy**: authenticated
      operationId: TemplateList
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            $ref: '#/definitions/templates.listResponse'
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: List available templates
      tags:
      - templates
  /templates/{id}/file:
    post:
      consumes:
      - application/json
      description: |-
        Get a template's file
        **Access policy**: authenticated
      operationId: TemplateFile
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
            $ref: '#/definitions/templates.fileResponse'
        "400":
          description: Invalid request
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Get a template's file
      tags:
      - templates
  /templates/helm:
    get:
      description: '**Access policy**: authenticated'
      operationId: HelmRepoSearch
      parameters:
      - description: Helm repository URL (required if registryId not provided)
        in: query
        name: repo
        type: string
      - description: Helm registry ID (required if repo not provided)
        in: query
        name: registryId
        type: string
      - description: Helm chart name
        in: query
        name: chart
        type: string
      - description: If true will use cache to search
        in: query
        name: useCache
        type: string
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            type: string
        "400":
          description: Bad request
        "401":
          description: Unauthorized
        "404":
          description: Not found
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Search Helm Charts
      tags:
      - helm
  /templates/helm/{command}:
    get:
      consumes:
      - application/json
      description: |-
        **Access policy**: authenticated
        Either `repo` or `registryId` parameter is required (but not both)
      operationId: HelmShow
      parameters:
      - description: Helm repository URL (required if registryId not provided)
        in: query
        name: repo
        type: string
      - description: Helm registry ID (required if repo not provided)
        in: query
        name: registryId
        type: string
      - description: Environment ID (required if registryId is provided and user is
          not an admin)
        in: query
        name: environmentId
        type: string
      - description: Chart name
        in: query
        name: chart
        required: true
        type: string
      - description: Chart version
        in: query
        name: version
        required: true
        type: string
      - description: chart/values/readme
        in: path
        name: command
        required: true
        type: string
      produces:
      - text/plain
      responses:
        "200":
          description: Success
          schema:
            type: string
        "401":
          description: Unauthorized
        "404":
          description: Environment(Endpoint) or ServiceAccount not found
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Show Helm Chart Information
      tags:
      - helm
  /upload/tls/{certificate}:
    post:
      consumes:
      - multipart/form-data
      description: |-
        Use this environment(endpoint) to upload TLS files.
        **Access policy**: administrator
      operationId: UploadTLS
      parameters:
      - description: TLS file type. Valid values are 'ca', 'cert' or 'key'.
        enum:
        - ca
        - cert
        - key
        in: path
        name: certificate
        required: true
        type: string
      - description: Folder where the TLS file will be stored. Will be created if
          not existing
        in: formData
        name: folder
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
      summary: Upload TLS files
      tags:
      - upload
  /useractivity/authlogs:
    get:
      description: |-
        List logs by provided query
        **Access policy**: admin
      operationId: AuthLogsList
      parameters:
      - description: Pagination offset
        in: query
        name: offset
        type: integer
      - description: Limit results
        in: query
        name: limit
        type: integer
      - description: Results before timestamp (unix)
        in: query
        name: before
        type: integer
      - description: Results after timestamp (unix)
        in: query
        name: after
        type: integer
      - description: Sort by this column
        in: query
        name: sortBy
        type: string
      - description: Sort order, if true will return results by descending order
        in: query
        name: sortDesc
        type: boolean
      - description: Query logs by this keyword
        in: query
        name: keyword
        type: string
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            items:
              $ref: '#/definitions/portaineree.AuthActivityLog'
            type: array
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: List auth activity logs
      tags:
      - useractivity
  /useractivity/authlogs.csv:
    get:
      description: |-
        Download auth logs as CSV by provided query
        **Access policy**: admin
      operationId: AuthLogsCSV
      parameters:
      - description: Results before timestamp (unix)
        in: query
        name: before
        type: integer
      - description: Results after timestamp (unix)
        in: query
        name: after
        type: integer
      - description: Sort by this column
        in: query
        name: sortBy
        type: string
      - description: Sort order, if true will return results by descending order
        in: query
        name: sortDesc
        type: boolean
      - description: Limit results
        in: query
        name: limit
        type: integer
      - description: Query logs by this keyword
        in: query
        name: keyword
        type: string
      produces:
      - text/csv
      responses:
        "200":
          description: Success
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Download auth logs as CSV
      tags:
      - useractivity
  /useractivity/logs:
    get:
      description: |-
        List logs by provided query
        **Access policy**: admin
      operationId: LogsList
      parameters:
      - description: Pagination offset
        in: query
        name: offset
        type: integer
      - description: Limit results
        in: query
        name: limit
        type: integer
      - description: Results before timestamp (unix)
        in: query
        name: before
        type: integer
      - description: Results after timestamp (unix)
        in: query
        name: after
        type: integer
      - description: Sort by this column
        in: query
        name: sortBy
        type: string
      - description: Sort order, if true will return results by descending order
        in: query
        name: sortDesc
        type: boolean
      - description: Query logs by this keyword
        in: query
        name: keyword
        type: string
      - collectionFormat: csv
        description: Filter by context
        in: query
        items:
          type: string
        name: context
        type: array
      - collectionFormat: csv
        description: Filter by usernames
        in: query
        items:
          type: string
        name: username
        type: array
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            $ref: '#/definitions/useractivity.logsListResponse'
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: List user activity logs
      tags:
      - useractivity
  /useractivity/logs.csv:
    get:
      description: |-
        Download user activity logs as CSV by provided query
        **Access policy**: admin
      operationId: LogsCSV
      parameters:
