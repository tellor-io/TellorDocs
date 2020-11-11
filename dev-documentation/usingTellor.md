---
description: >-
  This page is designed to give you a quick overview of using Tellor to get data
  into your smart contracts.
---

# Using Tellor 

Now that you have Tellor integrated into your smart contracts, you'll want to know what to do on a daily basis to make sure you have timely and accurate updates to your price feed. 

## Updating Values

#### Checking Last Update 

Before calling a function to update your values, you should first just check if it's already there!  Tellor values, once onchain, are free for anyone to read.  This means that if someone else just updated the value, you can use it free of charge!  

To check when the value was last updated, you can run the following usingTellor function:


```text
 function getCurrentValue(uint256 _requestId) public view returns (bool ifRetrieve, uint256 value, uint256 _timestampRetrieved);
````

The last returned values is the timestamp last updated.

#### Adding a Tip

If the time the value was last updated is not sufficient, you can add a tip to your requestID in order to get it mined.  

```text
    addTip(uint _requestId, uint _tip)
```

Tellor works by selecting the top five tipped requests for each Tellor block.  As an example, assume ID's [1,2,3,4,5] are currently being mined.  If ID's [6,7,8,9,10,11,12] have corresponding tips of [10,20,30,40,50,60,70], then once the first ID's are mined, the ID's with the highest tipes (ID's 8-12 in this case) will be chosen.  ID 6 and 7 will not be mined and will have to wait for a block where they are the highest tipped (this is very similar to gas prices and transaction fees on Ethereum or Bitcoin).  If you for instance are ID 6 and want to get your ID included in the next block, you will need to tip >20 (you have 10 and need over 30). 

In order to see how much you will need to tip, you can see the current ID's on deck and their corresponding tips using the following function in the main Tellor contract: 

```text
 function getNewVariablesOnDeck() public view returns (uint256[5] memory idsOnDeck, uint256[5] memory tipsOnDeck)
 ```

Note that once you call for an update, you will need to wait until at least the next block is mined to get an update.  Currently, Tellor blocks are 5 minutes.  


### Monitoring Values and Disputing

Once Values are on-chain, we reccommend you don't just take them right away.  Tellor has a robust network of miners and watch dogs that are viligantly checking and ensuring accuracy, but the best person to know if your data is correct is you.  

You can monitor values and submit disputes by either reading the value on-chain:

```text
 function getCurrentValue(uint256 _requestId) public view returns (bool ifRetrieve, uint256 value, uint256 _timestampRetrieved);
```

Or using the [Tellor Dispute Center](https://disputes.tellorscan.com)


Disputes cost a lot of TRB, but are returned (along with a one stake reward) if the dispute was valid.  


Once the dispute goes through, be sure to request your data again, so the miners have another chance to push through a valid price.  



#### Automating Jobs

To automate adding a tip on a certain request ID by time or volatility, as well as scheduling other Tellor related tasks, we recommend (and use) [Buidlhub](https://www.buidlhub.com).