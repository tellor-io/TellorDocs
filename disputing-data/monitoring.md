# Monitoring

## **The Disputable Values Monitor (DVM)**

The DVM is a CLI dashboard & text alerts app for disputable values reported to Tellor oracles.  The DVM constantly monitors Tellor data submissions and compares them to the data available on the API specified by the user. &#x20;

Once a disputable value is picked up by the DVM it sends an alert to a discord server you specify via webhook.  You'll need to take note of the `queryid` and `timestamp` located in the transaction link you receive in these alerts.

### Auto-Disputer

The DVM has an Auto-Disputer.  The Auto-disputer is a complex event listener for any EVM chain, but specifically it listens for NewReport events on the Tellor networks the user wants to monitor.

When the Auto-disputer receives new NewReport events, it parses the reported value from the log, then compares the reported value to the trusted value from the Tellor reporter reference implementation, telliot.

In order to auto-dispute, users need to define what a "disputable value" is. To do this, users can set "thresholds" for feeds they want to monitor. Thresholds in the auto-disputer serve to set cutoffs between a healthy value and a disputable value. Users can pick from three types of thresholds: **range, percentage, and equality**.

{% hint style="info" %}
For set up instructions visit this [repository.](https://github.com/tellor-io/disputable-values-monitor)&#x20;
{% endhint %}

Please continue to the next section for instructions on how to dispute.

