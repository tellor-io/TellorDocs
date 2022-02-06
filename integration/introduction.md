---
description: >-
  This page is designed to give you a quick overview of using Tellor to get data
  into your smart contracts.
---

# Introduction

## Integrating Tellor Oracle Data in Ethereum Smart Contracts

We provide a [helper contract](https://github.com/tellor-io/usingtellor) that provides convenient functions for interacting with the Tellor system.

### Installation

```bash
npm install usingtellor
```

### Using in a contract in solidity:

Just import the UsingTellor contract into your solidity file passing the desired Tellor address (see [references page](reference/)) as a parameter. For testing, use a TellorPlayground address. In production, use either the TellorMaster address on Ethereum mainnet or the TellorFlex address on Polygon.

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
 * @dev Retrieve value from oracle based on queryId/timestamp
 * @param _queryId being requested
 * @param _timestamp to retrieve data/value from
 * @return bytes value for query/timestamp submitted
 */
function retrieveData(bytes32 _queryId, uint256 _timestamp)
        public
        view
        returns (bytes memory);

/**
 * @dev Determines whether a value with a given queryId and timestamp has been disputed
 * @param _queryId is the value id to look up
 * @param _timestamp is the timestamp of the value to look up
 * @return bool true if queryId/timestamp is under dispute
 */
function isInDispute(bytes32 _queryId, uint256 _timestamp)
        public
        view
        returns (bool);

/**
 * @dev Counts the number of values that have been submitted for the queryId
 * @param _queryId the id to look up
 * @return uint256 count of the number of values received for the queryId
 */
function getNewValueCountbyQueryId(bytes32 _queryId)
        public
        view
        returns (uint256);

/**
 * @dev Gets the timestamp for the value based on its index
 * @param _queryId is the id to look up
 * @param _index is the value index to look up
 * @return uint256 timestamp
 */
function getTimestampbyQueryIdandIndex(bytes32 _queryId, uint256 _index)
        public
        view
        returns (uint256);

/**
 * @dev Allows the user to get the latest value for the queryId specified
 * @param _queryId is the id to look up the value for
 * @return ifRetrieve bool true if non-zero value successfully retrieved
 * @return value the value retrieved
 * @return _timestampRetrieved the retrieved value's timestamp
 */
function getCurrentValue(bytes32 _queryId)
        public
        view
        returns (
            bool _ifRetrieve,
            bytes memory _value,
            uint256 _timestampRetrieved
        );

/**
 * @dev Retrieves the latest value for the queryId before the specified timestamp
 * @param _queryId is the queryId to look up the value for
 * @param _timestamp before which to search for latest value
 * @return _ifRetrieve bool true if able to retrieve a non-zero value
 * @return _value the value retrieved
 * @return _timestampRetrieved the value's timestamp
 */
function getDataBefore(bytes32 _queryId, uint256 _timestamp)
        public
        view
        returns (
            bool _ifRetrieve,
            bytes memory _value,
            uint256 _timestampRetrieved
        );

```

{% hint style="info" %}
**Line 68:** When retrieving your data from Tellor, it's recommended you use the `getDataBefore` function with a time buffer to allow time for a bad value to be disputed.
{% endhint %}

#### Query IDs

The query ID is used to look up values in the Tellor Oracle. You will need to figure out what the query ID is for the data you want. The BTC/USD price is query ID 2.

#### Example usage

```solidity
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

```solidity
     /**
     * @dev Public function to mint tokens for the passed address
     * @param user The address which will own the tokens
     *
     */
    function faucet(address user) external;


    /**
     * @dev A mock function for submitting a value without reporter staking needed
     * @param _queryId the ID to associate the value to
     * @param _value the requested oracle value
     * @param _nonce the current value count for the query id
     * @param _queryData the data used by reporters to fulfill the data query
     */
    function submitValue(
        bytes32 _queryId,
        bytes calldata _value,
        uint256 _nonce,
        bytes memory _queryData
    ) external;
```

#### Running tests

```bash
npx hardhat test
```

## Sample Project

We provide a repo with this setup installed and ready for use: [SampleUsingTellor](https://github.com/tellor-io/sampleUsingTellor).
