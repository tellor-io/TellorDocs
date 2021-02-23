# Contracts

**TellorMaster.sol** -- contains the storage and a proxy contract to allow delegate calls to a specified Tellor.sol

* **TellorGetters.sol** -- stores a series of getters for Tellor values Tellor.sol variables
* **Tellor.sol** --contains the logic for the functions in TellorGetters.sol

**Tellor.sol** -- is the Tellor oracle contract and it allows miners to submit the proof of work, requestId, and value, sorts the values, pays the miners, allows the data users to request data and "tip" the miners to incentivize them to provide values, allows the users to retrieve and dispute the values.

* **TellorStake.sol** --contains the staking and disputing functions' logic for the functions in Tellor.sol
* **TellorStorage.sol** --contains the storage variables used in Tellor.sol
* **TellorTransfer.sol** --contains the transfer and ERC20 functions' logic for the functions in Tellor.sol

\*\*\*\*

\*\*\*\*



### 

