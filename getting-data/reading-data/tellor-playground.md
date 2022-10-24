# Tellor Playground

## Overview

[Tellor Playground](https://github.com/tellor-io/TellorPlayground) aims to help anyone building on Tellor to quickly test and implement ideas. See the [reference page](https://app.gitbook.com/s/tcQlo49FAqTaOimNOz0X/getting-data/using-tellor) for deployed addresses on various test networks.

### Why use Tellor Playground?

When testing their smart contracts, most projects that want to integrate Tellor only need to test functions for reading and requesting tellor data.

The Playground is a simplified (and not a real oracle) Tellor, containing only the small bits that developers need to worry about when building and testing: submitting data, getting data, reading events and so forth.

#### Why not use the real Tellor

There are a few reasons not to use even the testnet version of the real system, the first one being that it is identical to the mainnet version, where there are only so many datapoints available for reading. You can easily get the value of USD or BTC, but if your project needs to read a value from an exotic token, it might not be available.

To include a value in the Rinkeby version, it would first need to be added to the reporter software client. Or a developer could report the value themselves, but they would have to acquire 100 Rinkeby test TRB, stake it, and then they would only be able to submit a value once every 12 hours. If you're testing an idea or building a hackathon project, it might be overkill to go through all of that and it's far easier to make use of Tellor Playground.

### How to use

#### Reading values

If your smart contract needs to read Tellor values, you might want to use the helper [usingtellor](https://github.com/tellor-io/usingtellor), which already provides a few helpful functions to fetch data.

The first step is to install usingtellor, then inherit the UsingTellor contract, passing the TellorPlayground address as a constructor argument. Here's an example:

```
npm install usingtellor
```

```solidity
import "usingtellor/contracts/UsingTellor.sol";

contract BtcPriceContract is UsingTellor {
  //This contract now has access to all functions in UsingTellor

  bytes public btcPrice;
  bytes32 public btcQueryId = 0x0000000000000000000000000000000000000000000000000000000000000002;

  constructor(address payable _tellorAddress) UsingTellor(_tellorAddress) public {}

  function setBtcPrice() external {
      // TIP: For best practices, use getDataBefore with a time buffer to allow time for a value to be disputed
      (bool _ifRetrieve, bytes memory _value, uint256 _timestampRetrieved) = getDataBefore(btcQueryId, block.timestamp - 2 hours);
      if(_ifRetrieve) {
          btcPrice = _value;
      }
  }
}
```

#### Setting values in the Playground

To be able to properly read a value from playground, you'll need to first set the value yourself, since it does not rely on reporters.

To do that, you can choose some arbitrary `queryData`, which is a `bytes` value, and then take the keccak256 hash of the `queryData` to get the `queryId`. For the `nonce`, you can always input a value of `0`. Then call `submitValue` with any value you wish, which will add a data point to the Playground. Your contract can now easily read Tellor values.

```solidity
function submitValue(
        bytes32 _queryId,
        bytes calldata _value,
        uint256 _nonce,
        bytes memory _queryData
) external;
```

### Available Functions

Tellor Playground features all [Tellor Functions](../tellor-functions.md) with the addition of a faucet for minting test tokens:

```solidity
    /**
     * @dev Public function to mint tokens to the given address
     * @param _user The address which will receive the tokens
     */
    function faucet(address _user) external;
```
