# Data Request IDs

The Tellor system is a way to push data on-chain.  **What the pieces of data are pushed on-chain are specified off-chain in the miner code.**

{% hint style="info" %}
Note that each request ID corresponds to a specific datapoint.  Example:  Request ID 4 is BTC/USD in a 24 Hour Time Weighted Average.
{% endhint %}

 The tellor mining system is set up to pull data to generate these values to submit on-chain once a correct nonce is mined. These specific APIs are just suggestions. The system is not guaranteed to work for everyone. It is up to the consensus of the Tellor token holders to determine what a correct value is.  In our example, request ID 4 is BTC/USD. If the APIs all go down, it is the responsibility of the miner to still submit a valid BTC/USD price. If they do not, they risk being disputed and slashed.

| TellorID | Data | Granularity | Transformation |
| :--- | :--- | :--- | :--- |
| 1 | ETH/USD | 1000000 | Median |
| 2 | BTC/USD | 1000000 | Median |
| 3 | BNB/USD | 1000000 | Median |
| 4 | BTC/USD | 1000000 | 24 Hour TWAP |
| 5 | ETH/BTC | 1000000 | Median |
| 6 | BNB/BTC | 1000000 | Median |
| 7 | BNB/ETH | 1000000 | Median |
| 8 | ETH/USD | 1000000 | 24 Hour TWAP |
| 9 | ETH/USD | 1000000 | EOD Median |
| 10 | AMPL/USD | 1000000 | Custom |
| 11 | ZEC/ETH | 1000000 | Median |
| 12 | TRX/ETH | 1000000 | Median |
| 13 | XRP/USD | 1000000 | Median |
| 14 | XMR/ETH | 1000000 | Median |
| 15 | ATOM/USD | 1000000 | Median |
| 16 | LTC/USD | 1000000 | Median |
| 17 | WAVES/BTC | 1000000 | Median |
| 18 | REP/BTC | 1000000 | Median |
| 19 | TUSD/ETH | 1000000 | Median |
| 20 | EOS/USD | 1000000 | Median |
| 21 | IOTA/USD | 1000000 | Median |
| 22 | ETC/USD | 1000000 | Median |
| 23 | ETH/PAX | 1000000 | Median |
| 24 | ETH/BTC | 1000000 | 24 Hour TWAP |
| 25 | USDC/USDT | 1000000 | Median |
| 26 | XTZ/USD | 1000000 | Median |
| 27 | LINK/USD | 1000000 | Median |
| 28 | ZRX/BNB | 1000000 | Median |
| 29 | ZEC/USD | 1000000 | Median |
| 30 | XAU/USD | 1000000 | Median |
| 31 | MATIC/USD | 1000000 | Median |
| 32 | BAT/USD | 1000000 | Median |
| 33 | ALGO/USD | 1000000 | Median |
| 34 | ZRX/USD | 1000000 | Median |
| 35 | COS/USD | 1000000 | Median |
| 36 | BCH/USD | 1000000 | Median |
| 37 | REP/USD | 1000000 | Median |
| 38 | GNO/USD | 1000000 | Median |
| 39 | DAI/USD | 1000000 | Median |
| 40 | STEEM/BTC | 1000000 | Median |
| 41 | USPCE | 1000000 | Median |
| 42 | BTC/USD | 1000000 | EOD Median |
| 43 | TRB/ETH | 1000000 | Median |
| 44 | BTC/USD | 1000000 | 1 Hour TWAP |
| 45 | TRB/USD | 1000000 | EOD Median |
| 46 | ETH/USD | 1000000 | 1 Hour TWAP |
| 47 | BSV/USD | 1000000 | Median |
| 48 | MAKER/USD | 1000000 | Median |
| 49 | BCH/USD | 1000000 | 24 Hour TWAP |
| 50 | TRB/USD | 1000000 | Median |
| 51 | XMR/USD | 1000000 | Median |
| 52 | XFT/USD | 1000000 | Median |
| 53 | BTCDominance | 1000000 | Median |

