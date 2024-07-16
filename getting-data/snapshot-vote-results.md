---
description: >-
  DAOs using Snapshot are able to bring proposal results onchain via the Gnosis
  Zodiac Tellor module, allowing decisions made by DAOs can experience an
  end-to-end decentralized process.
---

# SnapShot Vote Results

The primary components of this process are:

\- Snapshot proposal

\-Tellor Reporters

\-Gnosis Safe wallet

\-The Tellor Zodiac Module



Step-by-Step Process:

1. The DAO will create a proposal on [snapshot](https://snapshot.org/), the results of which contain transactions that need to be executed onchain.
2. The DAO will also create a [gnosis safesnap account](https://safe.global/) , assigning it’s chosen addresses as part of the multi-sig.
3.  Once created, the user will go to apps > zodiac > Tellor Module

    <figure><img src="../.gitbook/assets/Screenshot 2024-07-03 at 1.35.15 PM.png" alt=""><figcaption><p>Apps on the left-hand dropdown</p></figcaption></figure>

<figure><img src="../.gitbook/assets/Screenshot 2024-07-03 at 1.44.51 PM.png" alt=""><figcaption><p>zodiac App</p></figcaption></figure>

<figure><img src="../.gitbook/assets/Screenshot 2024-07-03 at 1.42.40 PM.png" alt=""><figcaption><p>Tellor module</p></figcaption></figure>

Setting the appropriate parameters:

\-Owner address: address of the multi-sig

\-Address of the oracle contract where the results will be reported [(reference here)](https://docs.tellor.io/tellor/the-basics/contracts-reference)

\-Cooldown- Length of time to allow for disputing of reported results

\-Expiration - Length of time before reported result is no longer valid

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXeUnlfwqhEbYjxuQeNOl4InJxeIPMbD-WPmN95S7hcgPLA6vjQKUAgN7Q8UODoqfXjgDgsSu1gl-uT6dNXwDxDw8KE4PukL2sN9Kx2UuOljXEJl8lWbZ2TOU7hwzMR9FfMcqwgzk4YtDsr4J63us8_VA65k?key=LUoEMTFhtTrSJNXuFk6nUQ" alt=""><figcaption></figcaption></figure>

4. Once added, the DAO can select the module - > Click the ‘Write Contract’ tab -> and select addProposal from the ‘function’ dropdown before ‘Expiration’ is over (\*even before snapshot proposal voting is closed.)

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXelhnSntMKJdtJWeVVS3AsHTGEbTwQC0dhq5Z_nHFX-4zJDmZhfV6fj47_1pvpHsixxkWr1eipVQ1iJPHgSYd2cEFc_PXwyvRMrpBFWkAXcH3kqGyDedDsHPp70laYZq3M5jD3-IYgyYGqKA92kDhRjxew?key=LUoEMTFhtTrSJNXuFk6nUQ" alt=""><figcaption></figcaption></figure>

5. Once the voting period for the proposal ends, Tellor reporters race to report the following data pertaining the to snapshot proposal:

&#x20;                 a. the query data (includes the proposal id, tx hashes, module address)&#x20;

&#x20;                 b. Actual reported value: input t/f that it passed

6.  The DAO will then select ‘executeProposal’ from the function dropdown after “cooldown period” is over&#x20;

    (established when setting up zodiac module,; cooldown clock starts once value is reported)

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXeG3WPvauMldLAJDIGTSX-Ox7-mnXJ_H5RPnypNUX6n6remnJ8SRyE-3RnJGsQqdQ8ijF5MFjSB9bDfVhA0Vzlh-UkVcJYGbZERGTIbBIOxLh785LGnBlmnsCFwjK532SacYQineXyHO5ZHo9eLy9pBKjQq?key=LUoEMTFhtTrSJNXuFk6nUQ" alt=""><figcaption></figcaption></figure>

\
