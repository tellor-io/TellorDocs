# Testnet

{% hint style="info" %}
### Need testnet TRB?

* [How to get Testnet TRB](https://docs.tellor.io/tellor/the-basics/readme#need-testnet-tokens-trb)
{% endhint %}

As seen in the [local testing setup](localtesting.md) an address must be passed into the constructor.  With local testing it was the playground address, but for testnets you'll need to use the Tellor oracle address corresponding to the testnet of your choice.  For those please visit our [Contracts Reference](../the-basics/contracts-reference.md) page.

#### reference example:

```solidity
pragma solidity >=0.8.0;

import "usingtellor/contracts/UsingTellor.sol";

contract MyContract is UsingTellor {

  constructor(address payable _tellorAddress) UsingTellor(_tellorAddress) {

  }

  // ...

}
```

Unlike local testing and using the Tellor playground, where you simply mimic the data submitting yourself, testnet is a good place to simulate production use of Tellor.   This requires the user to specify the data they want and incentivize Tellor's network of reporters to fetch it.  You can even [run your own reporter](../reporting-data/becoming-a-reporter.md) should you choose so. &#x20;

Next Steps:

* Create Query
* Setting up a reporter (optional)
* Incentivize reporting (funding a feed)
