##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/stacks/operation/EdgeStackWebhookInvoke)Webhook for triggering edge stack updates from git
**Access policy** : public
##### path Parameters
webhookIDrequired |  string Stack identifier
---|---
### Responses
**200**
Success
**400**
Invalid request
**409**
Conflict
**500**
Server error
post/edge_stacks/webhooks/{webhookID}
https://api-docs.portainer.io/api/edge_stacks/webhooks/{webhookID}
