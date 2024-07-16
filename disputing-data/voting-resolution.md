# Voting/Resolution

There are 4 steps required for resolving disputes. Each step corresponds to a function called from the appropriate [governance contract](https://app.gitbook.com/s/tcQlo49FAqTaOimNOz0X/the-basics/contracts-reference). All steps can be performed via Etherscan.

{% hint style="info" %}
**Note: After a dispute is initiated, there is a voting period equal to 24 hours times the number of voting rounds, up to a maximum of 6 days.**
{% endhint %}

<details>

<summary>Step 1: Determine the disputeID</summary>

On a block explorer, navigate to the appropriate governance [contract](../the-basics/contracts-reference.md).  Click on on the txnhash for the `beginDispute` txn you'd like to dispute.  Click Logs() and scroll down to the `NewDispute` event which contains the **disputeID**.

</details>

<details>

<summary>Step 2: Vote</summary>

Go back to the governance contract on the block explorer, click the `Write Contract` button. Log into your Web3 compatible wallet and Click `Connect to Web3` with the address that holds your tellor voting power. Click function 5 `vote.`

Inputs:

* `_disputeID`: Enter the `disputeID` from step 1.
* `_supports (bool)`: Here is where you can choose whether or not to support the dispute. Enter `true` if you wish to vote in favor of the disputer. Enter `false` if you wish to vote on the side of the reporter.
* `_invalidQuery`: If you believe that the dispute was invalid and there is no clear correct option, enter `true` here. Otherwise, input `false`.

Note: 24-144 hours after the dispute is initiated, depending on the current vote round, votes can be tallied. Which brings us to...

</details>

<details>

<summary>Step 3: Tally Votes</summary>

* Connect your web3 compatible wallet to the governance contract via etherscan.
* Click on function 4. tallyVotes
* Input the disputeID from step one and click Write to sign the transaction.

Note: 24 hours after tallyVotes is called, the vote can be executed. Which brings us to...

</details>

<details>

<summary>Step 4: Execute Vote</summary>

The last step for resolving a dispute is `executeVote`. After this function is called, the winner of the dispute receives the locked TRB tokens.

* Connect your web3 compatible wallet to the governance contract via etherscan.
* Click on function 2. `executeVote`.
* Input the `disputeID` from step one and click Write to sign the transaction

</details>

###
