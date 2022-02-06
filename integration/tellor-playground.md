---
description: >-
  This page is designed to give you a quick overview of using Tellor to get data
  into your smart contracts.
---

# Tellor Playground

## TL:DR

[Tellor Playground](https://github.com/tellor-io/TellorPlayground) aims to help anyone building on Tellor to quickly test and implement ideas. It's available on various testnets at these addresses:

Rinkeby: [`0x3477EB82263dabb59AC0CAcE47a61292f28A2eA7`](https://rinkeby.etherscan.io/address/0x3477EB82263dabb59AC0CAcE47a61292f28A2eA7#code)

Kovan: [`0x3477EB82263dabb59AC0CAcE47a61292f28A2eA7`](https://kovan.etherscan.io/address/0x3477EB82263dabb59AC0CAcE47a61292f28A2eA7#code)

Ropsten: [`0x3477EB82263dabb59AC0CAcE47a61292f28A2eA7`](https://ropsten.etherscan.io/address/0x3477EB82263dabb59AC0CAcE47a61292f28A2eA7#code)

Goerli: [`0x3477EB82263dabb59AC0CAcE47a61292f28A2eA7`](https://goerli.etherscan.io/address/0x3477EB82263dabb59AC0CAcE47a61292f28A2eA7#code)

BSC Testnet: [`0x3477EB82263dabb59AC0CAcE47a61292f28A2eA7`](https://testnet.bscscan.com/address/0x3477EB82263dabb59AC0CAcE47a61292f28A2eA7#code)

Polygon Mumbai Testnet: [`0x3477EB82263dabb59AC0CAcE47a61292f28A2eA7`](https://explorer-mumbai.maticvigil.com/address/0x3477EB82263dabb59AC0CAcE47a61292f28A2eA7/contracts)

Arbitrum Testnet: [`0x3477EB82263dabb59AC0CAcE47a61292f28A2eA7`](https://rinkeby-explorer.arbitrum.io/address/0x3477EB82263dabb59AC0CAcE47a61292f28A2eA7)

### Why use Tellor Playground

The [TellorX](https://github.com/tellor-io/tellorX) repository is a large project that holds all the on-chain logic of the system, but a lot of the code there is aimed at dealing with stakers, reporters, and disputes, among other stuff, which most projects that want to request and read tellor values don't really need to worry about.

The Playground is a simplified (and not a real oracle) Tellor, containing only the small bits that third party developers integrating need to worry about: getting data, adding tips, reading events and so forth.

#### Why not use the real Tellor

There are a few reasons not to use even the testnet version of the real system, the first one being that it is identical to the mainnet version, where there are only 50 datapoints available for reading. You can easily get the value of USD or BTC, but if your project needs to read a value from an exotic token, it might not be available.

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

To do that, you can choose some arbitrary `queryData`, which is a `bytes` value, and then take the keccak256 hash of the `queryData` to get the `queryId`. Then call `submitValue` with any value you wish, which will add a data point to the Playground. Your contract can now easily read Tellor values.

### Available Functions

Here are all the functions available in Tellor Playground:

```solidity
    /**
     * @dev A mock function to submit a value to be read without miners needed
     * @param _queryId The tellorId to associate the value to
     * @param _value the value for the queryId
     * @param _nonce the current value count for the query id
     * @param _queryData the data used by reporters to fulfill the data query
     */
    function submitValue(bytes32 _queryId, bytes calldata _value, uint256 _nonce, bytes memory _queryData) external;

    /**
     * @dev A mock function to create a dispute
     * @param _queryId The tellorId to be disputed
     * @param _timestamp the timestamp of the value to be disputed
     */
    function beginDispute(bytes32 _queryId, uint256 _timestamp) external;

    /**
     * @dev Retrieve bytes value from oracle based on queryId/timestamp
     * @param _queryId being retrieved
     * @param _timestamp to retrieve data/value from
     * @return bytes value for queryId/timestamp submitted
     */
    function retrieveData(bytes32 _queryId, uint256 _timestamp) public view returns (bytes memory);

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
     * @dev Adds a tip to a given query ID.
     * @param _queryId is the queryId to look up
     * @param _amount is the amount of tips
     * @param _queryData is the extra bytes data needed to fulfill the request
     */
    function tipQuery(bytes32 _queryId, uint256 _amount, bytes memory _queryData) external;
```

Tellor Playground is also an ERC20 token, and if you want to add tips to your request, you might need to get some test tokens. For that there's an available function:

```solidity
     /**
     * @dev Public function to mint tokens for the passed address
     * @param user The address which will own the tokens
     *
     */
    function faucet(address user) external;
```
