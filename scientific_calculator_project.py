from tkinter import *
import math

def factorial(n):
   
    if n==0:
        return 1
    
        return -res
    else:
        res=n*factorial(n-1)
        return res

def buttonclick(numbers):
    global operator
    global answer
    if numbers=="**":
        operator1=operator+"^"
        operator=operator+str(numbers)
        text_Input.set(operator1)
    elif numbers=="**(1/":
        operator1=operator+"^(1/"
        operator=operator+str(numbers)
        text_Input.set(operator1)
    elif numbers=="e":
        operator1=operator+"e"
        operator=operator+str(math.e)
        text_Input.set(operator1)
    elif numbers=="π":
        operator1=operator+"π"
        operator=operator+str(math.pi)
        text_Input.set(operator1)
    elif numbers=="/100":
        operator1=operator+"%"
        operator=operator+str(numbers)
        text_Input.set(operator1)

    elif numbers=="**2":
        operator1=operator+"^2"
        operator=operator+str(numbers)
        text_Input.set(operator1)

    elif numbers=="e**":
        operator1=operator+"e^"
        operator=operator+"2.718281828459045**"
        text_Input.set(operator1)

    elif numbers=="**3":
        operator1=operator+"^3"
        operator=operator+str(numbers)
        text_Input.set(operator1)

    elif numbers=="2e":
        operator1=operator+"2e"
        operator=operator+str(math.e*2)
        text_Input.set(operator1)
    
    elif numbers=="2π":
        operator1=operator+"2π"
        operator=operator+str(math.pi*2)
        text_Input.set(operator1)
    

    else:
        operator=operator+str(numbers)
        if "**" in operator:
            operator3=operator
            operator2=operator3.replace("**","^")
            text_Input.set(operator2)
        
        else:
            text_Input.set(operator)
    if "**" in operator:
            operator3=operator
            operator2=operator3.replace("**","^")
            text_Input.set(operator2)
    
def buttonclear():
    global operator
    operator=''
    text_Input.set('')
  
def buttonequalsinput():
    global operator
    global answer
    sumupoperator=str(eval(operator))
    text_Input.set(sumupoperator)
    answer=sumupoperator
    operator=answer

def oneclear():
    global operator
    d=list(operator)
    d.pop(-1)
    e=len(d)
    operator = ''
    for i in range(0,e):
        operator=operator+d[i]
    if "**" in operator:
        operator3=operator
        operator2=operator3.replace("**","^")
        text_Input.set(operator2)
    else:
        text_Input.set(operator)            

def buttonans(ans):
    global operator
    global answer
    operator=operator+str(answer)
    text_Input.set(operator)

