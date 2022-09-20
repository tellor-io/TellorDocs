---
description: >-
  Anyone staked reporter can place data on-chain regardless of whether it is
  requested or payed for.  If however you do not want to report your own data,
  you can request data using the Autopay contract.
---

# Requesting / Paying for Data

### Getting a Data ID

To check out our current supported data types and/or use our tool to make a new one, checkout our querybuilder:  [https://queryidbuilder.herokuapp.com/](https://queryidbuilder.herokuapp.com)&#x20;

### Funding a one time request

To tip a query ID for an instant report (whoever submits the value next gets the reward), you just need to run one function:&#x20;

```
/**
 * @dev Function to run a single tip
 * @param _queryId id of tipped data
 * @param _amount amount to tip
 * @param _queryData the data used by reporters to fulfill the query
*/
function tip(
    bytes32 _queryId,
    uint256 _amount,
    bytes calldata _queryData
) external 
```

be sure to approve the transfer of the token before you call the function: &#x20;
```
token.approve(address(autopay), _amount);
```
### Funding a recurring data feed

To fund a data feed, you will need to run two functions, one to set up the feed and the other to fund it.  If a fund is already set up with your specifications, you can simply call the function to fund it.&#x20;

To set up your data feed:

```
/**
 * @dev Initializes dataFeed parameters.
 * @param _token address of ERC20 token used for tipping
 * @param _queryId id of specific desired data feet
 * @param _reward tip amount per eligible data submission
 * @param _startTime timestamp of first autopay window
 * @param _interval amount of time between autopay windows
 * @param _window amount of time after each new interval when reports are eligible for tips
 * @param _priceThreshold amount price must change to automate update regardless of time (negated if 0, 100 = 1%)
 * @param _queryData the data used by reporters to fulfill the query
 */
function setupDataFeed(
    bytes32 _queryId,
    uint256 _reward,
    uint256 _startTime,
    uint256 _interval,
    uint256 _window,
    uint256 _priceThreshold,
    bytes calldata _queryData
) external {
```

As an example, if on Polygon you want to tip 1 TRB token each hour for the spot BTC price.  You need it every hour, starting tomorrow, and you need it updated within 5 minutes of the hour.

```
_queryId =0xa6f013ee236804827b77696d350e9f0ac3e879328f2a3021d473a0b778ad78ac (keccak256 of queryData)
_reward = 1000000000000000000 (1 TRB)
_startTime = 1647435600 (tomorrow start time (UNIX))
_interval = 3600 (seconds in hour)
_window = 300 (seconds in 5 minutes)
_priceThreshold = 0
_queryData = 0x00000000000000000000000000000000000000000000000000000000000000400000000000000000000000000000000000000000000000000000000000000080000000000000000000000000000000000000000000000000000000000000000953706f745072696365000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000c0000000000000000000000000000000000000000000000000000000000000004000000000000000000000000000000000000000000000000000000000000000800000000000000000000000000000000000000000000000000000000000000003627463000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000037573640000000000000000000000000000000000000000000000000000000000
//_queryData = abi.encode("SpotPrice",abi.encode("btc","usd"))
```

To fund the feed:

```
/**
 * @dev Allows dataFeed account to be filled with tokens
 * @param _feedId unique dataFeed Id for queryId
 * @param _queryId id of reported data associated with feed
 * @param _amount quantity of tokens to fund feed account
 */
function fundFeed(
    bytes32 _feedId,
    bytes32 _queryId,
    uint256 _amount
) external 
```

The \_feedId is simply the keccak256 has of the variables defined in setupFeed:&#x20;

```
    bytes32 _feedId = keccak256(
        abi.encode(
            _queryId,
            _reward,
            _startTime,
            _interval,
            _window,
            _priceThreshold,
        )
    );
```

The \_amount is the amount of the token you would want to fund it with.  For example, if you are tipping 1 TRB per hour, if you fund the feed with 24 TRB, it would pay out for the next 24 hours.&#x20;

Be sure to approve the token transfer before calling this function:&#x20;

```
token.approve(address(autopay), _amount);
```
