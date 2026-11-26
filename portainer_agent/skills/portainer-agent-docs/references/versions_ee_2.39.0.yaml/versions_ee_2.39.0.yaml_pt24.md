        type: integer
      - description: Namespace
        in: path
        name: namespace
        required: true
        type: string
      - description: Pod identifier
        in: path
        name: name
        required: true
        type: string
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            $ref: '#/definitions/v1beta1.PodMetrics'
        "400":
          description: Invalid request payload, such as missing required fields or
            fields not meeting validation criteria.
        "401":
          description: Unauthorized access - the user is not authenticated or does
            not have the necessary permissions. Ensure that you have provided a valid
            API key or JWT token, and that you have the required permissions.
        "500":
          description: Server error occurred while attempting to retrieve the live
            metrics for the specified pod.
      security:
      - ApiKeyAuth: []
        jwt: []
      summary: Get live metrics for a pod
      tags:
      - kubernetes
  /kubernetes/{id}/namespaces:
    delete:
      description: |-
        Delete a kubernetes namespace within the given environment.
        **Access policy**: Authenticated user.
      operationId: DeleteKubernetesNamespace
      parameters:
      - description: Environment identifier
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
          description: Invalid request payload, such as missing required fields or
            fields not meeting validation criteria.
        "403":
          description: Unauthorized access or operation not allowed.
        "500":
          description: Server error occurred while attempting to delete the namespace.
      security:
      - ApiKeyAuth: []
        jwt: []
      summary: Delete a kubernetes namespace
      tags:
      - kubernetes
    get:
      description: |-
        Get a list of all namespaces within the given environment based on the user role and permissions. If the user is an admin, they can access all namespaces. If the user is not an admin, they can only access namespaces that they have access to.
        **Access policy**: Authenticated user.
      operationId: GetKubernetesNamespaces
      parameters:
      - description: Environment identifier
        in: path
        name: id
        required: true
        type: integer
      - description: When set to true, include the resource quota information as part
          of the Namespace information. Default is false
        in: query
        name: withResourceQuota
        required: true
        type: boolean
      - description: When set to true, include the unhealthy events information as
          part of the Namespace information. Default is false
        in: query
        name: withUnhealthyEvents
        required: true
        type: boolean
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            items:
              $ref: '#/definitions/portainer.K8sNamespaceInfo'
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
            of namespaces.
      security:
      - ApiKeyAuth: []
        jwt: []
      summary: Get a list of namespaces
      tags:
      - kubernetes
    post:
      consumes:
      - application/json
      description: |-
        Create a namespace within the given environment.
        **Access policy**: Authenticated user.
      operationId: CreateKubernetesNamespace
      parameters:
      - description: Environment identifier
        in: path
        name: id
        required: true
        type: integer
      - description: Namespace configuration details
        in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/models.K8sNamespaceDetails'
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            $ref: '#/definitions/portainer.K8sNamespaceInfo'
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
        "409":
          description: Conflict - the namespace already exists.
        "500":
          description: Server error occurred while attempting to create the namespace.
      security:
      - ApiKeyAuth: []
        jwt: []
      summary: Create a namespace
      tags:
      - kubernetes
    put:
      consumes:
      - application/json
      description: |-
        Update a namespace within the given environment.
        **Access policy**: Authenticated user.
      operationId: UpdateKubernetesNamespaceDeprecated
      parameters:
      - description: Environment identifier
        in: path
        name: id
        required: true
        type: integer
      - description: Namespace
        in: path
        name: namespace
        required: true
        type: string
      - description: Namespace details
        in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/models.K8sNamespaceDetails'
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            $ref: '#/definitions/portainer.K8sNamespaceInfo'
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
            or unable to find a specific namespace.
        "500":
          description: Server error occurred while attempting to update the namespace.
      security:
      - ApiKeyAuth: []
        jwt: []
      summary: Update a namespace
      tags:
      - kubernetes
  /kubernetes/{id}/namespaces/{namespace}:
    get:
      description: |-
        Get namespace details for the provided namespace within the given environment.
        **Access policy**: Authenticated user.
      operationId: GetKubernetesNamespace
      parameters:
      - description: Environment identifier
        in: path
        name: id
        required: true
        type: integer
      - description: The namespace name to get details for
        in: path
        name: namespace
        required: true
        type: string
      - description: When set to true, include the resource quota information as part
          of the Namespace information. Default is false
        in: query
        name: withResourceQuota
        required: true
        type: boolean
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            $ref: '#/definitions/portainer.K8sNamespaceInfo'
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
            or unable to find a specific namespace.
        "500":
          description: Server error occurred while attempting to retrieve specified
            namespace information.
      security:
      - ApiKeyAuth: []
        jwt: []
      summary: Get namespace details
      tags:
      - kubernetes
    put:
      consumes:
      - application/json
      description: |-
        Update a namespace within the given environment.
        **Access policy**: Authenticated user.
      operationId: UpdateKubernetesNamespace
      parameters:
      - description: Environment identifier
        in: path
        name: id
        required: true
        type: integer
      - description: Namespace
        in: path
        name: namespace
        required: true
        type: string
      - description: Namespace details
        in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/models.K8sNamespaceDetails'
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            $ref: '#/definitions/portainer.K8sNamespaceInfo'
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
            or unable to find a specific namespace.
        "500":
          description: Server error occurred while attempting to update the namespace.
      security:
      - ApiKeyAuth: []
        jwt: []
      summary: Update a namespace
      tags:
      - kubernetes
  /kubernetes/{id}/namespaces/{namespace}/applications/{kind}/{name}/restart:
    post:
      consumes:
      - application/json
      description: |-
        Restart a Kubernetes deployment, statefulset and daemonset application, using a kubectl rollout-restart
        **Access policy**: authenticated
      operationId: restartKubernetesApplication
      parameters:
      - description: Environment(Endpoint) identifier
        in: path
        name: id
        required: true
        type: integer
      - description: The namespace
        in: path
        name: namespace
        required: true
        type: string
      - description: deployment, statefulset or daemonset
        in: path
        name: kind
        required: true
        type: string
      - description: name of the application
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
            or unable to find a specific application.
        "500":
          description: Server error occurred while attempting to restart application.
      security:
      - ApiKeyAuth: []
        jwt: []
      summary: Restart a Kubernetes application
      tags:
      - kubernetes
  /kubernetes/{id}/namespaces/{namespace}/applications/{name}:
    get:
      consumes:
      - application/json
      description: |-
        Get an application by name in a specific namespace
        **Access policy**: authenticated
      operationId: GetAllKubernetesApplication
      parameters:
      - description: Environment(Endpoint) identifier
        in: path
        name: id
        required: true
        type: integer
      - description: The namespace
        in: path
        name: namespace
        required: true
        type: string
      - description: Application name
        in: path
        name: name
        required: true
        type: string
      - description: The resource type to get the application for
        in: query
        name: resourceType
        type: string
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            $ref: '#/definitions/models.K8sApplication'
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
          description: Server error occurred while attempting to retrieve the application.
      security:
      - ApiKeyAuth: []
        jwt: []
      summary: Get an application by name in a specific namespace
      tags:
      - kubernetes
  /kubernetes/{id}/namespaces/{namespace}/configmaps/{configmap}:
    get:
      description: |-
        Get a ConfigMap by name for a given namespace.
        **Access policy**: Authenticated user.
      operationId: GetKubernetesConfigMap
      parameters:
      - description: Environment identifier
        in: path
        name: id
        required: true
        type: integer
      - description: The namespace name where the configmap is located
        in: path
        name: namespace
        required: true
        type: string
      - description: The configmap name to get details for
        in: path
        name: configmap
        required: true
        type: string
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            $ref: '#/definitions/models.K8sConfigMap'
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
            or a configmap with the specified name in the given namespace.
        "500":
          description: Server error occurred while attempting to retrieve a configmap
            by name within the specified namespace.
      security:
      - ApiKeyAuth: []
        jwt: []
      summary: Get a ConfigMap
      tags:
      - kubernetes
  /kubernetes/{id}/namespaces/{namespace}/events:
    get:
      description: |-
        Get events by optional query param resourceId for a given namespace.
        **Access policy**: Authenticated user.
      operationId: getKubernetesEventsForNamespace
      parameters:
      - description: Environment identifier
        in: path
        name: id
        required: true
        type: integer
      - description: The namespace name the events are associated to
        in: path
        name: namespace
        required: true
        type: string
      - description: The resource id of the involved kubernetes object
        in: query
        name: resourceId
        type: string
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            items:
              $ref: '#/definitions/kubernetes.K8sEvent'
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
        "500":
          description: Server error occurred while attempting to retrieve the events
            within the specified namespace.
      security:
      - ApiKeyAuth: []
        jwt: []
      summary: Gets kubernetes events for namespace
      tags:
      - kubernetes
  /kubernetes/{id}/namespaces/{namespace}/ingresscontrollers:
    get:
      description: |-
        Get a list of ingress controllers for the given environment in the provided namespace.
        **Access policy**: Authenticated user.
      operationId: GetKubernetesIngressControllersByNamespace
      parameters:
      - description: Environment identifier
        in: path
        name: id
        required: true
        type: integer
      - description: Namespace
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
              $ref: '#/definitions/models.K8sIngressController'
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
          description: Unable to find an environment with the specified identifier
            or a namespace with the specified name.
        "500":
          description: Server error occurred while attempting to retrieve ingress
            controllers by a namespace
      security:
      - ApiKeyAuth: []
        jwt: []
      summary: Get a list ingress controllers by namespace
      tags:
      - kubernetes
    put:
      consumes:
      - application/json
      description: |-
        Update (block/unblock) ingress controllers by namespace for the provided environment.
        **Access policy**: Authenticated user.
      operationId: UpdateKubernetesIngressControllersByNamespace
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
      - description: Ingress controllers
        in: body
        name: body
        required: true
        schema:
          items:
            $ref: '#/definitions/models.K8sIngressController'
          type: array
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
          description: Server error occurred while attempting to update ingress controllers
            by namespace.
      security:
      - ApiKeyAuth: []
        jwt: []
      summary: Update (block/unblock) ingress controllers by namespace
      tags:
      - kubernetes
  /kubernetes/{id}/namespaces/{namespace}/ingresses:
    get:
      description: |-
        Get a list of Ingresses. If namespace is provided, it will return the list of Ingresses in that namespace.
        **Access policy**: Authenticated user.
      operationId: GetAllKubernetesIngresses
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
              $ref: '#/definitions/models.K8sIngressInfo'
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
          description: Server error occurred while attempting to retrieve ingresses
      security:
      - ApiKeyAuth: []
        jwt: []
      summary: Get a list of Ingresses
      tags:
      - kubernetes
    post:
      consumes:
      - application/json
      description: |-
        Create an Ingress for the provided environment.
        **Access policy**: Authenticated user.
      operationId: CreateKubernetesIngress
      parameters:
      - description: Environment identifier
        in: path
        name: id
        required: true
        type: integer
      - description: Namespace name
