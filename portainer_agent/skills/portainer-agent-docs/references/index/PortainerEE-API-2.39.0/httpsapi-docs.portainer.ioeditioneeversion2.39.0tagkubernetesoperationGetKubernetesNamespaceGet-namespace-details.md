##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/kubernetes/operation/GetKubernetesNamespace)Get namespace details
Get namespace details for the provided namespace within the given environment. **Access policy** : Authenticated user.
##### Authorizations:
(_ApiKeyAuth_ _jwt_)
##### path Parameters
idrequired |  integer Environment identifier
---|---
namespacerequired |  string The namespace name to get details for
##### query Parameters
withResourceQuotarequired |  boolean When set to true, include the resource quota information as part of the Namespace information. Default is false
---|---
### Responses
**200**
Success
**400**
Invalid request payload, such as missing required fields or fields not meeting validation criteria.
**401**
Unauthorized access - the user is not authenticated or does not have the necessary permissions. Ensure that you have provided a valid API key or JWT token, and that you have the required permissions.
**403**
Permission denied - the user is authenticated but does not have the necessary permissions to access the requested resource or perform the specified operation. Check your user roles and permissions.
**404**
Unable to find an environment with the specified identifier or unable to find a specific namespace.
**500**
Server error occurred while attempting to retrieve specified namespace information.
get/kubernetes/{id}/namespaces/{namespace}
https://api-docs.portainer.io/api/kubernetes/{id}/namespaces/{namespace}
###  Response samples
  * 200


Content type
application/json
Copy
Expand all  Collapse all
`{

  *  "Annotations": {
    *  "property1": "string",

    *  "property2": "string"
  },

  *  "CreationDate": "string",

  *  "Id": "string",

  *  "IsDefault": true,

  *  "IsSystem": true,

  *  "Name": "string",

  *  "NamespaceOwner": "string",

  *  "ResourceQuota": {
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

    *  "spec": {
      *  "hard": {
        *  "property1": {
          *  "Format": "DecimalExponent"
 },

        *  "property2": {
          *  "Format": "DecimalExponent"
 }
  },

      *  "scopeSelector": {
        *  "matchExpressions": [
          *  {
            *  "operator": "In",

            *  "scopeName": "Terminating",

            *  "values": [
              * "string"
 ]
  }
 ]
 },

      *  "scopes": [
        * "Terminating"
 ]
  },

    *  "status": {
      *  "hard": {
        *  "property1": {
          *  "Format": "DecimalExponent"
 },

        *  "property2": {
          *  "Format": "DecimalExponent"
 }
  },

      *  "used": {
        *  "property1": {
          *  "Format": "DecimalExponent"
 },

        *  "property2": {
          *  "Format": "DecimalExponent"
 }
  }
  }
  },

  *  "Status": {
    *  "conditions": [
      *  {
        *  "lastTransitionTime": "string",

        *  "message": "string",

        *  "reason": "string",

        *  "status": "True",

        *  "type": "NamespaceDeletionDiscoveryFailure"
  }
 ],

    *  "phase": "Active"
  },

  *  "UnhealthyEventCount": 0

 }`
