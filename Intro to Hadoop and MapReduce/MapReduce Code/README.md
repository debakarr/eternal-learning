We have our mapper and reducer in `code` folder.

**[training@localhost code]** `ls`
mapper.py  purchases.txt  reducer.py

**[training@localhost code]** `cat mapper.py`
```python
#!/usr/bin/python

import sys
for line in sys.stdin:
  data = line.strip().split("\t")
  if len(data) == 6:
    date, time, store, item, cost, payment = data
    print "{0}\t{1}".format(store, cost)
```

**[training@localhost code]** `cat reducer.py`
```python
#!/usr/bin/python

import sys

salesTotal = 0
oldKey = None

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisSale = data
    if oldKey and oldKey != thisKey:
      print oldKey, "\t", salesTotal
      oldKey = thisKey
      salesTotal = 0

    oldKey = thisKey
    salesTotal += float(thisSale)

if oldKey != None:
    print oldKey, "\t", salesTotal
```

Our mapper takes input from standard input. So, in order to test it, we can take few sample lines and pipe that into the mapper from `purchases.txt` file(Six fields, separated by tabs). You can see that the mapper outputs the results, just as expected.

**[training@localhost code]** `head -20 purchases.txt`
```
2012-01-01  09:00 San Jose  Men's Clothing  214.05  Amex
2012-01-01  09:00 Fort Worth  Women's Clothing  153.57  Visa
2012-01-01  09:00 San Diego Music 66.08 Cash
2012-01-01  09:00 Pittsburgh  Pet Supplies  493.51  Discover
2012-01-01  09:00 Omaha Children's Clothing 235.63  MasterCard
2012-01-01  09:00 Stockton  Men's Clothing  247.18  MasterCard
2012-01-01  09:00 Austin  Cameras 379.6 Visa
2012-01-01  09:00 New York  Consumer Electronics  296.8 Cash
2012-01-01  09:00 Corpus Christi  Toys  25.38 Discover
2012-01-01  09:00 Fort Worth  Toys  213.88  Visa
2012-01-01  09:00 Las Vegas Video Games 53.26 Visa
2012-01-01  09:00 Newark  Video Games 39.75 Cash
2012-01-01  09:00 Austin  Cameras 469.63  MasterCard
2012-01-01  09:00 Greensboro  DVDs  290.82  MasterCard
2012-01-01  09:00 San Francisco Music 260.65  Discover
2012-01-01  09:00 Lincoln Garden  136.9 Visa
2012-01-01  09:00 Buffalo Women's Clothing  483.82  Visa
2012-01-01  09:00 San Jose  Women's Clothing  215.82  Cash
2012-01-01  09:00 Boston  Cameras 418.94  Amex
2012-01-01  09:00 Houston Baby  309.16  Visa
```

**[training@localhost code]** `head -20 purchases.txt | ./mapper.py`
```
San Jose  214.05
Fort Worth  153.57
San Diego 66.08
Pittsburgh  493.51
Omaha 235.63
Stockton  247.18
Austin  379.6
New York  296.8
Corpus Christi  25.38
Fort Worth  213.88
Las Vegas 53.26
Newark  39.75
Austin  469.63
Greensboro  290.82
San Francisco 260.65
Lincoln 136.9
Buffalo 483.82
San Jose  215.82
Boston  418.94
Houston 309.16
```

If we have problems, we could just go back and edit the mapper until it works. It's really nice and fast to be able to do this without having to run a complete hadoop job every time during the development phase. 

We can do a similar thing with the reducer. It's expecting a set of lines, each of which looks like the store name then a tab then the value. So, again, we can create a sample file which looks like that and pass it in to the reducer. But even nicer, we can test the entire pipeline. Remember that the mapper's output is sorted by the hadoop framework, and then passed to the reducer. So, we can simulate the entire thing on the Unix command line, like this. I take few lines from `purchases.txt`. I pipe it to the mapper. I then pass that to the Unix sort command, and pass that output to the reducer. When I run that, that simulates the entire map followed by shuffle and sort, followed by reduced phase, and as you can see, I've got the output from the reducer. 

