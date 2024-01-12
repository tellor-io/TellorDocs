# User Checklists

These checklists are designed to guide you through the necessary preparations & processes for using the Tellor oracle.&#x20;

**Find below 2 checklists:** &#x20;

\***Development** - actions for the security of your code / integration.&#x20;

\***Maintenance** - actions to help make sure the data flowing into your contracts is properly checked & monitored.

## Development Checklist

<details>

<summary><strong>Communicate what oracle data is needed, the desired frequency, &#x26; how the feeds will be funded</strong></summary>

This helps the Tellor team & reporters to better understand your needs. Feel free to ask for help & advice! This can be done by making an issue in the [dataSpecs repo](https://github.com/tellor-io/dataSpecs/tree/main), or by reaching out in [the Tellor discord](https://discord.gg/tellor).&#x20;

</details>

<details>

<summary>Review Best Practices </summary>

[This repository](https://github.com/tellor-io/best-practices-user/tree/main) is a reference implementation for integrating Tellor price feed data into your protocol. It demonstrates some best practices for using Tellor, including implementing a dispute time buffer and a data staleness check. It also mitigates back-in-time dispute attacks by caching the most recent value and timestamp.

</details>

<details>

<summary><strong>Build in a delay to allow time for disputes on bad data</strong></summary>

A reporter can submit any value at any time if they are willing to forfeit their staked TRB tokens.  By delaying use of a value, or by delaying the finality of functions that use the latest Tellor value, you can prevent the use of inaccurate data.\


**The best practice for reading Tellor data** is to use the`getDataBefore` function with a buffer time that allows time for bad values to be disputed:

`getDataBefore(_queryId,`**`block.timestamp - 20 minutes`**`);`\
&#x20;\
[This repo](https://github.com/tellor-io/tellor-caller-liquity/blob/main/contracts/TellorCaller.sol) is a great reference for integrating Tellor.

</details>

<details>

<summary>Add a staleness check</summary>

It's also best practice to require/check that the data is not too old for your use-case. For example:

`require(block.timestamp -`**`_timestampRetrieved < 24 hours`**`);`

</details>

<details>

<summary><strong>Prevent a "back in time" attack</strong></summary>

In the event where a Tellor value is disputed, the disputed value is removed & previous values remain. Prevent potential attackers from going back in time to find a desired value with a [check in your contracts](https://github.com/tellor-io/best-practices-user/blob/74c08870f81bbdbec773b36d5bf084f65da59927/contracts/TellorUser.sol#L57).  &#x20;

</details>

<details>

<summary><strong>Share code with the Tellor team for security review</strong>  </summary>

This step ensures the security of your code & allows the Tellor team to provide you with valuable feedback.

</details>

## Maintenance Checklist

<details>

<summary><strong>Hold TRB for disputes</strong></summary>

This ensures that you are ready to dispute any incorrect values that may occur in the oracle data feed.

</details>

<details>

<summary><strong>Hold TRB for staking reporters (as insurance)</strong></summary>

In the event of a critical situation, this allows you to act as the reporter of last resort for your protocol.

</details>

<details>

<summary><strong>Monitor the data</strong> </summary>

Monitoring clients like the Disputable Values Monitor / Auto-Disputer can be found in the Tellor github.

</details>

<details>

<summary><strong>Become Familiar w/ Telliot</strong> </summary>

Telliot is currently the standard open-source tool for reporting and interacting with Tellor's oracle network.

</details>

<details>

<summary><strong>Communicate Questions/Concerns</strong>  </summary>

To address your specific monitoring needs, it is important to communicate any questions or  concerns that arise with the Tellor team and they’ll be happy to address them all.

</details>

{% hint style="info" %}
**Remember:**  Communication and careful planning are key to a successful integration!
{% endhint %}



\
