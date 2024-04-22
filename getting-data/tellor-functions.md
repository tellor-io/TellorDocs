# Tellor Functions

## Available Tellor Functions

When your contract inherits the [usingtellor](https://github.com/tellor-io/usingtellor) helper contract, it has access to the following functions:


### `_getDataAfter`

> Retrieves the next undisputed value for a given queryId after a given timestamp

```solidity
function _getDataAfter(bytes32 _queryId, uint256 _timestamp)
        internal
        view
        returns (bytes memory _value, uint256 _timestampRetrieved);
```

### `_getDataBefore`

> Finds the most recent undisputed submission for a given queryId **before** a specific timestamp.
>
> * It is recommended that you use this function with a buffer time when retrieving oracle values.  This [allows time](../the-basics/fundamentals.md#finality) for bad values to be disputed.

```solidity
function _getDataBefore(bytes32 _queryId, uint256 _timestamp)
        internal
        view
        returns (bytes memory _value, uint256 _timestampRetrieved);
```

### `_getIndexForDataAfter`

> Returns the index of the next value reported for a given queryId after a given timestamp.
```solidity
function _getIndexForDataAfter(bytes32 _queryId, uint256 _timestamp)
        internal
        view
        returns (bool _found, uint256 _index);
```

### `_getIndexForDataBefore`

> Returns the index of the most recent value reported for a given queryId before a given timestamp. 

```solidity
function _getIndexForDataBefore(bytes32 _queryId, uint256 _timestamp)
        internal
        view
        returns (bool _found, uint256 _index);
```

### `_getMultipleValuesBefore`

> Returns the multiple most recent values for a given queryId before a given timestamp. 

```solidity
function _getMultipleValuesBefore(
        bytes32 _queryId,
        uint256 _timestamp,
        uint256 _maxAge,
        uint256 _maxCount
    )
        internal
        view
        returns (bytes[] memory _values, uint256[] memory _timestamps);
```

### `_getNewValueCountbyQueryId`

> Returns the total number of values submitted for a given queryId

```solidity
function _getNewValueCountbyQueryId(bytes32 _queryId)
        internal
        view
        returns (uint256);
```

### `_getReporterByTimestamp`

> Retrieves the address of the reporter for a given queryId and timestamp.

```solidity
function _getReporterByTimestamp(bytes32 _queryId, uint256 _timestamp)
        internal
        view
        returns (address);
```

### `_getTimestampbyQueryIdandIndex`

> Returns the timestamp at a specific index for a given queryId.
>
> * Values start at the 0 index

```solidity
function _getTimestampbyQueryIdandIndex(bytes32 _queryId, uint256 _index)
        internal
        view
        returns (uint256);
```

### `_isInDispute`

> Determines whether a specific value with a given queryId and timestamp has been disputed

```solidity
function _isInDispute(bytes32 _queryId, uint256 _timestamp)
        internal
        view
        returns (bool);
```

### `_retrieveData`

> Retrieves a specific value by queryId and timestamp

```solidity
function _retrieveData(bytes32 _queryId, uint256 _timestamp)
        internal
        view
        returns (bytes memory);
```
