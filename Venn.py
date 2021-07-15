from matplotlib import pyplot as plt
import numpy as np
from matplotlib_venn import venn3, venn3_circles
from matplotlib_venn import venn2, venn2_circles



import numpy as np
import os
os.chdir('F:\\EngineData')

plt.close('all')

dFile_data = np.loadtxt("matrixOverlaps.txt", dtype=int)
file=open("TagsOverlaps.txt","r")
fileSC=open("IntraTrialVENNS.txt","r")

SC=fileSC.readlines()


TAGS=file.readlines()

TAKE_TAGS= [0, 1, 9]; 
bDoTwoNOTSQUARECIRC=0 
bDOSQUARECIRC=1

Conly=0
jj28only=0
concPlusJ28only=0
J14only=0
concenptPlus14only=0
a28plus14only=0
Maxunioson=0
index=0
TAKE_TAGSCopy = [x+4 for x in TAKE_TAGS]
passerindex=0
rows, columns = dFile_data.shape
taglen=len(TAKE_TAGS)
for x in dFile_data:
    # scan across and fine proportion matches! 
    
    RowCurrent=x
    RowCurrent=RowCurrent[TAKE_TAGSCopy]
    

    if taglen==3: 
      if RowCurrent[0]==0 and RowCurrent[1]==0 and RowCurrent[2]==0: 
         passerindex=passerindex+1

      if RowCurrent[0]==1 and RowCurrent[1]==0 and RowCurrent[2]==0: 
         Conly=Conly+1 

      if RowCurrent[0]==0 and RowCurrent[1]==1 and RowCurrent[2]==0: 
         jj28only=jj28only+1 

      if RowCurrent[0]==1 and RowCurrent[1]==1 and RowCurrent[2]==0: 
         concPlusJ28only=concPlusJ28only+1 

      if RowCurrent[0]==0 and RowCurrent[1]==0 and RowCurrent[2]==1: 
         J14only=J14only+1 

      if RowCurrent[0]==1 and RowCurrent[1]==0 and RowCurrent[2]==1: 
         concenptPlus14only=concenptPlus14only+1 

      if RowCurrent[0]==0 and RowCurrent[1]==1 and RowCurrent[2]==1: 
         a28plus14only=a28plus14only+1 

      if RowCurrent[0]==1 and RowCurrent[1]==1 and RowCurrent[2]==1: 
         Maxunioson=Maxunioson+1 

  

if bDOSQUARECIRC==1: 
   SCrow=SC[TAKE_TAGS[0]]
# extract out values... 
   strparts=SCrow.split('\t')
   strparts.pop(3)
   strparts[0]=int(strparts[0])
   strparts[1]=int(strparts[1])
   strparts[2]=int(strparts[2])

plt.figure(figsize=(4,4))

if bDOSQUARECIRC==0:
   if bDoTwoNOTSQUARECIRC==0: 

   
      v = venn3(subsets=(Conly, jj28only, concPlusJ28only, J14only, concenptPlus14only, a28plus14only, Maxunioson), set_labels = (TAGS[TAKE_TAGS[0]], TAGS[TAKE_TAGS[1]], TAGS[TAKE_TAGS[2]]))
         
   else:
      v = venn2(subsets=(Conly+concenptPlus14only, jj28only+a28plus14only, concPlusJ28only), set_labels = (TAGS[TAKE_TAGS[0]], TAGS[TAKE_TAGS[1]]))
      
if bDOSQUARECIRC==1: 
   v = venn2(subsets=(strparts[0], strparts[1], strparts[2]), set_labels = ('SQUARE', 'CIRCLE'))
   plt.title(TAGS[TAKE_TAGS[0]])


   
#v.get_patch_by_id('100').set_alpha(1.0)
#v.get_patch_by_id('100').set_color('white')
#.get_label_by_id('100').set_text('Unknown')
#c = venn3_circles(subsets=(1, 1, 1, 1, 1, 1, 1), linestyle='dashed')
#c[0].set_lw(1.0)
#c[0].set_ls('dotted')

#plt.annotate('Unknown set', xy=v.get_label_by_id('100').get_position() - np.array([0, 0.05]), xytext=(-70,-70),
#             ha='center', textcoords='offset points', bbox=dict(boxstyle='round,pad=0.5', fc='gray', alpha=0.1),
#             arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0.5',color='gray'))

plt.show()