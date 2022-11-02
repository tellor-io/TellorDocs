# Fundamentals

### The Oracle Problem

Blockchains such as ethereum only have access to a limited amount of information. They are great for tracking an account's cryptocurrency balance, for example. If you want your smart contracts to use information about the outside world such as cryptocurrency prices, sporting events, or weather, that data has to be put on chain somehow. One way of solving this problem is by having a single whitelisted address submit this data on-chain. This creates a central point of weakness in a protocol, however, as this single address could fail or be malicious.&#x20;

Tellor solves this problem by aligning the incentives of data reporters, data consumers, and [Tellor token holders](https://etherscan.io/token/0x88df592f8eb5d7bd38bfef7deb0fbc02cf3778a0). In brief, anyone can deposit a stake and report data. For a period of time, anyone can pay a [dispute fee to challenge any piece of data](https://app.gitbook.com/s/tcQlo49FAqTaOimNOz0X/disputing-data). Tellor stakeholders vote to determine the outcome of the dispute. If the data reporter loses the dispute, the reporter's stake goes to the disputing party. This creates a system where bad actors are punished and good actors are rewarded.

### Subjectivity&#x20;

Oracle systems seek to extend the capabilities of the chain to arbitrary information not agreed upon by the base validators via the chain's consensus mechanism.

Many oracle solutions simply grab responses from an API and put it on-chain. This is a great tool for builders or MVPs, but it’s not a complete oracle solution.

If you assume that the data from an API is always correct, you put complete trust in the operator of the API. The manipulability / censorship resistance of centralized APIs should be a serious concern for any project.&#x20;

Instead of being reliant on any specific API or source, Tellor provides a way to agree upon "truth." The Tellor oracle is not some magical cryptographic technique for monitoring the outside world and relaying it to Ethereum. It’s a network of individual participants who are crypto-economically incentivized to report and validate accurate data.

### Finality

When someone transfers their bitcoin to a centralized exchange, the exchange usually waits a period of time before allowing the user to sell their cryptocurrency and transfer their balance to their bank account. This practice is necessary because, even though a transaction may have been included in a block, that block is not actually finalized. A big miner could potentially mine a new block which reverts the original transaction, and the exchange would not receive the cryptocurrency. As time passes, it gets increasingly expensive to revert a block.&#x20;

Tellor operates under a similar principle of finality. When a Tellor data reporter submits some data, it's usually unwise to immediately use that value in your protocol. For[ best practices](https://tellor.io/best-practices-for-oracle-users-on-ethereum/), values should only be used once they have been on chain for a period of time to allow for someone to dispute a bad value. The longer a value has been on chain, the more likely it is to be valid.&#x20;

### Permissionlessness

Tellor allows anyone to stake and report data. This means that the Tellor protocol does not depend on the Tellor team. If you integrate Tellor into your protocol, you can rest assured that you will always be able to either pay someone else to submit your data, or just stake and report the data yourself. In other words, Tellor is as permissionless as the blockchain it's running on.


## FAQ

#### What chains?

Tellor is compatible with any EVM chain, as well as Algorand. Here is a list of the [currently deployed Tellor contracts](https://app.gitbook.com/s/tcQlo49FAqTaOimNOz0X/the-basics/contracts-reference).

#### Does requesting data cost money?

Tellor data reporters need a reason to report your requested data. If you want data in your smart contracts, you can either stake to [become a data reporter](https://app.gitbook.com/s/tcQlo49FAqTaOimNOz0X/reporting-data/setup-and-usage) yourself, or [add a tip](https://app.gitbook.com/s/tcQlo49FAqTaOimNOz0X/getting-data/funding-a-feed) with your data request to incentivize reporters. The cost of paying someone else to report is whatever the market determines, ie. cover gas plus some profit. The cost to report yourself is just the cost of gas.

#### Where does the data come from?

The data gets put on chain by [staked data reporters](https://app.gitbook.com/s/tcQlo49FAqTaOimNOz0X/reporting-data/telliot). In many cases, reporters can get the data from wherever they want, but they risk losing their stake if they report bad data. Alternatively, if you need data from a specific set of sources, a [custom query type](https://github.com/tellor-io/dataSpecs/issues/25) can be created for your unique use-case.

####
