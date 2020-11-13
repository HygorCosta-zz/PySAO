** **************************************************************************
**
** *IO
**
** **************************************************************************
** 2015-11-18, 14:11:29, LabestWX
RESULTS SIMULATOR IMEX 201210

** <@> JewelSuite(TM) ECLIPSE Deck Builder

** <+> Start of deck ECL

*TITLE1
'Egg Model'

** ascii formatted output
**FMTOUT   **This option specifies SI units for input data.

**------------------------------------------------------------
**DIM  *MAX_LAYERS  100

****************************************************************************
**
***GRID
**
****************************************************************************

*INCLUDE '/home/hygorcosta/Documentos/Phd/SAO/PyMEX/reservoir_tpl/egg_model/Egg_trad/Egg_Model_Grid.inc'

*NETGROSS *ALL
25200*1

*POR *ALL
25200*0.2

*DEPTH-TOP *ALL
3600*4000    3600*4004    3600*4008    3600*4012    3600*4016    3600*4020
3600*4024


*CPOR 1E-10
*PRPOR 40000

****************************************************************************
**
**                *Permeability Field
**
****************************************************************************

**INCLUDE 'PERM_IMX_11.inc'    **Theta     Permeabilidade fixa
*INCLUDE '/home/hygorcosta/Documentos/Phd/SAO/PyMEX/reservoir_tpl/egg_model/Egg_trad/PERM_IMX_1.inc'

**$  0 = pinched block, 1 = active block
PINCHOUTARRAY CON            1


****************************************************************************
**
**              *MODEL
**
****************************************************************************

*MODEL *OILWATER

*PVT BG 1  **Taked from Brugge Model
**$     p        Rs        Bo      Bg      viso     visg
	  40000     0.0        1     0.01       5       0.01

**    p (Pressure)
**	  Rs (Solution gas-oil ratio at pressure p)
**    Bo (Formation volume factor for saturated oil at pressure p)
**	  Bg (Gas formation volume factor at pressure p)
**    viso (Viscosity  of saturated oil )
**    visg

**CO 1.000E-05	**CO indicates input of oil compressibility (for a PVT region).
*DENSITY *OIL 900   ** KG/M3;
*DENSITY *GAS 1
*DENSITY *WATER 1000
*BOT 1		**BOT indicates the input of an Bo table that is a function of both pressure,
			**P, and bubble point pressure, Pb.
0    1
**0    0
*VOT 1		**VOT indicates the input of an oil viscosity (Vo) table that is a function of
			** both pressure, P,  and bubble point pressure, Pb.
0    1    056
0    1    056
*REFPW 40000   **400 bar = 40000 kPa
*BWI 1		**BWI indicates the input of the water formation volume factor (for a PVT region).
*CW 0.00001 **Alterado de 0.0001 para 0.00001
*VWI 1         **VWI signals the input of water viscosity (for a PVT region).
*CVW 0		   **CVW signals the input of cvw (for a PVT region).
PTYPE CON  1  **PTYPE indicates the start of input of PVT region types.


****************************************************************************
**
**              *ROCKFLUID
**
****************************************************************************

*ROCKFLUID


*KROIL *SEGREGATED
*RPT 1
*SWT
0.1000 0          8.0000E-01 0
0.2000 0          8.0000E-01 0
0.2500 2.7310E-04 5.8082E-01 0
0.3000 2.1848E-03 4.1010E-01 0
0.3500 7.3737E-03 2.8010E-01 0
0.4000 1.7478E-02 1.8378E-01 0
0.4500 3.4138E-02 1.1473E-01 0
0.5000 5.8990E-02 6.7253E-02 0
0.5500 9.3673E-02 3.6301E-02 0
0.6000 1.3983E-01 1.7506E-02 0
0.6500 1.9909E-01 7.1706E-03 0
0.7000 2.7310E-01 2.2688E-03 0
0.7500 3.6350E-01 4.4820E-04 0
0.8000 4.7192E-01 2.8000E-05 0
0.8500 6.0000E-01 0          0
0.9000 7.4939E-01 0          0

****************************************************************************
**
**              *INITIAL
**
****************************************************************************

*INITIAL
*VERTICAL *DEPTH_AVE *WATER_OIL

**RPTSOL
**    RESTART=2 FIP=3/
REFDEPTH 4000
REFPRES 40000
DWOC 5000
WOC_PC 0
PB CON            0
NUMERICAL

