# Contracts

**TellorMaster.sol** -- contains the storage and a proxy contract to allow delegate calls to a specified Controller contract

**Controller.sol** -- defines functionality for changing contract addresses and minting and migrating tokens

* **Token.sol** -- handles TRB token functionality
* **Getters.sol** -- contains getters for retrieving values from the oracle contract
* **Transition.sol** -- contains functionality which allows a smooth transition from tellor3 to tellorX
* **TellorStaking.sol** -- handles logic for staking, unstaking, and slashing reporters

**Governance.sol** -- defines functionality for proposing and executing proposal votes and disputes

**Treasury.sol** -- handles logic for Tellor treasuries, or staking pools
