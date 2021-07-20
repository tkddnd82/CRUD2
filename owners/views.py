import json
from django.shortcuts import render
from django.http     import JsonResponse

#음.....연우님 CRUD2 너무어려워요 ㅜㅜ	


from django.views    import View
from owners.models import Owner,Dog


class OwnersView(View): # 장고의 view를 상속받아 사용  
    # post - 생성할때 주로 사용
    def post(self,request): # 신규 주인 등록
        data = json.loads(request.body) # 들어온 body를 data로 저장

        owner = Owner.objects.create(
            name= data['name'],  # name='시고르자브'가 들어오면 시고르자브가 name이 된다. 즉 'name'과 들어오는 키값이 같아야함
            email = data['email'],
            age = data['age'],
        )
        return JsonResponse({'MESSAGE':'SUCCESS'} , status = 201)
        # http -v POST 127.0.0.1:8000/owners/owners name='시고르자브' email='c@gmail.com' age=27

class DogsView(View): # 장고의 view를 상속받아 사용  
    # post
    def post(self,request): # 강아지 등록
        data = json.loads(request.body)
        owner = Owner.objects.get(name=data['owner']) # 밑의 owner= owner를 위해 따로 빼줌  , owner='철수'라면 value값 철수, get(id=data['id']) 
        
        dog = Dog.objects.create(
            name= data['name'], 
            age = data['age'],
            owner = owner # 이 부분 , foreign key
            )
        return JsonResponse({'MESSAGE':'SUCCESS'} , status = 201)
#http -v POST 127.0.0.1:8000/owners/dogs name='홈런볼' age=30 owner='제이크'

class GetOwners(View):
    def get(self, request):              
        owners = Owner.objects.all()	  #음.....연우님 CRUD2 너무어려워요 ㅜㅜ	
        results=[]
        for owner in owners:			
            results.append(
                {
                    "name" : owner.name,
                    "email": owner.email,
                    "age"  : owner.age
                }
            )
        return JsonResponse({'resutls':results}, status=200)

#path 지정을 자꾸 잘못해서 class를 제대로 시행하는데 어려웠어요 ㅜㅜ 자꾸 오류가 어쩌다 끼워 맞췄는데 ... 잘할수 있겠죠? 음 .. ㅎ 항상 감사합니다  :) 채팅이 느려요 빨라지도록 노력해볼게요!

class GetDogs(View):
    def get(self, request):	
        dogs = Dog.objects.all()	
        results=[]
        for dog in dogs:		
            results.append(
                {
                    "name"   : dog.name,	
                    "age"    : dog.age,
                    "owner"  : dog.owner.name
                }
            )
        return JsonResponse({'resutls':results}, status=200)

class GetDogOwner(View):
    def get(self, request):
        owners = Owner.objects.all()
        results=[]

        for owner in owners:
            list= []		
            for dog in Dog.objects.filter(owner = owner).values('name', 'age'):
                list.append(dog) 	
            results.append(
                {
                    "name" : owner.name,
                    "age"  : owner.age,
                    "dogs" : list
                }
            )
        
        return JsonResponse({'resutls':results}, status=200)
 