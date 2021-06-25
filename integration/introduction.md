---
description: >-
  This page is designed to give you a quick overview of using Tellor to get data
  into your smart contracts.
---

# Introduction

## Integrating Tellor Oracle Data in Ethereum Smart Contracts

For this, we provide a helper contract that will provide convenience functions to interact with the Tellor System.

### Installation

```text
npm install usingtellor
```

### Using in the contract in solidity:

Just import the usingTellor contract to your solidity file passing the desired Tellor address\(see references page\) as a parameter.

Test: Use the TellorPlayground contract

```text
pragma solidity >=0.4.21 <0.7.0;

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

**Line 7:** Your constructor needs to specify the Tellor Oracle contract address\(see references page for the address\)
{% endhint %}

#### Available Tellor Functions

Children contracts have access to the following functions:

```text
    /**
    * @dev Retreive value from oracle based on requestId/timestamp
    * @param _requestId being requested
    * @param _timestamp to retreive data/value from
    * @return uint value for requestId/timestamp submitted
    */
    function retrieveData(uint256 _requestId, uint256 _timestamp) public view returns(uint256);

    /**
    * @dev Gets if the mined value for the specified requestId/_timestamp is currently under dispute
    * @param _requestId to looku p
    * @param _timestamp is the timestamp to look up miners for
    * @return bool true if requestId/timestamp is under dispute
    */
    function isInDispute(uint256 _requestId, uint256 _timestamp) public view returns(bool);

    /**
    * @dev Counts the number of values that have been submitted for the request
    * @param _requestId the requestId to look up
    * @return uint count of the number of values received for the requestId
    */
    function getNewValueCountbyRequestId(uint256 _requestId) public view returns(uint);

    /**
    * @dev Gets the timestamp for the value based on their index
    * @param _requestId is the requestId to look up
    * @param _index is the value index to look up
    * @return uint timestamp
    */
    function getTimestampbyRequestIDandIndex(uint256 _requestId, uint256 _index) public view returns(uint256);

    /**
    * @dev Allows the user to get the latest value for the requestId specified
    * @param _requestId is the requestId to look up the value for
    * @return bool true if it is able to retreive a value, the value, and the value's timestamp
    */
    function getCurrentValue(uint256 _requestId) public view returns (bool ifRetrieve, uint256 value, uint256 _timestampRetrieved);

    /**
    * @dev Allows the user to get the first value for the requestId before the specified timestamp
    * @param _requestId is the requestId to look up the value for
    * @param _timestamp before which to search for first verified value
    * @return bool true if it is able to retreive a value, the value, and the value's timestamp
    */
    function getDataBefore(uint256 _requestId, uint256 _timestamp)
        public
        view
        returns (bool _ifRetrieve, uint256 _value, uint256 _timestampRetrieved);
```

#### Request IDs

The request ID is used to look up prices in the Tellor Oracle. _You will need to_ figure out what the request ID is for the price data you want. The BTC/USD price is request ID 2.

#### Example usage

```text
contract BtcPriceContract is UsingTellor {

  //This Contract now have access to all functions on UsingTellor

  uint256 btcPrice;
  uint256 btcRequestId = 2;

  constructor(address payable _tellorAddress) UsingTellor(_tellorAddress) public {}

  function setBtcPrice() public {
    bool _didGet;
    uint _timestamp;
    uint _value;

    (_didGet, btcPrice, _timestamp) = getCurrentValue(btcRequestId);
  }
}
```

{% hint style="info" %}
**Line 4:** The`btcRequetId` is set local to`2`, the BTC/USD request ID

**Line 12:** The call to `getCurrentValue` returns the value into `btcPrice`
{% endhint %}

### Testing your contracts

For ease of use, the `UsingTellor` repo comes with Tellor Playground system for easier integration. This mock version contains a few helper functions:

```text
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
npm run test
```

### Migration

Just run truffle migrate with the desired Network

```bash
truffle migrate --network rinkeby
```

## Sample Project

We provide a repo with this setup installed and ready for use: [SampleUsingTellor](https://github.com/tellor-io/sampleUsingTellor). Watch the video walkthrough [here](https://youtu.be/fNuAmpYzztg).

