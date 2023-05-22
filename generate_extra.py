import cadquery as cq
from ols import keycap

r3_2u = keycap(unitX=2.0)
r3_2u_cut = keycap(unitX=2.0, cut=True).rotate((0,0,0),(1,0,0),90)
r3c_2u = keycap(unitX=2.0, depth=-1.5)
r3c_2u_cut = keycap(unitX=2.0, depth=-1.5, cut=True).rotate((0,0,0),(1,0,0),90)
r3t = keycap(angle=-6, height=5.5, depth=-1.5)
r3t_cut = keycap(angle=6, height=5.5, depth=-1.5, cut=0.4).rotate((0,0,0),(1,0,0),90)

#assembly = cq.Assembly(cq.Workplane("XY").transformed(rotate=(0,0,90)), color=cq.Color(1,173/255,0))
#assembly.add(r3)
#assembly.add(r2, loc=cq.Location((0, -19.05, 0)))
##assembly.add(r1, loc=cq.Location((0, -19.05*2, 0)))
#assembly.add(r4, loc=cq.Location((0, 19.05, 0)))
#assembly.add(r3h_dot, loc=cq.Location((0, 19.05 * 2, 0)))
##assembly.add(keycap(depth=-1.0, height=5.5, cut=0.5), loc=cq.Location((0, 19.05*3, 0)))

if 'show_object' in locals():
    show_object(r3_2u)
    show_object(r3c_2u.rotate((0,0,0),(0,0,1),-90).translate((-19.05, 0)))
    show_object(r3t.rotate((0,0,0),(0,0,1),-90).translate((19.05, 0)))
    
if __name__ == '__main__':
    cq.exporters.export(r3_2u, 'generated/mx-extra/ols-v1-r3-2u.stl', tolerance=0.001, angularTolerance=0.05)
    cq.exporters.export(r3_2u_cut, 'generated/mx-extra/ols-v1-r3-2u-cut.stl', tolerance=0.001, angularTolerance=0.05)
    cq.exporters.export(r3c_2u, 'generated/mx-extra/ols-v1-r3c-2u.stl', tolerance=0.001, angularTolerance=0.05)
    cq.exporters.export(r3c_2u_cut, 'generated/mx-extra/ols-v1-r3c-2u-cut.stl', tolerance=0.001, angularTolerance=0.05)

    cq.exporters.export(r3_2u, 'generated/mx-extra/ols-v1-r3-2u.step')
    cq.exporters.export(r3_2u_cut, 'generated/mx-extra/ols-v1-r3-2u-cut.step')
    cq.exporters.export(r3c_2u, 'generated/mx-extra/ols-v1-r3c-2u.step')
    cq.exporters.export(r3c_2u_cut, 'generated/mx-extra/ols-v1-r3c-2u-cut.step')
