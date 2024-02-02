from pysnmp.hlapi import *
import time
import sqlserver

def get_oids(ip_address):
    community = "public_RKF"
    oid = "1.3.6.1.4.1.21796.4.1.3.1.4.1"

    # errorIndication, errorStatus, errorIndex, varBinds = \
    #    getCmd(SnmpEngine(), CommunityData(community), UdpTransportTarget(ip_address, 161), ObjectType(oid), bulk=True)
    
    iterator = getCmd(SnmpEngine(),
        CommunityData(community, mpModel=0),
        UdpTransportTarget((ip_address, 161)),
        ContextData(),
        ObjectType(ObjectIdentity(oid))
    )

    errorIndication, errorStatus, errorIndex, varBinds = next(iterator)

    if errorIndication:
        print(errorIndication)
        return

    if errorStatus:
        print("Error: %s at %s" % (errorStatus.prettyPrint(), errorIndex))
        return

    for varBind in varBinds:
        _value = str(varBind)[str(varBind).find("=")+2:]
        sqlserver.insertTemperature(_value)

t_end = time.time() + 90 * 1
while time.time() < t_end:
    get_oids("192.168.88.200")
    time.sleep(5)
