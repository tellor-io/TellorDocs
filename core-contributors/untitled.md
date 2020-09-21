# Deploying

### Contracts Description

* **Tellor.sol** -- is the Tellor oracle contract and it allows miners to submit the proof of work, requestId, and value, sorts the values, pays the miners, allows the data users to request data and "tip" the miners to incentivize them to provide values, allows the users to retrieve and dispute the values.
  * **Tellor.sol** --contains all the functions
    * **TellorDispute.sol** --contains the dispute functions' logic for the functions in Tellor.sol
    * **TellorLibrary.sol** --contains the logic for the functions in Tellor.sol relating to requesting data and submitting mined values.
    * **TellorStake.sol** --contains the staking functions' logic for the functions in Tellor.sol
    * **TellorStorage.sol** --contains the storage variables used in Tellor.sol
    * **TellorTransfer.sol** --contains the transfer and ERC20 functions' logic for the functions in Tellor.sol
  * **TellorMaster.sol** -- contains the delegate calls to allow Tellor.sol to write to the TellorGetters.sol. TellorMaster is TellorGetters.sol
    * **TellorGetters.sol** -- stores all the Tellor.sol variables
    * **TellorGettersLibrary.sol** --contains the logic for the functions in TellorGetters.sol

### Scripts Description

* **01\_DeployTellor.js** -- deploys and connects Tellor.sol and TellorMaster.sol

### Deploy Tellor

Tellor can be deployed using the 01\_DeployTellor.js script and folowing the [Instructions for quick start with Truffle Deployment](https://github.com/tellor-io/TellorDocumentation/blob/master/docs/DevDocumentation.md#Quick-Deployment) . However, the process is documented below for deploying through any environment.

The following documentation is noted for acting as the operator. Specific contract details are laid out for ease of use regardless of dev environment.

**Step 1: Operator - Deploy Tellor.sol**  
The first deployed Tellor.sol.

```text
Tellor();
TellorMaster(Tellor.address); //where the tellor.address is the address of the deployed Tellor() above.
```

### Instructions for quick start with Truffle Deployment

Follow the steps below to launch the Oracle contracts using Truffle.

* Open two terminals.
* On one terminal run: Clone the repo, cd into it, and then run: $ npm install $ truffle compile $ truffle migrate $ truffle exec scripts/01\_DeployTellor.js

#### Testing through Truffle

* On the second termial run:

```text
   $ ganache-cli -m "nick lucian brenda kevin sam fiscal patch fly damp ocean produce wish"
```

* On the first terminal run:

```text
    $   truffle test
```

* And wait for the message 'START MINING RIG!!'
* Kick off the python miner file [./miner/testMinerB.py](https://github.com/tellor-io/TellorCore/tree/master/miner/testMinerB.py).

Production and test python miners are available under the miner subdirectory [here](https://github.com/tellor-io/TellorCore/tree/master/miner). You will need to get at least 5 miners running.

Step by step instructions on setting up a Tellor Oracle without truffle are available here: [Detailed documentation for self setup](https://tellor.readthedocs.io/en/latest/DevDocumentation/)

