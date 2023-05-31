import cadquery as cq
from ols import keycap

params = dict(
           bx = 17.3,
           by = 16.3,
           tx = 12.5,
           ty = 12.5,
           stemType='choc',
           stemTolerance=0.05,
          )

r3 = keycap(**params)
r3_cut = keycap(**params, cut=True).rotate((0,0,0),(1,0,0),90)
r3h = keycap(**params, depth=2.0)
r3h_cut = keycap(**params, depth=2.0, cut=True).rotate((0,0,0),(1,0,0),90)
r3h_dot = keycap(**params, depth=2.0, homingDot=True)
r3h_dot_cut = keycap(**params, depth=2.0, homingDot=True, cut=True).rotate((0,0,0),(1,0,0),90)
r2 = keycap(**params, angle=-6, height=5.5)
r2_cut = keycap(**params, angle=-6, height=5.5, cut=0.8).rotate((0,0,0),(1,0,0),90)
r4 = keycap(**params, angle=6, height=5.5)
r4_cut = keycap(**params, angle=6, height=5.5, cut=0.4).rotate((0,0,0),(1,0,0),90)
thumb = keycap(**params, angle=-6, depth=-1.0, height=5.5)
thumb_cut = keycap(**params, angle=-6, depth=-1.0, height=5.5, cut=0.8).rotate((0,0,0),(1,0,0),90)
thumb15 = keycap(**params, unitY=1.5, stemRot=90, angle=-6, depth=-1.0, height=5.5)
thumb15_cut = keycap(**params, unitY=1.5, stemRot=90, angle=-6, depth=-1.0, height=5.5, cut=0.8).rotate((0,0,0),(1,0,0),90)

#assembly = cq.Assembly(cq.Workplane("XY").transformed(rotate=(0,0,90)), color=cq.Color(1,173/255,0))
#assembly.add(r3)
#assembly.add(r2, loc=cq.Location((0, -19.05, 0)))
##assembly.add(r1, loc=cq.Location((0, -19.05*2, 0)))
#assembly.add(r4, loc=cq.Location((0, 19.05, 0)))
#assembly.add(r3h_dot, loc=cq.Location((0, 19.05 * 2, 0)))
##assembly.add(keycap(depth=-1.0, height=5.5, cut=0.5), loc=cq.Location((0, 19.05*3, 0)))

if 'show_object' in locals():
    show_object(r3.rotate((0,0,0),(0,0,1),-90))
    show_object(r2.rotate((0,0,0),(0,0,1),-90).translate((-19.05, 0)))
    show_object(r4.rotate((0,0,0),(0,0,1), -90).translate((19.05, 0)))
    show_object(thumb.rotate((0,0,0),(0,0,1), -90).translate((19.05*2, 0)))
    show_object(thumb15.rotate((0,0,0),(0,0,1), -90).translate((19.05*2, 19.05)))
    
if __name__ == '__main__':
    cq.exporters.export(r3, 'generated/choc-sm/ols-v1-r3.stl', tolerance=0.001, angularTolerance=0.05)
    cq.exporters.export(r3_cut, 'generated/choc-sm/ols-v1-r3-cut.stl', tolerance=0.001, angularTolerance=0.05)
    cq.exporters.export(r3h, 'generated/choc-sm/ols-v1-r3-home.stl', tolerance=0.001, angularTolerance=0.05)
    cq.exporters.export(r3h_cut, 'generated/choc-sm/ols-v1-r3-home-cut.stl', tolerance=0.001, angularTolerance=0.05)
    cq.exporters.export(r3h_dot, 'generated/choc-sm/ols-v1-r3-home-dot.stl', tolerance=0.001, angularTolerance=0.05)
    cq.exporters.export(r3h_dot_cut, 'generated/choc-sm/ols-v1-r3-home-dot-cut.stl', tolerance=0.001, angularTolerance=0.05)
    cq.exporters.export(r2, 'generated/choc-sm/ols-v1-r2.stl', tolerance=0.001, angularTolerance=0.05)
    cq.exporters.export(r2_cut, 'generated/choc-sm/ols-v1-r2-cut.stl', tolerance=0.001, angularTolerance=0.05)
    cq.exporters.export(r4, 'generated/choc-sm/ols-v1-r4.stl', tolerance=0.001, angularTolerance=0.05)
    cq.exporters.export(r4_cut, 'generated/choc-sm/ols-v1-r4-cut.stl', tolerance=0.001, angularTolerance=0.05)
    cq.exporters.export(thumb, 'generated/choc-sm/ols-v1-thumb.stl', tolerance=0.001, angularTolerance=0.05)
    cq.exporters.export(thumb_cut, 'generated/choc-sm/ols-v1-thumb-cut.stl', tolerance=0.001, angularTolerance=0.05)
    cq.exporters.export(thumb15, 'generated/choc-sm/ols-v1-thumb-1.5u.stl', tolerance=0.001, angularTolerance=0.05)
    cq.exporters.export(thumb15_cut, 'generated/choc-sm/ols-v1-thumb-1.5u-cut.stl', tolerance=0.001, angularTolerance=0.05)

    cq.exporters.export(r3, 'generated/choc-sm/ols-v1-r3.step')
    cq.exporters.export(r3_cut, 'generated/choc-sm/ols-v1-r3-cut.step')
    cq.exporters.export(r3h, 'generated/choc-sm/ols-v1-r3-home.step')
    cq.exporters.export(r3h_cut, 'generated/choc-sm/ols-v1-r3-home-cut.step')
    cq.exporters.export(r3h_dot, 'generated/choc-sm/ols-v1-r3-home-dot.step')
    cq.exporters.export(r3h_dot_cut, 'generated/choc-sm/ols-v1-r3-home-dot-cut.step')
    cq.exporters.export(r2, 'generated/choc-sm/ols-v1-r2.step')
    cq.exporters.export(r2_cut, 'generated/choc-sm/ols-v1-r2-cut.step')
    cq.exporters.export(r4, 'generated/choc-sm/ols-v1-r4.step')
    cq.exporters.export(r4_cut, 'generated/choc-sm/ols-v1-r4-cut.step')
    cq.exporters.export(thumb, 'generated/choc-sm/ols-v1-thumb.step')
    cq.exporters.export(thumb_cut, 'generated/choc-sm/ols-v1-thumb-cut.step')
    cq.exporters.export(thumb15, 'generated/choc-sm/ols-v1-thumb-1.5u.step')
    cq.exporters.export(thumb15_cut, 'generated/choc-sm/ols-v1-thumb-1.5u-cut.step')
