import cadquery as cq


# dimensions from datasheet
BOTTOM_OUTER = 15.00
#TOTAL_HEIGHT = 12.15
BODY_HEIGHT = 5.85
ABOVE_PLATE_HEIGHT = 3.35
POLE_DIA = 5.05
BOTTOM_INNER = 14.00
BOTTOM_INNER = 14.00
CROSS_DIA = 5.70
CROSS_LEN = 4.00
CROSS_THICKNESS_1 = 1.10
CROSS_THICKNESS_2 = 1.28
RGB_R = 4.70
TOP_WIDTH = 13.75
PLATE_THICKNESS = 1.20
CLIP_OUTER = 14.70
BELOW_PLATE_HEIGHT = 2.50  # includes foot bumps
BELOW_PLATE_TOTAL_HEIGHT = 5.75  # pole bottom
PIN_HEIGHT = 2.60
PIN_WIDTH = 1.00
PIN_THICKNESS = 0.45
PIN1_X = -2.60
PIN1_Y = 5.75
PIN2_X = 4.40
PIN2_Y = 4.70
RGB_WIDTH = 5.00
RGB_RIGHT = 3.20

# measured dimensions
TOTAL_HEIGHT = 11.8
STEM_WIDTH = 9.41
STEM_HEIGHT = 4.48
STEM_DIA = 6.40
BUMP_X = 9.90
BUMP_Y = 12.5
BUMP_HEIGHT = 0.25
RGB_HEIGHT = 2.91
TOP_HEIGHT = 13.20
TOP_OFFSET = 1.23 - 0.75
CUT2_WIDTH = 1.46
CUT2_HEIGHT = 1.38
LIP_TOP_THICKNESS = 0.83
LIP_BOTTOM_THICKNESS = 0.46
LIP_TOP_HEIGHT = 2.17
LIP_BOTTOM_HEIGHT = 3.33
BOTTOM_W1 = 11.85
BOTTOM_W2 = BOTTOM_INNER
BOTTOM_W3 = 11.68
BOTTOM_W4 = 12.90
BOTTOM_H1 = 0.7
BOTTOM_H2 = 1.05
BOTTOM_H3 = 3.3
BOTTOM_H4 = 1.9
BOTTOM_TAB_HEIGHT = (BOTTOM_INNER - BOTTOM_H1 - BOTTOM_H2*2 - BOTTOM_H3 - BOTTOM_H4)/2


a = cq.Assembly()


# bottom housing
lipTop = (cq.Workplane("XY").workplane(BELOW_PLATE_HEIGHT).move(0, BOTTOM_OUTER/2 - LIP_TOP_HEIGHT/2)
       .rect(BOTTOM_OUTER, LIP_TOP_HEIGHT)
       .extrude(LIP_TOP_THICKNESS)
       .edges("|Z and >Y").fillet(1))
lipBottom = (cq.Workplane("XY").workplane(BELOW_PLATE_HEIGHT).move(0, LIP_BOTTOM_HEIGHT/2 - BOTTOM_OUTER/2)
       .rect(BOTTOM_OUTER, LIP_BOTTOM_HEIGHT)
       .extrude(LIP_BOTTOM_THICKNESS)
       .edges("|Z and <Y").fillet(1))