def allclick(sp_op):
    global operator
    global answer
    if operator.isdigit()!=True:
        b=""
        a=len(operator)
        l=list(operator)
        for i in range(-1,-a-1,-1):
            if operator[i] not in ["+","*","/","-",]:
                b=operator[i]+b
                l.pop(-1)
            else:
                break

        if len(l)>2:    
            if l[-2] in ["+","*","/","-"]:
                if l[-1] in ["+","*","/","-",]:
                    b=l[-1]+b
                    b=float(b)
                    l.pop(-1)
        else:
            if len(l)<2  and len(l)>0 :
                    b=l[-1]+b
                    b=float(b)
                    l.pop(-1)
            else:
                b=float(b)
        
        b=float(b)
        c=len(l)    
        operator = ''
        for i in range(0,c):
                    operator=operator+l[i]
        
        if sp_op=="sin":
            if d_state.get()==1:
                b=math.radians(b)
            text_Input.set(operator+"sin"+"("+str(b)+")")
            operator=operator+str(math.sin(b))
            
        elif sp_op=="tan":
            if d_state.get()==1:
                b=math.radians(b)
            text_Input.set(operator+"tan"+"("+str(b)+")")
            operator=operator+str(math.tan(b))
            
        elif sp_op=="cos":
            if d_state.get()==1:
                b=math.radians(b)
            text_Input.set(operator+"cos"+"("+str(b)+")")
            operator=operator+str(math.cos(b))
            
        elif sp_op=="10power":
            text_Input.set(operator+"10^"+"("+str(b)+")")
            operator=operator+str(math.pow(10,b))
            
        elif sp_op=="abs":
            text_Input.set(operator+"abs"+"("+str(b)+")")
            operator=operator+str(abs(b))
        
        elif sp_op=="+-":
            text_Input.set(operator+"-"+"("+str(b)+")")
            operator=operator+str((-1)*b)
        
        elif sp_op=="asin":
            text_Input.set(operator+"sin-1"+"("+str(b)+")")
            operator=operator+str(math.asin(b))
            if d_state.get()==1:
                operator=float(operator)
                operator=math.degrees(operator)
                operator=str(operator)
                
            
        elif sp_op=="1/x":
           
            text_Input.set(operator+"1/("+str(b)+")" )  
            operator=operator+str(math.pow(b,-1))

        elif sp_op=="atan":
            text_Input.set(operator+"tan-1"+"("+str(b)+")")
            operator=operator+str(math.atan(b))
            if d_state.get()==1:
                operator=float(operator)
                operator=math.degrees(operator)
                operator=str(operator)
            
        elif sp_op=="acos":
            text_Input.set(operator+"cos-1"+"("+str(b)+")")
            operator=operator+str(math.acos(b))
            if d_state.get()==1:
                operator=float(operator)
                operator=math.degrees(operator)
                operator=str(operator)

        

            
        answer=operator
    else:
        if sp_op=="sin":
            if d_state.get()==1:
                operator=math.radians(float(operator))
            operator=float(operator)
            text_Input.set("sin"+"("+str(operator)+")")
            operator=str(math.sin(operator))
            
        elif sp_op=="tan":
            if d_state.get()==1:
                operator=math.radians(float(operator))
            operator=float(operator)
            text_Input.set("tan"+"("+str(operator)+")")
            operator=str(math.tan(operator))
            
        elif sp_op=="cos":
            if d_state.get()==1:
                operator=math.radians(float(operator))
            operator=float(operator)
            text_Input.set("cos"+"("+str(operator)+")")
            operator=str(math.cos(operator))
            
        elif sp_op=="10power":
            operator=float(operator)
            text_Input.set("10^"+"("+str(operator)+")")
            operator=str(math.pow(10,operator))
            
        elif sp_op=="abs":
            operator=float(operator)
            text_Input.set("abs"+"("+str(operator)+")")
            operator=str(abs(operator))
            
        elif sp_op=="+-":
            operator=float(operator)
            text_Input.set("-"+"("+str(operator)+")")
            operator=str((-1)*operator)

        elif sp_op=="asin":
            operator=float(operator)
            text_Input.set("sin-1"+"("+str(operator)+")")
            operator=str(math.asin(operator))
            if d_state.get()==1:
                operator=float(operator)
                operator=math.degrees(operator)
                operator=str(operator)

        elif sp_op=="1/x":                                     
            
            operator=float(operator)
            text_Input.set("1/("+str(operator)+")")
            operator=str(math.pow(operator,-1))
            
        elif sp_op=="atan":
            text_Input.set("tan-1"+"("+str(operator)+")")
            operator=str(math.atan(operator))
            if d_state.get()==1:
                operator=float(operator)
                operator=math.degrees(operator)
                operator=str(operator)
            
        elif sp_op=="acos":
            operator=float(operator)
            text_Input.set("cos-1"+"("+str(operator)+")")
            operator=str(math.acos(operator))
            if d_state.get()==1:
                operator=float(operator)
                operator=math.degrees(operator)
                operator=str(operator)
        

        answer=operator
def new1(sp_op):
    global operator
    global answer
    if operator.isdigit()!=True:
        b=""
        a=len(operator)
        l=list(operator)
        for i in range(-1,-a-1,-1):
            if operator[i] not in ["+","*","/","-"]:
                b=operator[i]+b
                l.pop(-1)
            else:
                break
        c=len(l)        
        operator = ''
        for i in range(0,c):
                    operator=operator+l[i]                
        b=float(b)
        
        
            
        if sp_op=="log":
            text_Input.set(operator+"log"+"("+str(b)+")")
            operator=operator+str(math.log(b,10))
            
        elif sp_op=="ln":
            text_Input.set(operator+"ln"+"("+str(b)+")")
            operator=operator+str(math.log(b))
        elif sp_op=="n!":
            text_Input.set(operator+str(b)+"!")
            operator=operator+str(factorial(b))
        answer=operator
    else:
        
            
        if sp_op=="log":    
            operator=float(operator)
            text_Input.set("log"+"("+str(operator)+")")
            operator=str(math.log(operator,10))
            
        elif sp_op=="ln":
            operator=float(operator)
            text_Input.set("ln"+"("+str(operator)+")")
            operator=str(math.log(operator))
        elif sp_op=="n!":
            text_Input.set(str(operator)+"!")
            operator=float(operator)
            operator=str(factorial(operator))
            
            
        
            
    
        
        answer=operator


