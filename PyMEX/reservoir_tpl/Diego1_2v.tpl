**
*TITLE1
   'OTIMIZACAO DE PRODUCAO'
**
*TITLE2
   'FASE 2'
**
*TITLE3
   'NEW TOY-CASE '
**
** Sistema de unidades
*INUNIT *MODSI
**
*XDR *OFF
*OUTUNIT *MODSI          ** Unidades internacionais modificadas

** *WPRN   *WELL   *TIME    ** Frequencia de impressao no arq. saida .OUT
*WPRN   *WELL   1        ** Frequencia de impressao no arq. saida .OUT
*WPRN   *GRID   0
*WPRN   *ITER   *BRIEF

*OUTPRN *WELL   *ALL     ** Informacoes a serem impressas arq.saida .OUT
*OUTPRN *RES    *ALL
*OUTPRN *TABLES *NONE
*OUTPRN *GRID   *NONE

*WSRF   *GRID   1        ** Frequencia de gravacao nos arq. .IRF e .MRF
*WSRF   *WELL   1

                                             ** Informacoes a serem gravadas nos
*OUTSRF *GRID *SW *SG *SO *PRES *DATUMPRES   ** arq. .IRF e .MRF
*OUTSRF *WELL *LAYER *ALL

**
**--------------------------------------------------------------------------
** 		Parte 2: Descricao do Reservatorio
**--------------------------------------------------------------------------
**
*GRID *CART 51 51 3
*KDIR *DOWN
*DI *CON    10
*DJ *CON    10
*DK *CON    4
*MOD
      1:51    1:51     2:3   =  8

*DTOP 2601*2000

*POR *CON    0.3
**NULL *IJK
**      1:51    1:51        2  0
**      1:51    1:51        3  0
*PERMI *IJK
      1:51    1:51        1  1000
      1:51    1:51        2  1000
      1:51    1:51        3  1000
*MOD
      1:26    26:51	1:3  * 1.50
     27:51    26:51	1:3  * 0.50
*PERMJ *EQUALSI
*PERMK *EQUALSI * 0.1
*SECTOR 'CAM1'
      1:51    1:51        1
*SECTOR 'CAM2'
      1:51    1:51        2
*SECTOR 'CAM3'
      1:51    1:51        3
**
*CROCKTYPE 1
*CPRPOR 200.000
*CCPOR 5E-005

**
**
**--------------------------------------------------------------------------
** 		Parte 3: Propriedades dos Componentes
**--------------------------------------------------------------------------
**
*MODEL *BLACKOIL

** Temperatura do Reservatorio (oC)

*TRES 100.000
**
** Regiao 1
**
*PVT *EG 1
**    P          Rs         Bo         Eg         VisO       VisG       co
**    (kg/cm2)   (sm3/sm3)  (rm3/sm3)  (sm3/rm3)  (cP)       (cP)       (cm2/kg)
         1.033        0.5      1.074     0.7774   5.812680   0.013292  0.0004267
         7.631        1.9      1.077     5.7924   5.412240   0.013353  0.0004267
        14.229        3.6      1.081    10.8956   5.010100   0.013438  0.0004267
        20.827        5.5      1.085    16.0867   4.636120   0.013539  0.0004267
        27.424        7.5      1.090    21.3645   4.297090   0.013653  0.0004267
        34.022        9.6      1.094    26.7276   3.992900   0.013780  0.0004267
        40.620       11.8      1.099    32.1738   3.721000   0.013919  0.0004267
        47.218       14.0      1.104    37.7002   3.478060   0.014068  0.0004267
        53.816       16.3      1.109    43.3033   3.260710   0.014229  0.0004267
        60.413       18.7      1.115    48.9786   3.065810   0.014400  0.0004267
        67.011       21.1      1.120    54.7210   2.890540   0.014582  0.0004267
        73.609       23.6      1.126    60.5243   2.732430   0.014775  0.0004267
        80.207       26.1      1.132    66.3817   2.589350   0.014978  0.0004267
        86.804       28.7      1.138    72.2854   2.459440   0.015191  0.0004267
        93.402       31.2      1.144    78.2270   2.341110   0.015414  0.0004267
       100.000       33.9      1.151    84.1972   2.233010   0.015646  0.0004267
       160.000       59.2      1.213   138.0790   1.564330   0.018155  0.000289776
       220.000       86.6      1.283   186.5890   1.201580   0.021108  0.000191717
       280.000      115.5      1.361   226.7390   0.976856   0.024144  0.000140259
       340.000      145.7      1.445   259.1040   0.824782   0.027056  0.000109074
       400.000      177.1      1.535   285.3140   0.715284   0.029768  8.83779e-005
**

** Massa especifica do oleo
*DENSITY *OIL      903.249

** Massa especifica do gas
*DENSITY *GAS        0.856

** Massa especifica da agua
*DENSITY *WATER      965.284

*CVO        0.001
*BWI        1.043
*CW     4.8e-005
*REFPW        1.033
*VWI     0.294779
*CVW            0


