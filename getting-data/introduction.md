Here are some technical docs for my company. Can you write an improved version of this in markdown?


# Introduction

The Tellor system allows users to request specific pieces of data, and reporters can then submit those values. Every piece of data that is requested, reported, and retrieved within the Tellor system is associated with a Query Typ_e,_ Query Data_,_ and a specific identifier, known as the Query ID.&#x20;

#### Some quick definitions before we move on:

{% tabs %}
{% tab title="Query Type" %}
A Query Type is a [specification](https://github.com/tellor-io/dataSpecs) for custom data you want to receive from the oracle.  It  defines the parameters of a Query that users can input for their specific requests.  For example:

#### Query Type - `SpotPrice`

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
The Query ID is your Query's unique identifier and [hash of the Query Data](creating-a-query.md#example-querydata-and-queryid). It's required for submitting, retrieving, and paying for all data in the Tellor system.&#x20;

#### To generate a query ID, use this simple tool:

{% embed url="https://queryidbuilder.herokuapp.com/" %}
Query ID Builder
{% endembed %}
{% endtab %}
{% endtabs %}

### **What data do you need?**

#### **Price data**

First check if the data is already [being reported](https://github.com/tellor-io/telliot-feeds/tree/main/src/telliot\_feeds/feeds) by viewing our [feeds](https://feed.tellor.io/).

Tellor data is free for anyone to read. This means that if someone else just updated the value, you can use it free of charge! ****&#x20;

{% hint style="success" %}
#### Need a spot price from Tellor?&#x20;

1. Generate a query ID for the `asset/currency`pair using [this tool.](https://app.gitbook.com/s/tcQlo49FAqTaOimNOz0X/getting-data/creating-a-query#getting-a-query-id-and-query-data) &#x20;
2. Next, use that ID to [pay reporters](https://app.gitbook.com/s/tcQlo49FAqTaOimNOz0X/getting-data/funding-a-feed#funding-a-one-time-request) to put that data on-chain.&#x20;
3. Then retrieve the reported spot price from the oracle [like this](reading-data/).
{% endhint %}

#### Custom Data

First, check in [`/types`](https://github.com/tellor-io/dataSpecs/blob/main/types) if there's already a query type that defines the data you need.

If not, you'll need to [create a new query type](https://app.gitbook.com/s/tcQlo49FAqTaOimNOz0X/getting-data/creating-a-query#creating-a-new-query-type).&#x20;

Once that is done you'll need to [pay reporters](https://app.gitbook.com/s/tcQlo49FAqTaOimNOz0X/getting-data/funding-a-feed#funding-a-one-time-request) to put that data on-chain, and retrieve that data from the Tellor oracle [like this](https://app.gitbook.com/s/tcQlo49FAqTaOimNOz0X/getting-data/using-tellor).
