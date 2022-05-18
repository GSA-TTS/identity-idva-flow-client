# identity-identity-flow-client

Flow client is used to invoke flows that require signed requests to access.
## Configure

Create an environment specific `vars-<env>.yaml` file. Configure it with the parameters needed for that environment. See `vars-env.yaml` for the format.

## Deploy

```
cf push --vars-file vars.yaml --vars-file vars-<env>.yaml --var ENVIRONMENT=<env>
```

## Use

The flow client can be used over http or with cli over ssh

### Web

Visit the flow client url and log in with idp account. After logging in, you will be able to invoke a flow.

### CLI

ssh into the instance and run `app/sign_url.sh` to produce a signed url.

```
    -n --name
        flow name url signature signed request is created for
    -u --url
        url signature signed request is created for
    -d --days
        num days is sig is valid for
    -s --seconds
        num seconds is sig is valid for
```
