import matplotlib.pyplot as pli # -> 시각화
import numpy as np # -> 데이터 분석
import math # -> 수학 관련 함수가 많음 파이, 절대값, 사인, 코사인
y_or_Y = 'd'
while y_or_Y != 'Y' and y_or_Y != 'y':
    shape = input('어떤 도형을 그릴까요?')
    if shape == '타원':
        a=input("타원을 그리겠습니다\nx^2/a+y^2/b일때\na를 입력해주세요") 
        b=input("타원을 그리겠습니다\nx^2/a+y^2/b일때\nb를 입력해주세요")
        a=int(a) 
        b=int(b)
        #x값 설정
        x = np.arange(0,math.sqrt(a)+0.01,0.00001)
        #y값 설정
        y=np.sqrt(b-b*x**2/a) 
        #각 사분면에 대해 대칭이라는 점을 이용하여 점을 찍음
        pli.plot(x,y,'b')
        pli.plot(x,-y,'b')
        pli.plot(-x,-y,'b')
        pli.plot(-x,y,'b')
        pli.axis("equal")
        pli.title('Ellipse')
        pli.grid(True)
        pli.gca().set_aspect("equal")
        pli.show()    

    elif shape == '쌍곡선':
        a=input("쌍곡선을 그리겠습니다\nx^2/a+y^2/b=1일때\na를 입력해주세요")
        b=input("쌍곡선을 그리겠습니다\nx^2/a+y^2/b=1일때\nb를 입력해주세요")
        asymptote=input("점근선을 표시할까요?")#예 -> 점근선 표시
        a=int(a)
        b=int(b)
        x = np.arange(0,50,0.00001)
        asymptote_a=np.array(x*b/a)
        asymptote_b=np.array(-x*b/a)
        y=np.sqrt(-b+b*x**2/a)
        pli.plot(x,y,'k')
        pli.plot(x,-y,'k')
        pli.plot(-x,-y,'k')
        pli.plot(-x,y,'k')
        if asymptote == '예':
            pli.plot(x,asymptote_a,'--b')
            pli.plot(x,asymptote_b,'--b')
            pli.plot(-x,asymptote_a,'--b')
            pli.plot(-x,asymptote_b,'--b')
        pli.title('Hyperbolic')
        pli.axis("equal")
        pli.grid(True)
        pli.gca().set_aspect("equal")
        pli.show()

    elif shape == '포물선':
        a=input("포물선을 그리겠습니다 4p를 입력해주세요")
        b=input("x축이 준선입니까? y축이 준선입니까?")
        asymptote=input("준선을 표시할까요?")
        a=int(a)
        if b == 'x' or b == 'x축':
            x = np.arange(-100,100,0.001)
            y = x**2/a
            pli.plot(x,y,'k')
            a = np.array([a/4 for i in range(0,200000)])
            if asymptote == '예':
                pli.plot(x,-a,'--b')
        if b == 'y' or b == 'y축':
            x = np.arange(-100,100,0.001)
            y = np.sqrt(x*a)
            pli.plot(x,y,'k')
            pli.plot(x,-y,'k')
            a = np.array([a/4 for i in range(0,200000)])
            if asymptote == '예':
                pli.plot(-a,x,'--b')
        pli.axis("equal")
        pli.grid(True)
        pli.gca().set_aspect("equal")
        pli.show()
    y_or_Y = input("종료하고싶다면 y나 Y를 눌러주세요")