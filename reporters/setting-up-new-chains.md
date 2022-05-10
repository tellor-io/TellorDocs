---
description: How to setup Tellor / report data on a new chain
---

# Setting up New Chains

Tellor is easy to deploy on any EVM chain. &#x20;

For instructions on how to deploy the smart contracts: [https://medium.com/tellor/how-to-deploy-tellor-on-an-evm-chain-c0243c60a98f](https://medium.com/tellor/how-to-deploy-tellor-on-an-evm-chain-c0243c60a98f)


## Telliot Configuration

To configure telliot for your new EVM chain make sure you have [configured your telliot](https://tellor-io.github.io/telliot-feed-examples/getting-started/) first.

To show your current configuration:

    telliot config show

## Add your EVM chain

### Edit the chains file

The chains configuration file allows you to add a chain to your telliot configuration.
For this example we will be adding the Kovan testnet chain.
Edit the `~/telliot/chains.json` and add the following:

```json
 {
      "type": "Chain",
      "name": "Ethereum Testnet Kovan",
      "chain": "ETH",
      "network": "kovan",
      "chain_id": 42,
      "currency": {
        "type": "EVMCurrency",
        "name": "Kovan Ether",
        "symbol": "KOV",
        "decimals": 18
      }
    }
```
### Edit the endpoints file
Next we'll edit the `~/telliot/endpoints.yaml` file to configure Telliot to use our Kovan endpoint.
If you don't have an endpoint, a free one is available at Infura.io. Simply replace INFURA_API_KEY with the one provided by Infura.

Add the following to your endpoints file:

```yaml
- type: RPCEndpoint
  chain_id: 42
  network: kovan
  provider: Infura
  url: wss://kovan.infura.io/ws/v3/{INFURA_API_KEY}
  explorer: https://rinkeby.etherscan.io
```

After your new chain has been added, you can now read the [Usage](https://tellor-io.github.io/telliot-feed-examples/usage/) section, and you'll be set to report.

For non-EVM chains, feel free to [reach out](mailto:info@tellor.io) and see if it's something we can do!&#x20;
