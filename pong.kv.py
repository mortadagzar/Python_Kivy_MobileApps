#:kivy 1.0.9

<PongBall>:
    size: 50, 50 
    canvas:
        Ellipse:
            pos: self.pos
            size: self.size          

<PongGame>:
    canvas:
        Rectangle:
            pos: self.center_x-5, 0
            size: 10, self.height
    
    Label:
        font_size: 70  
        center_x: root.width / 4
        top: root.top - 50
        text: "0"
        
    Label:
        font_size: 70  
        center_x: root.width * 3 / 4
        top: root.top - 50
        text: "0"
    
    PongBall:
        center: self.parent.center
fyyy
