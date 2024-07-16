# Becoming a Reporter

## Telliot Setup and Usage

The Telliot CLI handles all the functionality of reporting data and customizing the how you report.

{% hint style="success" %}
Follow the installation and setup instructions in the [Telliot Feeds Documentation. ](https://tellor-io.github.io/telliot-feeds/)
{% endhint %}

## Main Functions of Reporting

### Staking/Unstaking

Reporting data requires a staked reporter to run the [`submitValue` function](../getting-data/tellor-functions.md):

```solidity
/**
 * @dev Allows a reporter to submit a value to the oracle
 * @param _queryId is ID of the specific data feed. Equals keccak256(_queryData)
 * @param _value is the value the user submits to the oracle
 * @param _nonce is the current value count for the query id
 * @param _queryData is the data used to fulfill the data query
 */
function submitValue(
    bytes32 _queryId,
    bytes calldata _value,
    uint256 _nonce,
    bytes memory _queryData
) external {
```

#### Stake Amount:

To ensure that oracle data is always secured by a minimum amount, the stake amount is a function of the price of TRB, the stake amount dollar target, and the minimum stake amount:

`stakeAmount = maxUSD(stakeAmountDollarTarget, minStakeAmount)`

The stake amounts will vary from chain to chain, but as an example, Ethereum's mainnet stakeAmount is as follows:

`stakeAmount = maxUSD($1500, 100 TRB)`

> * whenever the price of TRB is greater than $15, the stakeAmount is always 100 TRB
> * whenever the price of TRB is less than $15, the stakeAmount is stakeAmountDollarTarget/priceOfTRB

The stake amount only changes when someone calls the function [updateStakeAmount](https://github.com/tellor-io/tellorFlex/blob/3b3820f2111ec2813cb51455ef68cf0955c51674/contracts/TellorFlex.sol#L351), which can be called by anyone, and depends on the 12+ hour old reported price of TRB.

#### Notes:

Once a value is submitted, the reporter is then locked from submitting again for the reporterLock time period (usually 12 hours) divided by the number of full stakes. If the stake amount is 10 TRB and a reporter has 60 TRB staked, for example, that reporter can submit once every two hours.

For all reported values, the `_queryId` must be the keccak256 hash of the `_queryData`. For information on how to get the queryId or how to parse the `_queryData`, see the [Creating a Query](https://app.gitbook.com/s/tcQlo49FAqTaOimNOz0X/getting-data/creating-a-query) section.

The `_nonce` can be either correct or `0` for a valid report. The nonce represents the number of submissions for a given query. The purpose of the `_nonce` is to prevent two parties from submitting at the same time for the same ID and wasting gas with no reward.

### Submitting Values

Reporting data requires a staked reporter to run the [`submitValue` function](../getting-data/tellor-functions.md):

```solidity
/**
 * @dev Allows a reporter to submit a value to the oracle
 * @param _queryId is ID of the specific data feed. Equals keccak256(_queryData)
 * @param _value is the value the user submits to the oracle
 * @param _nonce is the current value count for the query id
 * @param _queryData is the data used to fulfill the data query
 */
function submitValue(
    bytes32 _queryId,
    bytes calldata _value,
    uint256 _nonce,
    bytes memory _queryData
) external {
```