lip = lipTop + lipBottom
#show_object(lip)
#bottom = (cq.Workplane("XY").workplane(BELOW_PLATE_HEIGHT)
#          .rect(BOTTOM_INNER, BOTTOM_INNER)
#          .extrude(-(BELOW_PLATE_HEIGHT - BUMP_HEIGHT))
#          .edges("|Z").fillet(0.2))
#show_object(bottom)
bottom = (cq.Workplane("XY").workplane(BUMP_HEIGHT).sketch()
           .rect(BOTTOM_W3, BOTTOM_INNER)
           .push([(0, BOTTOM_INNER/2 - BOTTOM_H1/2)])
           .rect(BOTTOM_W1, BOTTOM_H1)
           .reset().push([(0, BOTTOM_H4/2 - BOTTOM_INNER/2)])
           .rect(BOTTOM_W1, BOTTOM_H4)
           .reset().push([
               (0, BOTTOM_INNER/2 - BOTTOM_H1 - BOTTOM_H2/2),
               (0, -BOTTOM_INNER/2 + BOTTOM_H4 + BOTTOM_H2/2)])
           .rect(BOTTOM_W2, BOTTOM_H2)
           .reset().push([(0, BOTTOM_INNER/2 - BOTTOM_H1 - BOTTOM_H2 - BOTTOM_TAB_HEIGHT - BOTTOM_H3/2)])
           .rect(BOTTOM_W4, BOTTOM_H3)
           .finalize()
           .extrude(BELOW_PLATE_HEIGHT - BUMP_HEIGHT)
           .wires(">Z").toPending().extrude(LIP_BOTTOM_THICKNESS)
           .faces(">Z").shell(-0.6))
#show_object(bottom)
rgb = (cq.Workplane("XY").workplane(BUMP_HEIGHT).sketch()
       .push([(-(RGB_RIGHT - RGB_WIDTH/2), POLE_DIA/2 + 1.3 + RGB_HEIGHT/2)])
       .rect(RGB_WIDTH, RGB_HEIGHT)
       .reset()
       .circle(RGB_R, mode='s'))
bottom = bottom.placeSketch(rgb).cutThruAll()
#show_object(bottom)
bottom = (bottom.moveTo(0, -(POLE_DIA/2 - 0.1 + CUT2_HEIGHT/2))
          .rect(CUT2_WIDTH, CUT2_HEIGHT).cutThruAll())

pole = (cq.Workplane("XY").workplane(BUMP_HEIGHT)
        .circle(POLE_DIA/2).extrude((BELOW_PLATE_HEIGHT - BUMP_HEIGHT)-BELOW_PLATE_TOTAL_HEIGHT)
        .edges("<Z").chamfer(0.8, (POLE_DIA-4)/2)
        .faces("<Z").circle(1.8/2).cutBlind(0.2))
#show_object(pole)
bumps = (cq.Workplane("XY").workplane(BUMP_HEIGHT)
         .rarray(BUMP_X, BUMP_Y, 2, 2).sphere(BUMP_HEIGHT))
#show_object(bumps)
bottom = bottom + lip + pole + bumps
#a.add(bottom, color=cq.Color("black"))

# pins
pin1 = (cq.Workplane("XY").workplane(0.2)
        .move(-PIN1_X, -PIN1_Y)
        .rect(PIN_WIDTH, PIN_THICKNESS).extrude(-PIN_HEIGHT)
        .edges("<Z and |Y").chamfer(0.6, 0.3))
a.add(pin1, color=cq.Color("gold"))
#show_object(pin1)
pin2 = (cq.Workplane("XY").workplane(0.2)
        .move(-PIN2_X, -PIN2_Y)
        .rect(PIN_THICKNESS, PIN_WIDTH).extrude(-PIN_HEIGHT)
        .edges("<Z and |X").chamfer(0.6, 0.3))
a.add(pin2, color=cq.Color("gold"))
#show_object(pin2)


# top housing
top = (cq.Workplane("XY").workplane(BELOW_PLATE_HEIGHT + LIP_BOTTOM_THICKNESS)
       .move(0, TOP_OFFSET)
       .sketch()
       .polygon([
           (TOP_WIDTH/2, TOP_HEIGHT/2), (TOP_WIDTH/2, -TOP_HEIGHT/2 + 2.5),
           (10.6/2, -TOP_HEIGHT/2), (-10.6/2, -TOP_HEIGHT/2), 
           (-TOP_WIDTH/2, -TOP_HEIGHT/2 + 2.5), (-TOP_WIDTH/2, TOP_HEIGHT/2)])
       .finalize()
       .extrude(ABOVE_PLATE_HEIGHT - LIP_BOTTOM_THICKNESS, taper=5)
       .edges("not #Z").fillet(0.5)
       .faces("<Z").shell(-0.6))
       #.edges(">Z").fillet(0.3))
