# Taxi data processing

## Code file

```
codes/trip_analysis_1106.ipynb
```

- With this notebook, we aggregate order level taxi data into trip level taxi data.
- For example, a passenger can make multiple attempts of taxi-hailing (a.k.a. orders) for one trip with a certain pair of origin-destination. For the method of defining trip, please see the notes in notebook.
- Several variables are created for each trip, including:

  - `n_order`: the number of orders for each trip
  - `n_trip`: if trip was not made, this should be 0; otherwise, it should be 1 – this will be the final outcome of the trip
  - `n_cancel`: the number of cancelled orders for each trip
  - `time_period`:
    - `midnight`: 12am-6am
    - `am_peak`: 6-10am
    - `day_nonpeak`: 10am-5pm
    - `pm_peak`: 5pm - 12am
  - `weekend`: if the trip is on weekend, this should be 1 ; if not, it is 0
  - `wait_time`: time between booking time of the first order and pick-up time of the completed order for each trip; if the trip is not made, this value is NaN
  - `travel_time`: time between drop-off time and pick-up time for a completed order; if the trip is not made, this values is NaN
  - `origin_subzone`: the pick-up location is within which subzone
  - `dest_subzone`: the drop-off location is within which subzone

## Input data

* `201911_demand.parquet` and `master-plan-2014-subzone-boundary-web-shp`
* The subzone boundary shp file is stored under the `data` folder; the demand data is not uploaded.
* The subzone boundary data is for generating the `origin_subzone` and `dest_subzone`.

## Output

* The general structure of the data output is the same as the input demand data: each row is an order, but a `trip_id` is attached to each row. Orders with same trip_id values belong to the same trip.
* A sample of the output is stored in: `results/trip_data_sample.csv`

## Others

* There is another code file: `trip_distance.py` for obtaining the distance between pick-up location and drop-off location using OneMap routing API.
* However, OneMap API can only call up to **250 requests per minute.** The `trip_distance.py` need to be further edited to be used for generating trip_distance varaible for all the trip records.
