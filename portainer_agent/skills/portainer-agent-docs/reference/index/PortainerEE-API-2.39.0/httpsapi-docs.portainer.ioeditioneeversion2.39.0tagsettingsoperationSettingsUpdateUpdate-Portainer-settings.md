##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/settings/operation/SettingsUpdate)Update Portainer settings
Update Portainer settings. **Access policy** : administrator
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### Request Body schema: application/json
required
New settings
AuthenticationMethod |  integer Active authentication method for the Portainer instance. Valid values are: 1 for internal, 2 for LDAP, or 3 for oauth
---|---
AutoPatchSettings |  object Whether to enable automatic patches
BlackListedLabels |  Array of objects (portainer.Pair)  A list of label name & value that will be used to hide containers when querying containers
CustomLoginBanner |  string The content in plaintext used to display in the login page. Will hide when value is empty string
DisableKubeRolesSync |  boolean Whether to disable kube roles sync for all built-in roles
DisableKubeShell |  boolean Whether to disable kubeshell access for non-admin users
DisableKubeconfigDownload |  boolean Whether to disable kubeconfig download for non-admin users
Edge |  object
EdgeAgentCheckinInterval |  integer The default check in interval for edge agent (in seconds)
EdgePortainerURL |  string EdgePortainerURL is the URL that is exposed to edge agents
EnableEdgeComputeFeatures |  boolean Whether edge compute features are enabled
EnforceEdgeID |  boolean EnforceEdgeID makes Portainer store the Edge ID instead of accepting anyone
GlobalDeploymentOptions |  object Deployment options for encouraging deployment as code
HelmRepositoryURL |  string Helm repository URL
InternalAuthSettings |  object (portainer.InternalAuthSettings)
KubeconfigExpiry |  string Default:  "0" The expiry of a Kubeconfig
KubectlShellImage |  string Kubec tl Shell Image Name/Tag
LDAPSettings |  object (portaineree.LDAPSettings)
LogoURL |  string URL to a logo that will be displayed on the login page as well as on top of the sidebar. Will use default Portainer logo when value is empty string
OAuthSettings |  object (portaineree.OAuthSettings)
SnapshotInterval |  string The interval in which environment(endpoint) snapshots are created
TemplatesURL |  string URL to the templates that will be displayed in the UI when navigating to App Templates
TrustOnFirstConnect |  boolean TrustOnFirstConnect makes Portainer accepting edge agent connection by default
UserSessionTimeout |  string The duration of a user session
### Responses
**200**
Success
**400**
Invalid request
**409**
Edge Compute features cannot be disabled while they are in use
**500**
Server error
put/settings
https://api-docs.portainer.io/api/settings
###  Request samples
  * Payload


