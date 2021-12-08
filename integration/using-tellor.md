# Using Tellor

## Updating Values

#### Checking Last Update

Before calling a function to update your values, you should first just check if it's already there! Tellor values, once onchain, are free for anyone to read. This means that if someone else just updated the value, you can use it free of charge!

To check when the value was last updated, you can run the following usingTellor function:

```solidity
 function getCurrentValue(bytes32 _queryId) public view returns (bool _ifRetrieve, bytes _value, uint256 _timestampRetrieved);
```

The last returned value is the timestamp last updated.

#### Adding a Tip

If the time the value was last updated is not sufficient, you can add a tip to your queryId in order to get it reported.

```solidity
 function tipQuery(bytes32 _queryId, uint256 _tip, bytes memory _queryData)
```

Tellor works by allowing any reporter to submit for any queryId. Each staked reporter just has to wait 12 hours after submitting in order to submit again. It stands to reason that, in order for a reporter to want to submit data, they have to be able to cover their gas costs and then earn a little more on top of that. When adding a tip, you should consider how much a reporter will have to pay in gas to report the data. You can get the current reward for a queryId with the following function, which returns the tip amount first, and then the time based reward:

```solidity
 function getCurrentReward(bytes32 _queryId) public view returns(uint256, uint256)
```

### Monitoring Values and Disputing

Once values are on-chain, we recommend you don't just take them right away. Tellor has a robust network of reporters and watchdogs that are valiantly checking and ensuring accuracy, but the best person to know if your data is correct is you.

You can monitor values and submit disputes by reading the value on-chain:

```solidity
 function getCurrentValue(bytes32 _queryId) public view returns (bool ifRetrieve, bytes value, uint256 _timestampRetrieved);

 function beginDispute(bytes32 _queryId, uint256 _timestamp) external
```

Dispute fees may be costly, but are returned (along with a stake reward) if the dispute is valid.

Once the dispute goes through, be sure to request your data again so the reporters have another chance to push through a valid price.

### Parsing Bytes

All Tellor oracle values are stored in `bytes` format. If you need your data in `uint256` format, you can parse `bytes` using a function like the one below:

```solidity
  function _sliceUint(bytes memory _b) public pure returns (uint256 _x) {
    uint256 _number = 0;
    for (uint256 _i = 0; _i < _b.length; _i++) {
      _number = _number * 2**8;
      _number = _number + uint8(_b[_i]);
    }
    return _number;
  }
```

If you need data parsed in a different way, see [this article](https://www.dhondt.tech/blog/2019/1/Parse-bytes-argument-in-Solidity.html) or reach out to the Tellor team for guidance.

#### Automating Jobs

To automate adding a tip on a certain query ID by time or volatility, as well as scheduling other Tellor related tasks, we recommend (and use) [Buidlhub](https://www.buidlhub.com).
