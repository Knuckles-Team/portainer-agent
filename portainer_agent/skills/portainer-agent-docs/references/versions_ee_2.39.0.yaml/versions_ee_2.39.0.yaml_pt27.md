          ''silenced''.'
        in: query
        name: status
        required: true
        type: string
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            items:
              type: object
            type: array
        "401":
          description: Unauthorized access - the user is not authenticated or does
            not have the necessary permissions. Ensure that you have provided a valid
            API key or JWT token, and that you have the required permissions.
        "403":
          description: Permission denied - the user is authenticated but does not
            have the necessary permissions to access the requested resource or perform
            the specified operation. Check your user roles and permissions.
        "500":
          description: Server error occurred while attempting to retrieve active or
            silenced alerts.
      security:
      - ApiKeyAuth: []
        jwt: []
      summary: Get active or silenced alerts
      tags:
      - observability
  /observability/alerting/connectivity:
    get:
      description: |-
        Test connectivity to an AlertManager instance by retrieving its status.
        **Access policy**: Authenticated user.
      operationId: TestAlertManagerConnectivity
      parameters:
      - description: AlertManager URL
        in: query
        name: url
        required: true
        type: string
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            additionalProperties: true
            type: object
        "401":
          description: Unauthorized access - the user is not authenticated or does
            not have the necessary permissions. Ensure that you have provided a valid
            API key or JWT token, and that you have the required permissions.
        "403":
          description: Permission denied - the user is authenticated but does not
            have the necessary permissions to access the requested resource or perform
            the specified operation. Check your user roles and permissions.
        "500":
          description: Server error occurred while attempting to test AlertManager
            connectivity.
      security:
      - ApiKeyAuth: []
        jwt: []
      summary: Test AlertManager connectivity
      tags:
      - observability
  /observability/alerting/rules:
    get:
      description: |-
        Get a list of all alert rules from the AlertManager.
        **Access policy**: Authenticated user.
      operationId: GetAllAlertRules
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            items:
              type: object
            type: array
        "401":
          description: Unauthorized access - the user is not authenticated or does
            not have the necessary permissions. Ensure that you have provided a valid
            API key or JWT token, and that you have the required permissions.
        "403":
          description: Permission denied - the user is authenticated but does not
            have the necessary permissions to access the requested resource or perform
            the specified operation. Check your user roles and permissions.
        "500":
          description: Server error occurred while attempting to retrieve all alert
            rules.
      security:
      - ApiKeyAuth: []
        jwt: []
      summary: Get all alert rules
      tags:
      - observability
  /observability/alerting/rules/{id}:
    delete:
      description: |-
        Delete a specific alert rule by its identifier.
        **Access policy**: Authenticated user.
      operationId: DeleteAlertRule
      parameters:
      - description: Alert rule identifier
        in: path
        name: id
        required: true
        type: integer
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
          description: Unable to find an alert rule with the specified identifier.
        "500":
          description: Server error occurred while attempting to delete the alert
            rule.
      security:
      - ApiKeyAuth: []
        jwt: []
      summary: Delete an alert rule
      tags:
      - observability
    get:
      description: |-
        Get a specific alert rule by its identifier.
        **Access policy**: Authenticated user.
      operationId: GetAlertRule
      parameters:
      - description: Alert rule identifier
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
            type: object
        "401":
          description: Unauthorized access - the user is not authenticated or does
            not have the necessary permissions. Ensure that you have provided a valid
            API key or JWT token, and that you have the required permissions.
        "403":
          description: Permission denied - the user is authenticated but does not
            have the necessary permissions to access the requested resource or perform
            the specified operation. Check your user roles and permissions.
        "404":
          description: Unable to find an alert rule with the specified identifier.
        "500":
          description: Server error occurred while attempting to retrieve the alert
            rule.
      security:
      - ApiKeyAuth: []
        jwt: []
      summary: Get an alert rule by ID
      tags:
      - observability
    put:
      consumes:
      - application/json
      description: |-
        Update a specific alert rule by its identifier.
        **Access policy**: Authenticated user.
      operationId: UpdateAlertRule
      parameters:
      - description: Alert rule identifier
        in: path
        name: id
        required: true
        type: integer
      - description: Alert rule details
        in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/observability.alertRuleUpdatePayload'
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            type: object
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
          description: Unable to find an alert rule with the specified identifier.
        "500":
          description: Server error occurred while attempting to update the alert
            rule.
      security:
      - ApiKeyAuth: []
        jwt: []
      summary: Update an alert rule
      tags:
      - observability
  /observability/alerting/settings:
    get:
      description: |-
        Get a list of all alerting settings with their connection status.
        **Access policy**: Authenticated user.
      operationId: GetAllAlertingSettings
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            items:
              type: object
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
          description: Server error occurred while attempting to retrieve all alerting
            settings.
      security:
      - ApiKeyAuth: []
        jwt: []
      summary: Get all alerting settings
      tags:
      - observability
    put:
      consumes:
      - application/json
      description: |-
        Update alerting settings and manage internal AlertManager lifecycle.
        **Access policy**: Authenticated user.
      operationId: UpdateAlertingSettings
      parameters:
      - description: Alerting settings details
        in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/observability.alertingUpdatePayload'
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            type: object
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
          description: Server error occurred while attempting to update the alerting
            settings.
      security:
      - ApiKeyAuth: []
        jwt: []
      summary: Update alerting settings
      tags:
      - observability
  /observability/alerting/settings/{id}:
    get:
      description: |-
        Get specific alerting settings by its identifier, including connection status.
        **Access policy**: Authenticated user.
      operationId: GetAlertingSettings
      parameters:
      - description: Alerting settings identifier
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
            type: object
        "401":
          description: Unauthorized access - the user is not authenticated or does
            not have the necessary permissions. Ensure that you have provided a valid
            API key or JWT token, and that you have the required permissions.
        "403":
          description: Permission denied - the user is authenticated but does not
            have the necessary permissions to access the requested resource or perform
            the specified operation. Check your user roles and permissions.
        "404":
          description: Unable to find alerting settings with the specified identifier.
        "500":
          description: Server error occurred while attempting to retrieve the alerting
            settings.
      security:
      - ApiKeyAuth: []
        jwt: []
      summary: Get alerting settings by ID
      tags:
      - observability
  /observability/alerting/silence:
    post:
      consumes:
      - application/json
      description: |-
        Create a new silence for alerts in the specified AlertManager.
        **Access policy**: Authenticated user.
      operationId: CreateSilence
      parameters:
      - description: Silence details
        in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/observability.createSilencePayload'
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            additionalProperties: true
            type: object
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
          description: Server error occurred while attempting to create the alert
            silence.
      security:
      - ApiKeyAuth: []
        jwt: []
      summary: Create an alert silence
      tags:
      - observability
  /observability/alerting/silence/{id}:
    delete:
      description: |-
        Delete a specific alert silence by its identifier from the specified AlertManager.
        **Access policy**: Authenticated user.
      operationId: DeleteSilence
      parameters:
      - description: Silence identifier
        in: path
        name: id
        required: true
        type: string
      - description: AlertManager URL
        in: query
        name: alertManagerURL
        required: true
        type: string
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            additionalProperties: true
            type: object
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
          description: Unable to find an alert silence with the specified identifier.
        "500":
          description: Server error occurred while attempting to delete the alert
            silence.
      security:
      - ApiKeyAuth: []
        jwt: []
      summary: Delete an alert silence
      tags:
      - observability
  /open_amt:
    post:
      consumes:
      - application/json
      deprecated: true
      description: |-
        Enable Portainer's OpenAMT capabilities
        **Access policy**: administrator
      operationId: OpenAMTConfigure
      parameters:
      - description: OpenAMT Settings
        in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/openamt.openAMTConfigurePayload'
      produces:
      - application/json
      responses:
        "204":
          description: Success
        "400":
          description: Invalid request
        "403":
          description: Permission denied to access settings
        "500":
          description: Server error
      security:
      - jwt: []
      summary: Enable Portainer's OpenAMT capabilities
      tags:
      - intel
  /open_amt/{id}/activate:
    post:
      deprecated: true
      description: |-
        Activate OpenAMT device and associate to agent endpoint
        **Access policy**: administrator
      operationId: openAMTActivate
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
        "400":
          description: Invalid request
        "403":
          description: Permission denied to access settings
        "500":
          description: Server error
      security:
      - jwt: []
      summary: Activate OpenAMT device and associate to agent endpoint
      tags:
      - intel
  /open_amt/{id}/devices:
    get:
      deprecated: true
      description: |-
        Fetch OpenAMT managed devices information for endpoint
        **Access policy**: administrator
      operationId: OpenAMTDevices
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
        "400":
          description: Invalid request
        "403":
          description: Permission denied to access settings
        "500":
          description: Server error
      security:
      - jwt: []
      summary: Fetch OpenAMT managed devices information for endpoint
      tags:
      - intel
  /open_amt/{id}/devices/{deviceId}/action:
    post:
      consumes:
      - application/json
      deprecated: true
      description: |-
        Execute out of band action on an AMT managed device
        **Access policy**: administrator
      operationId: DeviceAction
      parameters:
      - description: Environment identifier
        in: path
        name: id
        required: true
        type: integer
      - description: Device identifier
        in: path
        name: deviceId
        required: true
        type: integer
      - description: Device Action
        in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/openamt.deviceActionPayload'
      produces:
      - application/json
      responses:
        "204":
          description: Success
        "400":
          description: Invalid request
        "403":
          description: Permission denied to access settings
        "500":
          description: Server error
      security:
      - jwt: []
      summary: Execute out of band action on an AMT managed device
      tags:
      - intel
  /open_amt/{id}/devices_features/{deviceId}:
    post:
      consumes:
      - application/json
      deprecated: true
      description: |-
        Enable features on an AMT managed device
        **Access policy**: administrator
      operationId: DeviceFeatures
      parameters:
      - description: Environment identifier
        in: path
        name: id
        required: true
        type: integer
      - description: Device identifier
        in: path
        name: deviceId
        required: true
        type: integer
      - description: Device Features
        in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/openamt.deviceFeaturesPayload'
      produces:
      - application/json
      responses:
        "204":
          description: Success
        "400":
          description: Invalid request
        "403":
          description: Permission denied to access settings
        "500":
          description: Server error
      security:
      - jwt: []
      summary: Enable features on an AMT managed device
      tags:
      - intel
  /open_amt/{id}/info:
    get:
      deprecated: true
      description: |-
        Request OpenAMT info from a node
        **Access policy**: administrator
      operationId: OpenAMTHostInfo
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
        "400":
          description: Invalid request
        "403":
          description: Permission denied to access settings
        "500":
          description: Server error
      security:
      - jwt: []
      summary: Request OpenAMT info from a node
      tags:
      - intel
  /policies:
    get:
      description: |-
        List all policies in the bucket.
        **Access policy**: administrator
      operationId: PolicyList
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            $ref: '#/definitions/policies.policyListResponse'
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: List policies
      tags:
      - policies
    post:
      consumes:
      - application/json
      description: |-
        Create a new policy.
        **Access policy**: administrator
      operationId: PolicyCreate
      parameters:
      - description: Policy details
        in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/policies.policyCreatePayload'
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            $ref: '#/definitions/policies.Policy'
        "400":
          description: Invalid request payload
        "409":
          description: This name is already associated to a policy
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Create a new policy
      tags:
      - policies
  /policies/{id}:
    delete:
      description: |-
        Delete a policy.
        **Access policy**: administrator
      operationId: PolicyDelete
      parameters:
      - description: Policy identifier
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
          description: Policy not found
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Delete a policy
      tags:
      - policies
    get:
      description: |-
        Retrieve details about a policy.
        **Access policy**: authenticated
      operationId: PolicyInspect
      parameters:
      - description: Policy identifier
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
            $ref: '#/definitions/policies.Policy'
        "400":
          description: Invalid request
        "404":
          description: Policy not found
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Inspect a policy
      tags:
      - policies
    put:
      consumes:
      - application/json
      description: |-
        Update an existing policy.
        **Access policy**: administrator
      operationId: PolicyUpdate
      parameters:
      - description: Policy identifier
        in: path
        name: id
        required: true
        type: integer
      - description: Policy details
        in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/policies.policyUpdatePayload'
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            $ref: '#/definitions/policies.Policy'
        "400":
          description: Invalid request
        "404":
          description: Policy not found
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Update a policy
      tags:
      - policies
  /policies/conflicts:
    post:
      consumes:
      - application/json
      description: |-
        Returns detailed information about what will be affected when creating or updating a policy with specific environment groups.
        **Access policy**: administrator
      operationId: PolicyConflicts
      parameters:
      - description: Conflict check details
        in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/policies.policyConflictsPayload'
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            $ref: '#/definitions/policies.policyConflictsResponse'
        "400":
          description: Invalid request payload
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Get policy conflicts preview
      tags:
      - policies
  /policies/metadata:
    get:
      description: |-
        Retrieve policy metadata including minimum agent versions for each policy type.