Content type
application/json
Copy
Expand all  Collapse all
`{

  *  "AuthenticationMethod": 1,

  *  "AutoPatchSettings": {
    *  "Enabled": false,

    *  "PatchCron": "0 0 * * *",

    *  "PortainerRepository": "portainer/portainer-ee",

    *  "RegistryID": 1,

    *  "UpdaterRepository": "portainer/portainer-updater"
  },

  *  "BlackListedLabels": [
    *  {
      *  "name": "name",

      *  "value": "value"
  }
 ],

  *  "CustomLoginBanner": "notice or agreement",

  *  "DisableKubeRolesSync": false,

  *  "DisableKubeShell": false,

  *  "DisableKubeconfigDownload": false,

  *  "Edge": {
    *  "AsyncMode": true,

    *  "CommandInterval": 5,

    *  "MTLS": {
      *  "CaCert": "string",

      *  "Cert": "string",

      *  "Key": "string",

      *  "UseSeparateCert": true
  },

    *  "PingInterval": 5,

    *  "SnapshotInterval": 5,

    *  "TunnelServerAddress": "string"
  },

  *  "EdgeAgentCheckinInterval": 5,

  *  "EdgePortainerURL": "string",

  *  "EnableEdgeComputeFeatures": true,

  *  "EnforceEdgeID": false,

  *  "GlobalDeploymentOptions": {
    *  "hideAddWithForm": false,

    *  "hideFileUpload": false,

    *  "hideStacksFunctionality": false,

    *  "hideWebEditor": false,

    *  "minApplicationNoteLength": 10,

    *  "perEnvOverride": false,

    *  "requireNoteOnApplications": false
  },

  *  "HelmRepositoryURL": "",

  *  "InternalAuthSettings": {
    *  "RequiredPasswordLength": 0
 },

  *  "KubeconfigExpiry": "24h",

  *  "KubectlShellImage": "portainer/kubectl-shell:latest",

  *  "LDAPSettings": {
    *  "AdminAutoPopulate": true,

    *  "AdminGroupSearchSettings": [
      *  {
        *  "GroupAttribute": "member",

        *  "GroupBaseDN": "dc=ldap,dc=domain,dc=tld",

        *  "GroupFilter": "(objectClass=account"
  }
 ],

    *  "AdminGroups": [
      *  "['manager'",

      * "'operator']"
  ],

    *  "AnonymousMode": true,

    *  "AutoCreateUsers": true,

    *  "GroupSearchSettings": [
      *  {
        *  "GroupAttribute": "member",

        *  "GroupBaseDN": "dc=ldap,dc=domain,dc=tld",

        *  "GroupFilter": "(objectClass=account"
  }
 ],

    *  "Kerberos": {
      *  "Configuration": "string",

      *  "Password": "string",

      *  "Realm": "string",

      *  "Service": "string",

      *  "Username": "string"
  },

    *  "Password": "readonly-password",

    *  "ReaderDN": "cn=readonly-account,dc=ldap,dc=domain,dc=tld",

    *  "SearchSettings": [
      *  {
        *  "BaseDN": "dc=ldap,dc=domain,dc=tld",

        *  "Filter": "(objectClass=account)",

        *  "UserNameAttribute": "uid"
  }
 ],

    *  "ServerType": 1,

    *  "StartTLS": true,

    *  "TLSConfig": {
      *  "TLS": true,

      *  "TLSCACert": "/data/tls/ca.pem",

      *  "TLSCert": "/data/tls/cert.pem",

      *  "TLSKey": "/data/tls/key.pem",

      *  "TLSSkipVerify": false
  },

    *  "URL": "string",

    *  "URLs": [
      * "string"
 ]
  },

  *  "LogoURL": "",

  *  "OAuthSettings": {
    *  "AccessTokenURI": "string",

    *  "AuthStyle": 0,

    *  "AuthorizationURI": "string",

    *  "ClientID": "string",

    *  "ClientSecret": "string",

    *  "DefaultTeamID": 0,

    *  "HideInternalAuth": true,

    *  "KubeSecretKey": [
      * 0
 ],

    *  "LogoutURI": "string",

    *  "MicrosoftTenantID": "string",

    *  "OAuthAutoCreateUsers": true,

    *  "OAuthAutoMapTeamMemberships": true,

    *  "RedirectURI": "string",

    *  "ResourceURI": "string",

    *  "SSO": true,

    *  "Scopes": "string",

    *  "TeamMemberships": {
      *  "AdminAutoPopulate": true,

      *  "AdminGroupClaimsRegexList": [
        * "string"
 ],

      *  "OAuthClaimMappings": [
        *  {
          *  "ClaimValRegex": "string",

          *  "Team": 0
  }
 ],

      *  "OAuthClaimName": "string"
  },

    *  "UserIdentifier": "string"
  },

  *  "SnapshotInterval": "5m",

  *  "TemplatesURL": "",

  *  "TrustOnFirstConnect": false,

  *  "UserSessionTimeout": "5m"

 }`
###  Response samples
  * 200


