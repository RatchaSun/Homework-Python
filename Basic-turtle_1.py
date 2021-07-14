import turtle
import random
tao = turtle.Turtle() # ให้ tao = Turtle
color = ['red','blue','yellow','green'] # ตั้งค่าสีที่ใช้
tao.pensize(5)  # ตั้งค่าขนาดเส้นที่เต่าวาด
tao.shape('turtle') # เปลี่ยนลูกศรเป็นรูปเต่า

for i in range (1,11): # เริ่มต้นจาก 1 จนถึงน้อยกว่า 11
        c = random.choice(color) # สุ่มสี
        tao.color(c) #ให้เต่าสุ่มสี
        x = random.randint(-200,200) # สุ่มแกน x
        y = random.randint(-200,200) # สุ่มแกน y
        tao.penup()#สั่งให้ยกปากกาขึ้น (หบุดวาด)
        tao.goto(x,y)# ให้เต่าวิ่งไปจุดที่ต้องการ
        tao.pendown()# สั่งให้วาด
        size = random.randint(50,100) # ความยาวเส้นที่วาด
        
        
        for s in range (4): # วาดสีเหลี่ยม
            tao.forward(size)# ใช้ fd เพื่อย่อ forward ได้
            tao.left(90)# ใช้ l เพื่อย่อ left ได้


