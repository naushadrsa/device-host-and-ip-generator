#!/usr/bin/env python2

import requests
import sys
import getpass
import socket

"""
HTTP GET of the logStats from Log Decoder REST interface
"""
def httpGet(host, port):
    # Open CSV for writing
    # TODO: the path to this CSV will eventually point to the dropzone on NW Server (Node0) to host the CSV for custom feed ingest
    fpip = open("deviceip2devicehost.csv", "w")
    fphost = open("devicehost2deviceip.csv", "w")
    L = list() # empty list

    # get all data from logStats
    url = "http://%s:%s/decoder?msg=logStats&force-content-type=text/plain" % (host, port)
    r = requests.get(url, auth=(user, passwd))
    for line in r.content.splitlines():
        if "." in line:
            device = line.strip().split(" ")[4].split("=")[1]
            L.append(device)

    # sort the list into a set (unique list)
    sorted = set(L)
    
    # DNS lookup
    for device in sorted:

        try:
            socket.inet_aton(device)
            datatype = "IP"
        except:
            datatype = "HOST"

        # check here if IP, if not then do the 2nd part of the try/expect
        try:

            # if IP
            if "IP" in datatype:
                dns,a,b = socket.gethostbyaddr(device)

                # Write to CSV
                output = "%s,%s\n" % (device, dns)
                fpip.write(output)
            else:
                dns = socket.gethostbyname(device)
                # Write to CSV
                output = "%s,%s\n" % (device, dns)
                fphost.write(output)
        except:
            pass
            
    # Close CSV file
    fpip.close();
    fphost.close();

"""
"main" logic
"""
user = raw_input("Username: ")
passwd = getpass.getpass("Password for " + user + ": ")
host = raw_input("Host (Log Decoder): ")
port = "50102"
httpGet(host, port)
