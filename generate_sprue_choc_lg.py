import cadquery as cq


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

r2 = cq.importers.importStep("generated/choc-lg/ols-v1-r2.step")
a = sprue_assembly([r2]*10)
#show_object(a.toCompound())
a.save("generated/sprue/choc-lg-r2-x10.step", mode="fused")
a.save("generated/sprue/choc-lg-r2-x10.stl", mode="fused", tolerance=0.001, angularTolerance=0.05)

r4 = cq.importers.importStep("generated/choc-lg/ols-v1-r4.step")
a = sprue_assembly([r4]*10)
#show_object(a.toCompound())
a.save("generated/sprue/choc-lg-r4-x10.step", mode="fused")
a.save("generated/sprue/choc-lg-r4-x10.stl", mode="fused", tolerance=0.001, angularTolerance=0.05)

r3 = cq.importers.importStep("generated/choc-lg/ols-v1-r3.step")
r3dot = cq.importers.importStep("generated/choc-lg/ols-v1-r3-home-dot.step")
a = sprue_assembly([r3]*8+[r3dot]*2)
#show_object(a.toCompound())
a.save("generated/sprue/choc-lg-r3-x8-dot-x2.step", mode="fused")
a.save("generated/sprue/choc-lg-r3-x8-dot-x2.stl", mode="fused", tolerance=0.001, angularTolerance=0.05)

r3h = cq.importers.importStep("generated/choc-lg/ols-v1-r3-home.step")
a = sprue_assembly([r3]*8+[r3h]*2)
#show_object(a.toCompound())
a.save("generated/sprue/choc-lg-r3-x8-home-x2.step", mode="fused")
a.save("generated/sprue/choc-lg-r3-x8-home-x2.stl", mode="fused", tolerance=0.001, angularTolerance=0.05)

thumb = cq.importers.importStep("generated/choc-lg/ols-v1-thumb.step")
a = sprue_assembly([thumb]*6)
#show_object(a.toCompound())
a.save("generated/sprue/choc-lg-thumb-x6.step", mode="fused")
a.save("generated/sprue/choc-lg-thumb-x6.stl", mode="fused", tolerance=0.001, angularTolerance=0.05)

a = sprue_assembly([r2, r2, r3, r3, r4, r4])
#show_object(a.toCompound())
a.save("generated/sprue/choc-lg-mixed-x6.step", mode="fused")
a.save("generated/sprue/choc-lg-mixed-x6.stl", mode="fused", tolerance=0.001, angularTolerance=0.05)
