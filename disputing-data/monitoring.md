# Monitoring

## **The Disputable Values Monitor (DVM)**

The DVM is a CLI dashboard & text alerts app for disputable values reported to Tellor oracles.  The DVM constantly monitors Tellor data submissions and compares them to the data available on the API specified by the user. &#x20;

{% hint style="success" %}
Instructions for setting it up can be found in its [repository.](https://github.com/tellor-io/disputable-values-monitor)&#x20;
{% endhint %}

Once a disputable value is picked up by the DVM it sends a text alert to a phone number you specify with a transaction link.  You'll need to take note of the `queryid` and `timestamp` located in the transaction link you received.

Please continue to the next section for instructions on how to dispute.

