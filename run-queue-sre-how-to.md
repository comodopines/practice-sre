 > Q. How do I find what is current run queue?
<details><summary>Ans.</summary>
<p>

```
 
 1) Confirm using vmstat under First column "r" under procs-group
 $ vmstat -SM -w 1 5
 procs -----------------------memory---------------------- ---swap-- -----io---- -system-- --------cpu--------
 r  b         swpd         free         buff        cache   si   so    bi    bo   in   cs  us  sy  id  wa  st
 1  0            0         6485           53          642    0    0     1     0   24   13   0   0 100   0   0
 0  0            0         6478           53          649    0    0     0     0  265  288   0   1  99   0   0
 0  0            0         6478           53          649    0    0     0     0  326  407   1   1  98   0   0
 0  0            0         6477           53          650    0    0     0     0  467  526   1   1  98   0   0
 
 
 
 2) Confirm using sar with -q flag under runq-sz 
 $ sar -q 1 5
Linux 5.4.79-v7l+ (raspberrypi) 	05/20/2021 	_armv7l_	(4 CPU)

02:59:26 PM   runq-sz  plist-sz   ldavg-1   ldavg-5  ldavg-15   blocked
02:59:27 PM         0       779      1.05      1.96      1.42         0
02:59:28 PM         0       780      1.05      1.96      1.42         0
02:59:29 PM         0       781      1.05      1.96      1.42         0
02:59:30 PM         0       781      1.05      1.96      1.42         0
02:59:31 PM         0       780      1.05      1.96      1.42         0

"runq-sz - Run queue length (number of tasks waiting for run time)" and 
 "plist-sz Number of tasks in the task list."
-------

```
</p>
</details>
------

> Q. Where does vmstat pick blocked and running process stats from?
<details><summary>Ans.</summary>
<p>

```
 $ awk '{print $3}' /proc/*/stat | sort -n | uniq
 
```
</p>
</details>
------



 > Q. How does runq-sz or "r" relate to load on system and how do you check system load?
<details><summary>Ans.</summary>
<p>

```
 
 Load average can be checked via following commands:
 
 1) uptime
 
 $uptime
 15:10:24 up 1 day, 23:32,  2 users,  load average: 0.70, 0.82, 1.02

 2) top
 
 top - 16:46:58 up 2 days,  1:09,  2 users,  load average: 1.12, 0.47, 0.17
 Tasks: 205 total,   1 running, 204 sleeping,   0 stopped,   0 zombie
 %Cpu(s):  2.4 us,  2.7 sy,  0.0 ni, 94.9 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
 MiB Mem :   7875.9 total,   5055.7 free,   1662.7 used,   1157.5 buff/cache
 MiB Swap:    100.0 total,    100.0 free,      0.0 used.   5321.5 avail Mem 

 3) sar
 
 $ sar -q 1 5
Linux 5.4.79-v7l+ (raspberrypi) 	05/20/2021 	_armv7l_	(4 CPU)

02:59:26 PM   runq-sz  plist-sz   ldavg-1   ldavg-5  ldavg-15   blocked
02:59:27 PM         0       779      1.05      1.96      1.42         0
02:59:28 PM         0       780      1.05      1.96      1.42         0
02:59:29 PM         0       781      1.05      1.96      1.42         0
02:59:30 PM         0       781      1.05      1.96      1.42         0
02:59:31 PM         0       780      1.05      1.96      1.42         0

run queue size reported by sar can be 0 if the process is in un-interruptable sleep "D"
Check un-interruptable sleep process as they will be eating cpu usage (load average) even though there aren't anything to run.

ps -Leo state,pid,args | grep '^[RD]' 

```
</p>
</details>
------

> Q. What is blocked queue in vmstat output?
<details><summary>Ans.</summary>
<p>

```
 $ vmstat -SM -w 1 5
 procs -----------------------memory---------------------- ---swap-- -----io---- -system-- --------cpu--------
 r  b         swpd         free         buff        cache   si   so    bi    bo   in   cs  us  sy  id  wa  st
 1  0            0         6485           53          642    0    0     1     0   24   13   0   0 100   0   0
 0  0            0         6478           53          649    0    0     0     0  265  288   0   1  99   0   0
 0  0            0         6478           53          649    0    0     0     0  326  407   1   1  98   0   0
 0  0            0         6477           53          650    0    0     0     0  467  526   1   1  98   0   0
 
 
 Blocked process in "procs/b" column are process in uninterruptable sleep. Process which are waiting for an I/O. 
 High-speed I/O or some other external event. If your system consistentantly has large number , you may
have disk throughput problems. This doesnt take into account processes waiting for terminal I/O.

Try running iostat see what is going on with your disks it may be that you
have got heavily used logical volumes on 1 disk when they could be moved.
```
</p>
</details>
------

> Q. How can blocked queue in vmstat relate to IO debug?
<details><summary>Ans.</summary>
<p>

```
 $ vmstat -SM -w 1 5
 procs -----------------------memory---------------------- ---swap-- -----io---- -system-- --------cpu--------
 r  b         swpd         free         buff        cache   si   so    bi    bo   in   cs  us  sy  id  wa  st
 1  0            0         6485           53          642    0    0     1     0   24   13   0   0 100   0   0
 0  0            0         6478           53          649    0    0     0     0  265  288   0   1  99   0   0
 0  0            0         6478           53          649    0    0     0     0  326  407   1   1  98   0   0
 0  0            0         6477           53          650    0    0     0     0  467  526   1   1  98   0   0
 
 
```
</p>
</details>
------
