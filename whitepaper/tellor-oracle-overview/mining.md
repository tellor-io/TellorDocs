---
description: Miners are the data providers of Tellor
---

# Mining

Data submission is done through a competitive process where miners respond to PoW challenges and the winners get to submit data to Tellor’s on-chain data feed.   PoW provides an excellent source of sybil resistant randomness to Tellor’s smart contracts as well as provides an ideal system for token distribution.   

### Staking

Miners have to stake 1000 Tributes to be able to mine. Staking allows for economic penalties to miners submitting incorrect values.  If a miner wants to withdraw his stake, he can request a withdrawal at any point.  The miner’s tokens are then locked for 7 days in order to wait for potential disputes, at which point he can unlock his tokens for transfer.  

### Hash Function

Tellor uses a custom hash function based upon available functions in solidity.  In order to mine a block, the miners must produce a nonce solving the following equation: 

`sha256(ripemd160(keccak256(challenge, msg.sender, nonce))) % difficulty = 0`

### Becoming a Miner

Mining on Tellor is very competitive.  For more information on becoming a miner, please see our documentation:  [https://tellor.readthedocs.io/en/latest/MinerSetup/](https://tellor.readthedocs.io/en/latest/MinerSetup/)  