****************************************************************************
**
**              *RUN
**
****************************************************************************

*RUN
*DATE 2011 6 15
** <+> SCHEDULE 7/7/2011 (0 days)

GROUP 'EGGMODEL' ATTACHTO 'FIELD'

*WELL 'INJECT1' *ATTACHTO 'EGGMODEL'
*XFLOW-MODEL 'INJECT1' *FULLY-MIXED
*INJECTOR *MOBWEIGHT 'INJECT1'
*INCOMP *WATER
*OPERATE *MAX *STW 79.5  **m3/day
*OPERATE *MAX *BHP 42000    **kPa
**$          rad  geofac  wfrac  skin
GEOMETRY  K  0.1  0.37  1.  0.
PERF  GEOA  'INJECT1'
**$ UBA     ff  Status  Connection
    5 57 1  1.  OPEN    FLOW-FROM  'SURFACE'  REFLAYER
    5 57 2  1.  OPEN    FLOW-FROM  1
    5 57 3  1.  OPEN    FLOW-FROM  2
    5 57 4  1.  OPEN    FLOW-FROM  3
    5 57 5  1.  OPEN    FLOW-FROM  4
    5 57 6  1.  OPEN    FLOW-FROM  5
    5 57 7  1.  OPEN    FLOW-FROM  6

**
*WELL 'INJECT2' *ATTACHTO 'EGGMODEL'
*XFLOW-MODEL 'INJECT2' *FULLY-MIXED
*INJECTOR *MOBWEIGHT 'INJECT2'
*INCOMP *WATER
*OPERATE *MAX *STW 79.5  **m3/day
*OPERATE *MAX *BHP 42000
**$          rad  geofac  wfrac  skin
GEOMETRY  K  0.1  0.37  1.  0.
PERF  GEOA  'INJECT2'
**$ UBA      ff  Status  Connection
    30 53 1  1.  OPEN    FLOW-FROM  'SURFACE'  REFLAYER
    30 53 2  1.  OPEN    FLOW-FROM  1
    30 53 3  1.  OPEN    FLOW-FROM  2
    30 53 4  1.  OPEN    FLOW-FROM  3
    30 53 5  1.  OPEN    FLOW-FROM  4
    30 53 6  1.  OPEN    FLOW-FROM  5
    30 53 7  1.  OPEN    FLOW-FROM  6

**
*WELL 'INJECT3' *ATTACHTO 'EGGMODEL'
*XFLOW-MODEL 'INJECT3' *FULLY-MIXED
*INJECTOR *MOBWEIGHT 'INJECT3'
*INCOMP *WATER
*OPERATE *MAX *STW 79.5  **m3/day
*OPERATE *MAX *BHP 42000
**$          rad  geofac  wfrac  skin
GEOMETRY  K  0.1  0.37  1.  0.
PERF  GEOA  'INJECT3'
**$ UBA     ff  Status  Connection
    2 35 1  1.  OPEN    FLOW-FROM  'SURFACE'  REFLAYER
    2 35 2  1.  OPEN    FLOW-FROM  1
    2 35 3  1.  OPEN    FLOW-FROM  2
    2 35 4  1.  OPEN    FLOW-FROM  3
    2 35 5  1.  OPEN    FLOW-FROM  4
    2 35 6  1.  OPEN    FLOW-FROM  5
    2 35 7  1.  OPEN    FLOW-FROM  6

**
*WELL 'INJECT4' *ATTACHTO 'EGGMODEL'
*XFLOW-MODEL 'INJECT4' *FULLY-MIXED
*INJECTOR *MOBWEIGHT 'INJECT4'
*INCOMP *WATER
*OPERATE *MAX *STW 79.5  **m3/day
*OPERATE *MAX *BHP 42000  **kPa
**$          rad  geofac  wfrac  skin
GEOMETRY  K  0.1  0.37  1.  0.
PERF  GEOA  'INJECT4'
**$ UBA      ff  Status  Connection
    27 29 1  1.  OPEN    FLOW-FROM  'SURFACE'  REFLAYER
    27 29 2  1.  OPEN    FLOW-FROM  1
    27 29 3  1.  OPEN    FLOW-FROM  2
    27 29 4  1.  OPEN    FLOW-FROM  3
    27 29 5  1.  OPEN    FLOW-FROM  4
    27 29 6  1.  OPEN    FLOW-FROM  5
    27 29 7  1.  OPEN    FLOW-FROM  6

