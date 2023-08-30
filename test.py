import cadquery as cq

base = 19
depth = -1
height = 5
dishOffset = height + depth
angle = 30

s1 = cq.Sketch().rect(base,base).vertices().fillet(1)
s2 = cq.Sketch().rect(base-5,base-5).vertices().fillet(1)
f1 = cq.Workplane("XY").placeSketch(s1)
#f2 = cq.Workplane("XY").transformed(offset=(0,0,0), rotate=(angle,0,0)).placeSketch(s2.moved(cq.Location((0,0,height))))
f3 = cq.Workplane("XY").placeSketch(s1)
f4 = cq.Workplane("XY").transformed(offset=(0,0,0)).placeSketch(s2.moved(cq.Location((0,0,height))))
f2 = cq.Workplane("XY").transformed(rotate=(angle,0,0)).transformed(offset=(0,0,height)).placeSketch(s2)
show_object(s1)
show_object(s2)
#show_object(f1)
#show_object(f2)
show_object(f1.add(f2).loft())
#show_object(f3.add(f4).loft())

r = depth/2 + ((base/2+1)*2)**2/(8*depth)
dish = (cq.Workplane("XZ").transformed(rotate=(angle, 0, 0)).transformed(offset=(0, dishOffset, 0))
    .moveTo(-base/2-1,0).radiusArc((0, -depth),-r)
    .lineTo(0, height).lineTo(-base/2, height).close().revolve(360, combine=False)
)

show_object(dish)