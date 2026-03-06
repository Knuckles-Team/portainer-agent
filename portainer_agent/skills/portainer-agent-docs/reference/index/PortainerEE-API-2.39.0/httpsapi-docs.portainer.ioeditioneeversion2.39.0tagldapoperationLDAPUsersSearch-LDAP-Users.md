##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/ldap/operation/LDAPUsers)Search LDAP Users
**Access policy** : administrator
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### Request Body schema: application/json
required
details
LDAPSettings |  object (portaineree.LDAPSettings)
---|---
### Responses
**200**
Success
**400**
Invalid request
**500**
Server error
post/ldap/users
https://api-docs.portainer.io/api/ldap/users
###  Request samples
  * Payload


Content type
application/json
Copy
Expand all  Collapse all
`{
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
  }

 }`
