from pysnmp.hlapi import *
import time

def get_snmp_data(oid, host, community):
    errorIndication, errorStatus, errorIndex, varBinds = next(
        getCmd(SnmpEngine(),
               CommunityData(community),
               UdpTransportTarget((host, 161)),
               ContextData(),
               ObjectType(ObjectIdentity(oid)))
    )

    if errorIndication:
        print(errorIndication)
    elif errorStatus:
        print('%s at %s' % (errorStatus.prettyPrint(),
                            errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
    else:
        for varBind in varBinds:
            return varBind[1]

def calculate_bandwidth_utilization(host, community, interface_index):
    ifInOctets_oid = f'1.3.6.1.2.1.2.2.1.10.{interface_index}'
    ifOutOctets_oid = f'1.3.6.1.2.1.2.2.1.16.{interface_index}'
    ifSpeed_oid = f'1.3.6.1.2.1.2.2.1.5.{interface_index}'

    ifInOctets1 = get_snmp_data(ifInOctets_oid, host, community)
    ifOutOctets1 = get_snmp_data(ifOutOctets_oid, host, community)
    time.sleep(5)  # wait for 5 seconds
    ifInOctets2 = get_snmp_data(ifInOctets_oid, host, community)
    ifOutOctets2 = get_snmp_data(ifOutOctets_oid, host, community)

    delta_ifInOctets = ifInOctets2 - ifInOctets1
    delta_ifOutOctets = ifOutOctets2 - ifOutOctets1
    ifSpeed = get_snmp_data(ifSpeed_oid, host, community)

    bandwidth_utilization_in = (delta_ifInOctets * 8 * 100) / (ifSpeed * 5)
    bandwidth_utilization_out = (delta_ifOutOctets * 8 * 100) / (ifSpeed * 5)

    return bandwidth_utilization_in, bandwidth_utilization_out

# usage
host = 'your.snmp.device'
community = 'your_community_string'
interface_index = 'your_interface_index'
bandwidth_utilization_in, bandwidth_utilization_out = calculate_bandwidth_utilization(host, community, interface_index)
print(f'Input Bandwidth Utilization: {bandwidth_utilization_in}%')
print(f'Output Bandwidth Utilization: {bandwidth_utilization_out}%')



######

from pysnmp.hlapi import *
from datetime import timedelta

class snmp_monitor:
    def __init__(self,ip,community):
        self.ip=ip
        self.community=community
#return device name

    def get_devicename(self):
        errorIndication, errorStatus, errorIndex, varBinds = next(
            getCmd(SnmpEngine(),
                   CommunityData('ali'),
                   UdpTransportTarget(('192.168.1.1', 161)),
                   ContextData(),
                   ObjectType(ObjectIdentity('.1.3.6.1.2.1.1.5.0')))
        )

        if errorIndication:
            print(errorIndication)
        elif errorStatus:
            print('%s at %s' % (errorStatus.prettyPrint(),
                                errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
        else:
            for varBind in varBinds:
                print(varBind[1])
#return the interfaces using getnext

    def get_interfaces(self):
        iterator = nextCmd(SnmpEngine(),
                   CommunityData(self.community),
                   UdpTransportTarget((self.ip, 161)),
                   ContextData(),
                   ObjectType(ObjectIdentity('.1.3.6.1.2.1.2.2.1.2')),
                   maxCalls=self.get_numberofinter()
        )


        for errorIndication, errorStatus, errorIndex, varBinds in iterator:
            if errorIndication:
                print(errorIndication)
                break

            elif errorStatus:
                print('%s at %s' % (errorStatus.prettyPrint(),
                                    errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
                break

            else:
                for varBind in varBinds:
                    print(varBind[1])
#return the number of interfaces using get

    def get_numberofinter(self):
        errorIndication, errorStatus, errorIndex, varBinds = next(
            getCmd(SnmpEngine(),
                   CommunityData(self.community),
                   UdpTransportTarget((self.ip, 161)),
                   ContextData(),
                   ObjectType(ObjectIdentity('.1.3.6.1.2.1.2.1.0')))
        )

        if errorIndication:
            print(errorIndication)
        elif errorStatus:
            print('%s at %s' % (errorStatus.prettyPrint(),
                                errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
        else:
            for varBind in varBinds:
                return varBind[1]
#return uptime of the device
    def get_uptime(self):
        errorIndication, errorStatus, errorIndex, varBinds = next(
            getCmd(SnmpEngine(),
                   CommunityData(self.community),
                   UdpTransportTarget((self.ip, 161)),
                   ContextData(),
                   ObjectType(ObjectIdentity('.1.3.6.1.2.1.1.3.0')))
        )

        if errorIndication:
            print(errorIndication)
        elif errorStatus:
            print('%s at %s' % (errorStatus.prettyPrint(),
                                errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
        else:
            for varBind in varBinds:
                s = int(varBind[1])
                seconds = int(s / 100)
                up_time = timedelta(seconds=seconds)
                print(up_time)

m=snmp_monitor('192.168.1.1','ali')
m.get_devicename()
