class inventory:
    switches = { '192.168.152.187' : 'Switch_VSS',
            '192.168.130.195' : 'SWA-WELLS',
            '192.168.130.181' : 'SWA-WHOUSE',
            '192.168.130.190' : 'SWA-VIP',
            '192.168.130.139' : 'SWA1_Z1_IPTV',
            '192.168.130.100' : 'LT2-INETEC-SWA2.OFRKF.DZ',   
            '192.168.130.180' : 'ADMIN_STACK_SW',
            '192.168.130.147' : 'SWA-VIP-IPTV',
            '192.168.130.198' : 'SWA-DC-IDRAC',
            '192.168.130.188' : 'OPVOIP',
            '192.168.130.187' : 'SVR_FARM1',
            '192.168.130.103' : 'SWA-ITT',
            '192.168.130.190' : 'SWA-VIP',
            '192.168.130.195' : 'SWA-WELLS',
            '192.168.130.144' : 'SWA_Z4_IPTV',
            '192.168.130.145' : 'SWA_Z5_IPTV',
            '192.168.130.196' : 'SWA-Z4-DATA',
            '192.168.130.176' : 'SWA-Z1-WIFI',
            '192.168.130.189' : 'SWA-INITEC-WLAN-LT1',
            '192.168.130.149' : 'LT1-INETEC-SWA2',
            '192.168.130.173' : 'SWA-DC-WIFI',
            '192.168.130.193' : 'SWA-IT-OFFICE',
            '192.168.130.146' : 'SWA_DC_IPTV',
            '192.168.130.183' : 'SWA-Room-Z5.OFRKF.DZ',
            '192.168.130.184' : 'SWA-Security',
            '192.168.130.181' : 'SWA-WHOUSE',
            '192.168.130.197' : 'SWA-ADMANNEX'     
    }


"""
Device ID        Local Intrfce     Holdtme    Capability  Platform  Port ID
00b670d11042     Gig 2/2/24        139              S I   SF302-08P gi1
RKF-DC-WLC01     Gig 2/7/41        170               H    AIR-CT350 Gig 0/0/1
RKF-DC-WLC01     Gig 2/7/42        170               H    AIR-CT350 Gig 0/0/2
RKF-DC-WLC01     Gig 2/7/43        170               H    AIR-CT350 Gig 0/0/3
RKF-DC-WLC01     Gig 2/7/44        170               H    AIR-CT350 Gig 0/0/4
00b670d10ff4     Gig 2/2/18        123              S I   SF302-08P gi2
SWA1_Z1_IPTV     Gig 2/2/1         131              S I   WS-C2960X Gig 1/0/49
LT2-INETEC-SWA2.OFRKF.DZ
                 Gig 2/2/16        140              S I   C9200L-48 Gig 1/1/1
ADMIN_STACK_SW   Ten 1/1/11        179              S I   WS-C2960X Gig 2/0/49
ADMIN_STACK_SW   Ten 2/1/10        151              S I   WS-C2960X Gig 1/0/49
64d8145c7aa0     Gig 1/2/6         146              S I   SF 302-08 gi1
SWA-VIP-IPTV     Gig 2/2/7         159              S I   WS-C2960X Gig 1/0/25
SWA-DC-IDRAC     Ten 2/1/5         150              S I   WS-C2960X Gig 1/0/52
SWA-DC-IDRAC     Ten 1/1/5         138              S I   WS-C2960X Gig 1/0/51
OPVOIP           Ten 1/1/12        160              S I   WS-C3560X Gig 1/2
OPVOIP           Ten 2/1/12        160              S I   WS-C3560X Gig 1/1
SVR_FARM1        Ten 1/1/3         177              S I   WS-C2960X Ten 2/0/1
SVR_FARM1        Ten 2/1/3         177              S I   WS-C2960X Ten 1/0/1
SWA-ITT          Gig 1/2/3         132              S I   WS-C2960X Gig 1/0/25
SWA2-Room-Z4     Gig 1/2/1         141              S I   WS-C3560V Gig 0/1
SWA-VIP          Gig 2/2/17        165              S I   WS-C2960X Gig 1/0/27
SWA-WELLS        Ten 1/1/7         145              S I   WS-C3650- Gig 1/1/1
SWA-WELLS        Ten 2/1/7         122              S I   WS-C3650- Gig 1/1/2
SWA_Z4_IPTV      Gig 2/2/4         161              S I   WS-C2960X Gig 1/0/49
SWA_Z5_IPTV      Gig 2/2/5         166              S I   WS-C2960X Gig 1/0/49
SWA-Z4-DATA      Gig 1/2/4         162              S I   WS-C2960X Gig 1/0/51
SWA-Z1-WIFI      Gig 2/2/19        152              S I   WS-C2960X Gig 1/0/25
SWA-INITEC-WLAN-LT1
                 Gig 2/2/22        143              S I   WS-C2960X Gig 1/0/25
LT1-INETEC-SWA2  Gig 2/2/9         127              S I   WS-C2960L Gig 0/49
64d8145c922e     Gig 1/2/5         179              S I   SF302-08P gi1
SWA-DC-WIFI      Ten 2/1/6         162              S I   WS-C3560X Gig 1/1
SWA-IT-OFFICE    Gig 2/2/11        126              S I   WS-C2960X Gig 1/0/25
SWA_DC_IPTV      Gig 2/2/6         178              S I   WS-C2960X Gig 1/0/49
SWA-Room-Z5.OFRKF.DZ
                 Gig 1/2/2         149              S I   WS-C2960X Gig 1/0/49
SWA-Security     Ten 1/1/9         136              S I   WS-C2960X Gig 1/0/25
          
Device ID        Local Intrfce     Holdtme    Capability  Platform  Port ID
SWA-WHOUSE       Ten 2/1/11        164              S I   WS-C3560V Gig 0/2
SWA-WHOUSE       Ten 1/1/10        164              S I   WS-C3560V Gig 0/1
RKF-DC-WLC01-Standby
                 Gig 2/7/47        121               H    AIR-CT350 Gig 0/0/1
RKF-DC-WLC01-Standby
                 Gig 2/7/48        121               H    AIR-CT350 Gig 0/0/2
RKF-DC-WLC01-Standby
                 Gig 2/7/46        121               H    AIR-CT350 Gig 0/0/3
RKF-DC-WLC01-Standby
                 Gig 2/7/45        121               H    AIR-CT350 Gig 0/0/4
SWA-ADMANNEX     Gig 2/2/23        164              S I   WS-C2960X Gig 1/0/49

"""