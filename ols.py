#!/usr/bin/env python
# coding: utf-8

from typing import Union
import cadquery as cq

class ZSelector(cq.Selector):
    z: float = 0.0
    def __init__(self, z):
        self.z = z
    
    def filter(self, objectList):
        return [o for o in objectList if abs(o.Center().z - self.z) < 0.00001]

def keycap(*,
           unitX = 1,  # TODO
           unitY = 1,  # TOOD
           unit = 19.05,
           bx = 18.3,
           by = 18.3,
           rb = 1.5,
           tx = 13.5,
           ty = 13.5,
           rt = 2.5,
           height = 5.0,
           angle = 0,
           depth = 1.5,
           thickness = 1.5,
           topThickness = 1.5,
           fillet = 0.5,
           stemType = 'mx',
           stemTolerance = 0.0,
           stemTolerance2 = None,
           stemHeight = 1.0,
           stemChamfer1 = 0.2,
           stemChamfer2 = 0.5,
           homingDot = False,
           cut: Union[bool, float] = False):
    baseX = unit * (unitX - 1) + bx
    baseY = unit * (unitY - 1) + by
    base = cq.Sketch().rect(baseX, baseY).vertices().fillet(rb)
    topX = unit * (unitX - 1) + tx
    topY = unit * (unitY - 1) + ty
    top = cq.Sketch().rect(topX, topY).vertices().fillet(rt).moved(cq.Location(cq.Vector(0, 0, height)))
    #show(top, base)

    faceTop = cq.Workplane("XY").transformed(offset=(0,0,0), rotate=(angle,0,0)).placeSketch(top)
    keycap1 = cq.Workplane("XY").tag("base").placeSketch(base).add(faceTop).loft()
    #keycap1

    dishOffset = height + depth - 0.1 if depth < 0 else height
    scoop = (
        cq.Workplane("XZ").transformed(offset=(0, dishOffset, 0), rotate=(angle, 0, 0))
        .add(keycap1).moveTo(-topX/2-0.2,0).threePointArc((0, -depth),(topX/2+0.2,0))
        .lineTo(baseX/2,height).lineTo(-baseX/2,height).close()
    )
    #show(keycap1, scoop)

    if depth >= 0:
        r = depth/2 + ((baseX/2+0.5)*2)**2/(8*depth)
        dish = (cq.Workplane("XZ").transformed(offset=(0, dishOffset, -0.5), rotate=(angle, 0, 0))
            .moveTo(-baseX/2-0.5,0).radiusArc((0, -depth),-r)
            .lineTo(0, height).lineTo(-baseX/2, height).close().revolve(360, combine=False)
        )
    else:
        r = depth/2 + ((baseX/2+1)*2)**2/(8*depth)
        dish = (cq.Workplane("XZ").transformed(offset=(0, dishOffset, -1), rotate=(angle, 0, 0))
            .moveTo(-baseX/2-1,0).radiusArc((0, -depth),-r)
            .lineTo(0, height).lineTo(-baseX/2, height).close().revolve(360, combine=False)
        )
    keycap2 = keycap1 - dish

    if depth >= 0:
        keycap3 = keycap2.edges(">>Z[-2]").fillet(fillet)
    else:
        keycap3 = keycap2.edges(">>Z[-1]").fillet(fillet)
    #keycap3

    innerBase = cq.Sketch().rect(baseX - 2*thickness, baseY - 2*thickness).vertices().fillet(rb)
    #show(base, innerBase)

    innerTop = cq.Sketch().rect(topX - 2*thickness, topY - 2*thickness).vertices().fillet(rt).moved(cq.Location(cq.Vector(0, 0, height - abs(depth) - topThickness)))
    #show(top, innerTop)

    faceInnerTop = cq.Workplane("XY").transformed(offset=(0,0,0), rotate=(angle,0,0)).placeSketch(innerTop).tag("innerTop")
    inner = cq.Workplane("XY").placeSketch(innerBase).add(faceInnerTop).loft()
    #show(keycap3, inner)

    keycap4 = keycap3 - inner
    #show(keycap4)

    if stemType == 'mx':
        #cross = cq.Sketch().rect(1.17+0.6, 1.17+0.6).vertices().circle(0.3,mode='s').reset().rect(4.1, 1.17).rect(1.17, 4.1)
        cross = cq.Sketch().circle(5.3/2).rect(1.17+stemTolerance+0.6, 1.17+stemTolerance+0.6, mode='s', tag='x').vertices(tag='x').circle(0.3,mode='a').reset().rect(4.1+stemTolerance, 1.17+stemTolerance, mode='s').rect(1.17+stemTolerance, 4.1+stemTolerance, mode='s').clean()
        #cross
        points = [cq.Location(cq.Vector(0,0,-stemHeight))]
        if 2 <= unitX < 3:
            points.append(cq.Location(cq.Vector(unit*1.25/2,0,-stemHeight)))
            points.append(cq.Location(cq.Vector(-unit*1.25/2,0,-stemHeight)))
        elif unitX >= 3:
            points.append(cq.Location(cq.Vector((unitX-1)*unit/2,0,-stemHeight)))
            points.append(cq.Location(cq.Vector(-(unitX-1)*unit/2,0,-stemHeight)))
        wp = cq.Workplane("XY")
        wp = wp.placeSketch(*[cross.moved(p) for p in points]).tag('cross')
        stem = wp.extrude(height+stemHeight,combine=False).split(keycap4).solids("<Z")
    elif stemType == 'choc':
        if stemTolerance2 is None:
            stemTolerance2 = stemTolerance
        choc = (cq.Sketch()
            .push([(-5.7/2,0),(5.7/2,0)])
            .rect(0.45+stemTolerance,2.9+stemTolerance2)
            .rect(0.9+stemTolerance, 2.9-0.75+stemTolerance2)
            .rect(0.45+stemTolerance, 2.9-0.75+stemTolerance2, mode='c', tag='x')
            .vertices(tag='x').circle(0.75/2).clean()
        )
        #show_object(choc)
        stem = cq.Workplane("XY").placeSketch(choc.moved(cq.Location(cq.Vector(0,0,-stemHeight)))).tag('cross').extrude(height+stemHeight,combine=False).split(keycap4).solids("<Z")
    else:
        raise ValueError(stem)
    keycap5 = keycap4 + stem
    #keycap5

    if stemType == 'mx':
        if 2 <= unitX < 2.25:
            stemChamfer2 = min(0.2, stemChamfer2)
        keycap6 = keycap5.edges("<Z and %Line").chamfer(stemChamfer1)
        for point in points:
            (x,y,z), _ = point.toTuple()
            keycap6 = keycap6.edges(cq.NearestToPointSelector((x,y,height-thickness))).chamfer(stemChamfer2)
        #keycap6 = keycap5.edges("<Z and %Line").chamfer(stemChamfer1).wires(ZSelector(height - abs(depth) - topThickness) & cq.selectors.RadiusNthSelector(1)).chamfer(stemChamfer2)
        #keycap6
    else:
        keycap6 = keycap5

    if homingDot:
        keycap = cq.Workplane("XY").transformed(offset=(0,0,height-depth)).sphere(0.4).add(keycap6).combine()
    else:
        keycap = keycap6
        
    if cut is True:
        cut = 0.6
    if cut:
        keycap = cq.Workplane("XZ").add(keycap).workplane(by/2 - cut).split(keepBottom=True)
    
    return keycap


if 'show_object' in locals():
    #show_object(keycap(stemType="choc", angle=-6, depth=-1.5, stemTolerance=0.05))
    show_object(keycap(stemType="mx", angle=-6, depth=-1.5))
    #show_object(keycap(stemType="mx", angle=-6, depth=-1, unitX=6.25))
