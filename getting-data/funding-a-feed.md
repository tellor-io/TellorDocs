# Funding a Feed

### Quickstart

1. Get your QueryID
2. Use our [fund-a-feed tool](https://tellor.io/fund-a-feed/) to specify your pair, and fund the request
3. Chill

### Funding a one time request

To tip a query ID for an instant report (whoever submits the value next gets the reward), you just need to run one function:

```solidity
/**
 * @dev Function to run a single tip
 * @param _queryId id of tipped data
 * @param _amount amount to tip
 * @param _queryData the data used by reporters to fulfill the query
*/
function tip(bytes32 _queryId, uint256 _amount, bytes calldata _queryData)

```

Be sure to approve the transfer of the token before you call the function.

### Funding a recurring data feed

To fund a data feed, you will need to call a function to set it up with your desired parameters and an initial amount. If a feed is already set up with your specifications, you can simply call the function to fund it.

To set up your data feed:

```solidity
/**
* @dev Initializes dataFeed parameters.
* @param _queryId unique identifier of desired data feed
* @param _reward tip amount per eligible data submission
* @param _startTime timestamp of first autopay window
* @param _interval amount of time between autopay windows
* @param _window amount of time after each new interval when reports are eligible for tips
* @param _priceThreshold amount price must change to automate update regardless of time (negated if 0, 100 = 1%)
* @param _rewardIncreasePerSecond amount reward increases per second within a window (0 for flat reward)
* @param _queryData the data used by reporters to fulfill the query
* @param _amount optional initial amount to fund it with
*/
function setupDataFeed(
    bytes32 _queryId,
    uint256 _reward,
    uint256 _startTime,
    uint256 _interval,
    uint256 _window,
    uint256 _priceThreshold,
    uint256 _rewardIncreasePerSecond,
    bytes calldata _queryData,
    uint256 _amount
) external returns (bytes32 _feedId)
```

As an example, you want the BTC spot price updated once per hour. You need it every hour, starting tomorrow, and you need it updated within 5 minutes of the hour. To account for gas cost variance, you want the reward to start at 1 TRB and increase by 0.01 TRB per second within the window until a report is submitted. You initially fund the feed with 100 TRB.

```solidity
_queryId =0xa6f013ee236804827b77696d350e9f0ac3e879328f2a3021d473a0b778ad78ac (keccak256 of queryData)
_reward = 1000000000000000000 (1 TRB)
_startTime = 1647435600 (tomorrow start time (UNIX))
_interval = 3600 (seconds in hour)
_window = 300 (seconds in 5 minutes)
_priceThreshold = 0
_rewardIncreasePerSecond = 10000000000000000 (0.01 TRB)
_queryData = 0x00000000000000000000000000000000000000000000000000000000000000400000000000000000000000000000000000000000000000000000000000000080000000000000000000000000000000000000000000000000000000000000000953706f745072696365000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000c0000000000000000000000000000000000000000000000000000000000000004000000000000000000000000000000000000000000000000000000000000000800000000000000000000000000000000000000000000000000000000000000003627463000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000037573640000000000000000000000000000000000000000000000000000000000
_amount = 100000000000000000000 (100 TRB)
// _queryData = abi.encode("SpotPrice",abi.encode("btc","usd"))
```

To fund the feed:

```solidity
/**
 * @dev Allows dataFeed account to be filled with tokens
 * @param _feedId unique feed identifier
 * @param _queryId identifier of reported data type associated with feed
 * @param _amount quantity of tokens to fund feed
 */
function fundFeed(bytes32 _feedId, bytes32 _queryId, uint256 _amount)

```

The `_feedId` is simply the keccak256 has of the variables defined in `setupFeed`:

```solidity
bytes32 _feedId = keccak256(
        abi.encode(
            _queryId,
            _reward,
            _startTime,
            _interval,
            _window,
            _priceThreshold,
            _rewardIncreasePerSecond
        )
    );
```

The `_amount` is the amount of the token you would want to fund it with. For example, if you are tipping 1 TRB per hour and you fund the feed with 24 TRB, it would pay out for the next 24 hours.

Be sure to approve the token transfer before calling this function.