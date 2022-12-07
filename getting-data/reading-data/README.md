# Reading Data

## Connecting to the Oracle

To use Tellor data, you can use the [UsingTellor](https://github.com/tellor-io/usingtellor) helper contract. After connecting it to the Oracle, you can read a value using your `queryId`. This guide uses the `BTC/USD SpotPrice` as an example query.

### Installation
To install usingtellor, run the following command:
```bash
npm install usingtellor
```

### Importing

To import the UsingTellor contract into your Solidity file, pass the desired Tellor address (see the [references page](https://docs.tellor.io/tellor/the-basics/contracts-reference) for the address) as a parameter:

```solidity
pragma solidity >=0.8.0;

import "usingtellor/contracts/UsingTellor.sol";

contract MyContract is UsingTellor {

  constructor(address payable _tellorAddress) UsingTellor(_tellorAddress) public {

  }

  // ...

}
```

{% hint style="info" %}
**Note:** In the constructor on line 7, you need to specify the Tellor [contract address](https://docs.tellor.io/tellor/the-basics/contracts-reference). For testing, you can use a TellorPlayground address. In production, use the Oracle address on your chosen network.
{% endhint %}

### Reading data
Once you have created a `queryId`, you can add the Tellor data feed to your contract code. The best practice for reading Tellor data is to use the `getDataBefore` function with a buffer time. This allows time for bad values to be disputed.

In the example below, we add a function `getBtcSpotPrice` that reads the BTC/USD price feed from the Oracle:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity 0.8.3;

import "usingtellor/contracts/UsingTellor.sol";

contract ExampleContract is UsingTellor {

    ...

    function getBtcSpotPrice() external view returns(uint256) {
    
      bytes memory _queryData = abi.encode("SpotPrice", abi.encode("btc", "usd"));
      bytes32 _queryId = keccak256(_queryData);
      
      (bytes memory _value, uint256 _timestampRetrieved) =
          getDataBefore(_queryId, block.timestamp - 20 minutes);
      if (_timestampRetrieved == 0) return 0;
      return abi.decode(_value, (uint256);
    }
```

{% hint style="info" %}
**Note:** Use usingtellor's getDataBefore(bytes32 \_queryId, uint256 \_timestamp) function with a buffer time (20 minutes for example) to allow time for a bad value to be disputed
{% endhint %}

### Addendum: Tellor Playground

[Tellor Playground](https://github.com/tellor-io/TellorPlayground) aims to help anyone building on Tellor to quickly bootstrap, implement, and test a Tellor integration. See the [reference page](https://docs.tellor.io/tellor/the-basics/contracts-reference) for deployed addresses on various test networks.

The Playground is a simplified (and not a real oracle) Tellor, containing only the small bits that developers need to worry about: getting data, adding tips, reading events and so forth.

#### How to implement

Implementing the Playground is as simple as pointing the `UsingTellor` constructor to the Playground on your network. See the [reference page](https://docs.tellor.io/tellor/the-basics/contracts-reference) for deployed addresses on various test networks.

When finished testing with the Playground, switching back to the real Tellor only requires updating the oracle address in your UsingTellor implementation.

