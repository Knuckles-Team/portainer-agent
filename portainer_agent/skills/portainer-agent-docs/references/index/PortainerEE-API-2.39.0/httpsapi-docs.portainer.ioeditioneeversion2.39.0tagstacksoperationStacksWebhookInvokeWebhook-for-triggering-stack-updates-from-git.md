##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/stacks/operation/StacksWebhookInvoke)Webhook for triggering stack updates from git
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
Autoupdate for the stack isn't available
**500**
Server error
post/stacks/webhooks/{webhookID}
https://api-docs.portainer.io/api/stacks/webhooks/{webhookID}
