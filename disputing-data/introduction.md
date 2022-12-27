# Introduction

### Dispute Mechanism

Disputing and dispute resolution is the key governance piece in the Tellor system.

Any party can challenge data submissions of any reporters when a value is placed on-chain. A challenger must submit a dispute fee to each challenge. Once a challenge is submitted, the potentially malicious reporter who submitted the value is placed in a locked state for the duration of the vote. For the next two days, Tribute holders vote on the validity of the reported value. All Tribute holders have an incentive to maintain an honest oracle and can vote on the dispute. Proper submission is one that corresponds to a valid query around the time of the submission of the value. The [subjectivity](https://app.gitbook.com/s/tcQlo49FAqTaOimNOz0X/the-basics/fundamentals#subjectivity) of the validity is a feature and corresponds to “correct” being up to the interpretation of the Tellor community.

### Why it's Important

The security of Tellor comes through a deposit of TRB that acts as a bond or stake requirement in order for reporters to participate in providing data. The reporters risk losing this stake if they submit data that is successfully disputed.

### What This Means For Getting Data     

On a blockchain, [security](https://tellor.io/security-201/) and time can not be separated.  You can't have instant finality and still be secure, and this is very true for oracle data. &#x20;

Tellor data values can be used as soon as the data is placed on-chain, however the longer a user waits once the data is submitted on chain, the more probable it is to remain, and therefore be secure; assuming any value that remains on-chain is valid due to economic incentives to dispute invalid ones. Values are able to be disputed and taken off-chain for the same time frame as the reporter lock ( a configurable variable starting at 12 hours).

