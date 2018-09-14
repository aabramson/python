from pysnmp.hlapi import *
import sys
def walk(host,community,oid):


    for (errorIndication,errorStatus,errorIndex,varBinds) in nextCmd(SnmpEngine(),
                                                             CommunityData(community),
                                                             UdpTransportTarget((host, 161)),
                                                             ContextData(),
                                                             ObjectType(ObjectIdentity(oid)),
                                                             lexicographicMode=False):
        if errorIndication:

            print(errorIndication, file=sys.stderr)

            break

        elif errorStatus:

            print('%s at %s' % (errorStatus.prettyPrint(),
                                errorIndex and varBinds[int(errorIndex) - 1][0] or '?'), file=sys.stderr)

            break

        else:

            for varBind in varBinds:

                print(varBind)

#ip=input('Digite o IP do equipamento: ')
#com=input('Digite a community: ')
#oid=input('Digite a OID em formato decimal: ')

#walk(ip,com,oid)
walk('192.168.10.2','r0utz','1.3.6.1.2.1.1.1.0')   ### se quiser usar em formato standalone...
