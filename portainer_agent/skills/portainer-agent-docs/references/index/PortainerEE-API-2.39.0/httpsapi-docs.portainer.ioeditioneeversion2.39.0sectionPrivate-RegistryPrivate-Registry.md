##  [](https://api-docs.portainer.io/?edition=ee&version=2.39.0#section/Private-Registry)Private Registry
Using private registry, you will need to pass a based64 encoded JSON string ‘{"registryId":<registryID value>}’ inside the Request Header. The parameter name is "X-Registry-Auth". <registryID value> - The registry ID where the repository was created.
Example:
```
eyJyZWdpc3RyeUlkIjoxfQ==

```

**NOTE** : You can find more information on how to query the Docker API in the [this Portainer example](https://documentation.portainer.io/api/api-examples/).
