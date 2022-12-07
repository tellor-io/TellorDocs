# Tellor Functions

## Available Tellor Functions

When your contract inherits the [usingtellor](https://github.com/tellor-io/usingtellor) helper contract, it has access to the following functions:


### `getDataAfter`

> Retrieves the next undisputed value for a given queryId after a given timestamp

```solidity
function getDataAfter(bytes32 _queryId, uint256 _timestamp)
        public
        view
        returns (bytes memory _value, uint256 _timestampRetrieved);
```

### `getDataBefore`

> Finds the most recent submission for a given queryId **before** a specific timestamp.
>
> * It is recommended that you use this function with a buffer time when retrieving oracle values.  This [allows time](../the-basics/fundamentals.md#finality) for bad values to be disputed.

```solidity
function getDataBefore(bytes32 _queryId, uint256 _timestamp)
        public
        view
        returns (bytes memory _value, uint256 _timestampRetrieved);
```

### `getIndexForDataAfter`

> Returns the index of the next value reported for a given queryId after a given timestamp.
```solidity
function getIndexForDataAfter(bytes32 _queryId, uint256 _timestamp)
        public
        view
        returns (bool _found, uint256 _index);
```

### `getIndexForDataBefore`

> Returns the index of the most recent value reported for a given queryId before a given timestamp. 

```solidity
function getIndexForDataBefore(bytes32 _queryId, uint256 _timestamp)
        public
        view
        returns (bool _found, uint256 _index);
```

### `getMultipleValuesBefore`

> Returns the multiple most recent values for a given queryId before a given timestamp. 

```solidity
function getMultipleValuesBefore(
        bytes32 _queryId,
        uint256 _timestamp,
        uint256 _maxAge,
        uint256 _maxCount
    )
        public
        view
        returns (bytes[] memory _values, uint256[] memory _timestamps);
```

### `getNewValueCountbyQueryId`

> Returns the total number of values submitted for a given queryId

```solidity
function getNewValueCountbyQueryId(bytes32 _queryId)
        public
        view
        returns (uint256);
```

### `getReporterByTimestamp`

> Retrieves the address of the reporter for a given queryId and timestamp.

```solidity
function getReporterByTimestamp(bytes32 _queryId, uint256 _timestamp)
        public
        view
        returns (address);
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

### `isInDispute`

> Determines whether a specific value with a given queryId and timestamp has been disputed

```solidity
function isInDispute(bytes32 _queryId, uint256 _timestamp)
        public
        view
        returns (bool);
```

### `retrieveData`

> Retrieves a specific value by queryId and timestamp

```solidity
function retrieveData(bytes32 _queryId, uint256 _timestamp)
        public
        view
        returns (bytes memory);
```
