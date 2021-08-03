from django.shortcuts import render
from rest_framework import generics, views
from BajajApi.models import Details
from BajajApi.serializers import UserSerializer

from django.http import JsonResponse

# Create your views here.
class UserList(generics.ListAPIView):
    queryset = Details.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Details
    serializer_class = UserSerializer


def isnum(s):
    if(s=="0" or s == "1" or s == "2" or s == "3" or s == "4" or s == "5" or s == "6" or s == "7" or s == "8" or s == "9"):
        return True
        
    return False

def split(word):
    return [char for char in word]

def send_json(request, num):
    print(num)
    li = split(num)
    
    status = True
    odd = []
    even = []

    for i in range(len(li)):
        if(isnum(li[i])):
            if int(li[i])%2==0:
                even.append(int(li[i]))
            else:
                odd.append(int(li[i]))
        else:
            status = False
            break

    if(status):
        for i in range(len(li)):
            li[i] = int(li[i])
        userid = "anshuman_prajapati_05092000"
        data = {"Request":{
                   'numbers': li
                    },
                "Response":{
                    'is_success': status,
                    'user_id': userid,
                    'odd': odd, 
                    'even': even
                    }
                }

        return JsonResponse(data)

    else:
        for i in range(len(li)):
            if(isnum(li[i])):
                li[i] = int(li[i])

        userid = "anshuman_prajapati_05092000"
        data = {"Request":{
                   'numbers': li
                    },
                "Response":{
                    'is_success': status, 
                    'user_id': userid
                    }
                }

        return JsonResponse(data)



def send_json_empty(request):

    status = True
    odd = []
    even = []
    userid = "anshuman_prajapati_05092000"
    li = []

    data = {"Request":{
                   'numbers': li
                    },
                "Response":{
                    'is_success': status,
                    'user_id': userid,
                    'odd': odd, 
                    'even': even
                    }
                }

    return JsonResponse(data)