##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#tag/settings/operation/SettingsEdgeMTLSCACertificates)Retrieve Portainer Edge MTLS CA Certificates
Retrieve Portainer Edge MTLS CA Certificates. **Access policy** : administrator
##### Authorizations:
_ApiKeyAuth_ _jwt_
### Responses
**200**
Success
**500**
Server error
get/settings/edge/mtls_ca_certificate
https://api-docs.portainer.io/api/settings/edge/mtls_ca_certificate
###  Response samples
  * 200


Content type
application/json
Copy
Expand all  Collapse all
`{
  *  "MTLSCACertificate": {
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
