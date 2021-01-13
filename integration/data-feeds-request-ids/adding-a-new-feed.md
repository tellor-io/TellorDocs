# Adding a new feed

**1. Get familiar with some medium articles to understand the pitfalls and security concerns when using an oracle and designing a robust settlement price.**  
[**https://medium.com/tellor/best-practices-for-oracle-users-on-ethereum-1ad9e2a43c3b**](https://medium.com/tellor/best-practices-for-oracle-users-on-ethereum-1ad9e2a43c3b) ****[**https://medium.com/tellor/oracles-and-settlement-prices-7720d1732c76**](https://medium.com/tellor/oracles-and-settlement-prices-7720d1732c76) ****[**https://medium.com/tellor/tellor-security-201-72a367602af1**](https://medium.com/tellor/tellor-security-201-72a367602af1)  ****[**https://medium.com/tellor/tellor-security-and-rewards-1e365e1be8ae**](https://medium.com/tellor/tellor-security-and-rewards-1e365e1be8ae) ****

**2. Look through** [**how tellor works**](../../whitepaper/tellor-oracle-overview/)

**3. Open a TIP proposal\(see previous PRs for an example\)**  
[**https://github.com/tellor-io/TIPs**](https://github.com/tellor-io/TIPs) ****

**4.The final step is to open a PR to implement it in \`**[**telliot**](https://github.com/tellor-io/telliot)**\` which users use to submit the values.  
add the APIs used to extract the values in:**[  
**https://github.com/tellor-io/telliot/blob/master/configs/indexes.json**](https://github.com/tellor-io/telliot/blob/master/configs/indexes.json)   
**add the new Data ID to push to the oracle contract:**  
[**https://github.com/tellor-io/telliot/blob/master/pkg/tracker/psrs.go**](https://github.com/tellor-io/telliot/blob/master/pkg/tracker/psrs.go)  
**5. We will announce the new Data ID in the communication channels so that miners know that they need to start pushing this new feed.**

