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

*GRID  *VARI 8 8 2
*KDIR *DOWN

*DI *CON 64
*DJ *CON 64
*DK *KVAR 12 16

*NETGROSS *ALL
128*1

*POR *ALL
128*0.2

*DEPTH-TOP *ALL
64*4000    64*4012

*CPOR 1E-10
*PRPOR 40000

****************************************************************************
**
**                *Permeability Field
**
****************************************************************************
*INCLUDE '/home/hygorcosta/Documentos/Phd/SAO/PyMEX/reservoir_tpl/egg_model/Egg_88/NULL_LVL_2.inc'
*INCLUDE '/home/hygorcosta/Documentos/Phd/SAO/PyMEX/reservoir_tpl/egg_model/Egg_88/PERM_LVL_2.inc'
PERMJ  EQUALSI
PERMK  EQUALSI * 0.1

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
*INCLUDE '/home/hygorcosta/Documentos/Phd/SAO/PyMEX/reservoir_tpl/egg_model/Egg_88/WELLS.inc'

$$WELL_INC
