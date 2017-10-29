Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import turtle as t
>>> t.up()
>>> t.speed(0)                  #거북이 최대 속도
>>> t.goto(-200,-200)
>>> t.down()
>>> 
>>> for x in range(4):          #한 변의 크기가 500인 정사각형 
	t.fd(500)
	t.left(90)

	
>>> t.goto(300,247)
>>> ang = t.towards(-200,-200) 
>>> t.setheading(360-ang)
>>> t.goto(247,300)
>>> t.setheading(ang)
>>> t.goto(-200,-100)
>>> t.goto(-100,-200)
>>> 
>>> ang = t.towards(50,300)
>>> t.setheading(ang)
>>> t.goto(50,300)
>>> t.setheading(-ang)
>>> t.goto(200,-200)
>>> t.goto(300,50)
>>> 
>>> ang = t.towards(-200,300)
>>> t.setheading(ang)
>>> t.goto(-200,300)
>>> 
>>> t.up()
>>> t.goto(-130,70)
>>> t.setheading(0)
>>> t.down()
>>> 
>>> for x in range(4):         #한 변의 크기가 30인 정사각형
	t.fd(30)
	t.left(90)

	
>>> t.up()
>>> t.goto(-200,300)
>>> t.down()
>>> 
>>> ang = t.towards(-115,100)
>>> t.setheading(ang)
>>> t.goto(-115,100)
>>> t.setheading(-ang)
>>> t.fd(220)
>>> 
>>> ang = t.towards(50,-200)
>>> t.setheading(ang)
>>> t.goto(50,-200)
>>> 
>>> t.goto(-200,50)
>>> 
>>> t.setheading(0)
>>> t.fd(500)
>>> 
