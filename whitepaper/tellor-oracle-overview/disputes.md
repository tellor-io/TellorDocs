# Disputes

Tellor data values can always be disputed and taken off-chain, however the  longer a user waits once the data is submitted on chain, the more probable it is to remain, and therefore be secure; assuming any value that remains on-chain is valid due to economic incentives to dispute invalid ones.   

Any party can challenge data submissions of any of the five miners when a value is placed on-chain.  A challenger must submit a dispute fee to each challenge.  Once a challenge is submitted, the potentially malicious miner who submitted the value is placed in a locked state for the duration of the vote.  For the next two days, Tribute holders vote on the validity of the mined value.  All Tribute holders have an incentive to maintain an honest oracle and can vote on the dispute.  A proper submission is one that corresponds to a valid query requested within the time period between the release of the challenge and the submission of the value. The ambiguity of the validity is a feature and corresponds to “correct” being up to the interpretation of the Tellor community.

### Disputes Rounds 

Our dispute mechanism allows for multiple rounds of disputes.  The length of each dispute round and it's cost increases each round in steps:  

`now + 2 days * dispRounds`

`fee = disputeFee * dispRounds`

### Dispute Resolution

At the end of the vote period, and if no new round is initiated, the votes are tallied.   If found guilty, the malicious miner’s stake goes to the disputing party; otherwise the fee paid by the disputer is given to the wrongly accused miner.   


![](../../.gitbook/assets/tellor_infographics2_dispute_def_hd.png)

### Dispute Fees

The dispute fee is calculated based upon how many miners are in the system and for which value you are disputing.  The cost to dispute non-official values \(the non-median value\) is:

`max(15, stakeAmount * (1 - stakedMiners/200))`

For median values, since a dispute technically censors parties from reading the value, it is more expensive:

`stakeAmount * numberOfDisputesOnId`

As mentioned, there are also multiple dispute rounds which increase the fee for each subsequent round in the following fashion:

`fee = disputeFee * dispRounds`

For this reason, it quickly becomes prohibitively expensive for a malicious party to simply dispute good values to censor a contract from reading them.   