Content type
application/json
Copy
Expand all  Collapse all
`{

  *  "AdditionalFunctionality": {
    *  "Observability": true
 },

  *  "AgentSecret": "string",

  *  "AllowBindMountsForRegularUsers": true,

  *  "AllowContainerCapabilitiesForRegularUsers": true,

  *  "AllowDeviceMappingForRegularUsers": true,

  *  "AllowHostNamespaceForRegularUsers": true,

  *  "AllowPrivilegedModeForRegularUsers": true,

  *  "AllowStackManagementForRegularUsers": true,

  *  "AllowVolumeBrowserForRegularUsers": true,

  *  "AuthenticationMethod": 1,

  *  "AutoPatchSettings": {
    *  "Enabled": false,

    *  "PatchCron": "0 4 * * *",

    *  "PortainerRepository": "portainer/portainer-ee",

    *  "RegistryID": 0,

    *  "UpdaterRepository": "portainer/portainer-updater"
  },

  *  "BlackListedLabels": [
    *  {
      *  "name": "name",

      *  "value": "value"
  }
 ],

  *  "CloudApiKeys": {
    *  "CivoApiKey": "DgJ33kwIhnHumQFyc8ihGwWJql9cC8UJDiBhN8YImKqiX",

    *  "DigitalOceanToken": "dop_v1_n9rq7dkcbg3zb3bewtk9nnvmfkyfnr94d42n28lym22vhqu23rtkllsldygqm22v",

    *  "GKEApiKey": "an entire base64ed key file",

    *  "LinodeToken": "92gsh9r9u5helgs4eibcuvlo403vm45hrmc6mzbslotnrqmkwc1ovqgmolcyq0wc"
  },

  *  "CustomLoginBanner": "string",

  *  "DefaultRegistry": {
    *  "Hide": false
 },

  *  "DisableKubeRolesSync": false,

  *  "DisableKubeShell": false,

  *  "DisableKubeconfigDownload": false,

  *  "DisplayDonationHeader": true,

  *  "DisplayExternalContributors": true,

  *  "Edge": {
    *  "AsyncMode": false,

    *  "CommandInterval": 5,

    *  "MTLS": {
      *  "CaCertFile": "string",

      *  "CertFile": "string",

      *  "KeyFile": "string",

      *  "UseSeparateCert": true
  },

    *  "PingInterval": 5,

    *  "SnapshotInterval": 5,

    *  "TunnelServerAddress": "portainer.domain.tld"
  },

  *  "EdgeAgentCheckinInterval": 5,

  *  "EdgePortainerUrl": "string",

  *  "EnableEdgeComputeFeatures": true,

  *  "EnableHostManagementFeatures": true,

  *  "EnforceEdgeID": false,

  *  "ExperimentalFeatures": { },

  *  "FeatureFlagSettings": {
    *  "property1": true,

    *  "property2": true
  },

  *  "GlobalDeploymentOptions": {
    *  "hideAddWithForm": false,

    *  "hideFileUpload": false,

    *  "hideStacksFunctionality": false,

    *  "hideWebEditor": false,

    *  "minApplicationNoteLength": 10,

    *  "perEnvOverride": false,

    *  "requireNoteOnApplications": false
  },

  *  "HelmRepositoryURL": "",

  *  "InternalAuthSettings": {
    *  "RequiredPasswordLength": 0
 },

  *  "IsDockerDesktopExtension": true,

  *  "KubeconfigExpiry": "24h",

  *  "KubectlShellImage": "portainer/kubectl-shell",

  *  "LDAPSettings": {
    *  "AdminAutoPopulate": true,

    *  "AdminGroupSearchSettings": [
      *  {
        *  "GroupAttribute": "member",

        *  "GroupBaseDN": "dc=ldap,dc=domain,dc=tld",

        *  "GroupFilter": "(objectClass=account"
  }
 ],

    *  "AdminGroups": [
      *  "['manager'",

      * "'operator']"
  ],

    *  "AnonymousMode": true,

    *  "AutoCreateUsers": true,

    *  "GroupSearchSettings": [
      *  {
        *  "GroupAttribute": "member",

        *  "GroupBaseDN": "dc=ldap,dc=domain,dc=tld",

        *  "GroupFilter": "(objectClass=account"
  }
 ],

    *  "Kerberos": {
      *  "Configuration": "string",

      *  "Password": "string",

      *  "Realm": "string",

      *  "Service": "string",

      *  "Username": "string"
  },

    *  "Password": "readonly-password",

    *  "ReaderDN": "cn=readonly-account,dc=ldap,dc=domain,dc=tld",

    *  "SearchSettings": [
      *  {
        *  "BaseDN": "dc=ldap,dc=domain,dc=tld",

        *  "Filter": "(objectClass=account)",

        *  "UserNameAttribute": "uid"
  }
 ],

    *  "ServerType": 1,

    *  "StartTLS": true,

    *  "TLSConfig": {
      *  "TLS": true,

      *  "TLSCACert": "/data/tls/ca.pem",

      *  "TLSCert": "/data/tls/cert.pem",

      *  "TLSKey": "/data/tls/key.pem",

      *  "TLSSkipVerify": false
  },

    *  "URL": "string",

    *  "URLs": [
      * "string"
 ]
  },

  *  "LogoURL": "",

  *  "OAuthSettings": {
    *  "AccessTokenURI": "string",

    *  "AuthStyle": 0,

    *  "AuthorizationURI": "string",

    *  "ClientID": "string",

    *  "ClientSecret": "string",

    *  "DefaultTeamID": 0,

    *  "HideInternalAuth": true,

    *  "KubeSecretKey": [
      * 0
 ],

    *  "LogoutURI": "string",

    *  "MicrosoftTenantID": "string",

    *  "OAuthAutoCreateUsers": true,

    *  "OAuthAutoMapTeamMemberships": true,

    *  "RedirectURI": "string",

    *  "ResourceURI": "string",

    *  "SSO": true,

    *  "Scopes": "string",

    *  "TeamMemberships": {
      *  "AdminAutoPopulate": true,

      *  "AdminGroupClaimsRegexList": [
        * "string"
 ],

      *  "OAuthClaimMappings": [
        *  {
          *  "ClaimValRegex": "string",

          *  "Team": 0
  }
 ],

      *  "OAuthClaimName": "string"
  },

    *  "UserIdentifier": "string"
  },

  *  "SnapshotInterval": "5m",

  *  "TemplatesURL": "",

  *  "TrustOnFirstConnect": false,

  *  "UserSessionTimeout": "5m",

  *  "openAMTConfiguration": {
    *  "certFileContent": "string",

    *  "certFileName": "string",

    *  "certFilePassword": "string",

    *  "domainName": "string",

    *  "enabled": true,

    *  "mpsPassword": "string",

    *  "mpsServer": "string",

    *  "mpsToken": "string",

    *  "mpsUser": "string"
  }

 }`