**[training@localhost code]** `head -20 purchases.txt | ./mapper.py | sort`
```
Austin  379.6
Austin  469.63
Boston  418.94
Buffalo 483.82
Corpus Christi  25.38
Fort Worth  153.57
Fort Worth  213.88
Greensboro  290.82
Houston 309.16
Las Vegas 53.26
Lincoln 136.9
Newark  39.75
New York  296.8
Omaha 235.63
Pittsburgh  493.51
San Diego 66.08
San Francisco 260.65
San Jose  214.05
San Jose  215.82
Stockton  247.18
```

**[training@localhost code]** `head -20 purchases.txt | ./mapper.py | sort | ./reducer.py`
```
Austin  849.23
Boston  418.94
Buffalo   483.82
Corpus Christi  25.38
Fort Worth  367.45
Greensboro  290.82
Houston   309.16
Las Vegas   53.26
Lincoln   136.9
Newark  39.75
New York  296.8
Omaha   235.63
Pittsburgh  493.51
San Diego   66.08
San Francisco   260.65
San Jose  429.87
Stockton  247.18
```

So, now that we've tested this on the command line we can test it on the cluster. The best practice when you're developing map reduce jobs is first to test locally with a small data set before you run your code on the entire, huge, set of data. So, now that we've tested on the command line, we can test our code on the cluster. Best practice, when you're developing that reduced jobs, is to first test with a small data set. Before you run your code on your entire huge set of data. But, we're already, pretty, confident here. So, let's just run the thing on the whole `purchases.txt` file.

We'll use the `hs` alias to save some typing. I specified my mapper, my reducer, my input directory, and a new output directory which we'll call output two. And off hadoop goes. It starts running the job. 

**[training@localhost code]** `hs mapper.py reducer.py myinput myoutput`
```
packageJobJar: [mapper.py, reducer.py, /tmp/hadoop-training/hadoop-unjar9030416268142443792/] [] /tmp/streamjob2061235741260030596.jar tmpDir=null
18/07/08 04:08:16 WARN mapred.JobClient: Use GenericOptionsParser for parsing the arguments. Applications should implement Tool for the same.
18/07/08 04:08:16 WARN snappy.LoadSnappy: Snappy native library is available
18/07/08 04:08:16 INFO snappy.LoadSnappy: Snappy native library loaded
18/07/08 04:08:16 INFO mapred.FileInputFormat: Total input paths to process : 1
18/07/08 04:08:17 INFO streaming.StreamJob: getLocalDirs(): [/var/lib/hadoop-hdfs/cache/training/mapred/local]
18/07/08 04:08:17 INFO streaming.StreamJob: Running job: job_201807080307_0001
18/07/08 04:08:17 INFO streaming.StreamJob: To kill this job, run:
18/07/08 04:08:17 INFO streaming.StreamJob: UNDEF/bin/hadoop job  -Dmapred.job.tracker=0.0.0.0:8021 -kill job_201807080307_0001
18/07/08 04:08:17 INFO streaming.StreamJob: Tracking URL: http://0.0.0.0:50030/jobdetails.jsp?jobid=job_201807080307_0001
18/07/08 04:08:18 INFO streaming.StreamJob:  map 0%  reduce 0%
18/07/08 04:08:30 INFO streaming.StreamJob:  map 14%  reduce 0%
18/07/08 04:08:33 INFO streaming.StreamJob:  map 23%  reduce 0%
18/07/08 04:08:36 INFO streaming.StreamJob:  map 32%  reduce 0%
18/07/08 04:08:39 INFO streaming.StreamJob:  map 41%  reduce 0%
18/07/08 04:08:42 INFO streaming.StreamJob:  map 50%  reduce 0%
18/07/08 04:08:59 INFO streaming.StreamJob:  map 83%  reduce 17%
18/07/08 04:09:02 INFO streaming.StreamJob:  map 91%  reduce 17%
18/07/08 04:09:06 INFO streaming.StreamJob:  map 100%  reduce 25%
18/07/08 04:09:09 INFO streaming.StreamJob:  map 100%  reduce 33%
18/07/08 04:09:11 INFO streaming.StreamJob:  map 100%  reduce 68%
18/07/08 04:09:14 INFO streaming.StreamJob:  map 100%  reduce 76%
18/07/08 04:09:18 INFO streaming.StreamJob:  map 100%  reduce 84%
18/07/08 04:09:22 INFO streaming.StreamJob:  map 100%  reduce 90%
18/07/08 04:09:25 INFO streaming.StreamJob:  map 100%  reduce 97%
18/07/08 04:09:27 INFO streaming.StreamJob:  map 100%  reduce 100%
18/07/08 04:09:31 INFO streaming.StreamJob: Job complete: job_201807080307_0001
18/07/08 04:09:31 INFO streaming.StreamJob: Output: myoutput
```

