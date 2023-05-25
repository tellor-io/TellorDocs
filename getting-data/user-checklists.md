# User Checklists

These checklists are designed to guide you through the necessary preparations & processes for using the Tellor oracle.&#x20;

**Find below 2 checklists:** &#x20;

\***Development** - actions for the security of your code / integration.&#x20;

\***Maintenance** - actions to help make sure the data flowing into your contracts is properly checked & monitored.

## Development Checklist

These actions are essential for the security of your smart contracts:

<details>

<summary><strong>Communicate what oracle data is needed, the desired frequency, &#x26; how the feeds will be funded</strong></summary>

This helps the Tellor team & reporters to better understand your needs. Feel free to ask for help & advice! This can be done by making an issue in the [dataSpecs repo](https://github.com/tellor-io/dataSpecs/tree/main), or by reaching out in [the Tellor discord](https://discord.gg/tellor).&#x20;

</details>

<details>

<summary><strong>Build in a delay to allow time for disputes on bad values</strong></summary>

Tellor is an open & permissionless oracle, which means a reporter can submit any value at any time if they are willing to forfeit their staked TRB tokens. By using a value that is X minutes old, or by delaying the finality of functions that use the latest Tellor value, you can prevent the use of inaccurate data.

</details>

<details>

<summary><strong>Ensure that functions do not use old Tellor values</strong> </summary>

In the event where a Tellor value is disputed, the disputed value is removed & previous values remain. Prevent potential attackers from going back in time to find a desired value with a check in your contracts.

</details>

<details>

<summary><strong>Share code with the Tellor team for security review</strong>  </summary>

This step ensures the security of your code & allows the Tellor team to provide you with valuable feedback.

</details>

## Maintenance Checklist

These actions are highly recommended for maintaining a reliable & secure oracle system:

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
