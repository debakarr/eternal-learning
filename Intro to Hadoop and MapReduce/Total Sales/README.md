### Mapper and Reducer

We have two new mapper and reducer - **totalSaleMapper.py** and **totalSaleReducer.py**

**[training@localhost code]** `ls`
mapper.py         productReducer.py  reducer.py                 storeHighestSaleReducer.py  totalSaleReducer.py
productMapper.py  purchases.txt      storeHighestSaleMapper.py  totalSaleMapper.py

### Content of mapper and reducer

**[training@localhost code]** `cat totalSaleMapper.py `
```python
#!/usr/bin/python

import sys
for line in sys.stdin:
	data = line.strip().split("\t")
	if len(data) == 6:
		date, time, store, item, cost, payment = data
		print "{0}\t{1}".format(store, cost)
```

**[training@localhost code]** `cat totalSaleReducer.py `
```python
#!/usr/bin/python

import sys

salesTotal = 0
count = 0

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    _, thisSale = data_mapped

    salesTotal += float(thisSale)
    count = count + 1

print count, "\t", salesTotal
```

### Checking locally

**[training@localhost code]** `head -20 purchases.txt | ./totalSaleMapper.py | sort | ./totalSaleReducer.py`

20 	5004.43

### Run the MapReduce job

**[training@localhost code]** `hs totalSaleMapper.py totalSaleReducer.py myinput myoutput4`
```
packageJobJar: [totalSaleMapper.py, totalSaleReducer.py, /tmp/hadoop-training/hadoop-unjar5139695761542853766/] [] /tmp/streamjob1138384534497927341.jar tmpDir=null
18/07/06 07:02:30 WARN mapred.JobClient: Use GenericOptionsParser for parsing the arguments. Applications should implement Tool for the same.
18/07/06 07:02:31 WARN snappy.LoadSnappy: Snappy native library is available
18/07/06 07:02:31 INFO snappy.LoadSnappy: Snappy native library loaded
18/07/06 07:02:31 INFO mapred.FileInputFormat: Total input paths to process : 1
18/07/06 07:02:31 INFO streaming.StreamJob: getLocalDirs(): [/var/lib/hadoop-hdfs/cache/training/mapred/local]
18/07/06 07:02:31 INFO streaming.StreamJob: Running job: job_201807060555_0004
18/07/06 07:02:31 INFO streaming.StreamJob: To kill this job, run:
18/07/06 07:02:31 INFO streaming.StreamJob: UNDEF/bin/hadoop job  -Dmapred.job.tracker=0.0.0.0:8021 -kill job_201807060555_0004
18/07/06 07:02:31 INFO streaming.StreamJob: Tracking URL: http://0.0.0.0:50030/jobdetails.jsp?jobid=job_201807060555_0004
18/07/06 07:02:32 INFO streaming.StreamJob:  map 0%  reduce 0%
18/07/06 07:02:43 INFO streaming.StreamJob:  map 13%  reduce 0%
18/07/06 07:02:46 INFO streaming.StreamJob:  map 20%  reduce 0%
18/07/06 07:02:49 INFO streaming.StreamJob:  map 27%  reduce 0%
18/07/06 07:02:52 INFO streaming.StreamJob:  map 34%  reduce 0%
18/07/06 07:02:55 INFO streaming.StreamJob:  map 42%  reduce 0%
18/07/06 07:02:58 INFO streaming.StreamJob:  map 50%  reduce 0%
18/07/06 07:03:14 INFO streaming.StreamJob:  map 75%  reduce 0%
18/07/06 07:03:15 INFO streaming.StreamJob:  map 81%  reduce 17%
18/07/06 07:03:18 INFO streaming.StreamJob:  map 90%  reduce 17%
18/07/06 07:03:21 INFO streaming.StreamJob:  map 97%  reduce 25%
18/07/06 07:03:24 INFO streaming.StreamJob:  map 100%  reduce 25%
18/07/06 07:03:30 INFO streaming.StreamJob:  map 100%  reduce 73%
18/07/06 07:03:33 INFO streaming.StreamJob:  map 100%  reduce 81%
18/07/06 07:03:36 INFO streaming.StreamJob:  map 100%  reduce 89%
18/07/06 07:03:39 INFO streaming.StreamJob:  map 100%  reduce 97%
18/07/06 07:03:42 INFO streaming.StreamJob:  map 100%  reduce 100%
18/07/06 07:03:43 INFO streaming.StreamJob: Job complete: job_201807060555_0004
18/07/06 07:03:43 INFO streaming.StreamJob: Output: myoutput4
```

### Checking list of file in output directory

**[training@localhost code]** `hadoop fs -ls myoutput4`
```
Found 3 items
-rw-r--r--   1 training supergroup          0 2018-07-06 07:03 myoutput4/_SUCCESS
drwxr-xr-x   - training supergroup          0 2018-07-06 07:02 myoutput4/_logs
-rw-r--r--   1 training supergroup         23 2018-07-06 07:03 myoutput4/part-00000
```

### Checking content of output file

**[training@localhost code]** `hadoop fs -cat myoutput4/part-00000`

**4138476 	1034457953.26**
