##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/kubernetes/operation/GetKubernetesMetricsForAllNodes)Get a list of nodes with their live metrics
Get a list of metrics associated with all nodes of a cluster. **Access policy** : Authenticated user.
##### Authorizations:
(_ApiKeyAuth_ _jwt_)
##### path Parameters
idrequired |  integer Environment identifier
---|---
### Responses
**200**
Success
**401**
Unauthorized access - the user is not authenticated or does not have the necessary permissions. Ensure that you have provided a valid API key or JWT token, and that you have the required permissions.
**500**
Server error occurred while attempting to retrieve the list of nodes with their live metrics.
get/kubernetes/{id}/metrics/nodes
https://api-docs.portainer.io/api/kubernetes/{id}/metrics/nodes
###  Response samples
  * 200


Content type
application/json
Copy
Expand all  Collapse all
`{

  *  "apiVersion": "string",

  *  "items": [
    *  {
      *  "apiVersion": "string",

      *  "kind": "string",

      *  "metadata": {
        *  "annotations": {
          *  "property1": "string",

          *  "property2": "string"
  },

        *  "creationTimestamp": "string",

        *  "deletionGracePeriodSeconds": 0,

        *  "deletionTimestamp": "string",

        *  "finalizers": [
          * "string"
 ],

        *  "generateName": "string",

        *  "generation": 0,

        *  "labels": {
          *  "property1": "string",

          *  "property2": "string"
  },

        *  "managedFields": [
          *  {
            *  "apiVersion": "string",

            *  "fieldsType": "string",

            *  "fieldsV1": { },

            *  "manager": "string",

            *  "operation": "Apply",

            *  "subresource": "string",

            *  "time": "string"
  }
 ],

        *  "name": "string",

        *  "namespace": "string",

        *  "ownerReferences": [
          *  {
            *  "apiVersion": "string",

            *  "blockOwnerDeletion": true,

            *  "controller": true,

            *  "kind": "string",

            *  "name": "string",

            *  "uid": "string"
  }
 ],

        *  "resourceVersion": "string",

        *  "selfLink": "string",

        *  "uid": "string"
  },

      *  "timestamp": "string",

      *  "usage": {
        *  "property1": {
          *  "Format": "DecimalExponent"
 },

        *  "property2": {
          *  "Format": "DecimalExponent"
 }
  },

      *  "window": {
        *  "time.Duration": -9223372036854776000
 }
  }
 ],

  *  "kind": "string",

  *  "metadata": {
    *  "continue": "string",

    *  "remainingItemCount": 0,

    *  "resourceVersion": "string",

    *  "selfLink": "string"
  }

 }`
