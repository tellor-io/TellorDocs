# Contracts

**TellorMaster.sol** -- contains the delegate calls to allow Tellor.sol to write to the TellorGetters.sol. TellorMaster is TellorGetters.sol

* **TellorGetters.sol** -- stores all the Tellor.sol variables
* **TellorGettersLibrary.sol** --contains the logic for the functions in TellorGetters.sol

**Tellor.sol** -- is the Tellor oracle contract and it allows miners to submit the proof of work, requestId, and value, sorts the values, pays the miners, allows the data users to request data and "tip" the miners to incentivize them to provide values, allows the users to retrieve and dispute the values.

* **TellorDispute.sol** --contains the dispute functions' logic for the functions in Tellor.sol
* **TellorLibrary.sol** --contains the logic for the functions in Tellor.sol relating to requesting data and submitting mined values.
* **TellorStake.sol** --contains the staking functions' logic for the functions in Tellor.sol
* **TellorStorage.sol** --contains the storage variables used in Tellor.sol
* **TellorTransfer.sol** --contains the transfer and ERC20 functions' logic for the functions in Tellor.sol

\*\*\*\*

\*\*\*\*



### 

