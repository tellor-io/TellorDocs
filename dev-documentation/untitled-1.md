---
description: >-
  This page is designed to give you a quick overview of using Tellor to get data
  into your smart contracts.
---

# Quick Start

## Using Tellor Oracle Data in Ethereum Smart Contracts

Using the Tellor Oracle in Ethereum contracts involves two steps:

* Import UsingTellor Contract which contains the functionality needed to get data
* Add `getDataBefore` or `getCurrentValue` to get data into your contract by request ID



### Importing UsingTellor Contract

The `UsingTellor.sol` contract contains the solidity code for interacting with Tellor Oracle data. This project can be easily imported into Truffle projects by using npm:

```text
npm install usingtellor
```

This imports the UsingTellor contracts into `./node_modules/usingtellor/contracts`.

After importing the UsingTellor contracts, you can add them to your contract like int the example below:

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

**Line 7:** Your constructor needs to specify the [Tellor Oracle contract address](https://link-to-addresses) 
{% endhint %}

## Getting Data from the Tellor Oracle Inside Contracts

After you've set up a contract to be using Tellor, you can use the functions from `UsingTellor` to fetch price data. Before you integrate, you need to understand how Tellor **request IDs** and **price granularity** work.

### Request IDs

The request ID is used to look up prices in the Tellor Oracle. _You will need to_ figure out what the request ID is for the price data you want. The BTC/USD price is request ID 2.

### Price Granularity

Each price is a decimal \(e.g. BTC/USD 11885.31\). The prices are stored on chain as integrates \(e.g. 11885310000\). For each request ID, there exists a granularity, it is usually 100000. _You will need to_ figure out what the granularity if for the price data you want.

{% page-ref page="reference-page/data-request-ids-1.md" %}



### Functions for Accessing Data

There are two functions for accessing data on chain.

#### `getCurrentValue`

Allows the user to get the latest value for the request ID specified

**Param**

* `uint256 _requestId` - the requestId to look up the value for

  **Return**

* `bool ifRetrieve` - true if it is able to retreive a value
* `uint256 value` - the value for the request ID
* `uint256 _timestampRetrieved` - the value's timestamp

**Example Usage**

```text
contract BtcPriceContract is UsingTellor {

  uint256 btcPrice;
  uint256 btcRequetId = 2;

  constructor(address payable _tellorAddress) UsingTellor(_tellorAddress) public {}

  function setBtcPrice() public {
    bool _didGet;
    uint _timestamp;
    uint _value;

    (_didGet, btcPrice, _timestamp) = getCurrentValue(btcRequetId);
  }
}
```

{% hint style="info" %}
**Line 4:** The`btcRequetId` is set local to`2`, the BTC/USD request ID

**Line 12:** The call to `getCurrentValue` returns the value into `btcPrice`
{% endhint %}

#### `getDataBefore`

Use the getDataBefore function to pull older data by specifying two parameters to look within. First, the time stamp which is where the function sets one side of the parameter \(most recent\) then the "offset" \(index of array\) which is the starting point to begin the value lookup. You will need to look up the array length, and once you choose an index, check that the index is before the timestamp specified. Lastly, set a “limit," which is how many values to check, starting from the offset and going beyond the chosen timestamp. You should generally keep this under 100 times, since it basically specifies how many times to loop through and look up.

![](../.gitbook/assets/getdatabefore.png)

**Param**

* `uint256 _requestId` - the requestId to look up the value for
* `uint256 _timestamp` - before which to search for first verified value
* `uint256 _limit` - a limit on the number of values to look at
* `uint256 _offset` - the number of values to go back before looking for data values

  **Return**

* `bool ifRetrieve` - true if it is able to retrieve a value
* `uint256 value` - the value for the request ID
* `uint256 _timestampRetrieved` - the value's timestamp

**Example Usage**

```text
contract BtcPrice1HourAgoContract is UsingTellor {

  uint256 btcPrice;
  uint256 btcRequetId = 2;

  constructor(address payable _tellorAddress) UsingTellor(_tellorAddress) public {}

  function getBtcPriceBefore1HourAgo() public view returns (uint256) {
    bool _didGet;
    uint _timestamp;
    uint _value;

    // Get the price that is older than an hour (looking back at most 60 values)
    (_didGet, _value, _timestamp) = getDataBefore(btcRequetId, now - 1 hours, 60, 0);

    if(_didGet){
      btcPrice = _value;
    }

    // NOTE: Optionally, if a value that is older than 1 hour was not found in the
    // last 60 data values, return the most recent value
    // (_didGet, _value, _timestamp) = getCurrentValue(btcRequetId);
    // return _value;
  }
}
```

{% hint style="info" %}
**Line 14:**  The `getDataBefore`will look for the most recent value after `now - 1 hours`, the `60` means it will look back 60 values, this is required to avoid an unbounded for loop in the function execution

**Line 16:** In this case, there may not be a value older than one hour ago in the last `60` data values, it's unlikely but, for good measure, you should check that you `_didGet` a value before updating it
{% endhint %}

