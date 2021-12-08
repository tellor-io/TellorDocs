# Governance

Tellor governance is used to settle disputes, to vote on Tellor upgrades, as well as new features such as monetary policy. The Tellor governance system aims to balance the voting power amongst various members of the community, specifically: holders, reporters, and users. TRB stakeholders all want Tellor to continue to grow, but the approach and needs of each group can be different. Weighting their votes differently can provide some checks and balances when considering the benefits of various proposals.

For Tellor, there are three groups of stakeholders identified in the Tellor system:

* TRB holders
* Reporters
* Users

![](<../../.gitbook/assets/2 (3)>)

TRB holder weights are measured as the balance of TRB on the chain where the vote is taking place. For reporters, each submitted data point affords them additional non-transferable voting power weighted at 1TRB per successful submission. However, reporters must be actively bonded to be able to vote with their allocated non-transferable voting power. Users are weighted by the number of tips they have paid into the system at a .5 rate. As an example, if a user tips 2 TRB, they are afforded 1 TRB worth of voting power in the system.

It is important to note that Tellor can be deployed on multiple chains. Although the main Tellor token is staying on the Ethereum network, users or the Tellor team can launch Tellor on any-chain, however the governance process would need to be handled using a different set up. The exact structure of the governance on each separate chain would need to be on a case-by-case basis (tips and mining start out at zero, so the cost to break is low), but most likely the governance of that specific chain would be controlled by the stakeholders on that chain (e.g. Polygon could use a mix of Polygon reporters, Polygon tellor users, and MATIC token holders).

### Delegation

TRB holders, reporters, and users in the Tellor system are also able to delegate their voting rights. By specifying an address which they want to give their balances voting power to, it allows smaller and more inactive holders to give their vote to a trusted party, which will help increase the overall voting participation in the network.

### Technical Details

A proposal will be submitted for a vote by paying a fee. Parties then vote on the proposal for a week. Like disputes, these votes are also subject to multiple rounds if there is a dispute. Certain functions can also require various quorums or vote lengths, but will not be enforced at the governance level. Once the vote is settled with no disputes, the proposal is executed.

### Quorum

Governance proposals for system updates and token minting require a 5% quorum and have to be won by 5% percent above the losing option. Disputes have no quorum requirement.
