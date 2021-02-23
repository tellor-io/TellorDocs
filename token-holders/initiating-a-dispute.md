---
description: >-
  You can start the process to invalidate bad data by disputing values that are
  submitted by the mining network.
---

# Initiating a Dispute

Any party can challenge data submissions of any of the five miners when a value is placed on-chain.  A challenger must submit a dispute fee to each challenge.  Once a challenge is submitted, the potentially malicious miner who submitted the value is placed in a locked state for the duration of the vote.  For the next two days, Tribute holders vote on the validity of the mined value.  All Tribute holders have an incentive to maintain an honest oracle and can vote on the dispute.  Proper submission is one that corresponds to a valid query requested within the time period between the release of the challenge and the submission of the value. The ambiguity of the validity is a feature and corresponds to “correct” being up to the interpretation of the Tellor community.  For more information about Disputes, see the following section of the whitepaper:

{% page-ref page="../whitepaper/tellor-oracle-overview/disputes.md" %}

## How to Initiate a Dispute

* Navigate to the Tellor [Dispute Center](https://www.tellorscan.com)
* Here you will see any current mining events as they occur as well as a list of all recent mining events.

![](../.gitbook/assets/screen-shot-2020-09-18-at-10.08.23-am.png)



* Each row in the list of mining events represents a specific data request and displays the ID, Symbol, and official values.  However, Tellor takes the **median value of 5 submissions** as the official value, therefore for each request you have 5 data submissions that can be disputed.  **Click the +** to expand each row to see all the submissions associated with that specific event.  If you see a bad value you want to dispute, simply click the **dispute button.**

![](../.gitbook/assets/screen-shot-2020-09-18-at-10.08.36-am.png)

* A model window will pop up indicating the **TRB dispute fee** you must stake to initiate the dispute.  We call this a fee, but it will only be taken from you in the situation where the community votes against your dispute and in favor of the miner's value being valid.  In this case your dispute fee is given to the miner you disputed.  
* Once you've initiated the dispute the dispute is resolved by a vote of TRB holders.  If your dispute is successfully voted in favor of by the majority, **your dispute fee is returned along with the miner's staked tokens.**
* **Be careful and initiate a Dispute at your own risk.**  