**
*WELL 'INJECT5' *ATTACHTO 'EGGMODEL'
*XFLOW-MODEL 'INJECT5' *FULLY-MIXED
*INJECTOR *MOBWEIGHT 'INJECT5'
*INCOMP *WATER
*OPERATE *MAX *STW 79.5  **m3/day
*OPERATE *MAX *BHP 42000  **kPa
**$          rad  geofac  wfrac  skin
GEOMETRY  K  0.1  0.37  1.  0.
PERF  GEOA  'INJECT5'
**$ UBA      ff  Status  Connection
    50 35 1  1.  OPEN    FLOW-FROM  'SURFACE'  REFLAYER
    50 35 2  1.  OPEN    FLOW-FROM  1
    50 35 3  1.  OPEN    FLOW-FROM  2
    50 35 4  1.  OPEN    FLOW-FROM  3
    50 35 5  1.  OPEN    FLOW-FROM  4
    50 35 6  1.  OPEN    FLOW-FROM  5
    50 35 7  1.  OPEN    FLOW-FROM  6

**
*WELL 'INJECT6' *ATTACHTO 'EGGMODEL'
*XFLOW-MODEL 'INJECT6' *FULLY-MIXED
*INJECTOR *MOBWEIGHT 'INJECT6'
*INCOMP *WATER
*OPERATE *MAX *STW 79.5  **m3/day
*OPERATE *MAX *BHP 42000  **kPa
**$          rad  geofac  wfrac  skin
GEOMETRY  K  0.1  0.37  1.  0.
PERF  GEOA  'INJECT6'
**$ UBA    ff  Status  Connection
    8 9 1  1.  OPEN    FLOW-FROM  'SURFACE'  REFLAYER
    8 9 2  1.  OPEN    FLOW-FROM  1
    8 9 3  1.  OPEN    FLOW-FROM  2
    8 9 4  1.  OPEN    FLOW-FROM  3
    8 9 5  1.  OPEN    FLOW-FROM  4
    8 9 6  1.  OPEN    FLOW-FROM  5
    8 9 7  1.  OPEN    FLOW-FROM  6

**
*WELL 'INJECT7' *ATTACHTO 'EGGMODEL'
*XFLOW-MODEL 'INJECT7' *FULLY-MIXED
*INJECTOR *MOBWEIGHT 'INJECT7'
*INCOMP *WATER
*OPERATE *MAX *STW 79.5  **m3/day
*OPERATE *MAX *BHP 42000  **kPa
**$          rad  geofac  wfrac  skin
GEOMETRY  K  0.1  0.37  1.  0.
PERF  GEOA  'INJECT7'
**$ UBA     ff  Status  Connection
    32 2 1  1.  OPEN    FLOW-FROM  'SURFACE'  REFLAYER
    32 2 2  1.  OPEN    FLOW-FROM  1
    32 2 3  1.  OPEN    FLOW-FROM  2
    32 2 4  1.  OPEN    FLOW-FROM  3
    32 2 5  1.  OPEN    FLOW-FROM  4
    32 2 6  1.  OPEN    FLOW-FROM  5
    32 2 7  1.  OPEN    FLOW-FROM  6

**
*WELL 'INJECT8' *ATTACHTO 'EGGMODEL'
*XFLOW-MODEL 'INJECT8' *FULLY-MIXED
*INJECTOR *MOBWEIGHT 'INJECT8'
*INCOMP *WATER
*OPERATE *MAX *STW 79.5  **m3/day
*OPERATE *MAX *BHP 42000  **kPa
**$          rad  geofac  wfrac  skin
GEOMETRY  K  0.1  0.37  1.  0.
PERF  GEOA  'INJECT8'
**$ UBA     ff  Status  Connection
    57 6 1  1.  OPEN    FLOW-FROM  'SURFACE'  REFLAYER
    57 6 2  1.  OPEN    FLOW-FROM  1
    57 6 3  1.  OPEN    FLOW-FROM  2
    57 6 4  1.  OPEN    FLOW-FROM  3
    57 6 5  1.  OPEN    FLOW-FROM  4
    57 6 6  1.  OPEN    FLOW-FROM  5
    57 6 7  1.  OPEN    FLOW-FROM  6

