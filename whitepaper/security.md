# Security

Security is achieved through Tellor’s architecture, which uses a simple bond/dispute mechanism to source correct values.  Ultimate ownership and security in the system is afforded by our governance contract, which we aim to align incentives from holders, reporters, and users. &#x20;

There are two primary metrics used when determining the security of an oracle:

* How can a bad value get put on-chain? (e.g. BTC/USD is 10M)
* How much does it cost to censor the oracle? (no good values can get through)

For the former, this is the cost to break the governance contract of Tellor. If we assume that a bad value will get caught (not go through unnoticed), then the bad value would go to a dispute.  In order for the value to be put back on-chain, the vote would need to settle such that an incorrect value is deemed correct.  With multiple rounds of voting, the malicious party would need to get to the point where they have 51% of the voting power in the system.&#x20;

Since the governance contract is only partially based on the token weight (token weighted holders, reporters, users), there are other factors at play.  The cost to break is not straightforward as it could be garnered several ways:&#x20;

Where VS = voting shares&#x20;

&#x20;           VS = total supply + reporter votes + user(tipping) votes

If the system is newly deployed, there will be minimal reporter and tipping votes.  The system would therefore continue a straight token weighted vote, with the cost to get 51% simply being 51% of the market cap. &#x20;

In a system with reporter and tipper votes, the attack vectors are different.  The total number of reporter votes in the system is the count of all historical mining events among actively bonded reporters.  At a rate of one mining event per minute (a very fast chain), this would indicate 525,000 reporter votes given each year.  With a current supply of around 2M TRB and about 1/10 that many mining events, this makes even a best-case scenario for the attacker prohibitively expensive to carry out in any manner that is not a multi-year attack.  Since other chains are faster and cheaper than Ethereum, this governance parameter would need to be carefully considered when deploying to other chains. &#x20;

To break the system via tipping, the cost would be higher than if just using the token weighted option(holder). If you buy the token and tip, you get half a vote.  The malicious attacker could recycle the tips so as not to drain liquidity and increase the price (easier to buy in smaller lots and tip versus actually buying 51% of the total supply). Additionally, due to the fact that half of the tips are burned, the reduction in total supply would drastically increase the token price, making each additional tip more expensive.&#x20;

Overall, the cost to get a bad value on-chain is prohibitively high.  With Tellor’s current market cap over $100 Million dollars, breaking the governance system is no easy feat.  Unless a party was breaking Tellor just for the fun of it, the much cheaper option is to simply censor Tellor for a certain period of time, as most use cases require some finality in the oracle (they will not wait for the entire Tellor system to settle a bad value dispute).

Since any value that is disputed will be put to a vote by all token holders, the simple cost to censor is:

_Cost of a stake \* block time of underlying system (since Tellor is as fast the underlying system)_

As long as this value is higher than the cost to 51% attack a given chain (e.g. on Ethereum, to censor transactions at the miner level), Tellor should be considered a censorship resistant oracle for use on that network.  With current costs at a 100 TRB bond requirement and a $50 price, if you assume even 10 second block times on Ethereum, it would cost:&#x20;

_100 TRB bond \* $50/TRB \* (6\*60) = \~$1,800,000 / hr_

Currently it costs around $1,500,000/ hr to simply 51% attack Ethereum, so the security is sufficient for almost any application on the network.\[3] &#x20;

The cost to censor via disputes is:

_Cost to dispute = disputeFee \* 2^ blocks per period_

Therefore the cost to dispute for even 10 minutes on a 30 second block chain (assuming the minimum 10 TRB cost at a $50 price):&#x20;

_10 TRB bond \* $50/TRB \* 2^2\*10 = \~$524M_

Looking at our formula, we can summarize that security increases when:

* **The share of those voting increases**
* **The price of the token increases**

Additionally, a minimum threshold of reporters is also essential to the proper functioning of the Tellor system. The more parties that are available to submit data, the more decentralized our reporter set will be.  An active and watchful community is also one of the big missing pieces in many protocols.  Just because you are “theoretically” secure if there is an arbitrage opportunity, defi has seen many protocols exploited because those opportunities are left unfilled.  It is the job of the Tellor ecosystem to properly incentivize and monitor the activity to make sure active diligence is being performed.&#x20;

&#x20; 3\. [https://www.crypto51.app/](https://www.crypto51.app) ↑
