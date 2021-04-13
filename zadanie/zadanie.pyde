def setup():
    size(450, 400)
    textSize(110)
def draw():
    clear()
    background(275)
    text("NW", 100, height/2-75)
    
    n = createShape()
    n.beginShape()
    n.fill(255, 140, 26)
    n.vertex(width-200, height-222)
    n.vertex(width-220, height-260)
    n.vertex(100, height/3*2)
    n.vertex(300, 200)
    strokeWeight(5)
    n.endShape(CLOSE)
    shape(n, 110, 50)
    
    if hex(get(mouseX, mouseY)) == 'FFFF8C1A':
        fill(255, 0, 255)
            
    elif keyPressed:
        if key == 'N' or key == 'W' :
            fill(255, 0, 255)
    else:
         fill(255, 0, 0)
            
# 1,75 pkt
