[ ![Portainer Logo](https://api-docs.portainer.io/assets/images/portainer-logo.png) ](https://www.portainer.io "Portainer")
Portainer API Documentation
Portainer Edition:  BE CE
API Version:  2.39.0 2.38.1 2.38.0 2.37.0 2.36.0 2.35.0 2.34.0 2.33.7 2.33.6 2.33.5 2.32.0 2.31.3 2.30.1 2.29.2 2.28.1 2.27.9
  * auth
    * postAuthenticate
    * postLogout
    * postAuthenticate with OAuth
  * backup
    * postCreates an archive with a system data snapshot that could be used to restore the system.
    * postExecute backup to AWS S3 Bucket
    * postTriggers a system restore using details of s3 backup
    * getFetch s3 backup settings/configurations
    * postUpdates stored s3 backup settings and updates running cron jobs as needed
    * getFetch the status of the last scheduled backup run
    * postTriggers a system restore using provided backup file
  * custom_templates
    * getList available custom templates
    * postCreate a custom template
    * delRemove a template
    * getInspect a custom template
    * putUpdate a template
    * getGet Template stack file content.
    * putFetch the latest config file content based on custom template's git repository configuration
    * postCreate a custom template
    * postCreate a custom template
    * postCreate a custom template
  * docker
    * getFetch container gpus data
    * getFetch image status for container
    * postClear container image status cache
    * getGet counters for the dashboard
    * getFetch images
    * getFetch image status for service
    * postClear service image status cache
    * getFetch latest snapshot of environment
    * getFetch containers list from a snapshot
    * getFetch container from a snapshot
    * postClear stack image status cache
  * edge
    * postUpdate the logs collected from an Edge Job
    * getInspect an Edge Stack for an Environment(Endpoint)
    * postGenerate an EdgeKey
  * edge_groups
    * getlist EdgeGroups
    * postCreate an EdgeGroup
    * delDeletes an EdgeGroup
    * getInspects an EdgeGroup
    * putUpdates an EdgeGroup
  * edge_jobs
    * getFetch EdgeJobs list
    * delDelete an EdgeJob
    * getInspect an EdgeJob
    * putUpdate an EdgeJob
    * getFetch a file of an EdgeJob
    * getFetch the list of tasks on an EdgeJob
    * delClear the log for a specifc task on an EdgeJob
    * getFetch the log for a specifc task on an EdgeJob
    * postCollect the log for a specifc task on an EdgeJob
    * postCreate an EdgeJob from a file
    * postCreate an EdgeJob from a text
  * edge_stacks
    * getFetches the list of EdgeStacks
    * delDelete an EdgeStack
    * getInspect an EdgeStack
    * putUpdate an EdgeStack
    * getFetches the stack file for an EdgeStack
    * putUpdate git configuration and pulls the repository
    * delDeletes the available logs for a given edge stack and endpoint
    * getGets the status of the log collection for a given edgestack and environment
    * putSchedule the collection of logs for a given endpoint and edge stack
    * getDownloads the available logs for a given edge stack and endpoint
    * getInspect an EdgeStack's parallel update status
    * putUpdate an EdgeStack status
    * postCreate an EdgeStack from file
    * postCreate an EdgeStack from a git repository
    * postCreate an EdgeStack from a text
    * postParse registries from a stack file
    * getInspect an Edge Stack for an Environment(Endpoint)
  * edge_templates
  * endpoint_groups
    * getList Environment(Endpoint) groups
    * postCreate an Environment(Endpoint) Group
    * delRemove an environment(endpoint) group
    * getInspect an Environment(Endpoint) group
    * putUpdate an environment(endpoint) group
    * delRemoves environment(endpoint) from an environment(endpoint) group
    * putAdd an environment(endpoint) to an environment(endpoint) group
  * endpoints
    * getFetch latest snapshot of environment
    * getFetch containers list from a snapshot
    * getFetch container from a snapshot
    * delRemove multiple environments
    * getList environments(endpoints)
    * postCreate a new environment(endpoint)
    * delRemove an environment
    * getInspect an environment(endpoint)
    * putUpdate an environment(endpoint)
    * putDe-association an edge environment(endpoint)
    * postUpload a file under a specific path on the file system of an environment (endpoint)
    * getfetch docker pull limits
    * getGet environment(endpoint) charts to install
    * putUpdate environment(endpoint) policy chart installation statuses
    * postUpdate the logs collected from an Edge Job
    * getInspect an Edge Stack for an Environment(Endpoint)
    * getGet environment(endpoint) status
    * putforce update a docker service
    * getGet an environment(endpoint) mTLS certificate
    * getGet an agent(endpoint) mTLS certificate
    * putUpdate namespace access for a given namespace
    * getList Registries on environment
    * putupdate registry access for environment
    * putUpdate settings for an environment(endpoint)
    * postSnapshots an environment(endpoint)
    * getList agent versions
    * postRemove multiple environments
    * postGet environment(endpoint) status
    * postGenerate an EdgeKey
    * postAssociate one or more Edge environments in the waiting room to environments
    * postCreate or retrieve the endpoint for an EdgeID
    * putUpdate relations for a list of environments
    * postSnapshot all environment(endpoint)
  * gitops
    * postpreview the content of target file in the git repository
    * postSearch the file path from a git repository files with specified extensions
    * postPreview merged Helm values files from git repository
    * postList the refs of a git repository
  * helm
    * getList Helm Releases
    * postInstall Helm Chart
    * getGet a helm release
    * delDelete Helm Release
    * getGet a historical list of releases
    * postRollback a helm release
    * postHelm Git Dry Run
    * getSearch Helm Charts
    * getShow Helm Chart Information
    * getList a users helm repositories
    * postCreate a user helm repository
    * delDelete a users helm repository
  * intel
    * postEnable Portainer's OpenAMT capabilities
    * postActivate OpenAMT device and associate to agent endpoint
    * getFetch OpenAMT managed devices information for endpoint
    * postExecute out of band action on an AMT managed device
    * postEnable features on an AMT managed device
    * getRequest OpenAMT info from a node
  * kaas
    * getGet information about the provisioning options for a cloud provider.
    * postProvision a new CIVO, Linode or Digital Ocean cluster and create an environment
    * postProvision a new Amazon EKS and create an environment
    * postProvision a new Microsoft Azure cluster and create an environment
    * getGet a list of addons which are installed in a MicroK8s cluster.
    * postGet a list of addons which are installed in a MicroK8s cluster.
    * postAdd nodes to the cluster (scale up).
    * getGet the MicroK8s status for a control plane node.
    * postRemove nodes from the cluster and uninstall MicroK8s from them.
    * postUpgrade the cluster to the next stable kubernetes version.
    * getGet the current cluster version.
    * postProvision a new Google Kubernetes (GKE) cluster and create an environment
    * postTest SSH connection to nodes
  * kubernetes
    * getGet Pod Security Rule within k8s cluster, if not found, the frontend will create a default
    * putUpdate Pod Security Rule within k8s cluster
    * getGet a list of applications across all namespaces in the cluster. If the nodeName is provided, it will return the applications running on that node.
    * getGet Applications count
    * postDelete cluster role bindings
    * postDelete cluster roles
    * getGet a list of kubernetes cluster role bindings
    * getGet a list of kubernetes cluster roles
    * getGet a list of ConfigMaps
    * getGet ConfigMaps count
    * getGet a list of kubernetes Cron Jobs
    * postDelete Cron Jobs
    * getGet a list of kubernetes Custom Resource Definitions
    * delDelete a kubernetes Custom Resource Definition
    * getGet a kubernetes Custom Resource Definition
    * getGet a list of kubernetes Custom Resources
    * delDelete a cluster-scoped kubernetes Custom Resource
    * getGet a cluster-scoped kubernetes Custom Resource
    * delDelete a namespaced kubernetes Custom Resource
    * getGet a list of kubernetes Custom Resources
    * getGet the dashboard summary data
    * getGet a description of a kubernetes resource
    * getGets kubernetes events
    * getGet a list of ingress controllers
    * putUpdate (block/unblock) ingress controllers
    * getGet kubernetes ingresses at the cluster level
    * getGet Ingresses count
    * postDelete one or more Ingresses
    * getGet a list of kubernetes Jobs
    * postDelete Jobs
    * getGet max CPU and memory limits of all nodes within k8s cluster
    * getGet the total CPU (cores) and memory requests (MB) and limits of all applications across all namespaces
    * getGet a list of nodes with their live metrics
    * getGet live metrics for a node
    * getGet a list of pods with their live metrics
    * getGet live metrics for a pod
    * delDelete a kubernetes namespace
    * getGet a list of namespaces
    * postCreate a namespace
    * putUpdate a namespace
    * getGet namespace details
    * putUpdate a namespace
    * postRestart a Kubernetes application
    * getGet an application by name in a specific namespace
    * getGet a ConfigMap
    * getGets kubernetes events for namespace
    * getGet a list ingress controllers by namespace
    * putUpdate (block/unblock) ingress controllers by namespace
    * getGet a list of Ingresses
    * postCreate an Ingress
    * putUpdate an Ingress
    * getGet an Ingress by name
    * getGet a Secret
    * getGet a list of services for a given namespace
    * postCreate a service
    * putUpdate a service
    * putToggle the system state for a namespace
    * getGet Kubernetes volumes within a namespace in the given Portainer environment
    * getGet the total number of kubernetes namespaces within the given Portainer environment.
    * postDrain a Kubernetes node
    * getGet CPU and memory limits of all nodes within k8s cluster.
    * getCheck if RBAC is enabled
    * postDelete role bindings
    * getGet a list of kubernetes role bindings
    * getGet a list of kubernetes roles
    * postDelete roles
    * getGet a list of Secrets
    * getGet Secrets count
    * postDelete service accounts
    * getGet a list of kubernetes service accounts
    * getGet a list of services
    * getGet services count
    * postDelete services
    * getGet Kubernetes volumes within the given Portainer environment
    * getGet a Kubernetes volume within the given Portainer environment
    * getGet the total number of kubernetes volumes within the given Portainer environment.
  * ldap
    * postFetch LDAP admin groups
    * postTest LDAP connectivity
    * postSearch LDAP Groups
    * postTest Login to ldap server
    * postSearch LDAP Users
  * metrics
  * motd
    * getfetches the message of the day
  * registries
    * getList Registries
    * postCreate a new registry
    * delRemove a registry
    * getInspect a registry
    * putUpdate a registry
    * postConfigures a registry
    * delDelete ECR repository
    * delDelete tags
    * delDelete repository tags
    * postTest registry connection
  * resource_controls
    * postCreate a new resource control
    * delRemove a resource control
    * putUpdate a resource control
  * roles
    * getList roles
  * settings
    * getRetrieve Portainer settings
    * putUpdate Portainer settings
    * getRetrieve Portainer additional functionality settings
    * putUpdate Portainer additional functionality settings
    * putUpdate Portainer default registry settings
    * getRetrieve Portainer Edge MTLS CA Certificates
    * getRetrieve Portainer Edge MTLS Certificates
    * getRetrieve Portainer experimental settings
    * putUpdate Portainer experimental settings
    * getRetrieve Portainer public settings
  * stacks
    * postWebhook for triggering edge stack updates from git
    * getList stacks
    * delRemove a stack
    * getInspect a stack
    * putUpdate a stack
    * putAssociate an orphaned stack to a new environment(endpoint)
    * getRetrieve the content of the Stack file for the specified stack
    * postUpdate a stack's Git configs
    * putRedeploy a stack
    * getFetch image status for stack
    * postMigrate a stack to another environment(endpoint)
    * postStarts a stopped Stack
    * postStops a stopped Stack
    * postDeploy a new kubernetes stack from a git repository
    * postDeploy a new kubernetes stack from a file
    * postDeploy a new kubernetes stack from a url
    * postDeploy a new compose stack from a file
    * postDeploy a new compose stack from repository
    * postDeploy a new compose stack from a text
    * postDeploy a new swarm stack from a file
    * postDeploy a new swarm stack from a git repository
    * postDeploy a new swarm stack from a text
    * delRemove Kubernetes stacks by name
    * postWebhook for triggering stack updates from git
  * status
    * getCheck Portainer status
  * system
    * getRetrieve system info
    * getRetrieve the count of nodes
    * getCheck Portainer status
    * postUpdate Portainer to latest version
    * getCheck for portainer updates
  * tags
    * getList tags
    * postCreate a new tag
    * delRemove a tag
  * team_memberships
    * getList team memberships
    * postCreate a new team membership
    * delRemove a team membership
    * putUpdate a team membership
    * getList team memberships
  * teams
    * getList teams
    * postCreate a new team
    * delRemove a team
    * getInspect a team
    * putUpdate a team
  * templates
    * getList available templates
    * postGet a template's file
  * upload
    * postUpload TLS files
  * users
    * getList users
    * postCreate a new user
    * delRemove a user
    * getInspect a user
    * putUpdate a user
    * getGet all saved git credentials for a user
    * postStore a Git Credential for a user
    * delRemove a git-credential associated to a user
    * getGet the specific saved git credential for a user
    * putUpdate a git-credential associated to a user
    * getInspect a user memberships
    * getRetrieves all k8s namespaces for an user
    * putUpdate password for a user
    * getGet all API keys for a user
    * postGenerate an API key for a user
    * delRemove an api-key associated to a user
    * getCheck administrator account existence
    * postInitialize administrator account
    * getInspect the current user
    * getInspect environment authorizations for the current user
  * webhooks
    * getList webhooks
    * postCreate a webhook
    * delDelete a webhook
    * postExecute a webhook
    * putUpdate a webhook
    * putReassign a webhook to another resource
  * websocket
    * getAttach a websocket
    * getExecute a websocket
    * getExecute a websocket on kubectl shell pod
    * getConnect to a remote SSH Shell via a websocket
    * getExecute a websocket on pod
  * auto_updates
    * getList auto updates
  * cloud_credentials
    * getgetAll cloud credentials
    * postCreate a cloud credential
    * delDelete a cloud credential
    * getgetByID gets a cloud credential by ID
    * putUpdate a cloud credential
    * getGet Shared Git Credentials
    * postCreate Shared Git Credential
    * delDelete Shared Git Credential
    * getGet Shared Git Credential
    * putUpdate a Shared Git Credential
    * postGenerate ssh keypair
  * edge_configs
    * getList available Edge Configurations
    * postCreate an Edge Configuration
    * delDelete an Edge configuration
    * getInspect an Edge configuration
    * putUpdate an Edge Configuration
    * putUpdate the state of an Edge configuration
    * getGet the files for an Edge configuration
  * edge_update_schedules
    * getFetches the list of Edge Update Schedules
    * postCreates a scheduled remote update procedure for Edge agents
    * delDeletes an Edge Update Schedule
    * getReturns the Edge Update Schedule with the given ID
    * postUpdate a scheduled remote update procedure for Edge agents
    * postFetches the list of Active Edge Update Schedules
    * getFetches the supported versions of the agent to update/rollback
    * getReturns informations the help create edge update schedules
    * getFetches the previous versions of updated agents
  * license
    * getfetches the list of licenses on Portainer
    * postattaches a list of licenses to Portainer
    * getsummarizes licenses on Portainer
    * postdelete license from portainer instance
  * observability
    * getGet active or silenced alerts
    * getTest AlertManager connectivity
    * getGet all alert rules
    * delDelete an alert rule
    * getGet an alert rule by ID
    * putUpdate an alert rule
    * getGet all alerting settings
    * putUpdate alerting settings
    * getGet alerting settings by ID
    * postCreate an alert silence
    * delDelete an alert silence
  * policies
    * getList policies
    * postCreate a new policy
    * delDelete a policy
    * getInspect a policy
    * putUpdate a policy
    * postGet policy conflicts preview
    * getGet policy metadata
    * getList policy templates
    * getInspect a policy template
  * ssl
    * getInspect the ssl settings
    * putUpdate the ssl settings
  * support
    * getGet status of the global debug log
    * putEnables or disables the global debug log
    * postDownload a bundle of files to help support diagnose issues
  * useractivity
    * getList auth activity logs
    * getDownload auth logs as CSV
    * getList user activity logs
    * getDownload user activity logs as CSV
