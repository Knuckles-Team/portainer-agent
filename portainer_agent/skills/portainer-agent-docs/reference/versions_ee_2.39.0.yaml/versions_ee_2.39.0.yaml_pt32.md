        required: true
        schema:
          $ref: '#/definitions/webhooks.webhookReassignPayload'
      produces:
      - application/json
      responses:
        "200":
          description: OK
          schema:
            $ref: '#/definitions/portainer.Webhook'
        "204":
          description: No Content
        "400":
          description: Bad Request
        "404":
          description: Not Found
        "500":
          description: Internal Server Error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Reassign a webhook to another resource
      tags:
      - webhooks
  /websocket/attach:
    get:
      consumes:
      - application/json
      description: |-
        If the nodeName query parameter is present, the request will be proxied to the underlying agent environment(endpoint).
        If the nodeName query parameter is not specified, the request will be upgraded to the websocket protocol and
        an AttachStart operation HTTP request will be created and hijacked.
        **Access policy**: authenticated
      parameters:
      - description: environment(endpoint) ID of the environment(endpoint) where the
          resource is located
        in: query
        name: endpointId
        required: true
        type: integer
      - description: node name
        in: query
        name: nodeName
        type: string
      - description: JWT token used for authentication against this environment(endpoint)
        in: query
        name: token
        required: true
        type: string
      produces:
      - application/json
      responses:
        "200":
          description: OK
        "400":
          description: Bad Request
        "403":
          description: Forbidden
        "404":
          description: Not Found
        "500":
          description: Internal Server Error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Attach a websocket
      tags:
      - websocket
  /websocket/exec:
    get:
      consumes:
      - application/json
      description: |-
        If the nodeName query parameter is present, the request will be proxied to the underlying agent environment(endpoint).
        If the nodeName query parameter is not specified, the request will be upgraded to the websocket protocol and
        an ExecStart operation HTTP request will be created and hijacked.
      parameters:
      - description: environment(endpoint) ID of the environment(endpoint) where the
          resource is located
        in: query
        name: endpointId
        required: true
        type: integer
      - description: node name
        in: query
        name: nodeName
        type: string
      - description: JWT token used for authentication against this environment(endpoint)
        in: query
        name: token
        required: true
        type: string
      produces:
      - application/json
      responses:
        "200":
          description: OK
        "400":
          description: Bad Request
        "409":
          description: Conflict
        "500":
          description: Internal Server Error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Execute a websocket
      tags:
      - websocket
  /websocket/kubernetes-shell:
    get:
      consumes:
      - application/json
      description: |-
        The request will be upgraded to the websocket protocol. The request will proxy input from the client to the pod via long-lived websocket connection.
        **Access policy**: authenticated
      parameters:
      - description: environment(endpoint) ID of the environment(endpoint) where the
          resource is located
        in: query
        name: endpointId
        required: true
        type: integer
      - description: JWT token used for authentication against this environment(endpoint)
        in: query
        name: token
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
          description: Permission denied
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Execute a websocket on kubectl shell pod
      tags:
      - websocket
  /websocket/microk8s-shell:
    get:
      consumes:
      - application/json
      description: |-
        When called, an SSH session to a microk8s cluster node will be created
        an ssh session will be created and hijacked.
        **Access policy**: authenticated
      parameters:
      - description: environment(endpoint) ID of the environment(endpoint) where the
          resource is located
        in: query
        name: endpointId
        required: true
        type: integer
      - description: node ip address
        in: query
        name: nodeIp
        required: true
        type: string
      - description: JWT token used for authentication against this environment(endpoint)
        in: query
        name: token
        required: true
        type: string
      produces:
      - application/json
      responses:
        "200":
          description: OK
        "400":
          description: Bad Request
        "409":
          description: Conflict
        "500":
          description: Internal Server Error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Connect to a remote SSH Shell via a websocket
      tags:
      - websocket
  /websocket/pod:
    get:
      consumes:
      - application/json
      description: |-
        The request will be upgraded to the websocket protocol.
        **Access policy**: authenticated
      parameters:
      - description: environment(endpoint) ID of the environment(endpoint) where the
          resource is located
        in: query
        name: endpointId
        required: true
        type: integer
      - description: namespace where the container is located
        in: query
        name: namespace
        required: true
        type: string
      - description: name of the pod containing the container
        in: query
        name: podName
        required: true
        type: string
      - description: name of the container
        in: query
        name: containerName
        required: true
        type: string
      - description: command to execute in the container
        in: query
        name: command
        required: true
        type: string
      - description: JWT token used for authentication against this environment(endpoint)
        in: query
        name: token
        required: true
        type: string
      produces:
      - application/json
      responses:
        "200":
          description: OK
        "400":
          description: Bad Request
        "403":
          description: Forbidden
        "404":
          description: Not Found
        "500":
          description: Internal Server Error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Execute a websocket on pod
      tags:
      - websocket
schemes:
- http
- https
securityDefinitions:
  ApiKeyAuth:
    in: header
    name: X-API-KEY
    type: apiKey
  jwt:
    in: header
    name: Authorization
    type: apiKey
swagger: "2.0"
tags:
- description: Authenticate against Portainer HTTP API
  name: auth
- description: Manage backups
  name: backup
- description: Manage Custom Templates
  name: custom_templates
- description: Manage Docker resources
  name: docker
- description: Manage Edge related environment settings
  name: edge
- description: Manage Edge Groups
  name: edge_groups
- description: Manage Edge Jobs
  name: edge_jobs
- description: Manage Edge Stacks
  name: edge_stacks
- description: Manage Edge Templates
  name: edge_templates
- description: Manage environment groups
  name: endpoint_groups
- description: Manage environments
  name: endpoints
- description: Operate git repository
  name: gitops
- description: Manage Helm charts
  name: helm
- description: Manage Intel AMT settings
  name: intel
- name: kaas
- description: Manage Kubernetes cluster
  name: kubernetes
- description: Manage LDAP settings
  name: ldap
- description: Manage metrics
  name: metrics
- description: Fetch the message of the day
  name: motd
- description: Manage Docker registries
  name: registries
- description: Manage access control on Docker resources
  name: resource_controls
- description: Manage roles
  name: roles
- description: Manage Portainer settings
  name: settings
- description: Manage stacks
  name: stacks
- description: Information about the Portainer instance
  name: status
- description: Manage Portainer system
  name: system
- description: Manage tags
  name: tags
- description: Manage team memberships
  name: team_memberships
- description: Manage teams
  name: teams
- description: Manage App Templates
  name: templates
- description: Upload files
  name: upload
- description: Manage users
  name: users
- description: Manage webhooks
  name: webhooks
- description: Create exec sessions using websockets
  name: websocket

```
