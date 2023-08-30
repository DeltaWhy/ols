import cadquery as cq
from ols import keycap
from ols_old import keycap as keycap_old

k1 = keycap(stemType="mx", angle=-9, height=6.0)
k1_old = keycap_old(stemType="mx", angle=-9, height=6.0)
k2 = keycap(stemType="mx", angle=-12, height=6.0)
k2_old = keycap_old(stemType="mx", angle=-12, height=6.0)
k3 = keycap(stemType="mx", angle=-12, height=6.0, depth=-1.5)
k3_old = keycap_old(stemType="mx", angle=-12, height=6.0, depth=-1.5)
k4 = keycap(stemType="mx", angle=-6, height=6.0, depth=-1.5)
k4_old = keycap_old(stemType="mx", angle=-6, height=6.0, depth=-1.5)
k5 = keycap(stemType="mx", angle=-6, unitY=1.5, height=6.0, depth=-1.5)
k5_old = keycap_old(stemType="mx", angle=-6, unitY=1.5, height=6.0, depth=-1.5)


assembly = cq.Assembly(cq.Workplane("XY").transformed(rotate=(0,0,90)), color=cq.Color(1,173/255,0))
assembly.add(k1_old, loc=cq.Location((0,0,0)), color=cq.Color(1,0,0))
assembly.add(k2_old, loc=cq.Location((0,19.05,0)), color=cq.Color(1,0,0))
assembly.add(k3_old, loc=cq.Location((0,19.05*2,0)), color=cq.Color(1,0,0))
assembly.add(k4_old, loc=cq.Location((0,19.05*3,0)), color=cq.Color(1,0,0))
assembly.add(k5_old, loc=cq.Location((0,19.05*4.5,0)), color=cq.Color(1,0,0))
assembly.add(k1, loc=cq.Location((0,0,0)), color=cq.Color(0,1,0))
assembly.add(k2, loc=cq.Location((0,19.05,0)), color=cq.Color(0,1,0))
assembly.add(k3, loc=cq.Location((0,19.05*2,0)), color=cq.Color(0,1,0))
assembly.add(k4, loc=cq.Location((0,19.05*3,0)), color=cq.Color(0,1,0))
assembly.add(k5, loc=cq.Location((0,19.05*4.5,0)), color=cq.Color(0,1,0))
    
if 'show_object' in locals():
    show_object(assembly)
