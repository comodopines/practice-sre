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

```
</p>
</details>
------
