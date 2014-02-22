nmap2afterglow
==============

Converts NMAP XML traceroute output to an afterglow input file for rapid creation of network diagrams.

How to use nmap2afterglow:

<pre>
# python .\nmap2afterglow.py -h
usage: nmap2afterglow.py [-h] [-o OUTPUT] source

Converts Nmap XML output to Afterglow friendly input format

positional arguments:
  source                Source file.

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Destination file.
</pre>

<pre>

# python .\nmap2afterglow.py .\testdata.xml
192.168.55.1,192.168.55.1
192.168.55.1,142.254.148.25
142.254.148.25,184.59.243.211
184.59.243.211,65.29.1.38
65.29.1.38,107.14.19.58
107.14.19.58,107.14.19.135
107.14.19.135,66.109.9.66
66.109.9.66,209.85.252.46
209.85.252.46,72.14.236.148
72.14.236.148,66.249.95.229
66.249.95.229,72.14.234.55
72.14.234.55,8.8.8.8
192.168.55.1,192.168.55.1
192.168.55.1,142.254.148.25
142.254.148.25,184.59.243.211
184.59.243.211,65.29.1.38
65.29.1.38,66.109.6.70
66.109.6.70,66.109.1.49
66.109.1.49,74.125.49.181
74.125.49.181,72.14.236.152
72.14.236.152,209.85.246.37
209.85.246.37,72.14.237.132
72.14.237.132,209.85.240.150
209.85.240.150,74.125.225.96

</pre>
