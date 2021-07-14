import turtle
import random
tao = turtle.Turtle() # ให้ tao = Turtle
color = ['red','blue','yellow','green'] # ตั้งค่าสี
tao.pensize(5)  # ตั้งค่าขนาดเส้นที่เต่าวาด
tao.shape('turtle') # เปลี่ยนลูกศรเป็นรูปเต่า

for i in range (1,11): # เริ่มต้นจาก 1 จนถึงน้อยกว่า 11
	c = random.choice(color) # สุ่มสี
	tao.color(c) # เปลี่ยนสีเต่า
	r = random.randint(50,100) # สุ่มรัศมีระหว่าง 50-100
	print('สุ่มได้รัศมี:' ,r) # วาดแบบสุ่มรัศมี
	tao.circle(r) #  ให้เต่าเดินเป็นวงกลม
	tao.left(36) # หมุน 36 องศาต่อวง
	print('หมุนครั้งที่:' ,i)
