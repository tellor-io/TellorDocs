---
description: >-
  These instructions walk you through running Tellor Core locally using Ganache.
  With this documentation, you can setup Tellor Core and mine Tellor Tributes
  locally.
---

# Set up Tellor Core on Ganache

## Overview

In order to run Tellor Core locally, you will need to: 1. Run a Ethereum blockchain using Ganache 2. Deploy the Tellor Core smart contracts using Truffle Suite 3. Make a Data Request 3. Run 5 Staked Tellor Miners and 1 Data Server The instructions below are provided details for each of these steps.

### Step 0: Install Operating System Dependencies <a id="step-0-install-operating-system-dependancies"></a>

You'll need to install:

* Ganache
* Truffle
* Node
* Node Package Manager \(npm\)
* Go

### Step 1: Run an Ethereum blockchain using Ganache <a id="step-1-run-an-ethereum-blockchain-using-ganache"></a>

Start in a terminal using the following command:

```text
ganache-cli -m "nick lucian brenda kevin sam fiscal patch fly damp ocean produce wish"
```

If started correctly, you should see the following Available Accounts are the same as those listed below:

```text
Ganache CLI v6.9.1 (ganache-core: 2.10.2)

Available Accounts
==================
(0) 0xe010aC6e0248790e08F42d5F697160DEDf97E024 (100 ETH)
(1) 0xcdd8FA31AF8475574B8909F135d510579a8087d3 (100 ETH)
(2) 0xb9dD5AfD86547Df817DA2d0Fb89334A6F8eDd891 (100 ETH)
(3) 0x230570cD052f40E14C14a81038c6f3aa685d712B (100 ETH)
(4) 0x3233afA02644CCd048587F8ba6e99b3C00A34DcC (100 ETH)
(5) 0xE037EC8EC9ec423826750853899394dE7F024fee (100 ETH)
(6) 0x5d4eD2cC2C46f4144EC45C39C5aF9B69C7CDa8E8 (100 ETH)
(7) 0xE7E5c22A8f366B4418a06Dab6438fbA3a7259ceA (100 ETH)
(8) 0x7290C7292864aCc2E7f9a069E34BC91e929e64Af (100 ETH)
(9) 0xe0d7BAE200F0994B11423E8BE8F386060bBdd808 (100 ETH)
```

#### About the 12-word Seed Phrase \(Mnemonic\) Used By Ganache <a id="about-the-12-word-seed-phrase-mnemonic-used-by-ganache"></a>

The mnemonic used here will properly generate addresses that conform with the 6 hard-coded initial staked miners used to bootstrap Tellor. You can view these addresses in the source code here in the [TellorStake init method](https://github.com/tellor-io/TellorCore/blob/23098d4cc0c717d9d121e26d24e0723db4914f34/contracts/libraries/TellorStake.sol#L24).

**If you choose to edit the mnemonic**, you will need to change the TellorCore source code. A note is included in the next step about how to do this. Since this is a local deployment of TellorCore, you can use this mnemonic to make things easier and avoid changing the TellorCore code. **Do not use this seed phrase on mainnet**.

#### About using Ganache GUI <a id="about-using-ganache-gui"></a>

You may use the Ganache GUI but you must start a new workspace using the mnemonic or you will need to change the staked miner address in the TellorCore code based on the note above.

To set the mnemonic in the Ganache GUI, start by clicking **New Workspace** the go under **Accounts & Keys** and _Enter the Mnemonic you wish to use_ before Saving and starting the workspace.

### Step 2: Deploy the TellorCore Smart Contract Using Truffle <a id="step-2-deploy-the-tellorcore-smart-contract-using-truffle"></a>

In another terminal, clone the TellorCore repository:

```text
git clone https://github.com/tellor-io/TellorCore.git
```

After cloning the contract, change the director into the contract and install the Node packages:

```text
cd TellorCore
npm install
```

Make a `.env` file. Even though we don't need any environment variables, this will prevent unwanted messages later:

```text
touch .env
```

Next, compile the smart contracts:

```text
truffle compile
```

The compilation is successful if you receive a message like:

```text
> Artifacts written to /path/to/TellorCore/build/contracts
> Compiled successfully using:
   - solc: XXXXX
```

and depending on your version of Solidity, you may see _warnings_ but these are OK as they are not errors.

After the compilation has run successfully, migrate the smart contracts to deploy them to the local Ethereum blockchain set up in Step 1.

```text
truffle migrate
```

The migration \(deployment\) is successful if you receive a message like:

```text
Summary
=======
> Total deployments:   17
> Final cost:          0.5289897 ETH
```

#### Finding the Tellor Contract Address <a id="finding-the-tellor-contract-address"></a>

You will need to review the output of the `truffle migrate` step and save the **TellorMaster contract address** for later use. You can find this by looking for the following in the output of the `migrate` step:

```text
Deploying 'TellorMaster'
------------------------
> transaction hash:    0x72ba3d8c299ad5bb6d31358bb7587c531d6639a3e55045d90f0bd5a6133c89fb
> Blocks: 0            Seconds: 0
> contract address:    0x7DdC408C0Cd13D3543156AE2bc5772C56E91AA0f
```

:star: The contract address above will be `0x7DdC408C0Cd13D3543156AE2bc5772C56E91AA0f` and you will need this when setting up the 5 staked miners in the next step. Your contract address may be different.

#### Understanding Initial Stake Miners <a id="understanding-initial-stake-miners"></a>

At this point, the Tellor Core smart contracts have been deployed to the Ethereum blockchain you are running locally with Ganache. As part of the deployment, 6 addresses were given 1000 Tellor Tributes \(TRB\). This is done to bootstrap the Tellor mining process. Although only 5 miners are required for mining, a 6th stake was minted and used for handling disputes that would arise from submitting bad data to the Tellor Oracle.

### Step 3: Making a Data Request <a id="step-3-making-a-data-request"></a>

Once the contract is started and before you start the stake miners, make a request so that the miners have something to work on when they start up. This can be done from the Truffle console:

```text
truffle console
```

Then in the console, run the commands:

```text
let oracle = await TellorMaster.deployed()
let oracleAddress = (web3.utils.toChecksumAddress(oracle.address))
let oracle2 = await new web3.eth.Contract(Tellor.abi, oracleAddress)
await web3.eth.sendTransaction({to: oracleAddress, from: accounts[0], gas: 4000000, data: oracle2.methods.requestData("GLD","GLD/USD",1000,0).encodeABI()})
```

This will create a transaction that requests data from the Tellor oracles and will ensure the miner have something to work on when you move to the next step.

You can use this code later to make additional requests. The configuration of the miners in Step 4 will have them automatically make requests so you don't need to keep running this command.

### Step 4: Run Telliot Miners <a id="step-4-run-5-staked-tellor-miners-and-1-data-server"></a>

See the Telliot setup and usage.

## Conclusion <a id="conclusion"></a>

At this point you should see your miners are submitting transactions and if you want to check that the network difficulty is rising, you can use Truffle's console again and run the following commands:

```text
let difficulty = await oracle.getUintVar("0xb12aff7664b16cb99339be399b863feecd64d14817be7e1f042f97e3f358e64e")
difficulty.toNumber()
```

