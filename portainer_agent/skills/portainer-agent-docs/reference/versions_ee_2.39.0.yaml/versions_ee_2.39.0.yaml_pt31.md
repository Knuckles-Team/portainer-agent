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
      - description: Limit results (defaults to 1000000 if not provided, zero, negative,
          or exceeds maximum)
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
      summary: Download user activity logs as CSV
      tags:
      - useractivity
  /users:
    get:
      description: |-
        List Portainer users.
        Non-administrator users only receive non-administrator accounts.
        Passwords are never included in any response.
        **Access policy**: authenticated
      operationId: UserList
      parameters:
      - description: Identifier of the environment(endpoint) that will be used to
          filter the authorized users
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
              $ref: '#/definitions/users.User'
            type: array
        "400":
          description: Invalid request
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: List users
      tags:
      - users
    post:
      consumes:
      - application/json
      description: |-
        Create a new Portainer user.
        Only administrators can create users.
        **Access policy**: restricted
      operationId: UserCreate
      parameters:
      - description: User details
        in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/users.userCreatePayload'
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            $ref: '#/definitions/portaineree.User'
        "400":
          description: Invalid request
        "403":
          description: Permission denied
        "409":
          description: User already exists
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Create a new user
      tags:
      - users
  /users/{id}:
    delete:
      description: |-
        Remove a user.
        **Access policy**: administrator
      operationId: UserDelete
      parameters:
      - description: User identifier
        in: path
        name: id
        required: true
        type: integer
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
          description: User not found
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Remove a user
      tags:
      - users
    get:
      description: |-
        Retrieve details about a user.
        User passwords are filtered out, and should never be accessible.
        **Access policy**: authenticated
      operationId: UserInspect
      parameters:
      - description: User identifier
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
            $ref: '#/definitions/portaineree.User'
        "400":
          description: Invalid request
        "403":
          description: Permission denied
        "404":
          description: User not found
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Inspect a user
      tags:
      - users
    put:
      consumes:
      - application/json
      description: |-
        Update user details. A regular user account can only update his details.
        A regular user account cannot change their username or role.
        **Access policy**: authenticated
      operationId: UserUpdate
      parameters:
      - description: User identifier
        in: path
        name: id
        required: true
        type: integer
      - description: User details
        in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/users.userUpdatePayload'
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            $ref: '#/definitions/portaineree.User'
        "400":
          description: Invalid request
        "403":
          description: Permission denied
        "404":
          description: User not found
        "409":
          description: Username already exist or Edge Compute features are not enabled
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Update a user
      tags:
      - users
  /users/{id}/gitcredentials:
    get:
      description: |-
        Gets all saved git credentials for a user.
        Only the calling user can retrieve git credentials
        **Access policy**: authenticated
      operationId: UserGetGitCredentials
      parameters:
      - description: User identifier
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
              $ref: '#/definitions/portaineree.GitCredential'
            type: array
        "400":
          description: Invalid request
        "403":
          description: Permission denied
        "404":
          description: User not found
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Get all saved git credentials for a user
      tags:
      - users
    post:
      consumes:
      - application/json
      description: |-
        Store a Git Credential for a user.
        Only the calling user can store a git credential for themselves.
        **Access policy**: restricted
      operationId: UserCreateGitCredential
      parameters:
      - description: User identifier
        in: path
        name: id
        required: true
        type: integer
      - description: details
        in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/users.userGitCredentialCreatePayload'
      produces:
      - application/json
      responses:
        "201":
          description: Created
          schema:
            $ref: '#/definitions/users.gitCredentialResponse'
        "400":
          description: Invalid request
        "401":
          description: Unauthorized
        "403":
          description: Permission denied
        "500":
          description: Server error
      security:
      - jwt: []
      summary: Store a Git Credential for a user
      tags:
      - users
  /users/{id}/gitcredentials/{credentialID}:
    delete:
      description: |-
        Remove a git-credential associated to a user..
        Only the calling user can remove git-credential
        **Access policy**: authenticated
      operationId: UserRemoveGitCredential
      parameters:
      - description: User identifier
        in: path
        name: id
        required: true
        type: integer
      - description: Git Credential identifier
        in: path
        name: credentialID
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
      summary: Remove a git-credential associated to a user
      tags:
      - users
    get:
      description: |-
        Gets the specific saved git credential for a user.
        Only the calling user can retrieve git credential
        **Access policy**: authenticated
      operationId: UserGetGitCredential
      parameters:
      - description: User identifier
        in: path
        name: id
        required: true
        type: integer
      - description: Git Credential identifier
        in: path
        name: credentialID
        required: true
        type: integer
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            $ref: '#/definitions/portaineree.GitCredential'
        "400":
          description: Invalid request
        "403":
          description: Permission denied
        "404":
          description: User not found
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Get the specific saved git credential for a user
      tags:
      - users
    put:
      description: |-
        Update a git-credential associated to a user..
        Only the calling user can update git-credential
        **Access policy**: authenticated
      operationId: UserUpdateGitCredential
      parameters:
      - description: User identifier
        in: path
        name: id
        required: true
        type: integer
      - description: Git Credential identifier
        in: path
        name: credentialID
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
      summary: Update a git-credential associated to a user
      tags:
      - users
  /users/{id}/helm/repositories:
    get:
      description: |-
        Inspect a user helm repositories.
        **Access policy**: authenticated
      operationId: HelmUserRepositoriesList
      parameters:
      - description: User identifier
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
            $ref: '#/definitions/users.helmUserRepositoryResponse'
        "400":
          description: Invalid request
        "403":
          description: Permission denied
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: List a users helm repositories
      tags:
      - helm
    post:
      consumes:
      - application/json
      description: |-
        Create a user helm repository.
        **Access policy**: authenticated
      operationId: HelmUserRepositoryCreate
      parameters:
      - description: User identifier
        in: path
        name: id
        required: true
        type: integer
      - description: Helm Repository
        in: body
        name: payload
        required: true
        schema:
          $ref: '#/definitions/users.addHelmRepoUrlPayload'
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            $ref: '#/definitions/portainer.HelmUserRepository'
        "400":
          description: Invalid request
        "403":
          description: Permission denied
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Create a user helm repository
      tags:
      - helm
  /users/{id}/helm/repositories/{repositoryID}:
    delete:
      description: '**Access policy**: authenticated'
      operationId: HelmUserRepositoryDelete
      parameters:
      - description: User identifier
        in: path
        name: id
        required: true
        type: integer
      - description: Repository identifier
        in: path
        name: repositoryID
        required: true
        type: integer
      produces:
      - application/json
      responses:
        "204":
          description: Success
        "400":
          description: Invalid request
        "403":
          description: Permission denied
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Delete a users helm repository
      tags:
      - helm
  /users/{id}/memberships:
    get:
      description: |-
        Inspect a user memberships.
        **Access policy**: restricted
      operationId: UserMembershipsInspect
      parameters:
      - description: User identifier
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
            $ref: '#/definitions/portainer.TeamMembership'
        "400":
          description: Invalid request
        "403":
          description: Permission denied
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Inspect a user memberships
      tags:
      - users
  /users/{id}/namespaces:
    get:
      description: |-
        Retrieves user's role authorizations of all namespaces in all k8s environments(endpoints)
        **Access policy**: restricted
      operationId: UserNamespaces
      parameters:
      - description: User identifier
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
            $ref: '#/definitions/users.namespaceMapping'
        "400":
          description: Invalid request
        "403":
          description: Permission denied
        "404":
          description: User not found
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Retrieves all k8s namespaces for an user
      tags:
      - users
  /users/{id}/passwd:
    put:
      consumes:
      - application/json
      description: |-
        Update password for the specified user.
        **Access policy**: authenticated
      operationId: UserUpdatePassword
      parameters:
      - description: identifier
        in: path
        name: id
        required: true
        type: integer
      - description: details
        in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/users.userUpdatePasswordPayload'
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
          description: User not found
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Update password for a user
      tags:
      - users
  /users/{id}/tokens:
    get:
      description: |-
        Gets all API keys for a user.
        Only the calling user or admin can retrieve api-keys.
        **Access policy**: authenticated
      operationId: UserGetAPIKeys
      parameters:
      - description: User identifier
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
              $ref: '#/definitions/portainer.APIKey'
            type: array
        "400":
          description: Invalid request
        "403":
          description: Permission denied
        "404":
          description: User not found
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Get all API keys for a user
      tags:
      - users
    post:
      consumes:
      - application/json
      description: |-
        Generates an API key for a user.
        Only the calling user can generate a token for themselves.
        Password is required only for internal authentication.
        **Access policy**: restricted
      operationId: UserGenerateAPIKey
      parameters:
      - description: User identifier
        in: path
        name: id
        required: true
        type: integer
      - description: details
        in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/users.userAccessTokenCreatePayload'
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            $ref: '#/definitions/users.accessTokenResponse'
        "400":
          description: Invalid request
        "401":
          description: Unauthorized
        "403":
          description: Permission denied
        "404":
          description: User not found
        "500":
          description: Server error
      security:
      - jwt: []
      summary: Generate an API key for a user
      tags:
      - users
  /users/{id}/tokens/{keyID}:
    delete:
      description: |-
        Remove an api-key associated to a user..
        Only the calling user or admin can remove api-key.
        **Access policy**: authenticated
      operationId: UserRemoveAPIKey
      parameters:
      - description: User identifier
        in: path
        name: id
        required: true
        type: integer
      - description: Api Key identifier
        in: path
        name: keyID
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
      summary: Remove an api-key associated to a user
      tags:
      - users
  /users/admin/check:
    get:
      description: |-
        Check if an administrator account exists in the database.
        **Access policy**: public
      operationId: UserAdminCheck
      responses:
        "204":
          description: Success
        "404":
          description: User not found
      summary: Check administrator account existence
      tags:
      - users
  /users/admin/init:
    post:
      consumes:
      - application/json
      description: |-
        Initialize the 'admin' user account.
        **Access policy**: public
      operationId: UserAdminInit
      parameters:
      - description: User details
        in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/users.adminInitPayload'
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            $ref: '#/definitions/portaineree.User'
        "400":
          description: Invalid request
        "409":
          description: Admin user already initialized
        "500":
          description: Server error
      summary: Initialize administrator account
      tags:
      - users
  /users/me:
    get:
      description: |-
        Retrieve details about the current user.
        User passwords are filtered out, and should never be accessible.
        **Access policy**: authenticated
      operationId: CurrentUserInspect
      parameters:
      - description: Set to true to avoid including the environment authorizations
          in the response
        in: query
        name: noEndpointAuthorizations
        required: true
        type: boolean
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            $ref: '#/definitions/portaineree.User'
        "400":
          description: Invalid request
        "403":
          description: Permission denied
        "404":
          description: User not found
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Inspect the current user
      tags:
      - users
  /users/me/auth/{endpointID}:
    get:
      description: |-
        Retrieve environment authorizations for the current  user.
        **Access policy**: authenticated
      operationId: CurrentUserEndpointAuthorizationsInspect
      parameters:
      - description: Environment identifier
        in: path
        name: endpointID
        required: true
        type: integer
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            $ref: '#/definitions/users.CurrentUserEndpointAuthResponse'
        "400":
          description: Invalid request
        "403":
          description: Permission denied
        "404":
          description: User not found
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Inspect environment authorizations for the current user
      tags:
      - users
  /webhooks:
    get:
      consumes:
      - application/json
      description: '**Access policy**: authenticated'
      parameters:
      - description: Filters (json-string)
        example: '{"EndpointID":1,"ResourceID":"abc12345-abcd-2345-ab12-58005b4a0260"}'
        in: query
        name: filters
        type: string
      produces:
      - application/json
      responses:
        "200":
          description: OK
          schema:
            items:
              $ref: '#/definitions/portainer.Webhook'
            type: array
        "400":
          description: Bad Request
        "500":
          description: Internal Server Error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: List webhooks
      tags:
      - webhooks
    post:
      consumes:
      - application/json
      description: '**Access policy**: authenticated'
      parameters:
      - description: Webhook data
        in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/webhooks.webhookCreatePayload'
      produces:
      - application/json
      responses:
        "200":
          description: OK
          schema:
            $ref: '#/definitions/portainer.Webhook'
        "400":
          description: Invalid request
        "409":
          description: A webhook for this resource already exists
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Create a webhook
      tags:
      - webhooks
  /webhooks/{id}:
    delete:
      description: '**Access policy**: authenticated'
      parameters:
      - description: Webhook id
        in: path
        name: id
        required: true
        type: integer
      responses:
        "202":
          description: Webhook deleted
        "400":
          description: Bad Request
        "500":
          description: Internal Server Error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Delete a webhook
      tags:
      - webhooks
    post:
      description: |-
        Acts on a passed in token UUID to restart the docker service
        **Access policy**: public
      parameters:
      - description: Webhook token
        in: path
        name: id
        required: true
        type: string
      responses:
        "202":
          description: Webhook executed
        "400":
          description: Bad Request
        "500":
          description: Internal Server Error
      summary: Execute a webhook
      tags:
      - webhooks
    put:
      consumes:
      - application/json
      description: '**Access policy**: authenticated'
      parameters:
      - description: Webhook id
        in: path
        name: id
        required: true
        type: integer
      - description: Webhook data
        in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/webhooks.webhookUpdatePayload'
      produces:
      - application/json
      responses:
        "200":
          description: OK
          schema:
            $ref: '#/definitions/portainer.Webhook'
        "400":
          description: Bad Request
        "409":
          description: Conflict
        "500":
          description: Internal Server Error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Update a webhook
      tags:
      - webhooks
  /webhooks/{id}/reassign:
    put:
      consumes:
      - application/json
      description: '**Access policy**: authenticated'
      parameters:
      - description: Webhook id
        in: path
        name: id
        required: true
        type: integer
      - description: Webhook data
        in: body
        name: body
