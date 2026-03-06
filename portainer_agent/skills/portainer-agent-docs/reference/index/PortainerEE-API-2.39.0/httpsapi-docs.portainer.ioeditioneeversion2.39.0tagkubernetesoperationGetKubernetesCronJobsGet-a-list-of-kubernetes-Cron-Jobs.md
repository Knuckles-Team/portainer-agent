##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/kubernetes/operation/GetKubernetesCronJobs)Get a list of kubernetes Cron Jobs
Get a list of kubernetes Cron Jobs that the user has access to. **Access policy** : Authenticated user.
##### Authorizations:
(_ApiKeyAuth_ _jwt_)
##### path Parameters
idrequired |  integer Environment identifier
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
Unable to find an environment with the specified identifier.
**500**
Server error occurred while attempting to retrieve the list of Cron Jobs.
get/kubernetes/{id}/cron_jobs
https://api-docs.portainer.io/api/kubernetes/{id}/cron_jobs
###  Response samples
  * 200


Content type
application/json
Copy
Expand all  Collapse all
`[
  *  {
    *  "Command": "string",

    *  "Id": "string",

    *  "IsSystem": true,

    *  "Jobs": [
      *  {
        *  "BackoffLimit": 0,

        *  "Command": "string",

        *  "Completions": 0,

        *  "Container": {
          *  "args": [
            * "string"
 ],

          *  "command": [
            * "string"
 ],

          *  "env": [
            *  {
              *  "name": "string",

              *  "value": "string",

              *  "valueFrom": {
                *  "configMapKeyRef": {
                  *  "key": "string",

                  *  "name": "string",

                  *  "optional": true
  },

                *  "fieldRef": {
                  *  "apiVersion": "string",

                  *  "fieldPath": "string"
  },

                *  "fileKeyRef": {
                  *  "key": "string",

                  *  "optional": true,

                  *  "path": "string",

                  *  "volumeName": "string"
  },

                *  "resourceFieldRef": {
                  *  "containerName": "string",

                  *  "divisor": {
                    *  "Format": null
 },

                  *  "resource": "string"
  },

                *  "secretKeyRef": {
                  *  "key": "string",

                  *  "name": "string",

                  *  "optional": true
  }
  }
  }
 ],

          *  "envFrom": [
            *  {
              *  "configMapRef": {
                *  "name": "string",

                *  "optional": true
  },

              *  "prefix": "string",

              *  "secretRef": {
                *  "name": "string",

                *  "optional": true
  }
  }
 ],

          *  "image": "string",

          *  "imagePullPolicy": "Always",

          *  "lifecycle": {
            *  "postStart": {
              *  "exec": {
                *  "command": [
                  * "string"
 ]
 },

              *  "httpGet": {
                *  "host": "string",

                *  "httpHeaders": [
                  *  {
                    *  "name": null,

                    *  "value": null
  }
 ],

                *  "path": "string",

                *  "port": {
                  *  "IntVal": 0,

                  *  "StrVal": "string",

                  *  "Type": 0
  },

                *  "scheme": "HTTP"
  },

              *  "sleep": {
                *  "seconds": 0
 },

              *  "tcpSocket": {
                *  "host": "string",

                *  "port": {
                  *  "IntVal": 0,

                  *  "StrVal": "string",

                  *  "Type": 0
  }
  }
  },

            *  "preStop": {
              *  "exec": {
                *  "command": [
                  * "string"
 ]
 },

              *  "httpGet": {
                *  "host": "string",

                *  "httpHeaders": [
                  *  {
                    *  "name": null,

                    *  "value": null
  }
 ],

                *  "path": "string",

                *  "port": {
                  *  "IntVal": 0,

                  *  "StrVal": "string",

                  *  "Type": 0
  },

                *  "scheme": "HTTP"
  },

              *  "sleep": {
                *  "seconds": 0
 },

              *  "tcpSocket": {
                *  "host": "string",

                *  "port": {
                  *  "IntVal": 0,

                  *  "StrVal": "string",

                  *  "Type": 0
  }
  }
  },

            *  "stopSignal": "SIGABRT"
  },

          *  "livenessProbe": {
            *  "exec": {
              *  "command": [
                * "string"
 ]
 },

            *  "failureThreshold": 0,

            *  "grpc": {
              *  "port": 0,

              *  "service": "string"
  },

            *  "httpGet": {
              *  "host": "string",

              *  "httpHeaders": [
                *  {
                  *  "name": "string",

                  *  "value": "string"
  }
 ],

              *  "path": "string",

              *  "port": {
                *  "IntVal": 0,

                *  "StrVal": "string",

                *  "Type": 0
  },

              *  "scheme": "HTTP"
  },

            *  "initialDelaySeconds": 0,

            *  "periodSeconds": 0,

            *  "successThreshold": 0,

            *  "tcpSocket": {
              *  "host": "string",

              *  "port": {
                *  "IntVal": 0,

                *  "StrVal": "string",

                *  "Type": 0
  }
  },

            *  "terminationGracePeriodSeconds": 0,

            *  "timeoutSeconds": 0
  },

          *  "name": "string",

          *  "ports": [
            *  {
              *  "containerPort": 0,

              *  "hostIP": "string",

              *  "hostPort": 0,

              *  "name": "string",

              *  "protocol": "TCP"
  }
 ],

          *  "readinessProbe": {
            *  "exec": {
              *  "command": [
                * "string"
 ]
 },

            *  "failureThreshold": 0,

            *  "grpc": {
              *  "port": 0,

              *  "service": "string"
  },

            *  "httpGet": {
              *  "host": "string",

              *  "httpHeaders": [
                *  {
                  *  "name": "string",

                  *  "value": "string"
  }
 ],

              *  "path": "string",

              *  "port": {
                *  "IntVal": 0,

                *  "StrVal": "string",

                *  "Type": 0
  },

              *  "scheme": "HTTP"
  },

            *  "initialDelaySeconds": 0,

            *  "periodSeconds": 0,

            *  "successThreshold": 0,

            *  "tcpSocket": {
              *  "host": "string",

              *  "port": {
                *  "IntVal": 0,

                *  "StrVal": "string",

                *  "Type": 0
  }
  },

            *  "terminationGracePeriodSeconds": 0,

            *  "timeoutSeconds": 0
  },

          *  "resizePolicy": [
            *  {
              *  "resourceName": "cpu",

              *  "restartPolicy": "NotRequired"
  }
 ],

          *  "resources": {
            *  "claims": [
              *  {
                *  "name": "string",

                *  "request": "string"
  }
 ],

            *  "limits": {
              *  "property1": {
                *  "Format": "DecimalExponent"
 },

              *  "property2": {
                *  "Format": "DecimalExponent"
 }
  },

            *  "requests": {
              *  "property1": {
                *  "Format": "DecimalExponent"
 },

              *  "property2": {
                *  "Format": "DecimalExponent"
 }
  }
  },

          *  "restartPolicy": "Always",

          *  "restartPolicyRules": [
            *  {
              *  "action": "Restart",

              *  "exitCodes": {
                *  "operator": "In",

                *  "values": [
                  * 0
 ]
  }
  }
 ],

          *  "securityContext": {
            *  "allowPrivilegeEscalation": true,

            *  "appArmorProfile": {
              *  "localhostProfile": "string",

              *  "type": "Unconfined"
  },

            *  "capabilities": {
              *  "add": [
                * "string"
 ],

              *  "drop": [
                * "string"
 ]
  },

            *  "privileged": true,

            *  "procMount": "Default",

            *  "readOnlyRootFilesystem": true,

            *  "runAsGroup": 0,

            *  "runAsNonRoot": true,

            *  "runAsUser": 0,

            *  "seLinuxOptions": {
              *  "level": "string",

              *  "role": "string",

              *  "type": "string",

              *  "user": "string"
  },

            *  "seccompProfile": {
              *  "localhostProfile": "string",

              *  "type": "Unconfined"
  },

            *  "windowsOptions": {
              *  "gmsaCredentialSpec": "string",

              *  "gmsaCredentialSpecName": "string",

              *  "hostProcess": true,

              *  "runAsUserName": "string"
  }
  },

          *  "startupProbe": {
            *  "exec": {
              *  "command": [
                * "string"
 ]
 },

            *  "failureThreshold": 0,

            *  "grpc": {
              *  "port": 0,

              *  "service": "string"
  },

            *  "httpGet": {
              *  "host": "string",

              *  "httpHeaders": [
                *  {
                  *  "name": "string",

                  *  "value": "string"
  }
 ],

              *  "path": "string",

              *  "port": {
                *  "IntVal": 0,

                *  "StrVal": "string",

                *  "Type": 0
  },

              *  "scheme": "HTTP"
  },

            *  "initialDelaySeconds": 0,

            *  "periodSeconds": 0,

            *  "successThreshold": 0,

            *  "tcpSocket": {
              *  "host": "string",

              *  "port": {
                *  "IntVal": 0,

                *  "StrVal": "string",

                *  "Type": 0
  }
  },

            *  "terminationGracePeriodSeconds": 0,

            *  "timeoutSeconds": 0
  },

          *  "stdin": true,

          *  "stdinOnce": true,

          *  "terminationMessagePath": "string",

          *  "terminationMessagePolicy": "File",

          *  "tty": true,

          *  "volumeDevices": [
            *  {
              *  "devicePath": "string",

              *  "name": "string"
  }
 ],

          *  "volumeMounts": [
            *  {
              *  "mountPath": "string",

              *  "mountPropagation": "None",

              *  "name": "string",

              *  "readOnly": true,

              *  "recursiveReadOnly": "Disabled",

              *  "subPath": "string",

              *  "subPathExpr": "string"
  }
 ],

          *  "workingDir": "string"
  },

        *  "Duration": "string",

        *  "FailedReason": "string",

        *  "FinishTime": "string",

        *  "Id": "string",

        *  "IsSystem": true,

        *  "Name": "string",

        *  "Namespace": "string",

        *  "PodName": "string",

        *  "StartTime": "string",

        *  "Status": "string"
  }
 ],

    *  "Name": "string",

    *  "Namespace": "string",

    *  "Schedule": "string",

    *  "Suspend": true,

    *  "Timezone": "string"
  }

 ]`
