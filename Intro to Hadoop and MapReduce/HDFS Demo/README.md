Here I have a directory on my local machine, which contains a couple of files, and I want to put one of them into hdfs. 

**[training@localhost data]** `ls`
access_log.gz  purchases.txt

All of the commands which interact with the Hadoop file system start with **hadoop fs**. So first of all, let's see what we have in hdfs to start with. I do that by saying **hadoop fs -ls**. That gives me a listing of what's in my home directory on the Hadoop cluster. Because I'm logged in to the local machine as a user called training, my home directory in hdfs is /user/training. 

**[training@localhost data]** `hadoop fs -ls`

And as you can see, there's nothing there. So now, let's upload our purchases.txt file. We do that with **hadoop fs -put purchases.txt**. `hadoop fs -put` takes a local file and places it into hdfs. Since I'm not specifying a destination filename, it'll be uploaded with the same filename. 

**[training@localhost data]** `hadoop fs -put purchases.txt `

So, it takes a few seconds to upload. And now I can do another **hadoop fs -ls**, and we can see that that file is now in hdfs. 

**[training@localhost data]** `hadoop fs -ls`
Found 1 items
-rw-r--r--   1 training supergroup  211312924 2018-07-07 15:58 purchases.txt

I can take a look at the last few lines of the file by saying, **hadoop fs -tail**, and then the filename, and that just displays the last few lines on the screen for me. 

**[training@localhost data]** `hadoop fs -tail purchases.txt `
```
31	17:59	Norfolk	Toys	164.34	MasterCard
2012-12-31	17:59	Chula Vista	Music	380.67	Visa
2012-12-31	17:59	Hialeah	Toys	115.21	MasterCard
2012-12-31	17:59	Indianapolis	Men's Clothing	158.28	MasterCard
2012-12-31	17:59	Norfolk	Garden	414.09	MasterCard
2012-12-31	17:59	Baltimore	DVDs	467.3	Visa
2012-12-31	17:59	Santa Ana	Video Games	144.73	Visa
2012-12-31	17:59	Gilbert	Consumer Electronics	354.66	Discover
2012-12-31	17:59	Memphis	Sporting Goods	124.79	Amex
2012-12-31	17:59	Chicago	Men's Clothing	386.54	MasterCard
2012-12-31	17:59	Birmingham	CDs	118.04	Cash
2012-12-31	17:59	Las Vegas	Health and Beauty	420.46	Amex
2012-12-31	17:59	Wichita	Toys	383.9	Cash
2012-12-31	17:59	Tucson	Pet Supplies	268.39	MasterCard
2012-12-31	17:59	Glendale	Women's Clothing	68.05	Amex
2012-12-31	17:59	Albuquerque	Toys	345.7	MasterCard
2012-12-31	17:59	Rochester	DVDs	399.57	Amex
2012-12-31	17:59	Greensboro	Baby	277.27	Discover
2012-12-31	17:59	Arlington	Women's Clothing	134.95	MasterCard
2012-12-31	17:59	Corpus Christi	DVDs	441.61	Discover
```

There's also a `hadoop fs -cat`, which will display the entire contents of the file. There are plenty of other hadoop fs commands and as you'll probably have started to realize, they closely mirror standard UNIX file system commands. So, if I want to rename the file, for example, I can say **hadoop fs -mv**, which moves purchases.txt, in this case, to newname.txt. 

**[training@localhost data]** `hadoop fs -mv purchases.txt newname.txt`
**[training@localhost data]** `hadoop fs -ls`
Found 1 items
-rw-r--r--   1 training supergroup  211312924 2018-07-07 15:58 newname.txt

If I want to delete a file, **hadoop fs -rm** will remove that file for me. So, let's get rid of newname.txt from hdfs. 

**[training@localhost data]** `hadoop fs -rm newname.txt`
Deleted newname.txt

I create a directory in hdfs by saying **hadoop fs -mkdir** and then the directory name, and now let's upload purchases.txt and place it in the myinput directory so that it's ready for processing by hdfs. Once I've done that, `hadoop fs -ls myinput` will show me the contents of that directory. And just as I expected, there's the file.

**[training@localhost data]** `hadoop fs -mkdir myinput`
**[training@localhost data]** `hadoop fs -put purchases.txt myinput`
**[training@localhost data]** `hadoop fs -ls myinput`
Found 1 items
-rw-r--r--   1 training supergroup  211312924 2018-07-07 16:00 myinput/purchases.txt

