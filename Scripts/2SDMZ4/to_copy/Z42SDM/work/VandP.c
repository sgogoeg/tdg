#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "../../CalcHEP_src/include/extern.h"
#include "../../CalcHEP_src/include/VandP.h"
#include "autoprot.h"
extern int  FError;
/*  Special model functions  */
extern int access(const char *pathname, int mode);

int nModelParticles=19;
static ModelPrtclsStr ModelPrtcls_[19]=
{
  {"a","a",1, 22, "0","0",2,1,2,0}
, {"Z","Z",1, 23, "MZ","WZ",2,1,3,0}
, {"W+","W-",0, 24, "MW","WW",2,1,3,3}
, {"g","g",1, 21, "0","0",2,8,16,0}
, {"ve","ve~",0, 12, "0","0",1,1,2,0}
, {"vm","vm~",0, 14, "0","0",1,1,2,0}
, {"vt","vt~",0, 16, "0","0",1,1,2,0}
, {"e-","e+",0, 11, "0","0",1,1,2,-3}
, {"mu-","mu+",0, 13, "0","0",1,1,2,-3}
, {"ta-","ta+",0, 15, "MTA","0",1,1,2,-3}
, {"u","u~",0, 2, "0","0",1,3,6,2}
, {"c","c~",0, 4, "0","0",1,3,6,2}
, {"t","t~",0, 6, "MT","WT",1,3,6,2}
, {"d","d~",0, 1, "0","0",1,3,6,-1}
, {"s","s~",0, 3, "0","0",1,3,6,-1}
, {"b","b~",0, 5, "MB","0",1,3,6,-1}
, {"H","H",1, 25, "MH","WH",0,1,1,0}
, {"~DM1","~dm1",0, 301, "MDM1","0",0,1,1,0}
, {"~~DM2","~~DM2",1, 302, "MDM2","0",0,1,1,0}
};
ModelPrtclsStr *ModelPrtcls=ModelPrtcls_; 
int nModelVars=23;
int nModelFunc=6;
static int nCurrentVars=22;
int*currentVarPtr=&nCurrentVars;
static char*varNames_[29]={
 "cabi","DMlamb41","DMlamb42","DMlamb412","DMlambS1","DMlambS2","DMmuS1","DMlamb51","aEWM1","Gf"
,"aS","ymb","ymt","ymtau","MZ","MTA","MT","MB","MH","MDM1"
,"MDM2","E","Pi","CKM1x1","CKM1x2","CKM2x1","CKM2x2","aEW","MW"};
char**varNames=varNames_;
static REAL varValues_[29]={
   2.277360E-01,  1.000000E-01,  1.000000E-01,  1.000000E-01,  1.000000E-01,  1.000000E-01,  1.000000E-01,  1.000000E-01,  1.279000E+02,  1.166370E-05
,  1.184000E-01,  4.700000E+00,  1.720000E+02,  1.777000E+00,  9.118760E+01,  1.777000E+00,  1.720000E+02,  4.700000E+00,  1.250000E+02,  1.000000E+00
,  1.000000E+00,  2.718282E+00,  3.141593E+00};
REAL*varValues=varValues_;
int calcMainFunc(void)
{
   int i;
   static REAL * VV=NULL;
   static int iQ=-1;
   static int cErr=1;
   REAL *V=varValues;
   FError=0;
   if(VV && cErr==0)
   { for(i=0;i<nModelVars;i++) if(i!=iQ && VV[i]!=V[i]) break;
     if(i==nModelVars)     return 0;
   }
  cErr=1;
   nCurrentVars=23;
   V[23]=Cos(V[0]);
   if(!isfinite(V[23]) || FError) return 23;
   nCurrentVars=24;
   V[24]=Sin(V[0]);
   if(!isfinite(V[24]) || FError) return 24;
   nCurrentVars=25;
   V[25]=-Sin(V[0]);
   if(!isfinite(V[25]) || FError) return 25;
   nCurrentVars=26;
   V[26]=Cos(V[0]);
   if(!isfinite(V[26]) || FError) return 26;
   nCurrentVars=27;
   V[27]=Pow(V[8],-1);
   if(!isfinite(V[27]) || FError) return 27;
   nCurrentVars=28;
   V[28]=Pow(Pow(V[14],2)/(2.)+Pow(Pow(V[14],4)/(4.)-V[27]*V[22]*Pow(2,-0.5)*Pow(V[9],-1)*Pow(V[14],2),0.5),0.5);
   if(!isfinite(V[28]) || FError) return 28;
   if(VV==NULL) 
   {  VV=malloc(sizeof(REAL)*nModelVars);
      for(i=0;i<nModelVars;i++) if(strcmp(varNames[i],"Q")==0) iQ=i;
   }
   for(i=0;i<nModelVars;i++) VV[i]=V[i];
   cErr=0;
   nCurrentVars++;
   return 0;
}
