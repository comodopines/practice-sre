> Q. How do I find which engines are using high memory?
<details><summary>Ans.</summary>
<p>

```
https://www.eurovps.com/faq/how-to-troubleshoot-high-memory-usage-in-linux/
  
 1) Confirm if free reports free memory
 $free -m
              total        used        free      shared  buff/cache   available
 Mem:           7875         859        6228         303         787        6472
 Swap:            99           0          99
-------

 2) Look for memory usage using vmstat
 $ vmstat -SM -w 1 5
 procs -----------------------memory---------------------- ---swap-- -----io---- -system-- --------cpu--------
 r  b         swpd         free         buff        cache   si   so    bi    bo   in   cs  us  sy  id  wa  st
 1  0            0         6485           53          642    0    0     1     0   24   13   0   0 100   0   0
 0  0            0         6478           53          649    0    0     0     0  265  288   0   1  99   0   0
 0  0            0         6478           53          649    0    0     0     0  326  407   1   1  98   0   0
 0  0            0         6477           53          650    0    0     0     0  467  526   1   1  98   0   0
 
 If Free sections are low or swpd are high then chances are there is memory stress.
-------

 3) Confirm if memroy average usage has been high on system using sar
 $echo -n `sar -r -f /var/log/sysstat/sa20 | head -n 1 | awk '{print $4}'`; echo `sar -r -f /var/log/sysstat/sa20  | grep -i Average | sed "s/Average://"`

 05/20/2021      5990288   6244140   1146084     14.21     55736    805264   6165276     75.49   1314812    383940       160

 First part of cmmand picks date from sar file and prints without newline - echo -n `sar -r -f /var/log/sysstat/sa20 | head -n 1 | awk '{print $4}'`
 Second part of command just picks the average line and removes "Average" word - echo `sar -r -f /var/log/sysstat/sa20  | grep -i Average | sed "s/Average://"`
-------
 
 4) Once the history of usage has been established it can be compared to runnning averages using vmstat or sar -r
-------
 
 5) Use the following command to find the highest memory usage of processes
 ps -eo pid,ppid,cmd,%mem,%cpu --sort=-%mem | head
 
   PID  PPID CMD                         %MEM %CPU
18075 15799 /usr/lib/chromium-browser/c  3.2  4.2
15821 15794 /usr/lib/chromium-browser/c  2.9 11.8
16920 15799 /usr/lib/chromium-browser/c  2.9  2.9
15767   901 /usr/lib/chromium-browser/c  2.9 13.0
17582 15799 /usr/lib/chromium-browser/c  2.1  4.0
17541 15799 /usr/lib/chromium-browser/c  1.9 36.3
17384 15799 /usr/lib/chromium-browser/c  1.9  5.9
17070 15799 /usr/lib/chromium-browser/c  1.8  7.3
17282 15799 /usr/lib/chromium-browser/c  1.6  4.4

ps -eo pid,ppid,cmd,%mem,%cpu --sort=-%cpu | head
   PID  PPID CMD                         %MEM %CPU
 17541 15799 /usr/lib/chromium-browser/c  1.9 36.2
 15767   901 /usr/lib/chromium-browser/c  2.9 12.9
 15821 15794 /usr/lib/chromium-browser/c  2.9 11.8
 17070 15799 /usr/lib/chromium-browser/c  1.8  7.3
 17384 15799 /usr/lib/chromium-browser/c  1.9  5.9
 
 PS NOTE ON CPU- CPU usage is currently expressed as the percentage of time spent running during the entire lifetime of a process. This is not ideal, and it does 
 not  conform to the standards that ps otherwise conforms to.  CPU usage is unlikely to add up to exactly 100%.
 
 Depending on how you look at it, ps is not reporting the real memory usage of processes. What it is really doing is showing how much real memory each process would take up if it were the only process running. Of course, a typical Linux machine has several dozen processes running at any given time, which means that the VSZ and RSS numbers reported by ps are almost definitely wrong as it includes the shared memory pages in there.
 
-------
6) Detailed analysis using pmap
 https://stackoverflow.com/a/2816070
-------

7) How to find detailed analysis on the memory on redhat page:
  https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/5/html/tuning_and_optimizing_red_hat_enterprise_linux_for_oracle_9i_and_10g_databases/chap-oracle_9i_and_10g_tuning_guide-memory_usage_and_page_cache
  
 http://virtualthreads.blogspot.com/2006/02/understanding-memory-usage-on-linux.html
 
 https://stackoverflow.com/a/2816070
 

```
</p>
</details>
------

