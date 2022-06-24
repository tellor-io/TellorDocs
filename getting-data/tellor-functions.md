# Tellor Functions

## Available Tellor Functions

When your contract inherits the [usingtellor](https://github.com/tellor-io/usingtellor) helper contract, it has access to the following functions:

### `retrieveData`

> Retrieves a specific value by queryId and timestamp

```solidity
function retrieveData(bytes32 _queryId, uint256 _timestamp)
        public
        view
        returns (bytes memory);
```

### `isInDispute`

> Determines whether a specific value with a given queryId and timestamp has been disputed

```solidity
function isInDispute(bytes32 _queryId, uint256 _timestamp)
        public
        view
        returns (bool);
```

### `getNewValueCountbyQueryId`

> Returns the total number of values submitted for a given queryId

```solidity
function getNewValueCountbyQueryId(bytes32 _queryId)
        public
        view
        returns (uint256);
```



### `getTimestampbyQueryIdandIndex`

> Returns the timestamp at a specific index for a given queryId.
>
> * Values start at the 0 index

```solidity
function getTimestampbyQueryIdandIndex(bytes32 _queryId, uint256 _index)
        public
        view
        returns (uint256);
```



### `getCurrentValue`

> Finds the most recent submission for a given queryId and returns 3 things: a boolean for whether a value was found, the value itself, and a timestamp of the value
>
> * Note that this function should not be used in most cases since it does not include a dispute buffer time.&#x20;

```solidity
function getCurrentValue(bytes32 _queryId)
        public
        view
        returns (
            bool _ifRetrieve,
            bytes memory _value,
            uint256 _timestampRetrieved
        );
```



### getDataBefore

> Finds the most recent submission for a given queryId **before** a specific timestamp
>
> * It is recommended that you use this function with a buffer time when retrieving oracle values.  This [allows time](../the-basics/fundamentals.md#finality) for bad values to be disputed.

```solidity
function getDataBefore(bytes32 _queryId, uint256 _timestamp)
        public
        view
        returns (
            bool _ifRetrieve,
            bytes memory _value,
            uint256 _timestampRetrieved
        );
```

