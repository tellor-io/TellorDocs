# Introduction

The Tellor system allows users to request specific pieces of data, and reporters can then submit those values. Every piece of data that is requested, reported, and retrieved within the Tellor system is associated with a Query Type, Query Data, and a specific identifier, known as the Query ID.

{% hint style="success" %}
**Looking for help getting started?** We welcome you to [ask us anything](https://discord.gg/n7drGjh) in the developer's channel of our discord server. &#x20;
{% endhint %}

#### Some quick definitions before we move on:

{% tabs %}
{% tab title="Query Type" %}
A Query Type is a [specification](https://github.com/tellor-io/dataSpecs) for custom data you want to receive from the oracle. It defines the parameters of a Query that users can input for their specific requests. For example:

**Query Type - `SpotPrice`**

1. asset
   * description: Asset ID (e.g. BTC)
   * value type: string
2. currency
   * description: Selected currency (e.g. USD)
   * value type: string
{% endtab %}

{% tab title="Query Data" %}
Query Data is used to form your new Query's unique identifier, or Query ID. It's also emitted in data submission and payment contract events so Tellor users and reporters can programmatically construct query objects.

[Example of Query Data](https://app.gitbook.com/s/tcQlo49FAqTaOimNOz0X/getting-data/creating-a-query#example-querydata-and-queryid)
{% endtab %}

{% tab title="Query ID" %}
The Query ID is your Query's unique identifier and [hash of the Query Data](creating-a-query.md#example-querydata-and-queryid). It's required for submitting, retrieving, and paying for all data in the Tellor system.

**To generate a query ID, use this simple tool:**

{% embed url="https://queryidbuilder.herokuapp.com/" %}
Query ID Builder
{% endembed %}
{% endtab %}
{% endtabs %}

****
