# User Functions

## addTip

* **addTip** function allows the user to increase the payout for a specific request

```text
    addTip(uint _requestId, uint _tip)
```

where: \* \_requestId is the ID for the value to be mined \* \_tip is the amount the requester is willing to pay to get on the queue

## retrieveData

To read data, users will need to call these two functions:

* **retreiveData** function allows the user to read the data for the given API and timestamp

```text
retrieveData(uint _requestId, uint _timestamp)
```

where:

* \_requestId -- is the request ID
* \_timestamp -- is the unix timestamp to retrieve a value from

## getLastQuery

* **getLastQuery** function allows the user to read data from the latest API and timestamp mined.

```text
getLastNewValue()
```

This is an example of a function that would need to be added to a contract so that it can read data from an oracle contact if the contract holds Tributes:

```text
contract Oracle is usingTellor {
             ...
  function getLastNewValue() public returns(uint,bool) {
    (value,ifRetrieve)  = getLastNewValue();
                           return (value, ifRetreive);
             ...
  }
```

[Next ](https://tellor.readthedocs.io/en/latest/MinerFunctions/)[ Previous](https://tellor.readthedocs.io/en/latest/DevDocumentation/)  


