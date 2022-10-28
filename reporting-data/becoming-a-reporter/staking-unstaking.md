# Staking/Unstaking

## Staking

To stake funds in the Tellor contract, parties need to run one function.

```solidity
/**
 * @dev Allows a reporter to submit stake
 * @param _amount amount of tokens to stake
 */
function depositStake(uint256 _amount) external;
```

\*Note that the approve function needs to be run on the token before staking.

You can stake multiple times with one address. The way this works is that if the stake amount is 10 TRB and you stake 2 times (20 TRB), the reporterLock (time allowed between reports) is cut in half (or more if you deposit more).

## Unstaking

Unstaking is a process that requires two functions, one to request a withdraw and then another (allowed to be run one week later) to actually pull out the funds. The reason for this is that reporters are not allowed to report bad data and then run away.

Requesting a withdraw:

```solidity
/**
 * @dev Allows a reporter to request to withdraw their stake
 * @param _amount amount of staked tokens requesting to withdraw
 */
function requestStakingWithdraw(uint256 _amount) external;
```

and then to unstake:

```solidity
/**
 * @dev Withdraws a reporter's stake
 */
function withdrawStake() external;
```