When the job's finished, `hadoop fs -ls` of `myoutput` shows me the just I'd expect is a part-00000 file in that and just as we did before we can `hadoop fs -cat` that file to see our actual results.

**[training@localhost code]** `hadoop fs -ls myoutput`
Found 3 items
```
-rw-r--r--   1 training supergroup          0 2018-07-08 04:09 myoutput/_SUCCESS
drwxr-xr-x   - training supergroup          0 2018-07-08 04:08 myoutput/_logs
-rw-r--r--   1 training supergroup       2296 2018-07-08 04:09 myoutput/part-00000
```
**[training@localhost code]** `hadoop fs -cat myoutput/part-00000`
```
Albuquerque   10052311.42
Anaheim   10076416.36
Anchorage   9933500.4
Arlington   10072207.97
Atlanta   9997146.7
Aurora  9992970.92
Austin  10057158.9
Bakersfield   10031208.92
Baltimore   10096521.45
Baton Rouge   10131273.23
Birmingham  10076606.52
Boise   10039166.74
Boston  10039473.28
Buffalo   10001941.19
Chandler  9919559.86
Charlotte   10112531.34
Chesapeake  10038504.92
Chicago   10062522.07
Chula Vista   9974951.34
Cincinnati  10139505.74
Cleveland   10067835.84
Colorado Springs  10061105.87
Columbus  10035241.03
Corpus Christi  9976522.77
Dallas  10066548.45
Denver  10031534.87
Detroit   9979260.76
Durham  10153890.21
El Paso   10016409.97
Fort Wayne  10132594.02
Fort Worth  10120830.65
Fremont   10053242.36
Fresno  9976260.26
Garland   10071043.92
Gilbert   10062115.19
Glendale  10044493.97
Greensboro  10033781.39
Henderson   10053416.05
Hialeah   10047052.76
Honolulu  10006273.49
Houston   10042106.27
Indianapolis  10090272.77
Irvine  10084867.45
Irving  10133944.08
Jacksonville  10072003.33
Jersey City   9920141.87
Kansas City   9968118.73
Laredo  10144604.98
Las Vegas   10054257.98
Lexington   10084510.95
Lincoln   10069485.4
Long Beach  10006380.25
Los Angeles   10084576.8
Louisville  10008566.47
Lubbock   9958119.15
Madison   10032035.54
Memphis   10038565.32
Mesa  10053642.6
Miami   9947316.07
Milwaukee   10064482.65
Minneapolis   10011757.78
Nashville   9961450.51
New Orleans   9949257.75
New York  10085293.55
Newark  10144052.8
Norfolk   10088563.17
North Las Vegas   10029652.51
Oakland   9947292.52
Oklahoma City   10118986.25
Omaha   10026642.34
Orlando   10074922.52
Philadelphia  10190080.26
Phoenix   10079076.7
Pittsburgh  10090124.82
Plano   10046103.61
Portland  10007635.77
Raleigh   10061442.54
Reno  10079955.16
Richmond  9992941.59
Riverside   10006695.42
Rochester   10067606.92
Sacramento  10123468.18
Saint Paul  10057233.57
San Antonio   10014441.7
San Bernardino  9965152.04
San Diego   9966038.39
San Francisco   9995570.54
San Jose  9936721.41
Santa Ana   10050309.93
Scottsdale  10037929.85
Seattle   9936267.37
Spokane   10083362.98
St. Louis   10002105.14
St. Petersburg  9986495.54
Stockton  10006412.64
Tampa   10106428.55
Toledo  10020768.88
Tucson  9998252.47
Tulsa   10064955.9
Virginia Beach  10086553.5
Washington  10139363.39
Wichita   10083643.21
Winston–Salem   10044011.83
```