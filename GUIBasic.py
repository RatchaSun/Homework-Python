# GUIBasic.py

from tkinter import * # จากแพคเกจชื่อ tkinter ให้ดึงฟังชั่นทั้งหมด

GUI = Tk () #สร้าง GUI แล้วดึงฟังชั่น Tk()
GUI.geometry ('500x500') # ขนาดหน้าจอของโปรแกรม

L = Label (GUI,text='Hello World',font=(None,40)) # None = ชื่อฟอนต์
L.pack() # วางข้อความจากบนลงด้านล่าง

# Label คือข้อความ

# ทุกคำสั่งต้องเริ่มด้วยอักษรพิมพ์ใหญ่ เช่น Label, None

GUI.mainloop()
