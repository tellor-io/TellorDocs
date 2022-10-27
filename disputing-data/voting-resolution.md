# Voting/Resolution

There are 4 steps required for resolving disputes. Each step corresponds to a function called from the appropriate [governance contract](https://app.gitbook.com/s/tcQlo49FAqTaOimNOz0X/the-basics/contracts-reference). All steps can be performed via Etherscan.&#x20;

**Note: After a dispute is initiated, there is a 48 hour voting period.**&#x20;

### **Step 1: Determine the disputeID**

* On etherscan, locate the `Submit Value` transaction that was disputed. Click the Logs tab and copy the \_queryId.&#x20;
* Navigate to the [governance contract](https://app.gitbook.com/s/tcQlo49FAqTaOimNOz0X/the-basics/contracts-reference). Click the `contract` tab. Click the `Read Contract` Button. Click on function 6 `getOpenDisputesOnId`. Input the queryId and click Query for a list of open disputes on that QueryID.

_The dispute Id is most likely the highest number in the list; However, in case there have been multiple disputes on the same `queryId` in a short period of time, the disputeId can be cross checked by entering the_ `disputeID` _in the_ `getDisputeInfo` _function._

### Step 2: Vote

From step 1, click the `Write Contract` button. Log into your Web3 compatible wallet and Click `Connect to Web3` with the address that holds your tellor voting power. Click function `9. vote`.&#x20;

Inputs:&#x20;

* `_disputeID`: Enter the `disputeID` from step 1.
* `_supports (bool)`: Here is where you can choose whether or not to support the dispute. Enter `true` if you wish to vote in favor of the disputer. Enter `false` if you wish to vote on the side of the reporter.
* `_invalidQuery`: If you believe that the dispute was invalid and there is no clear correct option, enter `true` here. Otherwise, input `false`.&#x20;

Note: 48 hours after the dispute is initiated, votes can be tallied. Which brings us to...

### Step 3: Tally Votes

* Connect your web3 compatible wallet to the governance contract via etherscan.&#x20;
* Click on function 7. talleyVotes
* Input the disputeID from step one and click Write to sign the transaction.

Note: 24 hours after talleyVotes is called, the vote can be executed. Which brings us to...

### Step 4: Execute Vote

The last step for resolving a dispute is `executeVote`. After this function is called, the winner of the dispute receives the locked TRB tokens.&#x20;

* Connect your web3 compatible wallet to the governance contract via etherscan.&#x20;
* Click on function 3. `executeVote`.&#x20;
* Input the `disputeID` from step one and click Write to sign the transaction.&#x20;
