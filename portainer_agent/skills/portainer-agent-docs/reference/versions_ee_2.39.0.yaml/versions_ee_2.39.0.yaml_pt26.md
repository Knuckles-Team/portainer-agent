        Get a list of kubernetes roles that the user has access to.
        **Access policy**: Authenticated user.
      operationId: GetKubernetesRoles
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
              $ref: '#/definitions/models.K8sRole'
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
            of roles.
      security:
      - ApiKeyAuth: []
        jwt: []
      summary: Get a list of kubernetes roles
      tags:
      - kubernetes
  /kubernetes/{id}/roles/delete:
    post:
      consumes:
      - application/json
      description: |-
        Delete the provided list of roles.
        **Access policy**: Authenticated user.
      operationId: DeleteRoles
      parameters:
      - description: Environment identifier
        in: path
        name: id
        required: true
        type: integer
      - description: A map where the key is the namespace and the value is an array
          of roles to delete
        in: body
        name: payload
        required: true
        schema:
          $ref: '#/definitions/models.K8sRoleDeleteRequests'
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
            or unable to find a specific role.
        "500":
          description: Server error occurred while attempting to delete roles.
      security:
      - ApiKeyAuth: []
        jwt: []
      summary: Delete roles
      tags:
      - kubernetes
  /kubernetes/{id}/secrets:
    get:
      description: |-
        Get a list of Secrets for a given namespace. If isUsed is set to true, information about the applications that use the secrets is also returned.
        **Access policy**: Authenticated user.
      operationId: GetKubernetesSecrets
      parameters:
      - description: Environment identifier
        in: path
        name: id
        required: true
        type: integer
      - description: When set to true, associate the Secrets with the applications
          that use them
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
              $ref: '#/definitions/models.K8sSecret'
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
          description: Server error occurred while attempting to retrieve all secrets
            from the cluster.
      security:
      - ApiKeyAuth: []
        jwt: []
      summary: Get a list of Secrets
      tags:
      - kubernetes
  /kubernetes/{id}/secrets/count:
    get:
      description: |-
        Get the count of Secrets across all namespaces that the user has access to.
        **Access policy**: Authenticated user.
      operationId: GetKubernetesSecretsCount
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
            of all secrets from the cluster.
      security:
      - ApiKeyAuth: []
        jwt: []
      summary: Get Secrets count
      tags:
      - kubernetes
  /kubernetes/{id}/service_accounts/delete:
    post:
      consumes:
      - application/json
      description: |-
        Delete the provided list of service accounts.
        **Access policy**: Authenticated user.
      operationId: DeleteServiceAccounts
      parameters:
      - description: Environment identifier
        in: path
        name: id
        required: true
        type: integer
      - description: A map where the key is the namespace and the value is an array
          of service accounts to delete
        in: body
        name: payload
        required: true
        schema:
          $ref: '#/definitions/kubernetes.K8sServiceAccountDeleteRequests'
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
          description: Server error occurred while attempting to delete service accounts.
      security:
      - ApiKeyAuth: []
        jwt: []
      summary: Delete service accounts
      tags:
      - kubernetes
  /kubernetes/{id}/serviceaccounts:
    get:
      description: |-
        Get a list of kubernetes service accounts that the user has access to.
        **Access policy**: Authenticated user.
      operationId: GetKubernetesServiceAccounts
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
              $ref: '#/definitions/kubernetes.K8sServiceAccount'
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
            of service accounts.
      security:
      - ApiKeyAuth: []
        jwt: []
      summary: Get a list of kubernetes service accounts
      tags:
      - kubernetes
  /kubernetes/{id}/services:
    get:
      description: |-
        Get a list of services that the user has access to.
        **Access policy**: Authenticated user.
      operationId: GetKubernetesServices
      parameters:
      - description: Environment identifier
        in: path
        name: id
        required: true
        type: integer
      - description: Lookup applications associated with each service
        in: query
        name: withApplications
        type: boolean
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
          description: Server error occurred while attempting to retrieve all services.
      security:
      - ApiKeyAuth: []
        jwt: []
      summary: Get a list of services
      tags:
      - kubernetes
  /kubernetes/{id}/services/count:
    get:
      description: |-
        Get the count of services that the user has access to.
        **Access policy**: Authenticated user.
      operationId: GetAllKubernetesServicesCount
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
          description: Server error occurred while attempting to retrieve the total
            count of all services.
      security:
      - ApiKeyAuth: []
        jwt: []
      summary: Get services count
      tags:
      - kubernetes
  /kubernetes/{id}/services/delete:
    post:
      consumes:
      - application/json
      description: |-
        Delete the provided list of services.
        **Access policy**: Authenticated user.
      operationId: DeleteKubernetesServices
      parameters:
      - description: Environment identifier
        in: path
        name: id
        required: true
        type: integer
      - description: A map where the key is the namespace and the value is an array
          of services to delete
        in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/models.K8sServiceDeleteRequests'
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
            or unable to find a specific service.
        "500":
          description: Server error occurred while attempting to delete services.
      security:
      - ApiKeyAuth: []
        jwt: []
      summary: Delete services
      tags:
      - kubernetes
  /kubernetes/{id}/volumes:
    get:
      description: |-
        Get a list of all kubernetes volumes within the given environment (Endpoint). The Endpoint ID must be a valid Portainer environment identifier.
        **Access policy**: Authenticated user.
      operationId: GetAllKubernetesVolumes
      parameters:
      - description: Environment identifier
        in: path
        name: id
        required: true
        type: integer
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
            volumes.
      security:
      - ApiKeyAuth: []
        jwt: []
      summary: Get Kubernetes volumes within the given Portainer environment
      tags:
      - kubernetes
  /kubernetes/{id}/volumes/{namespace}/{volume}:
    get:
      description: |-
        Get a Kubernetes volume within the given environment (Endpoint). The Endpoint ID must be a valid Portainer environment identifier.
        **Access policy**: Authenticated user.
      operationId: GetKubernetesVolume
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
      - description: Volume name
        in: path
        name: volume
        required: true
        type: string
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            $ref: '#/definitions/kubernetes.K8sVolumeInfo'
        "400":
          description: Invalid request
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
        jwt: []
      summary: Get a Kubernetes volume within the given Portainer environment
      tags:
      - kubernetes
  /kubernetes/{id}/volumes/count:
    get:
      description: |-
        Get the total number of kubernetes volumes within the given environment (Endpoint). The total count depends on the user's role and permissions. The Endpoint ID must be a valid Portainer environment identifier.
        **Access policy**: Authenticated user.
      operationId: getAllKubernetesVolumesCount
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
        "403":
          description: Unauthorized access or operation not allowed.
        "500":
          description: Server error occurred while attempting to retrieve kubernetes
            volumes count.
      security:
      - ApiKeyAuth: []
        jwt: []
      summary: Get the total number of kubernetes volumes within the given Portainer
        environment.
      tags:
      - kubernetes
  /ldap/admin-groups:
    post:
      consumes:
      - application/json
      description: |-
        Fetch LDAP admin groups from LDAP server based on AdminGroupSearchSettings
        **Access policy**: administrator
      operationId: LDAPAdminGroups
      parameters:
      - description: LDAPSettings
        in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/ldap.adminGroupsPayload'
      produces:
      - application/json
      responses:
        "200":
          description: Success
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
      summary: Fetch LDAP admin groups
      tags:
      - ldap
  /ldap/check:
    post:
      consumes:
      - application/json
      description: |-
        Test LDAP connectivity using LDAP details
        **Access policy**: administrator
      operationId: LDAPCheck
      parameters:
      - description: details
        in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/ldap.checkPayload'
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
      summary: Test LDAP connectivity
      tags:
      - ldap
  /ldap/groups:
    post:
      consumes:
      - application/json
      description: '**Access policy**: administrator'
      operationId: LDAPGroups
      parameters:
      - description: details
        in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/ldap.groupsPayload'
      responses:
        "200":
          description: Success
          schema:
            items:
              $ref: '#/definitions/portainer.LDAPUser'
            type: array
        "400":
          description: Invalid request
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Search LDAP Groups
      tags:
      - ldap
  /ldap/test:
    post:
      consumes:
      - application/json
      description: '**Access policy**: administrator'
      operationId: LDAPTestLogin
      parameters:
      - description: details
        in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/ldap.testLoginPayload'
      responses:
        "200":
          description: Success
          schema:
            $ref: '#/definitions/ldap.testLoginResponse'
        "400":
          description: Invalid request
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Test Login to ldap server
      tags:
      - ldap
  /ldap/users:
    post:
      consumes:
      - application/json
      description: '**Access policy**: administrator'
      operationId: LDAPUsers
      parameters:
      - description: details
        in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/ldap.usersPayload'
      responses:
        "200":
          description: Success
          schema:
            items:
              $ref: '#/definitions/portainer.LDAPUser'
            type: array
        "400":
          description: Invalid request
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Search LDAP Users
      tags:
      - ldap
  /licenses:
    get:
      description: '**Access policy**: administrator'
      operationId: licensesList
      produces:
      - application/json
      responses:
        "200":
          description: Licenses
          schema:
            items:
              $ref: '#/definitions/liblicense.PortainerLicense'
            type: array
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: fetches the list of licenses on Portainer
      tags:
      - license
  /licenses/add:
    post:
      consumes:
      - application/json
      description: '**Access policy**: administrator'
      operationId: licensesAttach
      parameters:
      - description: list of licenses keys to attach
        in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/licenses.attachPayload'
      - description: remove conflicting licenses
        in: query
        name: force
        type: boolean
      produces:
      - application/json
      responses:
        "200":
          description: Success license data will be in `body.Licenses`, Failures will
            be in `body.ConflictingKeys = error`
          schema:
            $ref: '#/definitions/licenses.attachResponse'
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: attaches a list of licenses to Portainer
      tags:
      - license
  /licenses/info:
    get:
      description: '**Access policy**: administrator'
      operationId: licensesInfo
      produces:
      - application/json
      responses:
        "200":
          description: License info
          schema:
            $ref: '#/definitions/licenses.LicenseInfo'
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: summarizes licenses on Portainer
      tags:
      - license
  /licenses/remove:
    post:
      consumes:
      - application/json
      description: '**Access policy**: administrator'
      operationId: licensesDelete
      parameters:
      - description: list of license keys to remove
        in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/licenses.deletePayload'
      produces:
      - application/json
      responses:
        "200":
          description: OK
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: delete license from portainer instance
      tags:
      - license
  /motd:
    get:
      description: '**Access policy**: restricted'
      operationId: MOTD
      produces:
      - application/json
      responses:
        "200":
          description: OK
          schema:
            $ref: '#/definitions/motd.motdResponse'
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: fetches the message of the day
      tags:
      - motd
  /observability/alerting/alerts:
    get:
      description: |-
        Get a list of active or silenced alerts from the AlertManager.
        **Access policy**: Authenticated user.
      operationId: GetAlerts
      parameters:
      - description: 'Status of alerts to retrieve. Possible values: ''active'' or
