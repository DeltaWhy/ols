import cadquery as cq


# datasheet dimensions
TOTAL_HEIGHT = 3.00
BODY_HEIGHT = 1.85
PIN_HEIGHT = TOTAL_HEIGHT - BODY_HEIGHT
BODY_LENGTH = 11.85
TOTAL_LENGTH = 15.1
PIN_DIST_X = 7.00
PIN_DIST_Y = 1.05
SLOT_LENGTH = 1.20
TOTAL_WIDTH = 5.40
BODY_WIDTH = 4.35
TAB_WIDTH = 1.7
TAB_LENGTH = (TOTAL_LENGTH - BODY_LENGTH) / 2
PIN_DIA = 2.90
PIN_PCB_DIA = 3
PIN1_X = 4.4
PIN2_X = PIN1_X - PIN_DIST_X
PIN1_Y = 4.7
PIN2_Y = 5.75
POLE_DIA = 5.1
OUTLINE_SIZE = 14
PCB_THICKNESS = 1.2


# approximate dimensions
SLOT_WIDTH = 0.15


s1 = (cq.Workplane("XY").sketch()
      .rect(OUTLINE_SIZE, OUTLINE_SIZE)
      .circle(POLE_DIA/2, mode='s')
      .push([(PIN1_X, PIN1_Y), (PIN2_X, PIN2_Y)])
      .circle(PIN_PCB_DIA/2, mode='s'))
#show_object(s1)

pins = (cq.Workplane("XY").pushPoints([
        (PIN1_X, PIN1_Y, -PCB_THICKNESS), (PIN2_X, PIN2_Y, -PCB_THICKNESS)])
        .tag("pinPoints")
        .circle(PIN_DIA/2).extrude(PIN_HEIGHT)
        .pushPoints([
                (PIN1_X, PIN1_Y, -PCB_THICKNESS + PIN_HEIGHT),
                (PIN2_X, PIN2_Y, -PCB_THICKNESS + PIN_HEIGHT)])
        .rect(SLOT_LENGTH, SLOT_WIDTH).cutThruAll()
        .edges(">Z and %Line").chamfer(0.2)
        .edges(">Z and %Circle").chamfer(0.15))
#show_object(pins, options={"color":"black"})

CX = PIN1_X - PIN_DIST_X / 2
CY = PIN1_Y + PIN_DIST_Y / 2
bodySketch = (cq.Workplane("XY").workplane(-PCB_THICKNESS).tag("bodyTop").sketch()
        .push([(PIN1_X, PIN1_Y), (PIN2_X, PIN2_Y)])
        .circle(1)
        .reset()
        .push([(CX, CY)])
        #.rect(BODY_LENGTH, TOTAL_WIDTH)
        .reset()
        .polygon([
            (CX + BODY_LENGTH/2, PIN1_Y + BODY_WIDTH/2),
            (CX + BODY_LENGTH/2, PIN1_Y - BODY_WIDTH/2),
            (PIN1_X - 2, PIN1_Y - BODY_WIDTH/2),
            (PIN2_X + 3, PIN2_Y - BODY_WIDTH/2),
            (CX - BODY_LENGTH/2, PIN2_Y - BODY_WIDTH/2),
            (CX - BODY_LENGTH/2, PIN2_Y + BODY_WIDTH/2),
            (PIN2_X + 4, PIN2_Y + BODY_WIDTH/2),
            (PIN1_X - 1.5, PIN1_Y + BODY_WIDTH/2),
        ])
        )
#show_object(bodySketch)
body = (bodySketch.finalize().extrude(-BODY_HEIGHT)
        .edges("|Z").chamfer(0.1)
        .pushPoints([
                (PIN1_X, PIN1_Y, -BODY_HEIGHT),
                (PIN2_X, PIN2_Y, -BODY_HEIGHT)])
        .rect(SLOT_LENGTH, TAB_WIDTH+0.5).cutBlind(BODY_HEIGHT-0.1)
        .pushPoints([(CX+BODY_LENGTH/2, PIN1_Y, -BODY_HEIGHT), (CX-BODY_LENGTH/2, PIN2_Y, -BODY_HEIGHT)])
        .rect(5, TAB_WIDTH).cutBlind(0.5)
        .faces(">Z").sketch().circle(PIN_DIA/2).rect(10, PIN_DIA-0.5, mode='i').finalize().cutBlind(-0.11)
        .edges("#Z and (<Z or >Z)").chamfer(0.1)
        .pushPoints([(CX-1, CY + TOTAL_WIDTH/2)])
        .rect(1, 0.5).cutThruAll()
        )
#show_object(body, options={"color": "black"})

tab1Sketch = (cq.Workplane("YZ", (CX+BODY_LENGTH/2, PIN1_Y, -PCB_THICKNESS)).sketch()
        .push([(0,-0.3)]).rect(TAB_WIDTH, 0.15)
        .push([(TAB_WIDTH/2, -0.3-BODY_HEIGHT/2+0.3), (-TAB_WIDTH/2, -0.3-BODY_HEIGHT/2+0.3)])
        .rect(0.15, BODY_HEIGHT-0.6+0.15))
tab1 = (tab1Sketch.finalize().extrude(TAB_LENGTH)
        .edges(">Z and |X").fillet(0.15)
        .edges("<Z and >X and |Y").fillet(0.3))
tab1 = (tab1.faces(">Z").transformed(rotate=(90,0,0)).sketch()
        .push([(0,TAB_LENGTH/2)])
        .circle(0.2).rect(0.15, TAB_LENGTH)
        .push([(0,TAB_LENGTH),(0,0)]).circle(0.1)
        .finalize().cutThruAll())
tab2Sketch = (cq.Workplane("YZ", (CX-BODY_LENGTH/2, PIN2_Y, -PCB_THICKNESS)).transformed(rotate=(0,180,0)).sketch()
              .push([(0,-0.3)]).rect(TAB_WIDTH, 0.15)
              .push([(TAB_WIDTH/2, -0.3-BODY_HEIGHT/2+0.3), (-TAB_WIDTH/2, -0.3-BODY_HEIGHT/2+0.3)])
              .rect(0.15, BODY_HEIGHT-0.6+0.15))
tab2 = (tab2Sketch.finalize().extrude(TAB_LENGTH)
        .edges(">Z and |X").fillet(0.15)
        .edges("<Z and <X and |Y").fillet(0.3))
tab2 = (tab2.faces(">Z").transformed(rotate=(90,0,0)).sketch()
        .push([(0,TAB_LENGTH/2)])
        .circle(0.2).rect(0.15, TAB_LENGTH)
        .push([(0,TAB_LENGTH),(0,0)]).circle(0.1)
        .finalize().cutThruAll())
#show_object(tab1)
#show_object(tab2)

a = cq.Assembly()
a.add(pins + body, color=cq.Color("black"))
a.add(tab1 + tab2, color=cq.Color("gold"))
show_object(a)
a.save("ks33_socket.step")