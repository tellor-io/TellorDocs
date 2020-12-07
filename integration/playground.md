---
description: >-
  This page is designed to give you a quick overview of using Tellor to get data
  into your smart contracts.
---

# Tellor Playground

## TL:DR

Tellor Playground aims to help anyone building on Tellor quickly test and implement ideas. It's available on all testnets at the following addresses:

Rinkeby: [`0x20374E579832859f180536A69093A126Db1c8aE9`](https://rinkeby.etherscan.io/address/0x20374E579832859f180536A69093A126Db1c8aE9#code)

Kovan: [`0x20374E579832859f180536A69093A126Db1c8aE9`](https://kovan.etherscan.io/address/0x20374E579832859f180536A69093A126Db1c8aE9#code)

Ropsten: [`0x20374E579832859f180536A69093A126Db1c8aE9`](https://ropsten.etherscan.io/address/0x20374E579832859f180536A69093A126Db1c8aE9#code)

Goerli: [`0x20374E579832859f180536A69093A126Db1c8aE9`](https://goerli.etherscan.io/address/0x20374E579832859f180536A69093A126Db1c8aE9#code)

## Why use Tellor Playground?

The [Tellor Core](https://github.com/tellor-io/TellorCore) repository is a large project that holds all the on-chain logic of the system, but a lot of the code there is aimed at dealing with stakers, miners, disputes, etc. which most projects that want to ask and read Tellor values don't really need to worry about.

The Playground is a simplified \(and not a real oracle\) Tellor, containing only the small bits that third-party developer projects integrating need to worry about: getting data, adding tips, reading events and so forth.

### Why not use the real Tellor?

There are a few reasons why using the test version of the real system makes sense. The first one being that it is identical to the mainnet version, where only 50 data points are available for reading. You can easily get the value of USD or BTC, but if your project needs to read a value from an exotic token, it might not be available.

To include a value in the Rinkeby version, it would first need to be created at [Tellor Improvement Proposal\(TIPs\)](https://github.com/tellor-io/TIPs), which will be analyzed by the community and if there's no opposition, it'll go for implementation and then it'll be available on testnet. If you're testing an idea or building a hackathon project, it might be overkill to go through all of that and it's far easier to make use of Tellor Playground.

## How to use

### Reading values

If your smart contract needs to read Tellor values, you might want to use the helper [usingTellor](https://github.com/tellor-io/usingtellor), which already provides a few helpful functions to fetch data.

The first step is to inherit the UsingTellor contract, passing the TellorPlayground address as a constructor argument:

Here's an example

```text
contract BtcPriceContract is UsingTellor {

  //This Contract now have access to all functions on UsingTellor

  uint256 btcPrice;
  uint256 btcRequetId = 2;

  constructor(address payable _tellorAddress) UsingTellor(_tellorAddress) public {}

  ...
}
```

### Setting values in the Playground

To be able to properly read a value from playground, you'll need to first set the value yourself, since it does not rely on miners.

To do that, you can choose an arbitrary requestId, which is an `uint256`, and call the function `submitValue` with any value you wish. This will add a data point to the Playground and save the timestamp which was submitted. Your contract can now easily read Tellor values.

## Available Functions

Here are all the functions available in Tellor Playground:

```text
   /**
    * @dev A mock function to submit a value to be read withoun miners needed
    * @param _requestId The tellorId to associate the value to
    * @param _value the value for the requestId
    */
    function submitValue(uint256 _requestId,uint256 _value) external;

    /**
    * @dev A mock function to create a dispute
    * @param _requestId The tellorId to be disputed
    * @param _timestamp the timestamp that indentifies for the value
    */
    function disputeValue(uint256 _requestId, uint256 _timestamp) external;

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
    * @dev Counts the number of values that have been submited for the request
    * @param _requestId the requestId to look up
    * @return uint count of the number of values received for the requestId
    */
    function getNewValueCountbyRequestId(uint256 _requestId) public view returns(uint);

    /**
    * @dev Gets the timestamp for the value based on their index
    * @param _requestId is the requestId to look up
    * @param index is the value index to look up
    * @return uint timestamp
    */
    function getTimestampbyRequestIDandIndex(uint256 _requestId, uint256 index) public view returns(uint256);

    /**
    * @dev Adds a tip to a given request Id.
    * @param _requestId is the requestId to look up
    * @param _amount is the amount of tips
    */
    function addTip(uint256 _requestId, uint256 _amount) external;
```

Tellor Playground is also an ERC20 token, and if you want to add tips to your request, you might need to get some test tokens. For that there's an available function:

```text
     /**
     * @dev Public function to mint tokens for the passed address
     * @param user The address which will own the tokens
     *
     */
    function faucet(address user) external;
```

