# Creating a New Query Type

To add a new data type to Tellor, you'll just need to define a new [queryType](https://github.com/tellor-io/dataSpecs) . This is how you form a question so that Tellor reporters know exactly what data is being requested. You'll need to determine three things: a unique queryType _name_, _inputs_, and _outputs_. So let's say you want a query for getting the price of any asset in any currency. In human-readable form, your question could look like this:

_What is the price of   `asset`   in   `currency`  ?_

You might formally define your query like this:

**Name**: `SpotPrice`

**Inputs**:&#x20;

1\. _asset_ (string): Asset ID (e.g. btc)

2\. _currency_ (string): Selected currency (e.g. usd)

**Outputs**:

1\. _price_ (uint256)

&#x20;  \- `abi_type`: ufixed256x18 (18 decimals of precision)

&#x20;  \- `packed`: false

Once Tellor reporters are submitting your new queryType on chain, you can retrieve your desired data with the help of [UsingTellor](https://github.com/tellor-io/usingtellor), which is a helper contract that provides various Tellor data getters. You'll first put your question in `queryData` format, which means encoding your queryType name and arguments into bytes (see below). You'll then need to get a `queryId`, which is the bytes32 unique identifier for each Tellor data feed. The `queryId` is defined as the keccak256 hash of `queryData`. Once you know the `queryId` you'll be able to retrieve your data.

In Solidity, your contract can get data like this:

```solidity
contract ExampleContract is UsingTellor {

    // _tellorAddress is the address of the Tellor oracle
    constructor(address payable _tellorAddress) UsingTellor(_tellorAddress) {}

    function getSpotPrice(string memory _asset, string memory _currency) external view returns(bytes memory) {
      bytes memory _queryData = abi.encode("SpotPrice", abi.encode(_asset, _currency));
      bytes32 _queryId = keccak256(_queryData);
      (bool ifRetrieve, bytes memory _value, ) =
          getCurrentValue(_queryId);
      if (!ifRetrieve) return "0x";
      return _value;
    }
}
```

If you input `btc` and `usd`, respectively, the `queryData` would be&#x20;

`0x00000000000000000000000000000000000000000000000000000000000000400000000000000000000000000000000000000000000000000000000000000080000000000000000000000000000000000000000000000000000000000000000953706f745072696365000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000c0000000000000000000000000000000000000000000000000000000000000004000000000000000000000000000000000000000000000000000000000000000800000000000000000000000000000000000000000000000000000000000000003627463000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000037573640000000000000000000000000000000000000000000000000000000000`

and the `queryId` would be&#x20;

`0xa6f013ee236804827b77696d350e9f0ac3e879328f2a3021d473a0b778ad78ac`

Feel free to start building a query now and integrating it into your project. You can use the [Query Builder](https://queryidbuilder.herokuapp.com) app for help forming your query. When you reach the later stages of building your project, add an issue to Tellor's [dataSpecs](https://github.com/tellor-io/dataSpecs/issues) repository so that data reporters know how to fulfill your query. Feel free to reach out to the Tellor team for assistance, and happy building!

\


\


\


\
