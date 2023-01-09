# Solidity Integration

## Connecting to the Oracle

To use Tellor data, you can use the [UsingTellor](https://github.com/tellor-io/usingtellor) helper contract. After connecting it to the Oracle, you can read a value using your `queryId`. This guide uses the `BTC/USD SpotPrice` as an example query. &#x20;

{% hint style="info" %}
Example: [Sample project using Tellor](https://github.com/tellor-io/sampleUsingTellor)

Video: [Integration Tutorial](https://www.youtube.com/watch?v=1UMa9TACx48)
{% endhint %}

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

  constructor(address payable _tellorAddress) UsingTellor(_tellorAddress) {

  }

  // ...

}
```

{% hint style="info" %}
**Note:** In the constructor on line 7, you need to specify the Tellor [contract address](https://docs.tellor.io/tellor/the-basics/contracts-reference). For testing, you can use a Tellor Playground address. In production, use the Oracle address on your chosen network.
{% endhint %}

### Reading data

You can either use our[ QueryId builder ](https://tellor.io/queryidbuilder)to[ create a queryId ](creating-a-query.md)and hardcode it, or use solidity to generate it.  Once you have created a `queryId`, you can add the Tellor data feed to your contract code. The best practice for reading Tellor data is to use the `getDataBefore` function with a buffer time that allows time for bad values to be disputed.  It's also best practice to require/check that the data is not too old.  For example: `require(block.timestamp - _timestampRetrieved < 24 hours);`

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
      require(block.timestamp - _timestampRetrieved < 24 hours);
      return abi.decode(_value, (uint256);
    }
```

{% hint style="warning" %}
**Note:** Use usingtellor's getDataBefore(bytes32 \_queryId, uint256 \_timestamp) function with a buffer time (20 minutes for example) to allow time for a bad value to be disputed
{% endhint %}

###