*************************************************************************************
**
**--------------------------------------------------------------------------
** 		Parte 4: Propriedades Rocha-Fluido
**--------------------------------------------------------------------------
**
*ROCKFLUID
*RPT 1

** Tabela de Permeabilidade Relativa Oleo-Agua
*SWT
**    Sw         Krw        Krow       Pcow
**    (adm)      (adm)      (adm)      (kg/cm2)
0.08800000      0.000      0.800      0.000
0.10000000      0.000      0.750       *INT
0.15000000      0.000      0.563       *INT
0.20000000      0.002      0.411       *INT
0.25000000      0.005      0.288       *INT
0.30000000      0.011      0.193       *INT
0.35000000      0.020      0.122       *INT
0.40000000      0.034      0.070       *INT
0.45000000      0.053      0.036       *INT
0.50000000      0.079      0.015       *INT
0.55000000      0.111      0.005       *INT
0.60000000      0.151      0.001       *INT
0.65000000      0.200      0.000      0.000

** Tabela de Permeabilidade Relativa Gas-Oleo
*SLT
**    Sl         Krg        Krog       Pcog
**    (adm)      (adm)      (adm)      (kg/cm2)
0.17600000      0.900      0.000      0.000
0.20000000      0.824      0.000       *INT
0.25000000      0.679      0.001       *INT
0.30000000      0.552      0.003       *INT
0.35000000      0.442      0.008       *INT
0.40000000      0.347      0.016       *INT
0.45000000      0.268      0.029       *INT
0.50000000      0.201      0.049       *INT
0.55000000      0.147      0.075       *INT
0.60000000      0.103      0.109       *INT
0.65000000      0.069      0.152       *INT
0.70000000      0.043      0.206       *INT
0.75000000      0.025      0.270       *INT
0.80000000      0.013      0.347       *INT
0.85000000      0.005      0.438       *INT
0.90000000      0.002      0.543       *INT
0.95000000      0.000      0.663       *INT
1.00000000      0.000      0.800      0.000

**
**--------------------------------------------------------------------------
** 		Parte 5: Condicoes Iniciais
**--------------------------------------------------------------------------
**

*INITIAL

*VERTICAL *BLOCK_CENTER
** DATUM para gravacao
*DATUMDEPTH 1000.000
**
** Profundidade de Referencia
*REFDEPTH     2000.500

** Pressao inicial
*REFPRES      200.000

** Profundidade do contato oleo-agua
*DWOC        3000.000

** Profundidade do contato gas-oleo
*DGOC        1000.000



** Pressao de bolha (todas as celulas)
*PB *CON    273.033
**
**--------------------------------------------------------------------------
** 		Parte 6: Metodos Numericos
**--------------------------------------------------------------------------
**
*NUMERICAL
**
*DTMAX         30.             ** Tamanho maximo do timestep em dias

*MAXSTEPS      1000000        ** Numero maximo de timesteps

                              ** Controle do tamanho do timestep
*NORM *PRESS    10.0             ** max. variacao  pressao  no timestep
                                    ** unidade: kgf/cm2
*NORM *SATUR     0.05            ** max. variacao saturacao no timestep

                              ** Metodo implicito adaptativo
*AIM  *THRESH    0.25 .20        ** Criterio de mudanca: threshold

**

**--------------------------------------------------------------------------
** 		Parte 7: Pocos e Dados Recorrentes
**--------------------------------------------------------------------------
**

*RUN
*DATE 2006 01 01

*GROUP 'PLAT' *ATTACHTO 'FIELD'


** -------------------------------------------------------
*WELL  1  'PROD1' *ATTACHTO 'PLAT'

*PRODUCER 'PROD1' ** WELL no.1
*OPERATE *MAX *STL 30.0
**OPERATE *MIN *BHP 180.0
**MONITOR *WCUT     0.95   *STOP

*GEOMETRY *K 0.100 0.37 1 0
*PERF *GEO 'PROD1'
   51 51 1 1.000000
   51 51 2 1.000000
   51 51 3 1.000000

** -------------------------------------------------------
*WELL  2  'PROD2' *ATTACHTO 'PLAT'

*PRODUCER 'PROD2' ** WELL no.2
*OPERATE *MAX *STL 30.0
**OPERATE *MIN *BHP 180.0
**MONITOR *WCUT     0.95   *STOP

*GEOMETRY *K 0.100 0.37 1 0
*PERF *GEO 'PROD2'
   1 51 1 1.000000
   1 51 2 1.000000
   1 51 3 1.000000

** -------------------------------------------------------
*WELL  3  'INJ1' *ATTACHTO 'PLAT'

*INJECTOR 'INJ1' ** WELL no.3
*INCOMP *WATER
**OPERATE *MAX *BHP 220.000
*OPERATE *MAX *STW  44.000

*GEOMETRY *K 0.100 0.37 1 0
*PERF *GEO 'INJ1'
   26 1 3 1.000000
   26 1 2 1.000000
   26 1 1 1.000000

** -------------------------------------------------------
** RESTRICOES DA PLATAFORMA
 **GCONP 'PLAT'
 **MAX STL  40.0


**WELL_INC
