---
description: Listening for tips and checking for recurring payments.
---

# Getting Paid

The payments for tellor feeds are not held in the main tellor contract.  Technically you can pay for Tellor feeds however you want (off-chain, recurring, hand shake agreements, etc.), however the trustless way to do this on-chain is to use the [Autopay contract.](https://github.com/tellor-io/autoPay)&#x20;

The autopay contract allows parties to fund Tellor data feeds or submit one-time tips to Tellor queryID's.  For information on how to fund a queryID once or as a feed, [check out the docs. ](../integration/requesting-paying-for-data.md)

For most Tellor queryID's, the tellor token on the network will be the tipped token.&#x20;

#### One time tips

**Finding** - Autopay contracts will emit an event:

```
event TipAdded(address _token, bytes32 _queryId, uint256 _amount, bytes _queryData);
```

To see the current tip for any queryId, check:



```
/**
 * @dev Getter function to current oneTime tip by queryId
 * @param _queryId id of reported data
 * @param _token address of tipped token
 * @return amount of tip
 */
function getCurrentTip(bytes32 _queryId, address _token)
    external
    view
    returns (uint256)
{
```

**Getting Payment** - To get the payment for a one time tip, run:&#x20;

```
/**
 * @dev Function to claim singular tip
 * @param _token address of token tipped
 * @param _queryId id of reported data
 * @param _timestamps ID of timestamps you reported for
 */
function claimOneTimeTip(
    address _token,
    bytes32 _queryId,
    uint256[] calldata _timestamps
) external {
```

Note the timestamp array is so you can submit for many one time tips and just claim all of those tips at once. &#x20;

#### Recurring data feeds

**Finding** - When a new feed is funded, the following event will emit:

```
event DataFeedFunded(bytes32 _queryId, bytes32 _feedId, uint256 _amount);

```

To see all data feeds for a given queryID, check:

```
/**
 * @dev Getter function to read current data feeds
 * @param _queryId id of reported data
 * @return feedIds array for queryId
 */
function getCurrentFeeds(bytes32 _queryId)
    external
    view
    returns (bytes32[] memory)
{
```

Getting Payment - to submit for payments from a data feed, run:

```
/**
 * @dev Internal function which allows Tellor reporters to claim their autopay tips
 * @param _feedId of dataFeed
 * @param _queryId id of reported data
 * @param _timestamp timestamp of reported data eligible for reward
 * @return uint256 reward amount
 */
function _claimTip(
    bytes32 _feedId,
    bytes32 _queryId,
    uint256 _timestamp
) 
```

\*Note- The \_feedId is simply the keccak256 has of the variables defined in setupFeed:&#x20;

```
    bytes32 _feedId = keccak256(
        abi.encode(_queryId, _token, _reward, _startTime, _interval, _window)
    );
```
