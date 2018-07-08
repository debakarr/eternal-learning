### Mapper and Reducer

We have two new mapper and reducer - **storeHighestSaleMapper.py** and **storeHighestSaleReducer.py**

**[training@localhost code]** `ls`
mapper.py         productReducer.py  reducer.py                 storeHighestSaleReducer.py
productMapper.py  purchases.txt      storeHighestSaleMapper.py

### Content of mapper and reducer

**[training@localhost code]** `cat storeHighestSaleMapper.py #!/usr/bin/python`
```python
import sys
for line in sys.stdin:
	data = line.strip().split("\t")
	if len(data) == 6:
		date, time, store, item, cost, payment = data
		print "{0}\t{1}".format(store, cost)
```
**[training@localhost code]** `cat storeHighestSaleReducer.py `
```python
#!/usr/bin/python

import sys

maxSale = 0
oldKey = None

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

    thisKey, thisSale = data_mapped

    if float(thisSale) > maxSale:
    	maxSale= float(thisSale)

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", maxSale
        oldKey = thisKey;
	maxSale = 0

    oldKey = thisKey

if oldKey != None:
    print oldKey, "\t", maxSale
```

### Checking locally

**[training@localhost code]** `head -20 purchases.txt | ./storeHighestSaleMapper.py | sort | ./storeHighestSaleReducer.py `
```
Austin 	469.63
Boston 	483.82
Buffalo 	25.38
Corpus Christi 	153.57
Fort Worth 	290.82
Greensboro 	309.16
Houston 	53.26
Las Vegas 	136.9
Lincoln 	39.75
Newark 	296.8
New York 	235.63
Omaha 	493.51
Pittsburgh 	66.08
San Diego 	260.65
San Francisco 	214.05
San Jose 	247.18
Stockton 	0
```

### Run the MapReduce job

**[training@localhost code]** `hs storeHighestSaleMapper.py storeHighestSaleReducer.py myinput myoutput3`
```
packageJobJar: [storeHighestSaleMapper.py, storeHighestSaleReducer.py, /tmp/hadoop-training/hadoop-unjar4462345570275233869/] [] /tmp/streamjob5281220558292014941.jar tmpDir=null
18/07/06 06:46:24 WARN mapred.JobClient: Use GenericOptionsParser for parsing the arguments. Applications should implement Tool for the same.
18/07/06 06:46:24 WARN snappy.LoadSnappy: Snappy native library is available
18/07/06 06:46:24 INFO snappy.LoadSnappy: Snappy native library loaded
18/07/06 06:46:24 INFO mapred.FileInputFormat: Total input paths to process : 1
18/07/06 06:46:24 INFO streaming.StreamJob: getLocalDirs(): [/var/lib/hadoop-hdfs/cache/training/mapred/local]
18/07/06 06:46:24 INFO streaming.StreamJob: Running job: job_201807060555_0003
18/07/06 06:46:24 INFO streaming.StreamJob: To kill this job, run:
18/07/06 06:46:24 INFO streaming.StreamJob: UNDEF/bin/hadoop job  -Dmapred.job.tracker=0.0.0.0:8021 -kill job_201807060555_0003
18/07/06 06:46:24 INFO streaming.StreamJob: Tracking URL: http://0.0.0.0:50030/jobdetails.jsp?jobid=job_201807060555_0003
18/07/06 06:46:25 INFO streaming.StreamJob:  map 0%  reduce 0%
18/07/06 06:46:35 INFO streaming.StreamJob:  map 16%  reduce 0%
18/07/06 06:46:38 INFO streaming.StreamJob:  map 24%  reduce 0%
18/07/06 06:46:42 INFO streaming.StreamJob:  map 33%  reduce 0%
18/07/06 06:46:45 INFO streaming.StreamJob:  map 42%  reduce 0%
18/07/06 06:46:48 INFO streaming.StreamJob:  map 50%  reduce 0%
18/07/06 06:47:00 INFO streaming.StreamJob:  map 75%  reduce 0%
18/07/06 06:47:01 INFO streaming.StreamJob:  map 81%  reduce 17%
18/07/06 06:47:04 INFO streaming.StreamJob:  map 90%  reduce 17%
18/07/06 06:47:08 INFO streaming.StreamJob:  map 96%  reduce 25%
18/07/06 06:47:10 INFO streaming.StreamJob:  map 100%  reduce 25%
18/07/06 06:47:17 INFO streaming.StreamJob:  map 100%  reduce 72%
18/07/06 06:47:20 INFO streaming.StreamJob:  map 100%  reduce 79%
18/07/06 06:47:23 INFO streaming.StreamJob:  map 100%  reduce 87%
18/07/06 06:47:26 INFO streaming.StreamJob:  map 100%  reduce 95%
18/07/06 06:47:29 INFO streaming.StreamJob:  map 100%  reduce 100%
18/07/06 06:47:31 INFO streaming.StreamJob: Job complete: job_201807060555_0003
18/07/06 06:47:31 INFO streaming.StreamJob: Output: myoutput3
```