#Creating and calling the calculator GUI window

root=Tk()
root.title("SCIENTIFIC CALCULATOR")
root.config(background="black")
root.resizable(width=False,height=False)
text_Input=StringVar()
#text_Input="0"
operator=""
answer=""
answer1=""
answer2=""

#Initializing formats of the buttons
calc_font=("Bernard MT Condensed",15,"bold")
calc_fg="white"
calc_fgNum="black"
calc_bg="black"
calc_bgNum="azure4"
calc_padx=42
calc_bd=8
calc_wd=1



#Creating the Display Bar of the Calculator
display1=Entry(root,width=46,font=calc_font,textvariable=text_Input,bg="powder blue",bd=30,insertwidth=10,justify="right")                 
display1.grid(columnspan=6)

#Creation of Buttons
button_7=Button(root,padx=calc_padx,bd=calc_bd, width=calc_wd,fg=calc_fgNum,font=calc_font,bg=calc_bgNum,text="7 ",command=lambda:buttonclick(7))
button_7.grid(row=2,column=1)

button_8=Button(root,padx=calc_padx,bd=calc_bd, width=calc_wd, fg=calc_fgNum,font=calc_font,bg=calc_bgNum,text="8 ",command=lambda:buttonclick(8))
button_8.grid(row=2,column=2)

button_9=Button(root,padx=calc_padx,bd=calc_bd, width=calc_wd,fg=calc_fgNum,font=calc_font,bg=calc_bgNum,text="9 ",command=lambda:buttonclick(9))
button_9.grid(row=2,column=3)

button_add=Button(root,padx=calc_padx,bd=calc_bd, width=calc_wd,fg=calc_fg,font=calc_font,bg=calc_bg,text="+ ",command=lambda:buttonclick("+"))
button_add.grid(row=4,column=4)

button_4=Button(root,padx=calc_padx,bd=calc_bd, width=calc_wd,fg=calc_fgNum,font=calc_font,bg=calc_bgNum, text="4 ",command=lambda:buttonclick(4))
button_4.grid(row=3,column=1)

button_5=Button(root,padx=calc_padx,bd=calc_bd, width=calc_wd, fg=calc_fgNum,font=calc_font,bg=calc_bgNum,text=" 5 ",command=lambda:buttonclick(5))
button_5.grid(row=3,column=2)

button_6=Button(root,padx=calc_padx,bd=calc_bd, width=calc_wd,fg=calc_fgNum,font=calc_font,bg=calc_bgNum,text=" 6 ",command=lambda:buttonclick(6))
button_6.grid(row=3,column=3)

button_sub=Button(root,padx=calc_padx,bd=calc_bd, width=calc_wd, fg=calc_fg,font=calc_font,bg=calc_bg,text="  - ",command=lambda:buttonclick("-"))
button_sub.grid(row=3,column=4)

button_1=Button(root,padx=calc_padx,bd=calc_bd, width=calc_wd,fg=calc_fgNum,font=calc_font,bg=calc_bgNum,text=" 1 ",command=lambda:buttonclick(1))
button_1.grid(row=4,column=1)

button_2=Button(root,padx=calc_padx,bd=calc_bd, width=calc_wd,fg=calc_fgNum,font=calc_font,bg=calc_bgNum,text="2",command=lambda:buttonclick(2))
button_2.grid(row=4,column=2)

button_3=Button(root,padx=calc_padx,bd=calc_bd, width=calc_wd,fg=calc_fgNum,font=calc_font,bg=calc_bgNum, text="3",command=lambda:buttonclick(3))
button_3.grid(row=4,column=3)

