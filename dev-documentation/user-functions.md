# User Functions

## requestData

To request data, users will need Tributes to call this function:

* **requestData** function allows the user to specify the API, timestamp and tip \(this can be thought of as “gas”, the higher the tip/payout the higher the probability it will get mined next\) for the value they are requesting. If multiple parties are requesting the same data at the same time, their tips are combined to further incentivize miners at that time period and/or API.

```text
oracle.requestData(string calldata _c_sapi,string calldata _c_symbol,uint _requestId,uint _granularity, uint _tip)
```

where:

* \_c\_sapi string API being requested be mined
* \_c\_symbol is the short string symbol for the api request
* \_requestId being requested be mined if it exist otherwise use zero\(0\)
* \_granularity is the number of decimals miners should include on the submitted value
* \_tip amount the requester is willing to pay to be get on queue. Miners mine the onDeckQueryHash, or the api with the highest payout pool

## addTip

* **addTip** function allows the user to increase the payout for a specific request

```text
    addTip(uint _requestId, uint _tip)
```

where: \* \_requestId is the ID for the value to be mined \* \_tip is the amount the requester is willing to pay to be get on queue

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


