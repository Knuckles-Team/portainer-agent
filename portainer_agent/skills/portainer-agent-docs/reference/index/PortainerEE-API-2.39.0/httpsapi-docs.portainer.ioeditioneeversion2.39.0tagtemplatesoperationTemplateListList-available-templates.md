##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/templates/operation/TemplateList)List available templates
List available templates. **Access policy** : authenticated
##### Authorizations:
_ApiKeyAuth_ _jwt_
### Responses
**200**
Success
**500**
Server error
get/templates
https://api-docs.portainer.io/api/templates
###  Response samples
  * 200


Content type
application/json
Copy
Expand all  Collapse all
`{

  *  "templates": [
    *  {
      *  "administrator_only": true,

      *  "categories": [
        * "database"
 ],

      *  "command": "ls -lah",

      *  "description": "High performance web server",

      *  "env": [
        *  {
          *  "default": "default_value",

          *  "description": "MySQL root account password",

          *  "label": "Root password",

          *  "name": "MYSQL_ROOT_PASSWORD",

          *  "preset": false,

          *  "select": [
            *  {
              *  "default": false,

              *  "text": "text value",

              *  "value": "value"
  }
 ]
  }
 ],

      *  "hostname": "mycontainer",

      *  "id": 1,

      *  "image": "nginx:latest",

      *  "interactive": true,

      *  "labels": [
        *  {
          *  "name": "name",

          *  "value": "value"
  }
 ],

      *  "logo": "https://portainer.io/img/logo.svg[](https://portainer.io/img/logo.svg)",

      *  "name": "mystackname",

      *  "network": "mynet",

      *  "note": "This is my <b>custom</b> template",

      *  "platform": "linux",

      *  "ports": [
        * "8080:80/tcp"
 ],

      *  "privileged": true,

      *  "registry": "quay.io",

      *  "repository": {
        *  "stackfile": "./subfolder/docker-compose.yml",

        *  "url": ""
  },

      *  "restart_policy": "on-failure",

      *  "stackFile": "string",

      *  "title": "Nginx",

      *  "type": 1,

      *  "volumes": [
        *  {
          *  "bind": "/tmp",

          *  "container": "/data",

          *  "readonly": true
  }
 ]
  }
 ],

  *  "version": "string"

 }`
