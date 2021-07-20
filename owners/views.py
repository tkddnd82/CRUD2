import json
from django.shortcuts import render
from django.http     import JsonResponse

# Create your views here.


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
        # http -v POST 127.0.0.1:8000/owners name='시고르자브' email='c@gmail.com' age=23 

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

# get
    def get(self,request): # 주인 리스트 
        owners = Owner.objects.all() #저장된데이터베이스에서 객체를 다 가지고 와서
        results = []
        for owner in owners: #하나씩 돌면서 results에 추가
            dogs = owner.dogs_set.all() #역참조하기 : 테이블명소문자_set
            dog_list = []

            for dog in dogs:
                dog_info = { 
                        'name' : dog.name,
                        'age' : dog.age
                    }

                dog_list.append(dog_info) 
            results.append(
                {
                    "name" : owner.name, # 외래키로 다 연결되어있음
                    "email" : owner.email,
                    "age" :  owner.age,
                    'dog' : dog_list
                }
            )
        return JsonResponse({'results': results },status=200 )

        # http -v GET 127.0.0.1:8000/owners/owners

