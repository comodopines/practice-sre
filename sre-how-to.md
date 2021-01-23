> Q. How to find high CPU Utilization?
<details><summary>Ans.</summary>
<p>

```
Using top command
Using vmstat
Using sar

Example:
top -n 1 -H -p <pid>

Example:
vmstat 1 20

Example:
sar -u 1 3 Displays real time CPU usage every 1 second for 3 times.
sar -u ALL Same as “sar -u” but displays additional fields.

https://www.thegeekstuff.com/2011/03/sar-examples/

$ sar -P ALL 1 1
Linux 2.6.18-194.el5PAE (dev-db)        03/26/2011      _i686_  (8 CPU)

01:34:12 PM       CPU     %user     %nice   %system   %iowait    %steal     %idle
01:34:13 PM       all     11.69      0.00      4.71      0.69      0.00     82.90
01:34:13 PM         0     35.00      0.00      6.00      0.00      0.00     59.00
01:34:13 PM         1     22.00      0.00      5.00      0.00      0.00     73.00
01:34:13 PM         2      3.00      0.00      1.00      0.00      0.00     96.00
01:34:13 PM         3      0.00      0.00      0.00      0.00      0.00    100.00

$ sar -P 1 1 1
Linux 2.6.18-194.el5PAE (dev-db)        03/26/2011      _i686_  (8 CPU)

01:36:25 PM       CPU     %user     %nice   %system   %iowait    %steal     %idle
01:36:26 PM         1      8.08      0.00      2.02      1.01      0.00     88.89

```
</p>
</details>
------

> Q. How do I collect JVM data for troubleshooting - stack trace?
<details><summary>Ans.</summary>
<p>

```
Collect thread dump or stack trace.

kill -3 pid

PID=<pid>;jstack -F -l ${PID} > $(date +"%Y%m%d%H%M%S")_jstack_${PID}.log
```
</p>
</details>
------

> Q. How do I collect JVM data for troubleshooting - stack trace?
<details><summary>Ans.</summary>
<p>

```
Collect thread dump or stack trace.

kill -3 pid

PID=<pid>;jstack -F -l ${PID} > $(date +"%Y%m%d%H%M%S")_jstack_${PID}.log

jcmd <pid> Thread.print > <file-path>

jvisualVM has option to do thread dump on screen

https://blog.fastthread.io/2016/06/06/how-to-take-thread-dumps-7-options/
```
</p>
</details>
------

> Q. How do I collect JVM data for troubleshooting - heap dumps/heap histograms?
<details><summary>Ans.</summary>
<p>

```
For heap historgrams try:
jmap -histo:live <pid>

For heap dumps try
jmap -dump:live,format=b,file=/tmp/dump.hprof 12587
jmap -dump:format=b,file=c:\temp\HeapDump.hprof <pid>

jcmd <pid> GC.heap_dump <file-path>

java -XX:+HeapDumpOnOutOfMemoryError -XX:HeapDumpPath=<file-or-dir-path>
https://www.baeldung.com/java-heap-dump-capture
```
</p>
</details>
------

> Q. How to find current jvm settings?
<details><summary>Ans.</summary>
<p>

```
jinfo <pid>

```
</p>
</details>
------


> Q. How to print garbage collection logs?
<details><summary>Ans.</summary>
<p>

```

-Xloggc:<confluence-home>/logs/`date +%F_%H-%M-%S`-gc.log -XX:+PrintGCDetails -XX:+PrintGCDateStamps -XX:+PrintTenuringDistribution -XX:+PrintGCCause
-XX:+UseGCLogFileRotation -XX:NumberOfGCLogFiles=10 -XX:GCLogFileSize=5M
```
</p>
</details>
------
