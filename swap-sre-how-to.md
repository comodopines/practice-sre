> Q. Where does vmstat pick swapd data from?
<details><summary>Ans.</summary>
<p>

```
 $ ls -l /proc/meminfo 
-r--r--r-- 1 root root 0 May 18 16:01 /proc/meminfo
 $
 $ grep -i swap /proc/meminfo
 SwapCached:            0 kB
 SwapTotal:        102396 kB
 SwapFree:         102396 kB

```
</p>
</details>
------

> Q. How to find what is current swap usages besides vmstat and /proc/meminfo?
<details><summary>Ans.</summary>
<p>

```
 $ free -g
 $ top
```
</p>
</details>
------

> Q. How to find what the process using the most swap?
<details><summary>Ans.</summary>
<p>

```
 You can use the /proc/<pid>/status file to check the vmswap used.
 
 $ for file in `ls -1 /proc/*/status` ; do echo $file" : "`awk '/VmSwap/{print $2 " " $3;}' $file`; done 2>/dev/null | sort -nr -k2

```
</p>
</details>
------