### Checking list of file in output directory

**[training@localhost code]** `hadoop fs -ls myoutput3`
```
Found 3 items
-rw-r--r--   1 training supergroup          0 2018-07-06 06:47 myoutput3/_SUCCESS
drwxr-xr-x   - training supergroup          0 2018-07-06 06:46 myoutput3/_logs
-rw-r--r--   1 training supergroup       1815 2018-07-06 06:47 myoutput3/part-00000
```

### Checking content of output file

**[training@localhost code]** `hadoop fs -cat myoutput3/part-00000`
```
Albuquerque 	499.98
Anaheim 	499.98
Anchorage 	499.99
Arlington 	499.95
Atlanta 	499.96
Aurora 	499.97
Austin 	499.97
Bakersfield 	499.97
Baltimore 	499.99
Baton Rouge 	499.98
Birmingham 	499.99
Boise 	499.98
Boston 	499.99
Buffalo 	499.99
```
**Chandler 	499.98**
```
Charlotte 	499.98
Chesapeake 	499.98
Chicago 	499.99
Chula Vista 	499.99
Cincinnati 	499.98
Cleveland 	499.98
Colorado Springs 	499.99
Columbus 	499.98
Corpus Christi 	499.96
Dallas 	499.99
Denver 	499.97
Detroit 	499.99
Durham 	499.96
El Paso 	499.98
Fort Wayne 	499.96
Fort Worth 	499.98
Fremont 	499.99
Fresno 	499.99
Garland 	499.99
Gilbert 	499.99
Glendale 	499.98
Greensboro 	499.99
Henderson 	499.99
Hialeah 	499.99
Honolulu 	499.99
Houston 	499.99
Indianapolis 	499.98
Irvine 	499.99
Irving 	499.99
Jacksonville 	499.99
Jersey City 	499.99
Kansas City 	499.97
Laredo 	499.96
Las Vegas 	499.98
Lexington 	499.97
Lincoln 	499.99
Long Beach 	499.99
Los Angeles 	499.99
Louisville 	499.98
Lubbock 	499.98
Madison 	499.97
Memphis 	499.97
Mesa 	499.99
Miami 	499.98
Milwaukee 	499.97
Minneapolis 	499.97
Nashville 	499.97
New Orleans 	499.99
New York 	499.99
Newark 	499.99
Norfolk 	499.97
North Las Vegas 	499.98
Oakland 	499.99
Oklahoma City 	499.99
Omaha 	499.99
Orlando 	499.99
Philadelphia 	499.98
Phoenix 	499.99
Pittsburgh 	499.99
Plano 	499.99
Portland 	499.96
Raleigh 	499.99
```
**Reno 	499.99**
```
Richmond 	499.96
Riverside 	499.98
Rochester 	499.99
Sacramento 	499.96
Saint Paul 	499.98
San Antonio 	499.98
San Bernardino 	499.98
San Diego 	499.98
San Francisco 	499.97
San Jose 	499.99
Santa Ana 	499.97
Scottsdale 	499.98
Seattle 	499.99
Spokane 	499.99
St. Louis 	499.99
St. Petersburg 	499.95
Stockton 	499.98
Tampa 	499.99
```
**Toledo 	499.98**
```
Tucson 	499.98
Tulsa 	499.96
Virginia Beach 	499.98
Washington 	499.98
Wichita 	499.97
Winston–Salem 	499.98
```