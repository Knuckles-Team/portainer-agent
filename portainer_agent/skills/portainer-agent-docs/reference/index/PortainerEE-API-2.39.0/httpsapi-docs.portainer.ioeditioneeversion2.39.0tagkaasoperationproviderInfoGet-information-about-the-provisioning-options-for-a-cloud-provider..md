##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/kaas/operation/providerInfo)Get information about the provisioning options for a cloud provider.
The information returned can be used to provision a KaaS cluster. **Access policy** : administrator
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### path Parameters
providerrequired |  string Enum: "\"amazon\"" "\"azure\"" "\"civo\"" "\"digitalocean\"" "\"gke\"" "\"linode\"" Provider
---|---
##### query Parameters
force |  boolean If true, get the up-to-date information (instead of cached information).
---|---
### Responses
**200**
Success
**400**
Invalid request
**500**
Server error
**503**
Missing configuration
get/cloud/{provider}/info
https://api-docs.portainer.io/api/cloud/{provider}/info
