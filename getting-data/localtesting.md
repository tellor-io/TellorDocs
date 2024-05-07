# Local Testing

On this page we'll be showing how to test your Tellor integration using the Tellor Playground.

{% hint style="info" %}
Example: [test file](https://github.com/tellor-io/sampleUsingTellor/blob/master/test/testSampleTellor.js)

Video: [Local Testing Tutorial](https://www.youtube.com/watch?v=-n93QdRu9Ac)
{% endhint %}

### Tellor Playground

[Tellor Playground](https://github.com/tellor-io/TellorPlayground) is a simplified version of Tellor that allows developers to easily test and implement ideas without using the real system. The Playground contains only the core functions that developers need to worry about when building and testing, such as submitting and reading data. See the [reference page](https://docs.tellor.io/tellor/the-basics/contracts-reference) for deployed addresses on various test networks.

### Why use Tellor Playground?

Most projects that want to integrate Tellor only need to test functions for reading and requesting tellor data. The Playground is a simplified (and not a real oracle) Tellor, containing only the small bits that developers need to worry about when building and testing: submitting data, getting data, reading events and so forth.

### Why not use the real Tellor for testing?

There are a few reasons not to use even the testnet version of the real system, the first one being that it is identical to the mainnet version, where there are only so many data points available for reading. You can easily get the value of ETH or BTC, but if your project needs to read a value from an exotic token, it might not be available.

To include a value in the Goerli version, it would first need to be added to the reporter software client. Or a developer could report the value themselves, but they would have to acquire 100 Goerli test TRB, stake it, and then they would only be able to submit a value once every 12 hours. If you're testing an idea or building a hackathon project, it might be overkill to go through all of that and it's far easier to make use of Tellor Playground.

## Testing With Tellor

To read a value from Playground, you'll need to first set the value yourself, since it does not rely on reporters.

To do that, you can choose some arbitrary `queryData`, which is a `bytes` value, and then take the keccak256 hash of the `queryData` to get the `queryId`. For the `nonce`, you can always input a value of `0`. Then call `submitValue` with any value you wish, which will add a data point to the Playground. Your contract can now easily read Tellor values.

```solidity
function submitValue(
        bytes32 _queryId,
        bytes calldata _value,
        uint256 _nonce,
        bytes memory _queryData
) external;
```

### Using the Playground in Tests

##### Hardhat

To test your Tellor integration, you can easily deploy the Playground and submit values to it. If you have usingtellor installed, you can deploy the Playground in your hardhat test files like this:

```javascript
const {ethers} = require("hardhat");
const { abi, bytecode } = require("usingtellor/artifacts/contracts/TellorPlayground.sol/TellorPlayground.json")

...

const Factory = await ethers.getContractFactory(abi, bytecode);
tellor = await TellorPlayground.deploy();
```

Before you can submit data, you will need to generate queryData and queryId. This can be done with the following code:

```javascript
const abiCoder = new ethers.utils.AbiCoder();
let queryDataArgs = abiCoder.encode(["string", "string"], ["btc", "usd"]);
let queryData = abiCoder.encode(["string", "bytes"], ["SpotPrice", queryDataArgs]);
let queryId = ethers.utils.keccak256(queryData);
```

Once you have these values, you can submit a value to the playground:

```javascript
let value = BigInt(10000e18);
let valueBytes = abiCoder.encode(["uint256"], [value]);
await tellor.submitValue(queryId, valueBytes, 0, queryData);
```

Your contract can now read the value. If your contract uses a buffer time with `getDataBefore`, you will need to increase the block timestamp before your contract can read the data. You can do this as follows:

```javascript
await ethers.provider.send("evm_increaseTime", [1800]);
await ethers.provider.send("evm_mine");
```

Your contract can now read the reported value:

```javascript
await myContract.setBtcPrice();
let price = await myContract.btcPrice();
```

##### Foundry

To test your Tellor integration, you can easily deploy the Playground and submit values to it. If you have usingtellor installed, you can deploy the Playground in your foundry test files like this:

```javascript
import {TellorPlayground} from "usingtellor/TellorPlayground.sol";

...

TellorPlayground tellorPlayground = new TellorPlayground()
```

Before you can submit data, you will need to generate queryData and queryId. This can be done with the following code:

```javascript
bytes public queryData = abi.encode("SpotPrice", abi.encode("eth", "usd"));
bytes32 public queryId = keccak256(queryData);
```

Once you have these values, you can submit a value to the playground:

```javascript
uint256 mockValue = 2000e18;
tellorPlayground.submitValue(queryId, abi.encodePacked(mockValue), 0, queryData);
```

Your contract can now read the value. If your contract uses a buffer time with `getDataBefore`, you will need to increase the block timestamp before your contract can read the data. You can do this as follows:

```javascript
vm.warp(block.timestamp + 901 seconds);
```

Your contract can now read the reported value:

```javascript
myContract.setBtcPrice();
uint256 price = await myContract.btcPrice();
```

{% hint style="info" %}
For a full example of a test in either hardhat or foundry, see the [sampleUsingTellor project](https://github.com/tellor-io/sampleUsingTellor).
{% endhint %}

