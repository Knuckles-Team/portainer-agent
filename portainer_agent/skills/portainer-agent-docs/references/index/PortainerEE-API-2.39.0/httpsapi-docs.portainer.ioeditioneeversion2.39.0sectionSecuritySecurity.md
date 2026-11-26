##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#section/Security)Security
Each API environment(endpoint) has an associated access policy, it is documented in the description of each environment(endpoint).
Different access policies are available:
  * Public access
  * Authenticated access
  * Restricted access
  * Administrator access


### Public access
No authentication is required to access the environments(endpoints) with this access policy.
### Authenticated access
Authentication is required to access the environments(endpoints) with this access policy.
### Restricted access
Authentication is required to access the environments(endpoints) with this access policy. Extra-checks might be added to ensure access to the resource is granted. Returned data might also be filtered.
### Administrator access
Authentication as well as an administrator role are required to access the environments(endpoints) with this access policy.