button_mul=Button(root,padx=calc_padx,bd=calc_bd, width=calc_wd, fg=calc_fg,font=calc_font,bg=calc_bg, text="x",command=lambda:buttonclick("*"))
button_mul.grid(row=2,column=4)

button_equ=Button(root,padx=calc_padx,bd=calc_bd, width=calc_wd, fg=calc_fg,font=calc_font,bg=calc_bgNum,text="=",command=buttonequalsinput)
button_equ.grid(row=5,column=4)

button_0=Button(root,padx=calc_padx,bd=calc_bd, width=calc_wd,fg=calc_fgNum,font=calc_font,bg=calc_bgNum,text="0",command=lambda:buttonclick(0))
button_0.grid(row=5,column=2)

button_C=Button(root,padx=calc_padx,bd=calc_bd, width=calc_wd, fg=calc_fg,font=calc_font,bg="blue",text="C",command=lambda:oneclear())
button_C.grid(row=2,column=0)

button_div=Button(root,padx=calc_padx,bd=calc_bd, width=calc_wd, fg=calc_fg,font=calc_font,bg=calc_bg, text="/",command=lambda:buttonclick("/"))
button_div.grid(row=1,column=4)

button_dot=Button(root,padx=calc_padx,bd=calc_bd, width=calc_wd,fg=calc_fg,font=calc_font,bg=calc_bg,text=".",command=lambda:buttonclick("."))
button_dot.grid(row=5,column=3)

button_sin=Button(root,padx=calc_padx,bd=calc_bd, width=calc_wd,fg=calc_fg,font=calc_font,bg=calc_bg,text="sin",command=lambda:allclick("sin"))
button_sin.grid(row=6,column=1)

button_cos=Button(root,padx=calc_padx,bd=calc_bd, width=calc_wd, fg=calc_fg,font=calc_font,bg=calc_bg,text="cos",command=lambda:allclick("cos"))
button_cos.grid(row=6,column=2)

button_tan=Button(root,padx=calc_padx,bd=calc_bd, width=calc_wd,fg=calc_fg,font=calc_font,bg=calc_bg,text="tan",command=lambda:allclick("tan"))
button_tan.grid(row=6,column=3)

button_ln=Button(root,padx=calc_padx,bd=calc_bd, width=calc_wd,fg=calc_fg,font=calc_font,bg=calc_bg,text="ln",command=lambda:new1("ln"))
button_ln.grid(row=6,column=4)

button_antilog=Button(root,padx=calc_padx,bd=calc_bd, width=calc_wd, fg=calc_fg,font=calc_font,bg=calc_bg,text="10^",command=lambda:allclick("10power"))
button_antilog.grid(row=8,column=3)

button_power=Button(root,padx=calc_padx,bd=calc_bd, width=calc_wd, fg=calc_fg,font=calc_font,bg=calc_bg,text="x^y",command=lambda:buttonclick("**"))
button_power.grid(row=8,column=2)

button_root=Button(root,padx=calc_padx,bd=calc_bd, width=calc_wd,fg=calc_fg,font=calc_font,bg=calc_bg,text="n√",command=lambda:buttonclick("**(1/"))
button_root.grid(row=6,column=0)

button_ans=Button(root,padx=calc_padx,bd=calc_bd, width=calc_wd,fg=calc_fg,font=calc_font,bg="green", text="ans",command=lambda:buttonans("ans"))
button_ans.grid(row=3,column=0)

button_e=Button(root,padx=calc_padx,bd=calc_bd, width=calc_wd, fg=calc_fg,font=calc_font,bg=calc_bg, text="e",command=lambda:buttonclick("e"))
button_e.grid(row=9,column=1)

button_π=Button(root,padx=calc_padx,bd=calc_bd, width=calc_wd, fg=calc_fg,font=calc_font,bg=calc_bg,text="π",command=lambda:buttonclick("π"))
button_π.grid(row=4,column=0)

button_e=Button(root,padx=calc_padx,bd=calc_bd, width=calc_wd, fg=calc_fg,font=calc_font,bg=calc_bg,text="2e",command=lambda:buttonclick("2e"))
button_e.grid(row=9,column=2)

button_e=Button(root,padx=calc_padx,bd=calc_bd, width=calc_wd,fg=calc_fg,font=calc_font,bg=calc_bg,text="e^x",command=lambda:buttonclick("2e"))
button_e.grid(row=5,column=0)

