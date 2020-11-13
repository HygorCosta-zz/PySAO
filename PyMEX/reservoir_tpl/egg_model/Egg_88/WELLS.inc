*WELL 'PROD1'  *ATTACHTO 'EGGMODEL'
*XFLOW-MODEL 'PROD1' *FULLY-MIXED
                        **m3/day
                         **kPa
                            **Profitability Threshold
PRODUCER 'PROD1'
OPERATE  MAX  STL 120.0  CONT
OPERATE  MIN  BHP  39500.0  CONT
*MONITOR *WCUT     0.87   *SHUTIN  **Profitability Threshold
**$ UBA ff Satus Connection
**          rad  geofac  wfrac  skin
GEOMETRY  K  0.1  0.37  1.0  0.0
      PERF      GEOA  'PROD1'
** UBA             ff          Status  Connection
    2 6 1         1.0  OPEN    FLOW-TO  'SURFACE'  REFLAYER
    2 6 2         1.0  OPEN    FLOW-TO  1


*WELL 'PROD2'  *ATTACHTO 'EGGMODEL'
*XFLOW-MODEL 'PROD2' *FULLY-MIXED
                        **m3/day
                         **kPa
                            **Profitability Threshold
PRODUCER 'PROD2'
OPERATE  MAX  STL 120.0  CONT
OPERATE  MIN  BHP  39500.0  CONT
*MONITOR *WCUT     0.87   *SHUTIN  **Profitability Threshold
**$ UBA ff Satus Connection
**          rad  geofac  wfrac  skin
GEOMETRY  K  0.1  0.37  1.0  0.0
      PERF      GEOA  'PROD2'
** UBA             ff          Status  Connection
    5 5 1         1.0  OPEN    FLOW-TO  'SURFACE'  REFLAYER
    5 5 2         1.0  OPEN    FLOW-TO  1


*WELL 'PROD3'  *ATTACHTO 'EGGMODEL'
*XFLOW-MODEL 'PROD3' *FULLY-MIXED
                        **m3/day
                         **kPa
                            **Profitability Threshold
PRODUCER 'PROD3'
OPERATE  MAX  STL 120.0  CONT
OPERATE  MIN  BHP  39500.0  CONT
*MONITOR *WCUT     0.87   *SHUTIN  **Profitability Threshold
**$ UBA ff Satus Connection
**          rad  geofac  wfrac  skin
GEOMETRY  K  0.1  0.37  1.0  0.0
      PERF      GEOA  'PROD3'
** UBA             ff          Status  Connection
    3 2 1         1.0  OPEN    FLOW-TO  'SURFACE'  REFLAYER
    3 2 2         1.0  OPEN    FLOW-TO  1


*WELL 'PROD4'  *ATTACHTO 'EGGMODEL'
*XFLOW-MODEL 'PROD4' *FULLY-MIXED
                        **m3/day
                         **kPa
                            **Profitability Threshold
PRODUCER 'PROD4'
OPERATE  MAX  STL 120.0  CONT
OPERATE  MIN  BHP  39500.0  CONT
*MONITOR *WCUT     0.87   *SHUTIN  **Profitability Threshold
**$ UBA ff Satus Connection
**          rad  geofac  wfrac  skin
GEOMETRY  K  0.1  0.37  1.0  0.0
      PERF      GEOA  'PROD4'
** UBA             ff          Status  Connection
    6 3 1         1.0  OPEN    FLOW-TO  'SURFACE'  REFLAYER
    6 3 2         1.0  OPEN    FLOW-TO  1


*WELL 'INJECT1'  *ATTACHTO 'EGGMODEL'
*XFLOW-MODEL 'INJECT1' *FULLY-MIXED
                         **m3/day
                         **kPa
INJECTOR MOBWEIGHT 'INJECT1'
INCOMP  WATER
OPERATE  MAX   STW 79.5  CONT
OPERATE  MAX  BHP  42000.0  CONT
**$ UBA ff Satus Connection
**          rad  geofac  wfrac  skin
GEOMETRY  K  0.1  0.37  1.0  0.0
      PERF      GEOA  'INJECT1'
** UBA             ff          Status  Connection
    1 8 1         1.0  OPEN    FLOW-FROM  'SURFACE'  REFLAYER
    1 8 2         1.0  OPEN    FLOW-FROM  1


*WELL 'INJECT2'  *ATTACHTO 'EGGMODEL'
*XFLOW-MODEL 'INJECT2' *FULLY-MIXED
                         **m3/day
                         **kPa
INJECTOR MOBWEIGHT 'INJECT2'
INCOMP  WATER
OPERATE  MAX   STW 79.5  CONT
OPERATE  MAX  BHP  42000.0  CONT
**$ UBA ff Satus Connection
**          rad  geofac  wfrac  skin
GEOMETRY  K  0.1  0.37  1.0  0.0
      PERF      GEOA  'INJECT2'
