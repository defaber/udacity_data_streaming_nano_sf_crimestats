# SF Crime Stats

## Udacity Data Streaming Apache Spark and Kafka final project.

How did changing values on the SparkSession property parameters affect the throughput and latency of the data?
```
I was sitting at 0 rows processed when I left the parameters alone.  
When I started to adjust those properties the ProcessedRowsPerSecond started to increase.
```
What were the 2-3 most efficient SparkSession property key/value pairs? Through testing multiple variations on values, how can you tell these were the most optimal?
```
Increasing .option("maxRatePerPartition",1000), .option("maxOffsetsPerTrigger",2000) 
helped by actually given the data I needed.  When this was sitting as 200, I wasnt 
getting anywhere.  Adjusting the two seemed to help.
```
