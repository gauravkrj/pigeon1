from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
#from rest_framework import permissions
#from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from .serializers import TeacherSerializer, ParentSerializer, StudentSerializer, AdminstaffSerializer,ClassroomSerializer
from . import models


 #UseraccountSerializer, UsermanagerSerializer, 
class TeacherList(generics.ListCreateAPIView):
    queryset = models.Teacher.objects.all()
    serializer_class = TeacherSerializer
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [permissions.IsAuthenticated]

class TeacherDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Teacher.objects.all()
    serializer_class = TeacherSerializer
   # authentication_classes = [TokenAuthentication]
    #permission_classes = [permissions.IsAuthenticated]

@csrf_exempt    
def teacher_login(request):
    email=request.POST['email']
    password=request.POST['password']
    teacherloginData=models.Teacher.objects.get(email=email,password=password)
    if teacherloginData:
        return JsonResponse({'bool':True})
    else:
        return JsonResponse({'bool':False})






class StudentList(generics.ListCreateAPIView):
    queryset = models.Student.objects.all()
    serializer_class = StudentSerializer
   # authentication_classes = [TokenAuthentication]
    #permission_classes = [permissions.IsAuthenticated]
    

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Student.objects.all()
    serializer_class = StudentSerializer
   # authentication_classes = [TokenAuthentication]
    #permission_classes = [permissions.IsAuthenticated]

@csrf_exempt    
def student_login(request):
    email=request.POST['email']
    password=request.POST['password']
    studentloginData=models.Student.objects.get(email=email,password=password)
    if studentloginData:
        return JsonResponse({'bool':True})
    else:
        return JsonResponse({'bool':False})



    



class ParentList(generics.ListCreateAPIView):
    queryset = models.Parent.objects.all()
    serializer_class = ParentSerializer
   # authentication_classes = [TokenAuthentication]
    #permission_classes = [permissions.IsAuthenticated]
    

class ParentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Parent.objects.all()
    serializer_class = ParentSerializer
   # authentication_classes = [TokenAuthentication]
    #permission_classes = [permissions.IsAuthenticated]
    
@csrf_exempt    
def parent_login(request):
    email=request.POST['email']
    password=request.POST['password']
    parentloginData=models.Parent.objects.get(email=email,password=password)
    if parentloginData:
        return JsonResponse({'bool':True})
    else:
        return JsonResponse({'bool':False})






    
    

class AdminstaffList(generics.ListCreateAPIView):
    queryset = models.Adminstaff.objects.all()
    serializer_class = AdminstaffSerializer
   # authentication_classes = [TokenAuthentication]
   # permission_classes = [permissions.IsAuthenticated]
    

class AdminstaffDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Adminstaff.objects.all()
    serializer_class = AdminstaffSerializer
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [permissions.IsAuthenticated]

@csrf_exempt    
def adminstaff_login(request):
    email=request.POST['email']
    password=request.POST['password']
    adminstaffloginData=models.Adminstaff.objects.get(email=email,password=password)
    if adminstaffloginData:
        return JsonResponse({'bool':True})
    else:
        return JsonResponse({'bool':False})
        



class ClassroomList(generics.ListCreateAPIView):
    queryset = models.Classroom.objects.all()
    serializer_class = ClassroomSerializer
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [permissions.IsAuthenticated]
    
class ClassroomDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Classroom.objects.all()
    serializer_class = ClassroomSerializer
   # authentication_classes = [TokenAuthentication]
    #permission_classes = [permissions.IsAuthenticated]
    


# class UseraccountList(APIView):
#     def get(self,request):
#         useraccounts = models.Useraccount.objects.all()
#         serializer = UseraccountSerializer(useraccounts, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = UseraccountSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)
    

# class UsermanagerList(APIView):
#     def get(self,request):
#         usermanagers = models.Usermanager.objects.all()
#         serializer = UsermanagerSerializer(usermanagers, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = UsermanagerSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)