---
description: >-
  We believe a "whitepaper" should be easy to read and simply help you
  understand how the project works.   We hope the following information provides
  that.  Let's start with the basics.
---

# Introduction

Smart contracts on Ethereum are fully self contained and any access to off-chain data is restricted.  By creating a system where inputs to a data feed are secured by a network of staked miners, Tellor creates trustless access to off-chain information.  This paper highlights the structure of this system and gives an in-depth overview regarding the incentives and assumptions used to ensure an honest input of data to the oracle.  

Tellor is an oracle system where parties can request the value of an off-chain data point \(e.g. BTC/USD\) and miners compete to add this value to an on-chain data-bank, accessible by all Ethereum smart contracts.  The inputs to this data-bank are secured by a network of staked miners.   Tellor utilizes crypto-economic incentive mechanisms, rewarding honest data submissions by miners and punishing bad actors, through the issuance of Tellor’s token, Tributes \(TRB\) and a dispute mechanism.

## Background 

One of the biggest hurdles limiting the potential applicability of smart contracts is a lack of a trustless source of off-chain data.  Tellor aims to fill this gap with an on-chain data feed where data is inputted by a permissionless network of crypto-economically incentivized data providers. 

Blockchain networks allow for fast, secure, transfer and creation of digital goods in addition to the storage and execution of tamperproof programs that can manage digital assets. These programs, once deployed on-chain, cannot be changed.  They are available to everyone with access to the chain, execute based on the defined parameters and interactions \(transactions\), and are verified by the blockchain’s consensus mechanism.  These characteristics allow anonymous parties to enter into binding digital agreements, called smart contracts. However, blockchains are siloed from other networks and have no direct access to real-world data.  Unfortunately, for smart contracts to bring true utility, off-chain data is necessary.  And for smart contracts to truly be secure and censorship resistant, off-chain data must be trustlessly provided.

**The Tellor Oracle** provides a trustless and decentralized alternative for off-chain data. It provides the infrastructure for decentralized applications to query off-chain data by properly incentivizing miners to provide data.

