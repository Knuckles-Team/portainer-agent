        in: path
        name: namespace
        required: true
        type: string
      - description: Ingress details
        in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/models.K8sIngressInfo'
      produces:
      - application/json
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
          description: Unable to find an environment with the specified identifier.
        "409":
          description: Conflict - an ingress with the same name already exists in
            the specified namespace.
        "500":
          description: Server error occurred while attempting to create an ingress.
      security:
      - ApiKeyAuth: []
        jwt: []
      summary: Create an Ingress
      tags:
      - kubernetes
    put:
      consumes:
      - application/json
      description: |-
        Update an Ingress for the provided environment.
        **Access policy**: Authenticated user.
      operationId: UpdateKubernetesIngress
      parameters:
      - description: Environment identifier
        in: path
        name: id
        required: true
        type: integer
      - description: Namespace name
        in: path
        name: namespace
        required: true
        type: string
      - description: Ingress details
        in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/models.K8sIngressInfo'
      produces:
      - application/json
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
            or unable to find the specified ingress.
        "500":
          description: Server error occurred while attempting to update the specified
            ingress.
      security:
      - ApiKeyAuth: []
        jwt: []
      summary: Update an Ingress
      tags:
      - kubernetes
  /kubernetes/{id}/namespaces/{namespace}/ingresses/{ingress}:
    get:
      description: |-
        Get an Ingress by name for the provided environment.
        **Access policy**: Authenticated user.
      operationId: GetKubernetesIngress
      parameters:
      - description: Environment identifier
        in: path
        name: id
        required: true
        type: integer
      - description: Namespace name
        in: path
        name: namespace
        required: true
        type: string
      - description: Ingress name
        in: path
        name: ingress
        required: true
        type: string
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            $ref: '#/definitions/models.K8sIngressInfo'
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
            or unable to find an ingress with the specified name.
        "500":
          description: Server error occurred while attempting to retrieve an ingress.
      security:
      - ApiKeyAuth: []
        jwt: []
      summary: Get an Ingress by name
      tags:
      - kubernetes
  /kubernetes/{id}/namespaces/{namespace}/secrets/{secret}:
    get:
      description: |-
        Get a Secret by name for a given namespace.
        **Access policy**: Authenticated user.
      operationId: GetKubernetesSecret
      parameters:
      - description: Environment identifier
        in: path
        name: id
        required: true
        type: integer
      - description: The namespace name where the secret is located
        in: path
        name: namespace
        required: true
        type: string
      - description: The secret name to get details for
        in: path
        name: secret
        required: true
        type: string
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            $ref: '#/definitions/models.K8sSecret'
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
          description: Server error occurred while attempting to retrieve a secret
            by name belong in a namespace.
      security:
      - ApiKeyAuth: []
        jwt: []
      summary: Get a Secret
      tags:
      - kubernetes
  /kubernetes/{id}/namespaces/{namespace}/services:
    get:
      description: |-
        Get a list of services for a given namespace.
        **Access policy**: Authenticated user.
      operationId: GetKubernetesServicesByNamespace
      parameters:
      - description: Environment identifier
        in: path
        name: id
        required: true
        type: integer
      - description: Namespace name
        in: path
        name: namespace
        required: true
        type: string
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            items:
              $ref: '#/definitions/models.K8sServiceInfo'
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
          description: Server error occurred while attempting to retrieve all services
            for a namespace.
      security:
      - ApiKeyAuth: []
        jwt: []
      summary: Get a list of services for a given namespace
      tags:
      - kubernetes
    post:
      consumes:
      - application/json
      description: |-
        Create a service within a given namespace
        **Access policy**: Authenticated user.
      operationId: CreateKubernetesService
      parameters:
      - description: Environment identifier
        in: path
        name: id
        required: true
        type: integer
      - description: Namespace name
        in: path
        name: namespace
        required: true
        type: string
      - description: Service definition
        in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/models.K8sServiceInfo'
      produces:
      - application/json
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
          description: Unable to find an environment with the specified identifier.
        "500":
          description: Server error occurred while attempting to create a service.
      security:
      - ApiKeyAuth: []
        jwt: []
      summary: Create a service
      tags:
      - kubernetes
    put:
      consumes:
      - application/json
      description: |-
        Update a service within a given namespace.
        **Access policy**: Authenticated user.
      operationId: UpdateKubernetesService
      parameters:
      - description: Environment identifier
        in: path
        name: id
        required: true
        type: integer
      - description: Namespace name
        in: path
        name: namespace
        required: true
        type: string
      - description: Service definition
        in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/models.K8sServiceInfo'
      produces:
      - application/json
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
            or unable to find the service to update.
        "500":
          description: Server error occurred while attempting to update a service.
      security:
      - ApiKeyAuth: []
        jwt: []
      summary: Update a service
      tags:
      - kubernetes
  /kubernetes/{id}/namespaces/{namespace}/system:
    put:
      consumes:
      - application/json
      description: |-
        Toggle the system state for a namespace
        **Access policy**: Administrator or environment administrator.
      operationId: KubernetesNamespacesToggleSystem
      parameters:
      - description: Environment identifier
        in: path
        name: id
        required: true
        type: integer
      - description: Namespace name
        in: path
        name: namespace
        required: true
        type: string
      - description: Update details
        in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/github_com_portainer_portainer-ee_api_http_handler_kubernetes.namespacesToggleSystemPayload'
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
            or unable to find the namespace to update.
        "500":
          description: Server error occurred while attempting to update the system
            state of the namespace.
      security:
      - ApiKeyAuth: []
        jwt: []
      summary: Toggle the system state for a namespace
      tags:
      - kubernetes
  /kubernetes/{id}/namespaces/{namespace}/volumes:
    get:
      description: |-
        Get a list of kubernetes volumes within the specified namespace in the given environment (Endpoint). The Endpoint ID must be a valid Portainer environment identifier.
        **Access policy**: Authenticated user.
      operationId: GetKubernetesVolumesInNamespace
      parameters:
      - description: Environment identifier
        in: path
        name: id
        required: true
        type: integer
      - description: Namespace identifier
        in: path
        name: namespace
        required: true
        type: string
      - description: When set to True, include the applications that are using the
          volumes. It is set to false by default
        in: query
        name: withApplications
        type: boolean
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            additionalProperties:
              $ref: '#/definitions/kubernetes.K8sVolumeInfo'
            type: object
        "400":
          description: Invalid request payload, such as missing required fields or
            fields not meeting validation criteria.
        "403":
          description: Unauthorized access or operation not allowed.
        "500":
          description: Server error occurred while attempting to retrieve kubernetes
            volumes in the namespace.
      security:
      - ApiKeyAuth: []
        jwt: []
      summary: Get Kubernetes volumes within a namespace in the given Portainer environment
      tags:
      - kubernetes
  /kubernetes/{id}/namespaces/count:
    get:
      description: |-
        Get the total number of kubernetes namespaces within the given environment, including the system namespaces. The total count depends on the user's role and permissions.
        **Access policy**: Authenticated user.
      operationId: GetKubernetesNamespacesCount
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
          description: Server error occurred while attempting to compute the namespace
            count.
      security:
      - ApiKeyAuth: []
        jwt: []
      summary: Get the total number of kubernetes namespaces within the given Portainer
        environment.
      tags:
      - kubernetes
  /kubernetes/{id}/nodes/{name}/drain:
    post:
      consumes:
      - application/json
      description: |-
        Drain a Kubernetes node by safely evicting all pods from the node, preparing it for maintenance or removal
        **Access policy**: authenticated
      operationId: drainNode
      parameters:
      - description: Environment(Endpoint) identifier
        in: path
        name: id
        required: true
        type: integer
      - description: Name of the node to drain
        in: path
        name: name
        required: true
        type: string
      responses:
        "204":
          description: Success
        "400":
          description: Invalid request, such as missing required fields or fields
            not meeting validation criteria.
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
            or unable to find the specified node.
        "500":
          description: Server error occurred while attempting to drain node.
      security:
      - ApiKeyAuth: []
        jwt: []
      summary: Drain a Kubernetes node
      tags:
      - kubernetes
  /kubernetes/{id}/nodes_limits:
    get:
      description: |-
        Get CPU and memory limits of all nodes within k8s cluster.
        **Access policy**: Authenticated user.
      operationId: GetKubernetesNodesLimits
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
            $ref: '#/definitions/portainer.K8sNodesLimits'
        "400":
          description: Invalid request
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
          description: Server error occurred while attempting to retrieve nodes limits.
      security:
      - ApiKeyAuth: []
        jwt: []
      summary: Get CPU and memory limits of all nodes within k8s cluster.
      tags:
      - kubernetes
  /kubernetes/{id}/rbac_enabled:
    get:
      description: |-
        Check if RBAC is enabled in the specified Kubernetes cluster.
        **Access policy**: Authenticated user.
      operationId: GetKubernetesRBACStatus
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
          description: RBAC status
          schema:
            type: boolean
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
          description: Server error occurred while attempting to retrieve the RBAC
            status.
      security:
      - ApiKeyAuth: []
        jwt: []
      summary: Check if RBAC is enabled
      tags:
      - kubernetes
  /kubernetes/{id}/role_bindings/delete:
    post:
      consumes:
      - application/json
      description: |-
        Delete the provided list of role bindings.
        **Access policy**: Authenticated user.
      operationId: DeleteRoleBindings
      parameters:
      - description: Environment identifier
        in: path
        name: id
        required: true
        type: integer
      - description: A map where the key is the namespace and the value is an array
          of role bindings to delete
        in: body
        name: payload
        required: true
        schema:
          $ref: '#/definitions/models.K8sRoleBindingDeleteRequests'
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
            or unable to find a specific role binding.
        "500":
          description: Server error occurred while attempting to delete role bindings.
      security:
      - ApiKeyAuth: []
        jwt: []
      summary: Delete role bindings
      tags:
      - kubernetes
  /kubernetes/{id}/rolebindings:
    get:
      description: |-
        Get a list of kubernetes role bindings that the user has access to.
        **Access policy**: Authenticated user.
      operationId: GetKubernetesRoleBindings
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
            items:
              $ref: '#/definitions/models.K8sRoleBinding'
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
          description: Server error occurred while attempting to retrieve the list
            of role bindings.
      security:
      - ApiKeyAuth: []
        jwt: []
      summary: Get a list of kubernetes role bindings
      tags:
      - kubernetes
  /kubernetes/{id}/roles:
    get:
      description: |-
