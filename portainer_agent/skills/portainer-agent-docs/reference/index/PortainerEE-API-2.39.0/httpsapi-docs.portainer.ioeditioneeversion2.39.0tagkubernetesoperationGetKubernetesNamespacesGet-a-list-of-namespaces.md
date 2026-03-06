##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/kubernetes/operation/GetKubernetesNamespaces)Get a list of namespaces
Get a list of all namespaces within the given environment based on the user role and permissions. If the user is an admin, they can access all namespaces. If the user is not an admin, they can only access namespaces that they have access to. **Access policy** : Authenticated user.
##### Authorizations:
(_ApiKeyAuth_ _jwt_)
##### path Parameters
idrequired |  integer Environment identifier
---|---
##### query Parameters
withResourceQuotarequired |  boolean When set to true, include the resource quota information as part of the Namespace information. Default is false
---|---
withUnhealthyEventsrequired |  boolean When set to true, include the unhealthy events information as part of the Namespace information. Default is false
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
Unable to find an environment with the specified identifier.
**500**
Server error occurred while attempting to retrieve the list of namespaces.
get/kubernetes/{id}/namespaces
https://api-docs.portainer.io/api/kubernetes/{id}/namespaces
###  Response samples
  * 200


Content type
application/json
Copy
Expand all  Collapse all
`[
  *  {
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
  }

 ]`
