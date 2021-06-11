import high
import middle
import element

h = high.highschool
m = middle.middleschool
e = element.elementschool
counted_h=0
counted_m=0
counted_e=0

#중복 단어 지우기
for word in m:
    if word in h:
        h.remove(word)

for word in e:
    if word in h:
        h.remove(word)

for word in e:
    if word in m:
        m.remove(word)

sentence="""
안녕. 내 이름은 호민이야.

 I’m from Korea.

나는 한국 출신이야. 

I’m in the first year of middle school.

나는 중학교 1학년이야. 

Everything is new and exciting!

모든 것이 새롭고 신나!

There are many fun clubs in my school.

우리 학교에는 재미있는 동아리가 많아. 

I like sports clubs.

나는 운동 동아리를 좋아해. 

I am in the floorball club.

나는 플로어볼 동아리에 속해 있어.

 What is floorball?

플로어볼이 뭐냐고?

It’s like ice hockey.

그것은 아이스하키랑 비슷해. 

But we don't play on the ice.

그런데 우리는 얼음 위에서 하지 않아. 

We play on the floor in the gym.

우리는 체육관 안의 바닥 위에서 해. 

I like floorball a lot!

나는 플로어볼을 정말 좋아해!

Hello. I’m Judy from Australia.

안녕. 나는 호주 출신인 Judy야.

 What do you think of my school uniform?

내 교복에 대해 어떻게 생각하니?

The sunlight is very strong in my country.

우리나라는 햇빛이 무척 강해. 

The strong sunlight isn’t good for the skin.

강한 햇빛은 피부에 좋지 않아. 

So my school has a special rule in summer:

그래서 우리 학교에는 여름에 특별한 규칙이 있어: 

No Hat, No Play.

‘모자 없이, 놀기 금지.’

The hat is part of my school uniform.

모자는 우리 교복의 일부야. 

I always wear the hat outside.

나는 밖에서 항상 모자를 써. 

It looks great on me.

그것은 내게 잘 어울려.

I’m Emma and I’m French.

나는 Emma이고 프랑스 인이야. 

My favorite time at school is lunch time.

내가 학교에서 가장 좋아하는 시간은 점심시간이야. 

I have a delicious lunch every day.

나는 매일 맛있는 점심을 먹어.

 I usually have salad, fish, and bread with cheese.

나는 보통 샐러드, 생선, 그리고 치즈를 곁들인 빵을 먹어.

Lunch time is two hours long.

점심시간은 두 시간이야. 

I eat lunch slowly.

나는 천천히 점심을 먹어. 

I also learn about slow food at school.

나는 또 학교에서 ‘슬로푸드’에 관해 배워. 

Now I don’t eat fast food anymore!

이제 나는 더 이상 패스트푸드를 먹지 않아!
"""

sentence_=sentence.split()

for word in h:
    if sentence.find(word)!=-1:
        # 'at'이 word에 있으면 atmosphere나 ate도 계산에 포함되길래 이를 방지하고자 만든 조건문
        if ' ' not in word and word in sentence_:
            counted_h += 1
        elif ' ' in word:
            counted_h += 1
for word in m:
    if sentence.find(word)!=-1:
        if ' ' not in word and word in sentence_:
            counted_m += 1
        elif ' ' in word:
            counted_m += 1

for word in e:
    if sentence.find(word)!=-1:
        if ' ' not in word and word in sentence_:
            counted_e += 1
        elif ' ' in word:
            counted_e += 1

all_ = counted_e+counted_h+counted_m
rate_h = counted_h/all_*100
rate_m = counted_m/all_*100
rate_e = counted_e/all_*100

print("전체단어개수:{}\n단어장 내 포함된 단어 개수:{}\n초등학교 단어 개수:{}\n중학교 단어 개수:{}\n고등학교 단어 개수:{}"\
.format(len(sentence_),all_,counted_e,counted_m,counted_h))

print("초등학교 단어 비율: {} %\n중학교 단어 비율: {} %\n고등학교 단어 비율: {} %"\
.format(rate_e,rate_m,rate_h))

#2020수능 가장 쉬운 지문이 5%가 나와서 이를 표준으로 삼음
if rate_h >= 5:
    print("Pass")
if rate_h < 5:
    print("fail")