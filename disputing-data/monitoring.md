# Monitoring

Every time a new value is submitted to the Tellor contract, the following event is emitted:

```solidity
event NewReport(
    bytes32 _queryId,
    uint256 _time,
    bytes _value,
    uint256 _nonce,
    bytes _queryData,
    address _reporter
);
```

The value is the requested data, with the \_queryData being the description of the data.

To dispute a value, go to the governance contract and run:

```solidity
/**
 * @dev Helps initialize a dispute by assigning it a disputeId
 * @param _queryId being disputed
 * @param _timestamp being disputed
 */
function beginDispute(bytes32 _queryId, uint256 _timestamp) external {
```

Note that before beginning a dispute, the proper amount of TRB tokens must be approved to the contract to cover the disputeFee. The disputeFee is a constant public variable in the contracts, however doubles with each voting round or with each open dispute on a given ID.

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
    returns (uint256)
{
```

To open a dispute on a previously dispute (challenge the result of the vote), simply run beginDispute() with the same parameters (same timestamp/ queryID). Note that the disputeFee will need to be doubled from the previous round.