> Q. What is difference between buffers and cache?
<details><summary>Ans.</summary>
<p>

```
buffers - (file system metadata)
cache - (pages with actual contents of files or block devices)

This helps the system to run faster because disk information is already in memory which saves I/O operations. If space is needed by programs or applications like Oracle, then Linux will free up the buffers and cache to yield memory for the applications. If your system runs for a while you will usually see a small number under the field "free" on the first line.

  
  https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/5/html/tuning_and_optimizing_red_hat_enterprise_linux_for_oracle_9i_and_10g_databases/chap-oracle_9i_and_10g_tuning_guide-memory_usage_and_page_cache
  

```
</p>
</details>
------



> Q. How do I collect JVM data for troubleshooting - stack trace?
<details><summary>Ans.</summary>
<p>

```
Collect thread dump or stack trace.

1) kill -3 pid

2) PID=<pid>;jstack -F -l ${PID} > $(date +"%Y%m%d%H%M%S")_jstack_${PID}.log

3) jcmd <pid> Thread.print > <file-path>

4) jvisualVM has option to do thread dump on screen

https://blog.fastthread.io/2016/06/06/how-to-take-thread-dumps-7-options/
```
</p>
</details>
------

> Q. How do I collect JVM data for troubleshooting - heap dumps/heap histograms?
<details><summary>Ans.</summary>
<p>

```
1) For heap historgrams try:
jmap -histo:live <pid>

2) For heap dumps try
a) jmap -dump:live,format=b,file=/tmp/dump.hprof 12587
b) jmap -dump:format=b,file=c:\temp\HeapDump.hprof <pid>

c) jcmd <pid> GC.heap_dump <file-path>

d) java -XX:+HeapDumpOnOutOfMemoryError -XX:HeapDumpPath=<file-or-dir-path>
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

> Q. How to set various JVM options?
<details><summary>Ans.</summary>
<p>

```
-Xms	For setting the initial heap size when JVM starts

-Xmx	For setting the maximum heap size.

-Xmn	For setting the size of the Young Generation, rest of the space goes for Old Generation.

-XX:PermGen	For setting the initial size of the Permanent Generation memory

-XX:MaxPermGen	For setting the maximum size of Perm Gen

-XX:SurvivorRatio	For providing ratio of Eden space and Survivor Space, 
for example if Young Generation size is 10m and VM switch is -XX:SurvivorRatio=2 
then 5m will be reserved for Eden Space and 2.5m each for both the Survivor spaces. The default value is 8.
Ratio of 8 means 1:1:8 each survior space is 1/10th of total. 1/10 + 1/10 + 8/10 (or 1:8 between survivor and eden)

-XX:NewRatio	For providing ratio of old/new generation sizes. The default value is 2.
```
</p>
</details>
------


> Q. How to watch memory usage of a JVM?
<details><summary>Ans.</summary>
<p>

```
jstat -gc <pid> <time in ms>

xxxx@xxxx:~$ jstat -gc 9582 1000
 S0C    S1C    S0U    S1U      EC       EU        OC         OU       PC     PU        YGC     YGCT    FGC    FGCT     GCT
1024.0 1024.0  0.0    0.0    8192.0   7933.3   42108.0    23401.3   20480.0 19990.9    157    0.274  40      1.381    1.654
1024.0 1024.0  0.0    0.0    8192.0   8026.5   42108.0    23401.3   20480.0 19990.9    157    0.274  40      1.381    1.654
1024.0 1024.0  0.0    0.0    8192.0   8030.0   42108.0    23401.3   20480.0 19990.9    157    0.274  40      1.381    1.654
1024.0 1024.0  0.0    0.0    8192.0   8122.2   42108.0    23401.3   20480.0 19990.9    157    0.274  40      1.381    1.654
1024.0 1024.0  0.0    0.0    8192.0   8171.2   42108.0    23401.3   20480.0 19990.9    157    0.274  40      1.381    1.654
1024.0 1024.0  48.7   0.0    8192.0   106.7    42108.0    23401.3   20480.0 19990.9    158    0.275  40      1.381    1.656
1024.0 1024.0  48.7   0.0    8192.0   145.8    42108.0    23401.3   20480.0 19990.9    158    0.275  40      1.381    1.656

```
</p>
</details>
------