button_π=Button(root,padx=calc_padx,bd=calc_bd, width=calc_wd, fg=calc_fg,font=calc_font,bg=calc_bg, text="2π",command=lambda:buttonclick("2π"))
button_π.grid(row=5,column=0)

button_e=Button(root,padx=calc_padx,bd=calc_bd, width=calc_wd,  fg=calc_fg,font=calc_font,bg=calc_bg, text="x^2",command=lambda:buttonclick("**2"))
button_e.grid(row=8,column=0)

button_π=Button(root,padx=calc_padx,bd=calc_bd, width=calc_wd, fg=calc_fg,font=calc_font,bg=calc_bg,text="x^3",command=lambda:buttonclick("**3"))
button_π.grid(row=9,column=0)

button_π=Button(root,padx=calc_padx,bd=calc_bd, width=calc_wd, fg=calc_fg,font=calc_font,bg=calc_bg, text="e^x",command=lambda:buttonclick("e**"))
button_π.grid(row=9,column=3)

button_brac1=Button(root,padx=calc_padx,bd=calc_bd, width=calc_wd, fg=calc_fg,font=calc_font,bg=calc_bg,text="(",command=lambda:buttonclick("("))
button_brac1.grid(row=1,column=1)

button_brac2=Button(root,padx=calc_padx,bd=calc_bd, width=calc_wd,  fg=calc_fg,font=calc_font,bg=calc_bg,text=")",command=lambda:buttonclick(")"))
button_brac2.grid(row=1,column=2)

button_log=Button(root,padx=calc_padx,bd=calc_bd, width=calc_wd,fg=calc_fg,font=calc_font,bg=calc_bg,text="log",command=lambda:new1("log"))
button_log.grid(row=7,column=4)

button_CE=Button(root,padx=calc_padx,bd=calc_bd, width=calc_wd,fg=calc_fg,font=calc_font,bg="red",text="CE",command=buttonclear)
button_CE.grid(row=1,column=0)

button_abs=Button(root,padx=calc_padx,bd=calc_bd, width=calc_wd,fg=calc_fg,font=calc_font,bg=calc_bg,text="abs",command=lambda:allclick("abs"))
button_abs.grid(row=8,column=4)

button_percent=Button(root,padx=calc_padx,bd=calc_bd, width=calc_wd,fg=calc_fg,font=calc_font,bg=calc_bg,text="%",command=lambda:buttonclick("/100"))             
button_percent.grid(row=1,column=3)
         
button_plusmin=Button(root,padx=calc_padx,bd=calc_bd, width=calc_wd,fg=calc_fg,font=calc_font,bg=calc_bg,text="+/-",command=lambda:allclick("+-"))
button_plusmin.grid(row=5,column=1)

button_asin=Button(root,padx=calc_padx,bd=calc_bd, width=calc_wd,fg=calc_fg,font=calc_font,bg=calc_bg,text="sin-1",command=lambda:allclick("asin"))
button_asin.grid(row=7,column=1)

button_acos=Button(root,padx=calc_padx,bd=calc_bd, width=calc_wd,fg=calc_fg,font=calc_font,bg=calc_bg,text="cos-1",command=lambda:allclick("acos"))
button_acos.grid(row=7,column=2)

button_atan=Button(root,padx=calc_padx,bd=calc_bd, width=calc_wd,fg=calc_fg,font=calc_font,bg=calc_bg,text="tan-1",command=lambda:allclick("atan"))
button_atan.grid(row=7,column=3)


button_reci=Button(root,padx=calc_padx,bd=calc_bd, width=calc_wd, fg=calc_fg,font=calc_font,bg=calc_bg,text="1/x",command=lambda:allclick("1/x"))
button_reci.grid(row=8,column=1)

button_fact=Button(root,padx=calc_padx,bd=calc_bd, width=calc_wd,fg=calc_fg,font=calc_font,bg=calc_bg,text="n!",command=lambda:new1("n!"))
button_fact.grid(row=7,column=0)

d_state=IntVar()
degree=Checkbutton(root, text="DEGREES", variable=d_state,pady=16,padx=18, onvalue=1,bg="lightgrey")
degree.grid(row=9,column=4)

root.mainloop()