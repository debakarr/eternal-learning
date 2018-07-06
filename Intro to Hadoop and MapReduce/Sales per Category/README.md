### Mapper and Reducer

We have two new mapper and reducer - **productMapper.py** and **productReducer.py**

**[training@localhost code]** `ls`
mapper.py  productMapper.py  productReducer.py  purchases.txt  reducer.py

### Content of mapper and reducer

**[training@localhost code]** `cat productMapper.py `
```python
#!/usr/bin/python

import sys
for line in sys.stdin:
	data = line.strip().split("\t")
	if len(data) == 6:
		date, time, store, item, cost, payment = data
		print "{0}\t{1}".format(item, cost)
```

**[training@localhost code]** `cat productReducer.py `
```python
#!/usr/bin/python

import sys

salesTotal = 0
oldKey = None

# Loop around the data
# It will be in the format key\tval
# Where key is the product name, val is the sale amount
#
# All the sales for a particular product will be presented,
# then the key will change and we'll be dealing with the next product

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisSale = data_mapped

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", salesTotal
        oldKey = thisKey;
        salesTotal = 0

    oldKey = thisKey
    salesTotal += float(thisSale)

if oldKey != None:
    print oldKey, "\t", salesTotal
```

### Checking locally

**[training@localhost code]** `head -20 purchases.txt | ./productMapper.py | sort | ./productReducer.py `
Baby 	309.16
Cameras 	1268.17
Children's Clothing 	235.63
Consumer Electronics 	296.8
DVDs 	290.82
Garden 	136.9
Men's Clothing 	461.23
Music 	326.73
Pet Supplies 	493.51
Toys 	239.26
Video Games 	93.01
Women's Clothing 	853.21

### Run the MapReduce job

**[training@localhost code]** `hs productMapper.py productReducer.py myinput myoutput2`
packageJobJar: [productMapper.py, productReducer.py, /tmp/hadoop-training/hadoop-unjar5457240331668580390/] [] /tmp/streamjob6138608487494682313.jar tmpDir=null
18/07/06 06:03:53 WARN mapred.JobClient: Use GenericOptionsParser for parsing the arguments. Applications should implement Tool for the same.
18/07/06 06:03:53 WARN snappy.LoadSnappy: Snappy native library is available
18/07/06 06:03:53 INFO snappy.LoadSnappy: Snappy native library loaded
18/07/06 06:03:53 INFO mapred.FileInputFormat: Total input paths to process : 1
18/07/06 06:03:54 INFO streaming.StreamJob: getLocalDirs(): [/var/lib/hadoop-hdfs/cache/training/mapred/local]
18/07/06 06:03:54 INFO streaming.StreamJob: Running job: job_201807060555_0001
18/07/06 06:03:54 INFO streaming.StreamJob: To kill this job, run:
18/07/06 06:03:54 INFO streaming.StreamJob: UNDEF/bin/hadoop job  -Dmapred.job.tracker=0.0.0.0:8021 -kill job_201807060555_0001
18/07/06 06:03:54 INFO streaming.StreamJob: Tracking URL: http://0.0.0.0:50030/jobdetails.jsp?jobid=job_201807060555_0001
18/07/06 06:03:55 INFO streaming.StreamJob:  map 0%  reduce 0%
18/07/06 06:04:06 INFO streaming.StreamJob:  map 15%  reduce 0%
18/07/06 06:04:09 INFO streaming.StreamJob:  map 24%  reduce 0%
18/07/06 06:04:12 INFO streaming.StreamJob:  map 33%  reduce 0%
18/07/06 06:04:15 INFO streaming.StreamJob:  map 42%  reduce 0%
18/07/06 06:04:18 INFO streaming.StreamJob:  map 50%  reduce 0%
18/07/06 06:04:32 INFO streaming.StreamJob:  map 81%  reduce 17%
18/07/06 06:04:35 INFO streaming.StreamJob:  map 90%  reduce 25%
18/07/06 06:04:38 INFO streaming.StreamJob:  map 96%  reduce 25%
18/07/06 06:04:41 INFO streaming.StreamJob:  map 100%  reduce 25%
18/07/06 06:04:47 INFO streaming.StreamJob:  map 100%  reduce 71%
18/07/06 06:04:50 INFO streaming.StreamJob:  map 100%  reduce 77%
18/07/06 06:04:53 INFO streaming.StreamJob:  map 100%  reduce 84%
18/07/06 06:04:56 INFO streaming.StreamJob:  map 100%  reduce 90%
18/07/06 06:04:59 INFO streaming.StreamJob:  map 100%  reduce 98%
18/07/06 06:05:00 INFO streaming.StreamJob:  map 100%  reduce 100%
18/07/06 06:05:02 INFO streaming.StreamJob: Job complete: job_201807060555_0001
18/07/06 06:05:02 INFO streaming.StreamJob: Output: myoutput2

### Checking list of files in output directory

**[training@localhost code]** `hadoop fs -ls myoutput2`
```
Found 3 items
-rw-r--r--   1 training supergroup          0 2018-07-06 06:05 myoutput2/_SUCCESS
drwxr-xr-x   - training supergroup          0 2018-07-06 06:03 myoutput2/_logs
-rw-r--r--   1 training supergroup        426 2018-07-06 06:04 myoutput2/part-00000
```

### Checking content of output file

**[training@localhost code]** `hadoop fs -cat myoutput2/part-00000`
Baby 	57491808.44
Books 	57450757.91
CDs 	57410753.04
Cameras 	57299046.64
Children's Clothing 	57624820.94
Computers 	57315406.32
**Consumer Electronics 	57452374.13**
Crafts 	57418154.5
DVDs 	57649212.14
Garden 	57539833.11
Health and Beauty 	57481589.56
Men's Clothing 	57621279.04
Music 	57495489.7
Pet Supplies 	57197250.24
Sporting Goods 	57599085.89
**Toys 	57463477.11**
Video Games 	57513165.58
Women's Clothing 	57434448.97
