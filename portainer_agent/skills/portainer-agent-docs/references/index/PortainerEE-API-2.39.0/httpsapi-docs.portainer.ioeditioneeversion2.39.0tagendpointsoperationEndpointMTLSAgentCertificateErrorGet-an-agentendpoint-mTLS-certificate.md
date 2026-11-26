##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/endpoints/operation/EndpointMTLSAgentCertificateError)Get an agent(endpoint) mTLS certificate
Retrieve the mTLS certificate of an environment(endpoint). **Access policy** : administrator
##### Authorizations:
_ApiKeyAuth_ _jwt_
##### path Parameters
idrequired |  integer Environment(Endpoint) identifier
---|---
### Responses
**200**
Success
**400**
Invalid request
**404**
Environment(Endpoint) not found
**500**
Server error
get/endpoints/{id}/mtls_certificate_error
https://api-docs.portainer.io/api/endpoints/{id}/mtls_certificate_error
###  Response samples
  * 200


Content type
application/json
Copy
Expand all  Collapse all
`{
  *  "MTLSCertificate": {
    *  "AuthorityKeyId": "string",

    *  "CRLDistributionPoints": [
      * "string"
 ],

    *  "ExtendedKeyUsages": [
      * "string"
 ],

    *  "IsCertificateAuthority": true,

    *  "Issuer": {
      *  "Country": [
        * "string"
 ],

      *  "Locality": [
        * "string"
 ],

      *  "SerialNumber": "string",

      *  "StreetAddress": [
        * "string"
 ]
  },

    *  "IssuingCertificateURLs": [
      * "string"
 ],

    *  "KeyUsages": [
      * "string"
 ],

    *  "OCSPServers": [
      * "string"
 ],

    *  "Policies": [
      * "string"
 ],

    *  "PublicKey": {
      *  "Algorithm": "string",

      *  "Exponent": "string",

      *  "Modulus": "string",

      *  "Size": 0,

      *  "Value": "string"
  },

    *  "SHA256Fingerprint": "string",

    *  "SerialNumber": "string",

    *  "SignatureAlgorithm": "string",

    *  "Subject": {
      *  "Country": [
        * "string"
 ],

      *  "Locality": [
        * "string"
 ],

      *  "SerialNumber": "string",

      *  "StreetAddress": [
        * "string"
 ]
  },

    *  "SubjectAltDNSNames": [
      * "string"
 ],

    *  "SubjectAltEmailAddresses": [
      * "string"
 ],

    *  "SubjectAltIpAddresses": [
      * "string"
 ],

    *  "SubjectAltURIs": [
      * "string"
 ],

    *  "SubjectKeyId": "string",

    *  "ValidNotAfter": "string",

    *  "ValidNotBefore": "string",

    *  "Version": 0
  }

 }`
