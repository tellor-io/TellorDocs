# Introduction

{% hint style="info" %}
Important note: Data reporting on Tellor requires paying gas fees and staking TRB tokens that can be lost if incorrect data is submitted. New reporters should practice on a testnet like sepolia or mumbai while they learn the ropes. Reach out in [discord](https://discord.gg/n7drGjh) if you need test TRB tokens!
{% endhint %}

Anyone from anywhere in the world can learn how to be a Tellor data reporter, and submit data to Tellor’s multichain databases. Reporting can be as easy as calling the submitValue contract function on etherscan. For those who want to compete for time based rewards and TRB tips we have Telliot.

## Telliot

[Telliot](https://github.com/tellor-io/telliot-feeds) is a robust command line interface for providing oracle data on the Tellor network while competing for TRB rewards. It automatically stakes the required amount of TRB necessary for reporting. It can query APIs for off-chain data, calculate profitability for submissions, submit oracle data, and even decode submitted data to check for accuracy.

It is recommended that reporters also [monitor](../disputing-data/monitoring.md) their data submissions participate in community discussions and [vote on disputes!](broken-reference)

{% hint style="info" %}
Note: the easiest way to become a reporter is through Telliot. However, the tellor contracts do not require telliot usage. Tellor can be interacted with in any scripting language, and, in some cases, Etherscan.
{% endhint %}