**
*WELL 'PROD1' *ATTACHTO 'EGGMODEL'
*XFLOW-MODEL 'PROD1' *FULLY-MIXED
*PRODUCER 'PROD1'
*OPERATE *MAX *STL 120    **m3/day
*OPERATE *MIN *BHP 39500  **kPa
*MONITOR *WCUT     0.87   *SHUTIN  **Profitability Threshold
**$          rad  geofac  wfrac  skin
GEOMETRY  K  0.1  0.37  1.  0.
PERF  GEOA  'PROD1'
**$ UBA      ff  Status  Connection
    16 43 1  1.  OPEN    FLOW-TO  'SURFACE'  REFLAYER
    16 43 2  1.  OPEN    FLOW-TO  1
    16 43 3  1.  OPEN    FLOW-TO  2
    16 43 4  1.  OPEN    FLOW-TO  3
    16 43 5  1.  OPEN    FLOW-TO  4
    16 43 6  1.  OPEN    FLOW-TO  5
    16 43 7  1.  OPEN    FLOW-TO  6

**
*WELL 'PROD2' *ATTACHTO 'EGGMODEL'
*XFLOW-MODEL 'PROD2' *FULLY-MIXED
*PRODUCER 'PROD2'
*OPERATE *MAX *STL 120    **m3/day
*OPERATE *MIN *BHP 39500  **kPa
*MONITOR *WCUT     0.87   *SHUTIN  **Profitability Threshold
**$          rad  geofac  wfrac  skin
GEOMETRY  K  0.1  0.37  1.  0.
PERF  GEOA  'PROD2'
**$ UBA      ff  Status  Connection
    35 40 1  1.  OPEN    FLOW-TO  'SURFACE'  REFLAYER
    35 40 2  1.  OPEN    FLOW-TO  1
    35 40 3  1.  OPEN    FLOW-TO  2
    35 40 4  1.  OPEN    FLOW-TO  3
    35 40 5  1.  OPEN    FLOW-TO  4
    35 40 6  1.  OPEN    FLOW-TO  5
    35 40 7  1.  OPEN    FLOW-TO  6

**
*WELL 'PROD3' *ATTACHTO 'EGGMODEL'
*XFLOW-MODEL 'PROD3' *FULLY-MIXED
*PRODUCER 'PROD3'
*OPERATE *MAX *STL 120   **m3/day
*OPERATE *MIN *BHP 39500 **kPa
*MONITOR *WCUT     0.87   *SHUTIN  **Profitability Threshold
**$          rad  geofac  wfrac  skin
GEOMETRY  K  0.1  0.37  1.  0.
PERF  GEOA  'PROD3'
**$ UBA      ff  Status  Connection
    23 16 1  1.  OPEN    FLOW-TO  'SURFACE'  REFLAYER
    23 16 2  1.  OPEN    FLOW-TO  1
    23 16 3  1.  OPEN    FLOW-TO  2
    23 16 4  1.  OPEN    FLOW-TO  3
    23 16 5  1.  OPEN    FLOW-TO  4
    23 16 6  1.  OPEN    FLOW-TO  5
    23 16 7  1.  OPEN    FLOW-TO  6

**
*WELL 'PROD4' *ATTACHTO 'EGGMODEL'
*XFLOW-MODEL 'PROD4' *FULLY-MIXED
*PRODUCER 'PROD4'
*OPERATE *MAX *STL 120   **m3/day
*OPERATE *MIN *BHP 39500 **kPa
*MONITOR *WCUT     0.87   *SHUTIN  **Profitability Threshold
**$          rad  geofac  wfrac  skin
GEOMETRY  K  0.1  0.37  1.  0.
PERF  GEOA  'PROD4'
**$ UBA      ff  Status  Connection
    43 18 1  1.  OPEN    FLOW-TO  'SURFACE'  REFLAYER
    43 18 2  1.  OPEN    FLOW-TO  1
    43 18 3  1.  OPEN    FLOW-TO  2
    43 18 4  1.  OPEN    FLOW-TO  3
    43 18 5  1.  OPEN    FLOW-TO  4
    43 18 6  1.  OPEN    FLOW-TO  5
    43 18 7  1.  OPEN    FLOW-TO  6


**DTWELL 0.1
**DTMAX 30
**DTMIN 0.1

**Restricoes da Plataforma

**Producao
*GCONP 'EGGMODEL'
*MAX STL 400.0

**Injecao
*GCONI 'EGGMODEL'
*MAX STW 440.0


$$WELL_INC
