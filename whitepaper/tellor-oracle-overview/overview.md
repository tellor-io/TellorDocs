# Overview

At a high level, Tellor is an oracle system where miners compete to add data points to an on-chain data bank.  To create a properly incentivized system, Tellor mints a native token, “Tributes” \(TRB\).  Miners are incentivized to submit data using inflationary rewards, and which data types they update are chosen based upon the “tips” assigned to each query.  Parties holding TRB can add a “tip” to a specific data type they want updated, then every 5 minutes the Tellor smart contract groups the top five most funded data types and creates a PoW challenge for miners to solve.  The first five miners to provide the PoW solution and the five off-chain data points are rewarded with newly minted tokens + the accumulated tips for the specific data requests.  In addition to the security provided by the PoW process, our main layer of security comes through a deposit of TRB that acts as a bond or stake requirement in order for miners to participate in the PoW.  The miners risk losing this stake if they submit data that is successfully disputed by TRB holders.

![Tellor Overview ](../../.gitbook/assets/image-2020-06-05-10-40-41.jpg)

#### The basic flow for adding and retrieving data is as follows: 

1. The user submits a query to Tellor using Tributes to incentivize miners to choose this query over other submissions.
2. Other users who want the same data pay or ‘tip’ this data series to further incentivize selection by miners.
3. Every 5 minutes, Tellor’s smart contract selects the best funded queries and provides a new challenge for miners to solve.
4. Miners submit their PoW solution and off-chain data points to the Tellor contract. The Tellor contract sorts the values as they come in and as soon as five values are received, the official value \(median of the five\) is selected and saved on-chain. The miners are then allocated their payout \(base reward and tips\).  We refer to these data update cycles as **blocks**_**.**_
5. Anyone holding Tellor Tributes can dispute the validity of a mined value by paying a dispute fee.  Over the next two days Tellor token holders will vote on the validity of the data point. 
6. For the next day, parties have the opportunity to dispute the result of the vote by paying a higher \(double\) dispute fee.  The voting period is doubled and another vote is initiated.  This process continues indefinitely until no disputes of the result occur. If the data point is deemed to be false, the miner will lose their stake. However, if the vote determines the value is correct, the reporting party’s dispute fee is given to the reported miner.
7. Each miner address cannot win successive blocks.  The current wait time per miner is 15 minutes or approximately 3 blocks.

![Tellor takes the median as the official value](../../.gitbook/assets/tellor_infographics2_median_def_cropped.png)

## Data Requests, Tips, and Blocks

Similar to paying higher gas fees for prioritizing transactions, users incentivize miners to retrieve their value by paying TRB tokens to ensure the query they are interested in is mined.  Tellor refers to these as tips.   Half of the tips are paid out evenly to the five winning miners every block. The other half is burned \(removed from circulation\).  As the ecosystem expands, securing data to finalize or execute a contract will lead to higher tips and higher incentivization of miners to continue to mine. Scarcity is a key feature of the Tellor system.  Currently, the time target of the oracle is 5 minutes; meaning there are only 288 queries per day on average. 

![](../../.gitbook/assets/tellor_infographics2_queryqueue_def_cropped.png)

#### Supported Data

Details pertaining to the requested data sources are stored off chain and referenced on-chain by a numeric ID.  This model makes each request ID flexible enough to handle things such as multiple API medians, volume/time weighted averages, manually inputted data, as well as any potential future implementation for data transformation.  This makes Tellor more flexible and further targets our ideal use cases and proper usage of oracles which does not include providing the ability for smart contracts to query single API’s. In order to add data to the list of supported data queries, a _pull request_ can be made in the miner software so that data providers know what values, and transformations to that value, are being requested.    


