# Reading Data

## Connecting to the Oracle

To use Tellor data, import [usingTellor](https://github.com/tellor-io/usingtellor), our helper contract for any network, connect it to the Oracle, and read a value on your `queryId`. This quickstart uses the `BTC/USD SpotPrice` as an example query.

### Installation

```bash
npm install usingtellor
```

### Importing

Just import the UsingTellor contract into your solidity file passing the desired Tellor address (see [references page](https://app.gitbook.com/s/tcQlo49FAqTaOimNOz0X/getting-data/using-tellor)) as a parameter.

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
**Line 7:** Your constructor needs to specify the Tellor contract address (see references page for the address). For testing, use a TellorPlayground address. In production, use the Oracle address on your chosen network.
{% endhint %}

### Reading data

Once we've created a `queryId` , we're ready to add our Tellor data feed to our contract code. The best-practice for reading Tellor data is to use the function `getDataBefore` . We use this function to leave time for disputes. In the example below, we'll add to the snippet above a function `getBtcSpotPrice()` that reads the btc/usd price feed from the Oracle.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity 0.8.3;

import "usingtellor/contracts/UsingTellor.sol";

contract ExampleContract is UsingTellor {

    ...

    function getBtcSpotPrice() external view returns(uint256) {
    
      bytes memory _queryData = abi.encode("SpotPrice", abi.encode("btc", "usd"));
      bytes32 _queryId = keccak256(_queryData);
      
      (bool ifRetrieve, bytes memory _value, ) =
          getDataBefore(_queryId, block.timestamp - 1 hours);
      if (!ifRetrieve) return 0;
      return abi.decode(_value, (uint256);
    }
```

{% hint style="info" %}
**Line 16:** Use usingtellor's getDataBefore(bytes32 \_queryId, uint256 \_timestamp) function with a buffer time (1 hour for example) to allow time for a bad value to be disputed
{% endhint %}

### Addendum: Tellor Playground

[Tellor Playground](https://github.com/tellor-io/TellorPlayground) aims to help anyone building on Tellor to quickly bootstrap, implement, and test a Tellor integration. See the [reference page](https://app.gitbook.com/s/tcQlo49FAqTaOimNOz0X/getting-data/using-tellor) for deployed addresses on various test networks.

The Playground is a simplified (and not a real oracle) Tellor, containing only the small bits that developers need to worry about: getting data, adding tips, reading events and so forth.

#### How to implement

Implementing the Playground is as simple as pointing the `UsingTellor` constructor to the Playground on your network. See the [reference page](https://app.gitbook.com/s/tcQlo49FAqTaOimNOz0X/getting-data/using-tellor) for deployed addresses on various test networks.

When finished testing with the Playground, switching back to the real Tellor only requires updating the oracle address in your UsingTellor implementation.

