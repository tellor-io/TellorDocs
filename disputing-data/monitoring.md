# Monitoring

Every time a new value is submitted to the oracle contract, the following event is emitted:

```solidity
event NewReport(
    bytes32 indexed _queryId,
    uint256 indexed _time,
    bytes _value,
    uint256 _nonce,
    bytes _queryData,
    address indexed _reporter
);
```

To dispute a value, go to the governance contract and run:
```solidity
/**
 * @dev Helps initialize a dispute by assigning it a disputeId
 * @param _queryId being disputed
 * @param _timestamp being disputed
 */
function beginDispute(bytes32 _queryId, uint256 _timestamp) external;
```

Note that before beginning a dispute, the proper amount of TRB tokens must be approved to the contract to cover the disputeFee. The disputeFee starts at 1/10th of the stakeAmount, and doubles with each voting round or with each open dispute on a given queryId. The dispute fee is capped at the stakeAmount.

To get the current dispute fee:
```solidity
/**
 * @dev Get the latest dispute fee
 */
function getDisputeFee() public view returns (uint256);
```

To get the number of openDisputes on an ID:
```solidity
/**
 * @dev Returns the number of open disputes for a specific query ID
 * @param _queryId is the ID of a specific data feed
 * @return uint256 of the number of open disputes for the query ID
 */
function getOpenDisputesOnId(bytes32 _queryId)
    external
    view
    returns (uint256);
```

To open a dispute on a previously disputed value (challenge the result of the vote), simply run `beginDispute` with the same parameters (same timestamp/queryID). Note that the disputeFee will need to be doubled from the previous round, and the new round must begin after the previous vote is tallied, but before it is executed (24 hour window).

To determine whether a given value has already been disputed:
```solidity
/**
 * @dev Returns whether a given value is disputed
 * @param _queryId unique ID of the data feed
 * @param _timestamp timestamp of the value
 * @return bool whether the value is disputed
*/
function isInDispute(bytes32 _queryId, uint256 _timestamp);
    public
    view
    returns (bool);
```