# Security

Security is achieved through Tellor’s architecture \(mining algorithm and selection process for median value\) and incentives implemented for miners to promptly submit the correct values.  Using the median value instead of the average \(or simply just one\) protects the value from being manipulated by a single malicious party submitting an extreme value. Ultimate security however is provided by the staking/dispute mechanism.  

Since any value that is disputed will be put to a vote by all token holders, the simple cost to attack/censor is:

> _Cost to win PoW at least 3 out of 5 times +  number of malicious values submitted \* price of stake \* length of blocks wished to be attacked_

This “Staked PoW” model allows for Tellor to take advantage of the efficiency and minimalism of a pure PoW design as well as the final security of slashing. The main problem with a pure PoW consensus mechanism is that 51% of attacks for significant time periods are relatively trivial on smaller chains.  Tellor’s consensus mechanism is handled by Ethereum and the point of PoW is for security, but also for randomness, token distribution effects, and community engagement/selection.

Looking at our formula, we can summarize that security increases when:

* **The share of token holders voting on disputes increases**
* **The price of the token increases**
* **Demand for the Oracle increases \(tips\)**

