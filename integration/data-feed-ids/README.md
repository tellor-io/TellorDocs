# Data feed IDs

The Tellor system allows users to request specific pieces of data, and reporters can then submit those values. Every piece of data within the Tellor system is associated with a specific identifier, known as the `queryId`. When a user requests data using `tipQuery` and when a reporter submits data using `submitValue`, they have to input both the `queryId` and `queryData`. The `queryData` tells reporters how to fulfill the data query, while also informing voters how to verify the data in a dispute. The `queryId` is defined as the keccak256 hash of the `queryData` field.

{% hint style="info" %}
Note: Tellor legacy queries have IDs 1 through 100. Their queryId's are NOT defined as the hash of queryData.
{% endhint %}
