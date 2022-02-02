---
description: >-
  This page is designed to give you a quick overview of using Tellor to get data
  into your smart contracts.
---

# Introduction

## Integrating Tellor Oracle Data in Ethereum Smart Contracts

For this, we provide a [helper contract](https://github.com/tellor-io/usingtellor) that will provide convenient functions to interact with the Tellor System.

### Installation

```
npm install usingtellor
```

### Using in the contract in solidity:

Just import the usingTellor contract to your solidity file passing the desired Tellor address(see references page) as a parameters.

Test: Use the TellorPlayground contract

```solidity
pragma solidity >=0.8.0;

import "usingtellor/contracts/UsingTellor.sol";

contract MyContract is UsingTellor {

  constructor(address payable _tellorAddress) UsingTellor(_tellorAddress) public {

  }

  // ...

}
```

#### Important Details

{% hint style="info" %}
**Line 5:** Your contract inherits the functions needed to interact with Tellor

**Line 7:** Your constructor needs to specify the Tellor Oracle contract address(see references page for the address)
{% endhint %}

#### Available Tellor Functions

Children contracts have access to the following functions:

```solidity

    /**
     * @dev A mock function to create a dispute
     * @param _queryId The tellorId to be disputed
     * @param _timestamp the timestamp of the value to be disputed
     */
    function beginDispute(bytes32 _queryId, uint256 _timestamp) external;

    /**
     * @dev Counts the number of values that have been submitted for a given ID
     * @param _queryId the ID to look up
     * @return uint256 count of the number of values received for the queryId
     */
    function getNewValueCountbyQueryId(bytes32 _queryId) public view returns (uint256);

    /**
     * @dev Gets the timestamp for the value based on their index
     * @param _queryId is the queryId to look up
     * @param _index is the value index to look up
     * @return uint256 timestamp
     */
    function getTimestampbyQueryIdandIndex(bytes32 _queryId, uint256 _index) public view returns (uint256);

    /**
     * @dev Retrieve bytes value from oracle based on queryId/timestamp
     * @param _queryId being retrieved
     * @param _timestamp to retrieve data/value from
     * @return bytes value for queryId/timestamp submitted
     */
    function retrieveData(bytes32 _queryId, uint256 _timestamp) public view returns (bytes memory);

    /**
     * @dev A mock function to submit a value to be read without miners needed
     * @param _queryId The tellorId to associate the value to
     * @param _value the value for the queryId
     * @param _nonce the current value count for the query id
     * @param _queryData the data used by reporters to fulfill the data query
     */
    function submitValue(bytes32 _queryId, bytes calldata _value, uint256 _nonce, bytes memory _queryData) external;

    /**
     * @dev Adds a tip to a given query ID.
     * @param _queryId is the queryId to look up
     * @param _amount is the amount of tips
     * @param _queryData is the extra bytes data needed to fulfill the request
     */
    function tipQuery(bytes32 _queryId, uint256 _amount, bytes memory _queryData) external;
```

#### Query IDs

The query ID is used to look up values in the Tellor Oracle. You will need to figure out what the query ID is for the data you want. The BTC/USD price is query ID 2.

#### Example usage

```
contract BtcPriceContract is UsingTellor {

  // This contract now has access to all functions in UsingTellor

  bytes btcPrice;
  bytes32 btcQueryId = 0x0000000000000000000000000000000000000000000000000000000000000002;

  constructor(address payable _tellorAddress) UsingTellor(_tellorAddress) public {}

  function setBtcPrice() public {
    bool _didGet;
    uint _timestamp;

    (_didGet, btcPrice, _timestamp) = getCurrentValue(btcQueryId);
  }
}
```

{% hint style="info" %}
**Line 6:** The`btcQueryId` is set to`2 (in bytes32)`, the BTC/USD query ID
{% endhint %}

### Testing your contracts

For ease of use, the `UsingTellor` repo comes with Tellor Playground system for easier integration. This mock version contains a few helper functions:

```
     /**
     * @dev Public function to mint tokens for the passed address
     * @param user The address which will own the tokens
     *
     */
    function faucet(address user) external;


    /**
    * @dev A mock function to submit a value to be read without miners needed
    * @param _requestId The tellorId to associate the value to
    * @param _value the value for the requestId
    */
    function submitValue(uint256 _requestId,uint256 _value) external;
```

#### Running tests

```bash
npx hardhat test
```

## Sample Project

We provide a repo with this setup installed and ready for use: [SampleUsingTellor](https://github.com/tellor-io/sampleUsingTellor).
