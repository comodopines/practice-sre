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

