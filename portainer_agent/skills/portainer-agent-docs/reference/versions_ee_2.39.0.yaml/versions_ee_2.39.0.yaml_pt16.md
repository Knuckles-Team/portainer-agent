        Use this environment(endpoint) to authenticate against Portainer using a username and password.
      operationId: AuthenticateUser
      parameters:
      - description: Credentials used for authentication
        in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/auth.authenticatePayload'
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            $ref: '#/definitions/auth.authenticateResponse'
        "400":
          description: Invalid request
        "422":
          description: Invalid Credentials
        "500":
          description: Server error
      summary: Authenticate
      tags:
      - auth
  /auth/logout:
    post:
      description: '**Access policy**: public'
      operationId: Logout
      responses:
        "204":
          description: Success
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Logout
      tags:
      - auth
  /auth/oauth/validate:
    post:
      consumes:
      - application/json
      description: '**Access policy**: public'
      operationId: ValidateOAuth
      parameters:
      - description: OAuth Credentials used for authentication
        in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/auth.oauthPayload'
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            $ref: '#/definitions/auth.authenticateResponse'
        "400":
          description: Invalid request
        "422":
          description: Invalid Credentials
        "500":
          description: Server error
      summary: Authenticate with OAuth
      tags:
      - auth
  /auto_updates:
    get:
      description: '**Access policy**: administrator'
      operationId: AutoUpdateList
      produces:
      - application/json
      responses:
        "200":
          description: OK
          schema:
            $ref: '#/definitions/autoupdates.listResponse'
        "403":
          description: Forbidden
        "500":
          description: Internal Server Error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: List auto updates
      tags:
      - auto_updates
  /backup:
    post:
      consumes:
      - application/json
      description: |-
        Creates an archive with a system data snapshot that could be used to restore the system.
        **Access policy**: admin
      operationId: Backup
      parameters:
      - description: An object contains the password to encrypt the backup with
        in: body
        name: body
        schema:
          $ref: '#/definitions/backup.backupPayload'
      produces:
      - application/octet-stream
      responses:
        "200":
          description: Success
        "400":
          description: Invalid request
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Creates an archive with a system data snapshot that could be used to
        restore the system.
      tags:
      - backup
  /backup/s3/execute:
    post:
      consumes:
      - application/json
      description: |-
        Creates an archive with a system data snapshot and upload it to the target S3 bucket
        **Access policy**: administrator
      operationId: BackupToS3
      parameters:
      - description: S3 backup settings
        in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/backup.s3BackupPayload'
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
      summary: Execute backup to AWS S3 Bucket
      tags:
      - backup
  /backup/s3/restore:
    post:
      consumes:
      - application/json
      description: |-
        Triggers a system restore using details of s3 backup
        **Access policy**: public
      operationId: RestoreFromS3
      parameters:
      - description: S3 Location Payload
        in: body
        name: body
        schema:
          $ref: '#/definitions/backup.restoreS3Settings'
      responses:
        "200":
          description: Success
        "400":
          description: Invalid request
        "500":
          description: Server error
      summary: Triggers a system restore using details of s3 backup
      tags:
      - backup
  /backup/s3/settings:
    get:
      description: '**Access policy**: administrator'
      operationId: BackupSettingsFetch
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            $ref: '#/definitions/portaineree.S3BackupSettings'
        "401":
          description: Unauthorized
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Fetch s3 backup settings/configurations
      tags:
      - backup
    post:
      consumes:
      - application/json
      description: |-
        Updates stored s3 backup settings and updates running cron jobs as needed
        **Access policy**: administrator
      operationId: UpdateS3Settings
      parameters:
      - description: S3 backup settings
        in: body
        name: s3_backup_settings
        schema:
          $ref: '#/definitions/portaineree.S3BackupSettings'
      responses:
        "200":
          description: Success
        "400":
          description: Invalid request
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Updates stored s3 backup settings and updates running cron jobs as
        needed
      tags:
      - backup
  /backup/s3/status:
    get:
      description: '**Access policy**: public'
      operationId: BackupStatusFetch
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            $ref: '#/definitions/backup.backupStatus'
        "500":
          description: Server error
      summary: Fetch the status of the last scheduled backup run
      tags:
      - backup
  /cloud/{provider}/info:
    get:
      description: |-
        The information returned can be used to provision a KaaS cluster.
        **Access policy**: administrator
      operationId: providerInfo
      parameters:
      - description: Provider
        enum:
        - '"amazon"'
        - '"azure"'
        - '"civo"'
        - '"digitalocean"'
        - '"gke"'
        - '"linode"'
        in: path
        name: provider
        required: true
        type: string
      - description: If true, get the up-to-date information (instead of cached information).
        in: query
        name: force
        type: boolean
      produces:
      - application/json
      responses:
        "200":
          description: Success
        "400":
          description: Invalid request
        "500":
          description: Server error
        "503":
          description: Missing configuration
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Get information about the provisioning options for a cloud provider.
      tags:
      - kaas
  /cloud/{provider}/provision:
    post:
      consumes:
      - application/json
      description: |-
        Provision a new KaaS cluster and create an environment.
        This documentation is specifically for civo, digitial ocean and linode.

        For Azure, GKE and Amazon see:
        **/cloud/amazon/provision**
        **/cloud/azure/provision**
        **/cloud/gke/provision**

        **Access policy**: administrator
      operationId: provisionCluster
      parameters:
      - description: Provider
        enum:
        - '"civo"'
        - '"digitalocean"'
        - '"linode"'
        in: path
        name: provider
        required: true
        type: string
      - description: KaaS cluster provisioning details
        in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/providers.DefaultProvisionPayload'
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            $ref: '#/definitions/portaineree.Endpoint'
        "400":
          description: Invalid request
        "500":
          description: Server error
        "503":
          description: Missing configuration
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Provision a new CIVO, Linode or Digital Ocean cluster and create an
        environment
      tags:
      - kaas
  /cloud/amazon/provision:
    post:
      consumes:
      - application/json
      description: |-
        Provision a new KaaS cluster and create an environment.
        **Access policy**: administrator
      operationId: provisionClusterAmazon
      parameters:
      - description: KaaS cluster provisioning details
        in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/providers.AmazonProvisionPayload'
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            $ref: '#/definitions/portaineree.Endpoint'
        "400":
          description: Invalid request
        "500":
          description: Server error
        "503":
          description: Missing configuration
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Provision a new Amazon EKS and create an environment
      tags:
      - kaas
  /cloud/azure/provision:
    post:
      consumes:
      - application/json
      description: |-
        Provision a new KaaS cluster and create an environment.
        **Access policy**: administrator
      operationId: provisionClusterAzure
      parameters:
      - description: KaaS cluster provisioning details
        in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/providers.AzureProvisionPayload'
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            $ref: '#/definitions/portaineree.Endpoint'
        "400":
          description: Invalid request
        "500":
          description: Server error
        "503":
          description: Missing configuration
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Provision a new Microsoft Azure cluster and create an environment
      tags:
      - kaas
  /cloud/credentials:
    get:
      description: |-
        getAll cloud credential
        **Access policy**: authenticated
      operationId: getAll
      produces:
      - application/json
      responses:
        "200":
          description: OK
          schema:
            $ref: '#/definitions/models.CloudCredential'
        "400":
          description: Invalid request
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: getAll cloud credentials
      tags:
      - cloud_credentials
    post:
      consumes:
      - application/json
      - multipart/form-data
      description: |-
        Create a cloud credential
        **Access policy**: authenticated
      operationId: Create
      parameters:
      - description: cloud provider such as aws, aks, civo, digitalocean, etc.
        in: formData
        name: provider
        required: true
        type: string
      - description: name of the credentials such as rnd-test-credential
        in: formData
        name: name
        required: true
        type: string
      - description: credentials in json format
        in: formData
        name: credentials
        required: true
        type: string
      produces:
      - application/json
      responses:
        "200":
          description: OK
          schema:
            $ref: '#/definitions/models.CloudCredential'
        "400":
          description: Invalid request
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Create a cloud credential
      tags:
      - cloud_credentials
  /cloud/credentials/{id}:
    delete:
      description: |-
        Delete a cloud credential
        **Access policy**: authenticated
      operationId: cloudCredsDelete
      parameters:
      - description: ID of the cloud credential
        in: path
        name: id
        required: true
        type: string
      produces:
      - application/json
      responses:
        "200":
          description: OK
          schema:
            $ref: '#/definitions/models.CloudCredential'
        "400":
          description: Invalid request
        "403":
          description: 'Forbidden: the requested credential is associated with endpoint(s)'
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Delete a cloud credential
      tags:
      - cloud_credentials
    get:
      description: |-
        getByID gets a cloud credential by ID
        **Access policy**: authenticated
      operationId: cloudCredsGetByID
      parameters:
      - description: ID of the cloud credential
        in: path
        name: id
        required: true
        type: string
      produces:
      - application/json
      responses:
        "200":
          description: OK
          schema:
            $ref: '#/definitions/models.CloudCredential'
        "400":
          description: Invalid request
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: getByID gets a cloud credential by ID
      tags:
      - cloud_credentials
    put:
      consumes:
      - application/json
      - multipart/form-data
      description: |-
        Update a cloud credential
        **Access policy**: authenticated
      operationId: cloudCredsUpdate
      parameters:
      - description: ID of the cloud credential
        in: path
        name: id
        required: true
        type: string
      - description: cloud provider such as aws, aks, civo, digitalocean, etc.
        in: formData
        name: provider
        required: true
        type: string
      - description: name of the credentials such as rnd-test-credential
        in: formData
        name: name
        required: true
        type: string
      - description: credentials in json format
        in: formData
        name: credentials
        required: true
        type: string
      produces:
      - application/json
      responses:
        "200":
          description: OK
          schema:
            $ref: '#/definitions/models.CloudCredential'
        "400":
          description: Invalid request
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Update a cloud credential
      tags:
      - cloud_credentials
  /cloud/endpoints/{environmentId}/addons:
    get:
      description: |-
        The information returned can be used to query the MircoK8s cluster.
        **Access policy**: authenticated
      operationId: microk8sGetAddons
      parameters:
      - description: Environment(Endpoint) identifier
        in: path
        name: environmentId
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
          description: Permission denied
        "500":
          description: Server error
        "503":
          description: Missing configuration
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Get a list of addons which are installed in a MicroK8s cluster.
      tags:
      - kaas
    post:
      description: |-
        The information returned can be used to query the MircoK8s cluster.
        **Access policy**: authenticated
      operationId: microk8sUpdateAddons
      parameters:
      - description: Environment(Endpoint) identifier
        in: path
        name: environmentId
        required: true
        type: integer
      - description: The list of addons to install in the cluster.
        in: body
        name: addons
        required: true
        schema:
          $ref: '#/definitions/providers.Microk8sUpdateAddonsPayload'
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
        "503":
          description: Missing configuration
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Get a list of addons which are installed in a MicroK8s cluster.
      tags:
      - kaas
  /cloud/endpoints/{environmentId}/nodes/add:
    post:
      description: |-
        Add control plane and worker nodes to the cluster.
        **Access policy**: authenticated
      operationId: addNodes
      parameters:
      - description: Environment(Endpoint) identifier
        in: path
        name: environmentId
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
          description: Permission denied
        "500":
          description: Server error
        "503":
          description: Missing configuration
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Add nodes to the cluster (scale up).
      tags:
      - kaas
  /cloud/endpoints/{environmentId}/nodes/nodestatus:
    get:
      description: |-
        Get the MicroK8s status for a control plane node in a MicroK8s cluster.
        **Access policy**: authenticated
      operationId: microk8sGetNodeStatus
      parameters:
      - description: Environment(Endpoint) identifier
        in: path
        name: environmentId
        required: true
        type: integer
      - description: The external node ip of the control plane node.
        in: query
        name: nodeIP
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
        "503":
          description: Missing configuration
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Get the MicroK8s status for a control plane node.
      tags:
      - kaas
  /cloud/endpoints/{environmentId}/nodes/remove:
    post:
      description: |-
        Remove nodes from the cluster and uninstall MicroK8s from them.
        **Access policy**: authenticated
      operationId: removeNodes
      parameters:
      - description: Environment(Endpoint) identifier
        in: path
        name: environmentId
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
          description: Permission denied
        "500":
          description: Server error
        "503":
          description: Missing configuration
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Remove nodes from the cluster and uninstall MicroK8s from them.
      tags:
      - kaas
  /cloud/endpoints/{environmentId}/upgrade:
    post:
      description: |-
        Upgrade the cluster to the next stable kubernetes version.
        **Access policy**: authenticated
      operationId: upgrade
      parameters:
      - description: Environment(Endpoint) identifier
        in: path
        name: environmentId
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
          description: Permission denied
        "500":
          description: Server error
        "503":
          description: Missing configuration
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Upgrade the cluster to the next stable kubernetes version.
      tags:
      - kaas
  /cloud/endpoints/{environmentId}/version:
    get:
      description: |-
        Get the current cluster version.
        **Access policy**: authenticated
      operationId: kaasVersion
      parameters:
      - description: Environment(Endpoint) identifier
        in: path
        name: environmentId
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
          description: Permission denied
        "500":
          description: Server error
        "503":
          description: Missing configuration
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Get the current cluster version.
      tags:
      - kaas
  /cloud/gitcredentials:
    get:
      description: |-
        Get shared git credentials
        **Access policy**: Administrator only.
      operationId: SharedGitGetAll
      responses:
        "201":
          description: Success
        "401":
          description: Unauthorized
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
        jwt: []
      summary: Get Shared Git Credentials
      tags:
      - cloud_credentials
    post:
      description: |-
        Create a shared git credential
        **Access policy**: Administrator only.
      operationId: SharedGitCreate
      responses:
        "201":
          description: Success
        "400":
          description: Invalid request payload
        "401":
          description: Unauthorized
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
        jwt: []
      summary: Create Shared Git Credential
      tags:
      - cloud_credentials
  /cloud/gitcredentials/{id}:
    delete:
      description: |-
        Delete a shared git credential
        **Access policy**: Administrator only.
      operationId: SharedGitDelete
      responses:
        "201":
          description: Success
        "400":
          description: Invalid request payload
        "401":
          description: Unauthorized
        "403":
          description: Permission denied
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
        jwt: []
      summary: Delete Shared Git Credential
      tags:
      - cloud_credentials
    get:
      description: |-
        Get a shared git credential
        **Access policy**: Administrator only.
      operationId: SharedGitGet
      responses:
        "201":
          description: Success
        "400":
          description: Invalid request payload
        "401":
          description: Unauthorized
        "403":
          description: Permission denied
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
        jwt: []
      summary: Get Shared Git Credential
      tags:
      - cloud_credentials
    put:
      description: |-
        Update a shared git credential
        **Access policy**: Administrator only.
      operationId: SharedGitUpdate
      responses:
        "201":
          description: Success
        "400":
          description: Invalid request payload
        "401":
          description: Unauthorized
        "403":
          description: Permission denied
        "500":
          description: Server error
      security:
      - ApiKeyAuth: []
        jwt: []
      summary: Update a Shared Git Credential
      tags:
      - cloud_credentials
  /cloud/gke/provision:
    post:
      consumes:
      - application/json
      description: |-
        Provision a new KaaS cluster and create an environment.
        **Access policy**: administrator
      operationId: provisionClusterGKE
      parameters:
      - description: KaaS cluster provisioning details
        in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/providers.GKEProvisionPayload'
      produces:
      - application/json
      responses:
        "200":
          description: Success
          schema:
            $ref: '#/definitions/portaineree.Endpoint'
        "400":
          description: Invalid request
        "500":
          description: Server error
        "503":
          description: Missing configuration
      security:
      - ApiKeyAuth: []
      - jwt: []
      summary: Provision a new Google Kubernetes (GKE) cluster and create an environment
      tags:
      - kaas
  /cloud/testssh:
    post:
      consumes:
      - application/json
      description: |-
        Test SSH connection to nodes.
        **Access policy**: administrator
      operationId: testSSH
      parameters:
      - description: Node IPs and credential ID
        in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/providers.Microk8sTestSSHPayload'
      produces:
      - application/json
