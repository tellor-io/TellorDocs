# DataSpecs Registry

DataSpecsRegistry is an on-chain registry for tellor oracle query types. Users register a query type name and pay a fee which determines the registration duration. The user then sets the IPFS document hash of the dataspec document in the registry contract. This provides an on-chain, tamperproof record of all Tellor query type definitions.

{% hint style="info" %}
&#x20;[See the official frontend](https://tellorregistry.eth.limo/) to view and manage query type registrations.
{% endhint %}

### Deployed Contracts

#### Polygon - Official Deployment

[0x06Be23ea84148a5E439dFe2A0bcCE441ea74E2D6](https://polygonscan.com/address/0x06Be23ea84148a5E439dFe2A0bcCE441ea74E2D6)

#### Sepolia Testnet

[0x9413c3b2Fb74A7b7e6CDeBa683b31646Ceb534F2](https://sepolia.etherscan.io/address/0x9413c3b2Fb74A7b7e6CDeBa683b31646Ceb534F2)

### Contract Interactions

#### Register a Query Type

Registering a query type requires some TRB tokens and a unique query type name string. The minimum registration time is one year, and registrations cost $1000 per year in TRB. To find the current cost per year in TRB, we'll call `getCostperYearInTRB`:

<img src="../.gitbook/assets/Screenshot 2023-08-30 at 8.09.59 AM.png" alt="" data-size="original">

Now we know the minimum amount of TRB we need to register our query type.

***

Next, we will approve the token transfer in the token contract by inputting the registry contract address and an amount for one year's worth of tokens.

![](<../.gitbook/assets/Screenshot 2023-08-30 at 8.15.52 AM.png>)

***

Now we can register our query type in the registry contract. For the name of our query type, we'll use `ExampleQueryType`, and again we'll input a token fee amount for a one year registration:

&#x20;![](<../.gitbook/assets/Screenshot 2023-08-30 at 8.19.36 AM.png>)

***

We have officially registered a query type, but now we need to set our IPFS data specs document hash. There are many ways to get a document on IPFS, but one quick solution can be found at [nft.storage](https://nft.storage/docs/how-to/nftup/).

![](<../.gitbook/assets/Screenshot 2023-08-30 at 8.21.09 AM.png>)

Now we finally have a query type registered.

***

#### Manage a Query Type

There are a few actions you can take to manage your query type. The `extendRegistration` function can be used to extend the registration time for an existing query type. It can be called by anyone, and any amount of tokens can be paid.

![](<../.gitbook/assets/Screenshot 2023-08-30 at 8.23.05 AM.png>)

Each query type registration has a **manager** role and an **owner** role. The manager can set the document hash, and the owner can change the manager address and the owner address. The manager and owner addresses can be changed using these functions.

![](<../.gitbook/assets/Screenshot 2023-08-30 at 8.28.56 AM.png>)

#### &#x20;Query the Registry

<table><thead><tr><th width="393">Function Name</th><th>Function Purpose</th></tr></thead><tbody><tr><td><code>getAllRegisteredQueryTypes()</code></td><td>Get a list of all registered query type names:</td></tr><tr><td><code>getCostPerYearInTRB()</code></td><td>Get the registration cost per year in TRB tokens</td></tr><tr><td><code>getRegistration("ExampleQueryType")</code></td><td>Get all info for a given query type registration. </td></tr></tbody></table>

{% hint style="info" %}
`getRegistration`returns a struct in this form:

`struct Spec {`

&#x20;   `address owner; // sets the manager and owner addresses`

&#x20;   `address manager; // sets the document hash and lock time`

&#x20;   `string documentHash; // IPFS hash of data specs document (ex: ipfs://bafybeic6nwiuutq2fs3wq7qg5t5xcqghg6bnv65atis3aphjtatb26nc5u)`

&#x20;   `uint256 expirationTime; // timestamp when spec registration expires`

&#x20;   `bool registered; // registered at some point in time`

`}`
{% endhint %}

**Install Dependencies:**

`npm i`

**Compile Smart Contracts:**

`npx hardhat compile`

**Test Locally:**

`npx hardhat test`

### How to Contribute

Check out our issues log here on Github, join our [discord](https://discord.gg/B9B6ENxp) or feel free to reach out anytime at info@tellor.io.

\
