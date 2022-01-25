# Monetary Policy

Tellor utilizes a governance based monetary policy for managing circulating supply (the total supply is essentially meaningless) and the overall growth rate in the supply of TRB. There are two ways to manipulate the supply of Tellor, via locking/unlocking (reducing/increasing the circulating supply) and then minting/burning.

Many crypto-systems utilize fixed minting policies which either have no minting (a fixed supply), or mint at a constant/ programmatic rate (e.g. Bitcoin/ Ethereum). These systems work well for initially generating demand and finding an equilibrium in terms of price/ quantity, however fail to afford flexibility in the cases of multiple chains and large exogenous shocks to demand (i.e. speculation).

To create a system that allows the governance of Tellor to better achieve its mission of a secure, decentralized oracle, Tellor is introducing a new structure of flexible supply growth rates for mining networks (each chain can have a different inflationary reward system) as well as Tellor Treasuries (staking pools) to reduce the circulating supply and increase governance participation.

### Flexible Supply Growth Rates

The Tellor system will allow minting tokens at discrete intervals to be used for various endeavors. A proposal will be voted on (and subject to multiple rounds like other votes) by the governance contract. The proposal will be to initiate a one time minting event to a specific contract. Some examples of proposals can include:

#### Inflationary Mining Rewards

Inflationary mining rewards will no longer be built into the system (minting from the mining contract). Instead, each chain that has a mining operation will need to be funded by a vote. An initial vote will be put forth to fund the Ethereum mining contract for two years at a certain rate. When the vote is complete, a one time minting event will fund the oracle contract with tokens (e.g. 24,000 at a rate of \~1,000/ month). In two years, the community will need to vote again on whether to fund the Ethereum mining contract.

This flexibility allows for other chains to also be funded with inflationary rewards. The overall supply growth rate will need to be managed, but the more flexible nature of the monetary policy should afford an initial lower rate of inflation with the ability to mint more if needed.

#### Grants Program

The Tellor community can also begin a grants program, with votes to simply mint tokens to new users and promising projects. This inflationary based funding of grants means that the community can continue to grow even if large philanthropic individuals are not present in the ecosystem and can support projects that help Tellor succeed even if they are not profitable themselves.

#### Employee contracts and contributor payments

As Tellor moves toward a DAO structure, the idea of a “core” Tellor team will go away. Although minted tokens initially, future employees of the Tellor system, including the current Tellor team, will need to apply for future minting events if they want to continue being rewarded for their contributions.

### Tellor Treasuries

Tellor treasuries are staking pools that reward users for locking up their TRB in exchange for future TRB with interest. The purpose of Tellor treasuries is to enable the Tellor community to manipulate the circulating supply of Tellor to provide a more stable Tellor price. The security of the Tellor oracles stems in many ways from the price of TRB, so having a countercyclical way to remove tokens from circulation will be a key component of this stabilization.

The treasury events will work as quarterly votes to either increase, decrease, or continue a certain number of TRB locked in treasury contracts. For example, for the first 4 quarters of Tellor, the system will allow 100,000 TRB each quarter to be locked (A in Figure 4). Once one year comes around, 105,000 TRB are set to be released into circulation. If the price of TRB (D in Figure 4) has increased substantially, the community should allow these coins to be released, maybe even decreasing the amount locked (e.g. issue only 75,000 in Treasuries next month (B in Figure 4)). If the price however has decreased, the Tellor community can vote to increase the Treasury issuance to 200,000, thus creating external demand for parties to buy TRB to lock in the treasury, increasing the price by reducing the circulating supply (C in Figure 4).

![](<../../.gitbook/assets/3 (2)>)

Another benefit of locking participants is to increase voting activity. Upon exit of a Tellor treasury, parties are punished if they did not vote on Tellor governance proposals. Parties are subject to lose any percentage of the interest gained in the treasury contract based upon the percentage of votes they abstained from. As an example, if a holder has 100 TRB locked into a one year treasury contract at 5%, and there were 10 voting events over the year; if the party voted on only 2 of the events, they would only receive 101 TRB upon exiting versus 105 if they had voted on every event.

{% hint style="success" %}
In lieu of voting on governance proposals you can **delegate** your voting power to the address of your choice.  To do so, run the _`delegate`_ function with the Tellor governance contract here: [https://etherscan.io/address/0x51d4088d4EeE00Ae4c55f46E0673e9997121DB00](https://etherscan.io/address/0x51d4088d4EeE00Ae4c55f46E0673e9997121DB00)&#x20;
{% endhint %}

Although the treasury contracts have fixed interest rates, each new issuance can change the interest rate. If demand for treasuries is very high, the interest rate can be low. If however, there is little interest and some of the treasury offering remains empty, the community can vote to increase the interest rate on subsequent offerings.