** UBA             ff          Status  Connection
    4 7 1         1.0  OPEN    FLOW-FROM  'SURFACE'  REFLAYER
    4 7 2         1.0  OPEN    FLOW-FROM  1


*WELL 'INJECT3'  *ATTACHTO 'EGGMODEL'
*XFLOW-MODEL 'INJECT3' *FULLY-MIXED
                         **m3/day
                         **kPa
INJECTOR MOBWEIGHT 'INJECT3'
INCOMP  WATER
OPERATE  MAX   STW 79.5  CONT
OPERATE  MAX  BHP  42000.0  CONT
**$ UBA ff Satus Connection
**          rad  geofac  wfrac  skin
GEOMETRY  K  0.1  0.37  1.0  0.0
      PERF      GEOA  'INJECT3'
** UBA             ff          Status  Connection
    1 5 1         1.0  OPEN    FLOW-FROM  'SURFACE'  REFLAYER
    1 5 2         1.0  OPEN    FLOW-FROM  1


*WELL 'INJECT4'  *ATTACHTO 'EGGMODEL'
*XFLOW-MODEL 'INJECT4' *FULLY-MIXED
                         **m3/day
                         **kPa
INJECTOR MOBWEIGHT 'INJECT4'
INCOMP  WATER
OPERATE  MAX   STW 79.5  CONT
OPERATE  MAX  BHP  42000.0  CONT
**$ UBA ff Satus Connection
**          rad  geofac  wfrac  skin
GEOMETRY  K  0.1  0.37  1.0  0.0
      PERF      GEOA  'INJECT4'
** UBA             ff          Status  Connection
    4 4 1         1.0  OPEN    FLOW-FROM  'SURFACE'  REFLAYER
    4 4 2         1.0  OPEN    FLOW-FROM  1


*WELL 'INJECT5'  *ATTACHTO 'EGGMODEL'
*XFLOW-MODEL 'INJECT5' *FULLY-MIXED
                         **m3/day
                         **kPa
INJECTOR MOBWEIGHT 'INJECT5'
INCOMP  WATER
OPERATE  MAX   STW 79.5  CONT
OPERATE  MAX  BHP  42000.0  CONT
**$ UBA ff Satus Connection
**          rad  geofac  wfrac  skin
GEOMETRY  K  0.1  0.37  1.0  0.0
      PERF      GEOA  'INJECT5'
** UBA             ff          Status  Connection
    7 5 1         1.0  OPEN    FLOW-FROM  'SURFACE'  REFLAYER
    7 5 2         1.0  OPEN    FLOW-FROM  1


*WELL 'INJECT6'  *ATTACHTO 'EGGMODEL'
*XFLOW-MODEL 'INJECT6' *FULLY-MIXED
                         **m3/day
                         **kPa
INJECTOR MOBWEIGHT 'INJECT6'
INCOMP  WATER
OPERATE  MAX   STW 79.5  CONT
OPERATE  MAX  BHP  42000.0  CONT
**$ UBA ff Satus Connection
**          rad  geofac  wfrac  skin
GEOMETRY  K  0.1  0.37  1.0  0.0
      PERF      GEOA  'INJECT6'
** UBA             ff          Status  Connection
    1 2 1         1.0  OPEN    FLOW-FROM  'SURFACE'  REFLAYER
    1 2 2         1.0  OPEN    FLOW-FROM  1


*WELL 'INJECT7'  *ATTACHTO 'EGGMODEL'
*XFLOW-MODEL 'INJECT7' *FULLY-MIXED
                         **m3/day
                         **kPa
INJECTOR MOBWEIGHT 'INJECT7'
INCOMP  WATER
OPERATE  MAX   STW 79.5  CONT
OPERATE  MAX  BHP  42000.0  CONT
**$ UBA ff Satus Connection
**          rad  geofac  wfrac  skin
GEOMETRY  K  0.1  0.37  1.0  0.0
      PERF      GEOA  'INJECT7'
** UBA             ff          Status  Connection
    4 1 1         1.0  OPEN    FLOW-FROM  'SURFACE'  REFLAYER
    4 1 2         1.0  OPEN    FLOW-FROM  1


*WELL 'INJECT8'  *ATTACHTO 'EGGMODEL'
*XFLOW-MODEL 'INJECT8' *FULLY-MIXED
                         **m3/day
                         **kPa
INJECTOR MOBWEIGHT 'INJECT8'
INCOMP  WATER
OPERATE  MAX   STW 79.5  CONT
OPERATE  MAX  BHP  42000.0  CONT
**$ UBA ff Satus Connection
**          rad  geofac  wfrac  skin
GEOMETRY  K  0.1  0.37  1.0  0.0
      PERF      GEOA  'INJECT8'
** UBA             ff          Status  Connection
    8 1 1         1.0  OPEN    FLOW-FROM  'SURFACE'  REFLAYER
    8 1 2         1.0  OPEN    FLOW-FROM  1
