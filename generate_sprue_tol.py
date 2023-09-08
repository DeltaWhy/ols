import cadquery as cq
from ols import keycap


def sprue_assembly(objs):
    a = cq.Assembly()
    n = int((len(objs)+1)/2)
    
    spru1 = cq.Workplane("YZ").workplane(-1).move(0, -0.6).cylinder(2+20*(n-1), 0.8, centered=(True, True, False))
    a.add(spru1)
    
    for x in range(n):
        spru = cq.Workplane("XZ").move(20*x, -0.6).cylinder(10, 0.8)
        a.add(spru)
        
    for i in range(len(objs)):
        x = int(i/2)
        if i % 2 == 0:
            a.add(objs[i], loc=cq.Location((20*x, -12, 0), (0, 0, 1), 180))
        else:
            a.add(objs[i], loc=cq.Location((20*x, 12, 0)))
    return a

objs = []
for tol in (-0.05, -0.025, 0, 0.025, 0.05):
    objs.append(keycap(stemType="mx", stemTolerance=tol, bottomText=str(tol)))
    objs.append(keycap(stemType="choc", stemTolerance=tol, bottomText=str(tol)))
a = sprue_assembly(objs)
if 'show_object' in locals():
    show_object(a.toCompound())
a.save("generated/sprue/tol-test.step", mode="fused")
#a.save("generated/sprue/tol-test.stl", mode="fused", tolerance=0.001, angularTolerance=0.05)
