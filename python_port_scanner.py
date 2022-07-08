# /usr/bin/python3
# Filename : test_port_scanner.py

"""
A basic port-scanner in python, using standard socket libraries.
"""

import socket
import subprocess
import sys
import argparse
from datetime import datetime

def scan_ports(remoteServer, start_port='1', end_port='1000'):

    # Clear the screen
    subprocess.call('clear', shell=True)

    remoteServerIP = socket.gethostbyname(remoteServer)
    start_port = int(start_port)
    end_port = int(end_port)

    # Print a banner with information on which host we are about to scan
    print ("-" * 60)
    print ("Please wait, scanning remote host", remoteServerIP)
    print ("On ports: ", start_port, "to", end_port)
    print ("-" * 60)
    print ('\n')

    # Check what time the scan started
    begin_time = datetime.now()

    # Take the user input of 'start_port' and 'end_port' numbers and place them in a range
    # These are the port numbers to be scanned
    try:
        for port in range(start_port, end_port):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result = sock.connect_ex((remoteServerIP, port))
            if result == 0:
                print ("Port {}: \t Open".format(port))
            sock.close()

    # Error handling in the event host cannot be reached or no DNS available
    except KeyboardInterrupt:
        print ("You pressed Ctrl+C")
        sys.exit()

    except socket.gaierror:
        print ('Hostname could not be resolved. Exiting')
        sys.exit()

    except socket.error:
        print ('Socket creation failed. Error code: ' + str(socket.error[0]) + ' Error message: ' + socket.error[1])
        sys.exit()

    # Check the time once scan is complete, and compare the start - end times.
    end_time = datetime.now()
    total = end_time - begin_time

    # Print the scan time information
    print ('\n')
    print ('-' * 60)
    print ('Scanning Completed in: ', total)
    print ('-' * 60)

if __name__ == "__main__":
    # Command line arguments
    parser = argparse.ArgumentParser(description='Remote Port Scanner')
    parser.add_argument('--remoteServer', action="store", dest="remoteServerIP", default='localhost')
    parser.add_argument('--start-port', action="store", dest="start_port", default=1, type=int)
    parser.add_argument('--end-port', action="store", dest="end_port", default=100, type=int)
    # Parse arguments
    given_args = parser.parse_args()
    scan_ports(given_args.remoteServerIP, given_args.start_port, given_args.end_port)