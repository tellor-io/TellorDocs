# Staking / Unstaking

To stake funds in the Tellor contract, parties need to run one function. &#x20;

**On Ethereum:**

```
/**
 * @dev Allows a reporter to submit stake
 */
function depositStake() external {
```

**On any other network:**

```
/**
 * @dev Allows a reporter to submit stake
 * @param _amount amount of tokens to stake
 */
function depositStake(uint256 _amount) external {
```

\*Note that on Ethereum, the approve function does not need to be run on the token before staking, however it does on every other network for the staked asset (bridged TRB).&#x20;

For non-Ethereum Tellor, you can stake multiple times for one address.  The way this works is that if the stake amount is 10TRB and you stake 2 times (20 TRB), the reporterLock (time allowed between reports) is cut in half (or more if you deposit more).

\---------------------------------------------------

Unstaking is a process that requires two functions, one to request a withdraw and then another (allowed to be run one week later) to actually pull out the funds.  The reason for this is that reporters are not allowed to report bad data and then run away. &#x20;

**On Ethereum:**&#x20;

requesting a withdraw:

```
/**
 * @dev Allows a reporter to request to withdraw their stake
 */
function requestStakingWithdraw() external 
```

and unstaking:&#x20;

```
/**
 * @dev Withdraws a reporter's stake
 */
function withdrawStake() external {
```

**On any other network:**

requesting a withdraw:

```
/**
 * @dev Allows a reporter to request to withdraw their stake
 * @param _amount amount of staked tokens requesting to withdraw
 */
function requestStakingWithdraw(uint256 _amount) external
```

and then to unstake:

```
/**
 * @dev Withdraws a reporter's stake
 */
function withdrawStake() external {
```
