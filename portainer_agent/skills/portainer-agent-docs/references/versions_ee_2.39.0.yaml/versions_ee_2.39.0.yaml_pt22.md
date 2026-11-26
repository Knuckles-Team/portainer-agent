            bindings.
      security:
      - ApiKeyAuth: []
        jwt: []
      summary: Delete cluster role bindings
      tags:
      - kubernetes
  /kubernetes/{id}/cluster_roles/delete:
    post:
      consumes:
      - application/json
      description: |-
        Delete the provided list of cluster roles.
        **Access policy**: Authenticated user.
      operationId: DeleteClusterRoles
      parameters:
      - description: Environment identifier
        in: path
        name: id
        required: true
        type: integer
      - description: A list of cluster roles to delete
        in: body
        name: payload
        required: true
        schema:
          items:
            type: string
          type: array
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
            or unable to find a specific cluster role.
        "500":
          description: Server error occurred while attempting to delete cluster roles.
      security:
      - ApiKeyAuth: []
        jwt: []
      summary: Delete cluster roles
      tags:
      - kubernetes
  /kubernetes/{id}/clusterrolebindings:
    get:
      description: |-
        Get a list of kubernetes cluster role bindings within the given environment at the cluster level.
        **Access policy**: Authenticated user.
      operationId: GetAllKubernetesClusterRoleBindings
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
              $ref: '#/definitions/kubernetes.K8sClusterRoleBinding'
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
            of cluster role bindings.
      security:
      - ApiKeyAuth: []
        jwt: []
      summary: Get a list of kubernetes cluster role bindings
      tags:
      - kubernetes
  /kubernetes/{id}/clusterroles:
    get:
      description: |-
        Get a list of kubernetes cluster roles within the given environment at the cluster level.
        **Access policy**: Authenticated user.
      operationId: GetAllKubernetesClusterRoles
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
              $ref: '#/definitions/kubernetes.K8sClusterRole'
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
            of cluster roles.
      security:
      - ApiKeyAuth: []
        jwt: []
      summary: Get a list of kubernetes cluster roles
      tags:
      - kubernetes
  /kubernetes/{id}/configmaps:
    get:
      description: |-
        Get a list of ConfigMaps across all namespaces in the cluster. For non-admin users, it will only return ConfigMaps based on the namespaces that they have access to.
        **Access policy**: Authenticated user.
      operationId: GetAllKubernetesConfigMaps
      parameters:
      - description: Environment identifier
        in: path
        name: id
        required: true
        type: integer
      - description: Set to true to include information about applications that use
          the ConfigMaps in the response
        in: query
        name: isUsed
        required: true
        type: boolean
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            items:
              $ref: '#/definitions/models.K8sConfigMap'
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
          description: Server error occurred while attempting to retrieve all configmaps
            from the cluster.
      security:
      - ApiKeyAuth: []
        jwt: []
      summary: Get a list of ConfigMaps
      tags:
      - kubernetes
  /kubernetes/{id}/configmaps/count:
    get:
      description: |-
        Get the count of ConfigMaps across all namespaces in the cluster. For non-admin users, it will only return the count of ConfigMaps based on the namespaces that they have access to.
        **Access policy**: Authenticated user.
      operationId: GetAllKubernetesConfigMapsCount
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
          description: Server error occurred while attempting to retrieve the count
            of all configmaps from the cluster.
      security:
      - ApiKeyAuth: []
        jwt: []
      summary: Get ConfigMaps count
      tags:
      - kubernetes
  /kubernetes/{id}/cron_jobs:
    get:
      description: |-
        Get a list of kubernetes Cron Jobs that the user has access to.
        **Access policy**: Authenticated user.
      operationId: GetKubernetesCronJobs
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
              $ref: '#/definitions/kubernetes.K8sCronJob'
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
            of Cron Jobs.
      security:
      - ApiKeyAuth: []
        jwt: []
      summary: Get a list of kubernetes Cron Jobs
      tags:
      - kubernetes
  /kubernetes/{id}/cron_jobs/delete:
    post:
      consumes:
      - application/json
      description: |-
        Delete the provided list of Cron Jobs.
        **Access policy**: Authenticated user.
      operationId: DeleteCronJobs
      parameters:
      - description: Environment identifier
        in: path
        name: id
        required: true
        type: integer
      - description: A map where the key is the namespace and the value is an array
          of Cron Jobs to delete
        in: body
        name: payload
        required: true
        schema:
          $ref: '#/definitions/kubernetes.K8sCronJobDeleteRequests'
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
          description: Server error occurred while attempting to delete Cron Jobs.
      security:
      - ApiKeyAuth: []
        jwt: []
      summary: Delete Cron Jobs
      tags:
      - kubernetes
  /kubernetes/{id}/customresourcedefinitions:
    get:
      description: |-
        Get a list of kubernetes Custom Resource Definitions that the user has access to.
        **Access policy**: Authenticated user.
      operationId: getKubernetesCustomResourceDefinitions
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
              $ref: '#/definitions/models.K8sCustomResourceDefinition'
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
            resource definitions.
      security:
      - ApiKeyAuth: []
        jwt: []
      summary: Get a list of kubernetes Custom Resource Definitions
      tags:
      - kubernetes
  /kubernetes/{id}/customresourcedefinitions/{name}:
    delete:
      description: |-
        Delete a kubernetes Custom Resource Definition.
        **Access policy**: Authenticated user.
      operationId: deleteKubernetesCustomResourceDefinition
      parameters:
      - description: Environment identifier
        in: path
        name: id
        required: true
        type: integer
      - description: The name of the Custom Resource Definition to delete.
        in: path
        name: name
        required: true
        type: string
      produces:
      - application/json
      responses:
        "204":
          description: No content.
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
          description: Server error occurred while attempting to delete the custom
            resource definition.
      security:
      - ApiKeyAuth: []
        jwt: []
      summary: Delete a kubernetes Custom Resource Definition
      tags:
      - kubernetes
    get:
      description: |-
        Get a kubernetes Custom Resource Definition.
        **Access policy**: Authenticated user.
      operationId: getKubernetesCustomResourceDefinition
      parameters:
      - description: Environment identifier
        in: path
        name: id
        required: true
        type: integer
      - description: The name of the Custom Resource Definition to get.
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
            $ref: '#/definitions/models.K8sCustomResourceDefinition'
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
            resource definition.
      security:
      - ApiKeyAuth: []
        jwt: []
      summary: Get a kubernetes Custom Resource Definition
      tags:
      - kubernetes
  /kubernetes/{id}/customresources:
    get:
      description: |-
        Get a list of kubernetes Custom Resources that the user has access to.
        **Access policy**: Authenticated user.
      operationId: getKubernetesAllCustomResources
      parameters:
      - description: Environment identifier
        in: path
        name: id
        required: true
        type: integer
      - description: The CustomResourceDefinition name of the custom resource, e.g.
          'clusters.postgresql.cnpg.io'
        in: query
        name: definition
        required: true
        type: string
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            items:
              $ref: '#/definitions/models.K8sCustomResource'
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
            resources.
      security:
      - ApiKeyAuth: []
        jwt: []
      summary: Get a list of kubernetes Custom Resources
      tags:
      - kubernetes
  /kubernetes/{id}/customresources/{name}:
    delete:
      description: |-
        Delete a cluster-scoped kubernetes Custom Resource that the user has access to.
        **Access policy**: Authenticated user.
      operationId: deleteKubernetesClusterScopedCustomResource
      parameters:
      - description: Environment identifier
        in: path
        name: id
        required: true
        type: integer
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
      produces:
      - application/json
      responses:
        "204":
          description: No Content
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
          description: Server error occurred while attempting to delete the custom
            resource.
      security:
      - ApiKeyAuth: []
        jwt: []
      summary: Delete a cluster-scoped kubernetes Custom Resource
      tags:
      - kubernetes
    get:
      description: |-
        Get a cluster-scoped kubernetes Custom Resource that the user has access to.
        **Access policy**: Authenticated user.
      operationId: getKubernetesClusterScopedCustomResource
      parameters:
      - description: Environment identifier
        in: path
        name: id
        required: true
        type: integer
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
            $ref: '#/definitions/unstructured.Unstructured'
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
      summary: Get a cluster-scoped kubernetes Custom Resource
      tags:
      - kubernetes
  /kubernetes/{id}/customresources/{namespace}/{name}:
    delete:
      description: |-
        Delete a namespaced kubernetes Custom Resource that the user has access to.
        **Access policy**: Authenticated user.
      operationId: deleteKubernetesNamespacedCustomResource
      parameters:
      - description: Environment identifier
        in: path
        name: id
        required: true
        type: integer
      - description: The namespace name to delete the custom resource from
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
      produces:
      - application/json
      responses:
        "204":
          description: No Content
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
          description: Server error occurred while attempting to delete the custom
            resource.
      security:
      - ApiKeyAuth: []
        jwt: []
      summary: Delete a namespaced kubernetes Custom Resource
      tags:
      - kubernetes
    get:
      description: |-
        Get a list of kubernetes Custom Resources that the user has access to.
        **Access policy**: Authenticated user.
      operationId: getKubernetesNamespacedCustomResource
      parameters:
      - description: Environment identifier
        in: path
        name: id
