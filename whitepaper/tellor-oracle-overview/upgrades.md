# Upgrades

**Tellor uses an upgradeable proxy contract, separating the storage of data and the functionality of the contract.**   

The process for proposing an upgrade is as follows:

* Deploy a new Tellor contract \(with new Tellor functionality\)
* Propose vote to switch the proxy address to the new Tellor address
* A week long vote occurs on whether to switch over.  
* The result is a simple majority of the vote, token weighted at the block the vote was proposed.  
* After the voting period, there is a day long chance for parties to dispute the results and start another voting period \(after paying a fee\).  
* If the vote passes with no disputes, the Tellor contract is changed. 

