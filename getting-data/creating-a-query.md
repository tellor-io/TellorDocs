# Creating a Query

When a user requests data using `tipQuery` and when a reporter submits data using `submitValue`, they have to input both the `queryId` and `queryData`. The `queryData` tells reporters how to fulfill the data query, while also informing voters how to verify the data in a dispute. The `queryId` is defined as the keccak256 hash of the `queryData` field.

In order to query the Tellor oracle you'll need to first generate `queryData` and its hash, the `queryId`.&#x20;

### Getting a Query ID and Query Data

Use the tools below to generate a `queryId` and `queryData:`

{% embed url="https://queryidbuilder.herokuapp.com/spotprice" %}

{% embed url="https://www.youtube.com/watch?index=2&list=PLuJHbmh0kCXVPHDA2Q3J3TfatBRGrOsm-&v=thjXi7FGLpU" %}

{% hint style="info" %}
If the [existing Query Types](https://github.com/tellor-io/dataSpecs/tree/main/types) don't fit your needs you'll need to define a new one.
{% endhint %}

## Creating a new Query Type

To create a new Query Type, or specification, for custom data you need from Tellor oracles, there's two options:

* Make an issue like [this](https://github.com/tellor-io/dataSpecs/issues/25) and the Tellor team will help with the next steps.
* Fork this repository and make a pull request for a new Query type in `./types` using [this template](https://github.com/tellor-io/dataSpecs/blob/main/types/\_NewQueryTypeTemplate.md).

To add a new data type to Tellor, you'll just need to define a new [queryType](https://github.com/tellor-io/dataSpecs) . This is how you form a question so that Tellor reporters know exactly what data is being requested. You'll need to determine three things: a unique queryType _name_, _inputs_, and _outputs_. So let's say you want a query for getting the price of any asset in any currency. In human-readable form, your question could look like this:

_What is the price of `asset` in `currency` ?_

You might formally define your query like this:

**Name**: `SpotPrice`

**Inputs**:

1\. _asset_ (string): Asset ID (e.g. btc)

2\. _currency_ (string): Selected currency (e.g. usd)

**Outputs**:

1\. _price_ (uint256)

\- `abi_type`: ufixed256x18 (18 decimals of precision)

\- `packed`: false

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

### Example QueryData and QueryID

If you input `btc` and `usd`, respectively, the `queryData` would be:

> `0x00000000000000000000000000000000000000000000000000000000000000400000000000000000000000000000000000000000000000000000000000000080000000000000000000000000000000000000000000000000000000000000000953706f745072696365000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000c0000000000000000000000000000000000000000000000000000000000000004000000000000000000000000000000000000000000000000000000000000000800000000000000000000000000000000000000000000000000000000000000003627463000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000037573640000000000000000000000000000000000000000000000000000000000`

and the `queryId` would be

> `0xa6f013ee236804827b77696d350e9f0ac3e879328f2a3021d473a0b778ad78ac`

{% hint style="success" %}
Feel free to start building a query now and integrating it into your project. When you reach the later stages of building your project, add an issue to Tellor's [dataSpecs](https://github.com/tellor-io/dataSpecs/issues) repository so that data reporters know how to fulfill your query. Feel free to reach out to the Tellor team for assistance, and happy building!
{% endhint %}
