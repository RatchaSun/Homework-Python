from tkinter import *
from tkinter import ttk # theme ของ tkinter
import csv

GUI = Tk()
GUI.title('โปรแกรมบันทึกค่าใช้จ่าย by Sun')
GUI.geometry('500x300+500+50')
# กำหนดขนาดหน้าต่าง,+หมายถึงล๊อกตำแหน่งแสดงผลบนจอตามมุมซ้าย,บน

# B1 = ttk.Button(GUI,text='Hello') # สร้างปุ่ม
# B1.pack(ipadx=50,ipady=20) # ackติดปุ่มเข้ากับ GUI
# (ipadx=50,ipady=20)ปรับขนาดปุ่ม

F1 = Frame (GUI)
F1.place (x=100,y=50)

def Save(event=None):
    expense = V_expense.get () # .get คือการดึงข้อมูล
    price = V_price.get() 
    print('รายการ: {} ราคา: {}'.format(expense,price))
    V_expense.set ('')
    V_price.set('')
    # clear ข้อมูล .set คือการเซ็ตใหม่
    
    # บันทึกข้อมูล csv อย่าลืม import csv ด้วย
    with open('savedata.csv','a', encoding='utf-8',newline='') as f:
        # encoding='utf-8' เพื่อให้แสดงผลภาษาไทย
        # with คือการสั่งให้เปิดไฟล์แล้วปิดอัตโนมัติ
        #'a' การบันทึกเรื่อยๆ เพื่อต่อจากข้อมูลเก่า
        # newline='' ทำให้ข้อมูลไม่มีบรรทัดว่าง
        fw = csv.writer(f) # สร้างฟังชั่นสำหรับการเขียนข้อมูล
        data = [expense,price] #ข้อมูลที่เราใส่
        fw.writerow(data)

    E1.focus()
    # ทำให้เคอร์เซอร์กลับไปช่องแรก

GUI.bind('<Return>',Save)       
# ทำให้สามารถกด enter ได้ / ต้องเพิ่ม def save (event=None) ด้วย

FONT1 = (None,20) # ตั้งค่าฟอนต์

#----text1-----
L = ttk.Label(F1,text='รายการค่าใช้จ่าย',font=FONT1).pack() # ใส่หัวข้อ
V_expense = StringVar()
# StringVar() ตัวแปรพิเศษสำหรับเก็บข้อมูลในGUI
E1=ttk.Entry(F1,textvariable=V_expense,font=FONT1)
E1.pack()
#-----------

#----text2-----
L = ttk.Label(F1,text='ราคา (บาท)',font=FONT1).pack() # ใส่หัวข้อ
V_price = StringVar()
# StringVar() ตัวแปรพิเศษสำหรับเก็บข้อมูลในGUI
E2=ttk.Entry(F1,textvariable=V_price,font=FONT1)
E2.pack()
#-----------

B2 = ttk.Button(F1,text='Save',command=Save) # สร้างปุ่มกด
B2.pack(ipadx=50,ipady=20) # .place ทำปุ่มเข้ากับ GUI แบบกำหนดตำแหน่ง

GUI.mainloop() # เพื่อให้เกิดลูปเพื่อเชคตัวเอง(รัน)ตลอดเวลา
