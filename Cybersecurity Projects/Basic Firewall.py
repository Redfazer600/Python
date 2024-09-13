####################
# Basic Firewall
# Alex Bevan - UP2198095
# Disc: A breakdown of how a basic firewall works - easy understanding of firewalls
####################

# Imports
from random import randint
from time import sleep

# Misc function to generate IP addresses to simulate network traffic
def generateRandomIp():
    return f'10.0.0.{randint(0, 9)}'

# Function to check if the network traffic is allowed or not based off the assigned firewall rules
def enterFirewall(networkTrafficIP, firewallRestrctions):
    if networkTrafficIP in firewallRestrctions:
        return 'Blocked IP'
    return 'Allowed IP'


# The list containing the firewall rules
firewallBlockList = ['10.0.0.2', '10.0.0.5', '10.0.0.6', '10.0.0.8']

for i in range(10):     # looped to simulate - every loop the traffic enters the firewall and gets checked by firewall
    networkTraffic = generateRandomIp()
    firewallResponse = enterFirewall(networkTraffic, firewallBlockList)
    print(f'IP {networkTraffic}, Firewall Response: {firewallResponse}')
    sleep(1)
