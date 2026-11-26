        required: true
        type: integer
      - description: The namespace name to get details for
        in: path
        name: namespace
        required: true
        type: string
      - description: The name of the custom resource, e.g. 'pg-cluster'
        in: path
        name: name
        required: true
        type: string
      - description: The CustomResourceDefinition name of the custom resource, e.g.
          'clusters.postgresql.cnpg.io'
        in: query
        name: definition
        required: true
        type: string
      - description: The format of the custom resource, e.g. 'yaml' or 'json'
        in: query
        name: format
        type: string
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            items:
              $ref: '#/definitions/unstructured.Unstructured'
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
          description: Server error occurred while attempting to retrieve the custom
            resource.
      security:
      - ApiKeyAuth: []
        jwt: []
      summary: Get a list of kubernetes Custom Resources
      tags:
      - kubernetes
  /kubernetes/{id}/dashboard:
    get:
      consumes:
      - application/json
      description: |-
        Get the dashboard summary data which is simply a count of a range of different commonly used kubernetes resources.
        **Access policy**: Authenticated user.
      operationId: GetKubernetesDashboard
      parameters:
      - description: Environment (Endpoint) identifier
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
              $ref: '#/definitions/models.K8sDashboard'
            type: array
        "400":
          description: Invalid request
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
        jwt: []
      summary: Get the dashboard summary data
      tags:
      - kubernetes
  /kubernetes/{id}/describe:
    get:
      description: |-
        Get a description of a kubernetes resource.
        **Access policy**: Authenticated user.
      operationId: DescribeResource
      parameters:
      - description: Environment identifier
        in: path
        name: id
        required: true
        type: integer
      - description: Resource name
        in: query
        name: name
        required: true
        type: string
      - description: Resource kind
        in: query
        name: kind
        required: true
        type: string
      - description: Namespace
        in: query
        name: namespace
        type: string
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            $ref: '#/definitions/github_com_portainer_portainer-ee_api_http_handler_kubernetes.describeResourceResponse'
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
          description: Server error occurred while attempting to retrieve resource
            description
      security:
      - ApiKeyAuth: []
        jwt: []
      summary: Get a description of a kubernetes resource
      tags:
      - kubernetes
  /kubernetes/{id}/events:
    get:
      description: |-
        Get events by query param resourceId
        **Access policy**: Authenticated user.
      operationId: getAllKubernetesEvents
      parameters:
      - description: Environment identifier
        in: path
        name: id
        required: true
        type: integer
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
          description: Server error occurred while attempting to retrieve the events.
      security:
      - ApiKeyAuth: []
        jwt: []
      summary: Gets kubernetes events
      tags:
      - kubernetes
  /kubernetes/{id}/ingresscontrollers:
    get:
      description: |-
        Get a list of ingress controllers for the given environment. If the allowedOnly query parameter is set, only ingress controllers that are allowed by the environment's ingress configuration will be returned.
        **Access policy**: Authenticated user.
      operationId: GetAllKubernetesIngressControllers
      parameters:
      - description: Environment identifier
        in: path
        name: id
        required: true
        type: integer
      - description: Only return allowed ingress controllers
        in: query
        name: allowedOnly
        type: boolean
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
          description: Unable to find an environment with the specified identifier.
        "500":
          description: Server error occurred while attempting to retrieve ingress
            controllers
      security:
      - ApiKeyAuth: []
        jwt: []
      summary: Get a list of ingress controllers
      tags:
      - kubernetes
    put:
      consumes:
      - application/json
      description: |-
        Update (block/unblock) ingress controllers for the provided environment.
        **Access policy**: Authenticated user.
      operationId: UpdateKubernetesIngressControllers
      parameters:
      - description: Environment identifier
        in: path
        name: id
        required: true
        type: integer
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
          description: Unable to find an environment with the specified identifier
            or unable to find the ingress controllers to update.
        "500":
          description: Server error occurred while attempting to update ingress controllers.
      security:
      - ApiKeyAuth: []
        jwt: []
      summary: Update (block/unblock) ingress controllers
      tags:
      - kubernetes
  /kubernetes/{id}/ingresses:
    get:
      description: |-
        Get kubernetes ingresses at the cluster level for the provided environment.
        **Access policy**: Authenticated user.
      operationId: GetAllKubernetesClusterIngresses
      parameters:
      - description: Environment identifier
        in: path
        name: id
        required: true
        type: integer
      - description: Lookup services associated with each ingress
        in: query
        name: withServices
        type: boolean
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
          description: Server error occurred while attempting to retrieve ingresses.
      security:
      - ApiKeyAuth: []
        jwt: []
      summary: Get kubernetes ingresses at the cluster level
      tags:
      - kubernetes
  /kubernetes/{id}/ingresses/count:
    get:
      description: |-
        Get the number of kubernetes ingresses within the given environment.
        **Access policy**: Authenticated user.
      operationId: GetAllKubernetesClusterIngressesCount
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
          description: Server error occurred while attempting to retrieve ingresses
            count.
      security:
      - ApiKeyAuth: []
        jwt: []
      summary: Get Ingresses count
      tags:
      - kubernetes
  /kubernetes/{id}/ingresses/delete:
    post:
      consumes:
      - application/json
      description: |-
        Delete one or more Ingresses in the provided environment.
        **Access policy**: Authenticated user.
      operationId: DeleteKubernetesIngresses
      parameters:
      - description: Environment identifier
        in: path
        name: id
        required: true
        type: integer
      - description: Ingress details
        in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/models.K8sIngressDeleteRequests'
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
            or unable to find a specific ingress.
        "500":
          description: Server error occurred while attempting to delete specified
            ingresses.
      security:
      - ApiKeyAuth: []
        jwt: []
      summary: Delete one or more Ingresses
      tags:
      - kubernetes
  /kubernetes/{id}/jobs:
    get:
      description: |-
        Get a list of kubernetes Jobs that the user has access to.
        **Access policy**: Authenticated user.
      operationId: GetKubernetesJobs
      parameters:
      - description: Environment identifier
        in: path
        name: id
        required: true
        type: integer
      - description: Whether to include Jobs that have a cronjob owner
        in: query
        name: includeCronJobChildren
        type: boolean
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            items:
              $ref: '#/definitions/kubernetes.K8sJob'
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
            of Jobs.
      security:
      - ApiKeyAuth: []
        jwt: []
      summary: Get a list of kubernetes Jobs
      tags:
      - kubernetes
  /kubernetes/{id}/jobs/delete:
    post:
      consumes:
      - application/json
      description: |-
        Delete the provided list of Jobs.
        **Access policy**: Authenticated user.
      operationId: DeleteJobs
      parameters:
      - description: Environment identifier
        in: path
        name: id
        required: true
        type: integer
      - description: A map where the key is the namespace and the value is an array
          of Jobs to delete
        in: body
        name: payload
        required: true
        schema:
          $ref: '#/definitions/kubernetes.K8sJobDeleteRequests'
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
            or unable to find a specific service account.
        "500":
          description: Server error occurred while attempting to delete Jobs.
      security:
      - ApiKeyAuth: []
        jwt: []
      summary: Delete Jobs
      tags:
      - kubernetes
  /kubernetes/{id}/max_resource_limits:
    get:
      description: |-
        Get max CPU and memory limits (unused resources) of all nodes within k8s cluster.
        **Access policy**: Authenticated user.
      operationId: GetKubernetesMaxResourceLimits
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
      summary: Get max CPU and memory limits of all nodes within k8s cluster
      tags:
      - kubernetes
  /kubernetes/{id}/metrics/applications_resources:
    get:
      consumes:
      - application/json
      description: |-
        Get the total CPU (cores) and memory (bytes) requests and limits of all applications across all namespaces.
        **Access policy**: authenticated
      operationId: GetApplicationsResources
      parameters:
      - description: Environment(Endpoint) identifier
        in: path
        name: id
        required: true
        type: integer
      - description: Node name
        in: query
        name: node
        required: true
        type: string
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            $ref: '#/definitions/models.K8sApplicationResource'
        "400":
          description: Invalid request
        "401":
          description: Unauthorized
        "403":
          description: Permission denied
        "404":
          description: Environment(Endpoint) not found
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
        jwt: []
      summary: Get the total CPU (cores) and memory requests (MB) and limits of all
        applications across all namespaces
      tags:
      - kubernetes
  /kubernetes/{id}/metrics/nodes:
    get:
      description: |-
        Get a list of metrics associated with all nodes of a cluster.
        **Access policy**: Authenticated user.
      operationId: GetKubernetesMetricsForAllNodes
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
            $ref: '#/definitions/v1beta1.NodeMetricsList'
        "401":
          description: Unauthorized access - the user is not authenticated or does
            not have the necessary permissions. Ensure that you have provided a valid
            API key or JWT token, and that you have the required permissions.
        "500":
          description: Server error occurred while attempting to retrieve the list
            of nodes with their live metrics.
      security:
      - ApiKeyAuth: []
        jwt: []
      summary: Get a list of nodes with their live metrics
      tags:
      - kubernetes
  /kubernetes/{id}/metrics/nodes/{name}:
    get:
      description: |-
        Get live metrics for the specified node.
        **Access policy**: Authenticated user.
      operationId: GetKubernetesMetricsForNode
      parameters:
      - description: Environment identifier
        in: path
        name: id
        required: true
        type: integer
      - description: Node identifier
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
            $ref: '#/definitions/v1beta1.NodeMetrics'
        "400":
          description: Invalid request payload, such as missing required fields or
            fields not meeting validation criteria.
        "401":
          description: Unauthorized access - the user is not authenticated or does
            not have the necessary permissions. Ensure that you have provided a valid
            API key or JWT token, and that you have the required permissions.
        "500":
          description: Server error occurred while attempting to retrieve the live
            metrics for the specified node.
      security:
      - ApiKeyAuth: []
        jwt: []
      summary: Get live metrics for a node
      tags:
      - kubernetes
  /kubernetes/{id}/metrics/pods/{namespace}:
    get:
      description: |-
        Get a list of pods with their live metrics for the specified namespace.
        **Access policy**: Authenticated user.
      operationId: GetKubernetesMetricsForAllPods
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
            $ref: '#/definitions/v1beta1.PodMetricsList'
        "400":
          description: Invalid request payload, such as missing required fields or
            fields not meeting validation criteria.
        "401":
          description: Unauthorized access - the user is not authenticated or does
            not have the necessary permissions. Ensure that you have provided a valid
            API key or JWT token, and that you have the required permissions.
        "500":
          description: Server error occurred while attempting to retrieve the list
            of pods with their live metrics.
      security:
      - ApiKeyAuth: []
        jwt: []
      summary: Get a list of pods with their live metrics
      tags:
      - kubernetes
  /kubernetes/{id}/metrics/pods/{namespace}/{name}:
    get:
      description: |-
        Get live metrics for the specified pod.
        **Access policy**: Authenticated user.
      operationId: GetKubernetesMetricsForPod
      parameters:
      - description: Environment identifier
        in: path
        name: id
        required: true
