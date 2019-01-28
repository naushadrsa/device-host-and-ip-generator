# device-host-and-ip-generator

Generates a list of hosts and/or IPs for custom feeds to populate into device.ip or device.host.

Why is this necessary?

Unlike RSA enVision, NetWitness does not currently do DNS or Reverse DNS lookups. That is, when you have a Syslog event source log to NetWitness, there will only be device.ip populated (no device.host). Contrastly, if you setup a Log Collection process to collect logs and enter the "hostname" of the Event Source, then device.host will be populated in Investigator (not the device.ip). The output from this script can be used as input to Custom Feeds to ensure both device.ip and device.host are populated so users can search based on either key.

This script leverages a REST call to the Log Decoder (you specificied when you run the script). It then pulls a list of all "sources" from the Log Decoder and creates a list of IPs or Hosts to process.

If IP is found:
It will run a reverse DNS query to look up the hostname and populate a CSV file (deviceip2devicehost.csv)

If Hostname is found:
It will run a DNS query to lookup the IP and populate a CSV file (devicehost2deviceip.csv)
You can then use these 2 CSVs in separate Custom Feeds within the NetWitness UI to manage any device.host and populate the device.ip or vice versa.