TAB_DEPTH = BELOW_PLATE_HEIGHT + LIP_BOTTOM_THICKNESS - BUMP_HEIGHT - 0.25
TAB_THICKNESS = (BOTTOM_W2 - BOTTOM_W3)/2
TAB_Z = BELOW_PLATE_HEIGHT + LIP_BOTTOM_THICKNESS - TAB_DEPTH
TAB_Y1 = BOTTOM_INNER/2 - BOTTOM_H1 - BOTTOM_H2 - BOTTOM_TAB_HEIGHT
TAB_Y2 = TAB_Y1 - BOTTOM_TAB_HEIGHT - BOTTOM_H3
tabs = (cq.Workplane("XY").pushPoints([
        (TOP_WIDTH/2 - TAB_THICKNESS, TAB_Y1, TAB_Z),
        (TOP_WIDTH/2 - TAB_THICKNESS, TAB_Y2, TAB_Z),
        (-TOP_WIDTH/2, TAB_Y1, TAB_Z),
        (-TOP_WIDTH/2, TAB_Y2, TAB_Z),
        ])
        .box(TAB_THICKNESS,BOTTOM_TAB_HEIGHT,TAB_DEPTH,(False, False, False)))
#show_object(tabs)
top = top + tabs
CLIP_THICKNESS = 0.5
clips = (cq.Workplane("XY").workplane(BELOW_PLATE_HEIGHT - PLATE_THICKNESS).sketch()
         .push([(TOP_WIDTH/2 + CLIP_THICKNESS/2, TAB_Y1 + BOTTOM_TAB_HEIGHT/2),
                (TOP_WIDTH/2 + CLIP_THICKNESS/2, TAB_Y2 + BOTTOM_TAB_HEIGHT/2),
                (-TOP_WIDTH/2 - CLIP_THICKNESS/2, TAB_Y1 + BOTTOM_TAB_HEIGHT/2),
                (-TOP_WIDTH/2 - CLIP_THICKNESS/2, TAB_Y2 + BOTTOM_TAB_HEIGHT/2)])
         .rect(CLIP_THICKNESS, BOTTOM_TAB_HEIGHT)
         .finalize()
         .extrude(-0.8)
         .edges("<Z and (<X or >X)").chamfer(0.49))
#show_object(clips)
top = top + clips
bottom = bottom - top
#show_object(top)


stemPos = (cq.Workplane("XY").workplane(TOTAL_HEIGHT - BELOW_PLATE_TOTAL_HEIGHT + BELOW_PLATE_HEIGHT).sketch()
              .rect(STEM_WIDTH, STEM_HEIGHT, tag='outer')
              .circle(STEM_DIA/2))
stemNeg = (cq.Workplane("XY").workplane(TOTAL_HEIGHT - BELOW_PLATE_TOTAL_HEIGHT + BELOW_PLATE_HEIGHT).sketch()
              .circle(CROSS_DIA/2)
              .rect(CROSS_THICKNESS_1, CROSS_LEN, mode='s', tag='c1')
              .rect(CROSS_LEN, CROSS_THICKNESS_1, mode='s', tag='c2')
              .push([(CROSS_LEN/2-0.4/2, 0), (0.4/2-CROSS_LEN/2, 0)])
              .rect(0.4, CROSS_THICKNESS_2, mode='s', tag='bump')
              .vertices(tag='bump').fillet(0.09)
              )
stem = (stemPos.finalize().extrude(-4)
        .add(stemNeg).cutBlind(-3)
        .faces(">Z").circle(0.5).cutBlind(-0.2))
top = (top.add(stemPos.wires().offset(0.1)).cutThruAll())
#show_object(stem)

a.add(bottom, color=cq.Color("black"))
a.add(top, color=cq.Color(0.5,0.5,0.5,0.8))
a.add(stem, color=cq.Color("chocolate4"))
show_object(a)
a.save("ks33.step")