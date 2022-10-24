# Getting Paid

The payments for Tellor feeds are not held in the main tellor contract. Technically you can pay for Tellor feeds however you want (off-chain, recurring, hand shake agreements, etc.), however the trustless way to do this on-chain is to use the [Autopay contract.](https://github.com/tellor-io/autoPay)

The autopay contract allows parties to schedule and fund recurring data feeds or submit one-time tips to Tellor queryID's.&#x20;

{% hint style="info" %}
[For information on how to fund a queryID once or as a feed.](https://app.gitbook.com/s/tcQlo49FAqTaOimNOz0X/getting-data/funding-a-feed)
{% endhint %}

For most Tellor queryID's, the Tellor token on the network will be the tipped token.

There is a 12 hour waiting period after reporting data before tips can be claimed. This helps ensure that, if a value gets disputed, another reporter will be incentivized to submit the data and the user can still retrieve their requested data. Also note that tips must be claimed within 3 months of the original data submission.

### One time tips

**Finding** - Autopay contracts will emit an event:

```solidity
event TipAdded(bytes32 _queryId, uint256 _amount, bytes _queryData, address _tipper);
```

To see the current tip for any queryId, check:

```solidity
/**
 * @dev Getter function to current oneTime tip by queryId
 * @param _queryId id of reported data
 * @return amount of tip
 */
function getCurrentTip(bytes32 _queryId)
    external
    view
    returns (uint256)
{
```

**Getting Payment** - To get the payment for a one time tip, run:

```solidity
/**
 * @dev Function to claim singular tip
 * @param _queryId id of reported data
 * @param _timestamps ID of timestamps you reported for
 */
function claimOneTimeTip(
    bytes32 _queryId,
    uint256[] calldata _timestamps
) external {
```

Note the timestamp array is so you can submit for many one time tips and just claim all of those tips at once.

### Recurring data feeds

**Finding** - When a new feed is funded, the following event will emit:

```solidity
event DataFeedFunded(bytes32 _queryId, bytes32 _feedId, uint256 _amount, address _feedFunder);
```

To see all data feeds for a given queryID, check:

```solidity
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

```solidity
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

{% hint style="info" %}
The \_feedId is simply the keccak256 hash of the variables defined in setupFeed:

```solidity
    bytes32 _feedId = keccak256(
        abi.encode(_queryId, _reward, _startTime, _interval, _window, _priceThreshold)
    );
```
{% endhint %}

