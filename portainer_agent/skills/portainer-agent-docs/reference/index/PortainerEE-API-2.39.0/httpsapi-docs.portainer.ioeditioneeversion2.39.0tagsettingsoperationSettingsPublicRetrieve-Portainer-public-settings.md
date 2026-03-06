##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/settings/operation/SettingsPublic)Retrieve Portainer public settings
Retrieve public settings. Returns a small set of settings that are not reserved to administrators only. **Access policy** : public
### Responses
**200**
Success
**500**
Server error
get/settings/public
https://api-docs.portainer.io/api/settings/public
###  Response samples
  * 200


Content type
application/json
Copy
Expand all  Collapse all
`{

  *  "AuthenticationMethod": 1,

  *  "AutoPatchSettings": {
    *  "Enabled": true,

    *  "PatchCron": "0 4 * * *"
  },

  *  "CustomLoginBanner": "notice or agreement",

  *  "DefaultRegistry": {
    *  "Hide": false
 },

  *  "DisableKubeShell": false,

  *  "DisableKubeconfigDownload": false,

  *  "Edge": {
    *  "CheckinInterval": 60,

    *  "CommandInterval": 60,

    *  "MTLS": {
      *  "CaCertFile": "string",

      *  "CertFile": "string",

      *  "KeyFile": "string",

      *  "UseSeparateCert": true
  },

    *  "PingInterval": 60,

    *  "SnapshotInterval": 60
  },

  *  "EnableEdgeComputeFeatures": true,

  *  "FIPSMode": true,

  *  "Features": {
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

  *  "IsAMTEnabled": true,

  *  "IsObservabilityEnabled": true,

  *  "KubeconfigExpiry": "24h",

  *  "LogoURL": "",

  *  "OAuthHideInternalAuth": true,

  *  "OAuthLoginURI": "",

  *  "OAuthLogoutURI": "",

  *  "RequiredPasswordLength": 1,

  *  "TeamSync": true,

  *  "Whitelabel": "My Company"

 }`
