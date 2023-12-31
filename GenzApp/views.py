from django.shortcuts import render
from rest_framework.decorators import api_view

from rest_framework import status

from rest_framework import generics
from rest_framework import filters
from rest_framework import viewsets

from .models import *

from .serializer import *


from rest_framework.response import Response
from .models import *

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


@api_view(["GET"])
def enpoint(request):
    data = {
        "Enpoint" : "Api/",
        "Getting User" : "api/user",
        "Get, Update, Delete User" : "api/user/id",
        "Get and Update User Profile" : "api/userprofile/update",

        # ===================== NEWS ========================
        "Get and Create News" : "api/news",
        "Get and Create NewsLetter" : "api/newsLetter",


        # ===================== SUB ===============================
        "Monthly Subscription" : "api/subMonthly",
        "Yearly Subscription" : "api/subYearly",
        "Yearly Print Subscription" : "api/subYealyPrint",
        

    }

    return Response(data)

# class UserGetCreate(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

#     def create(self, request, *args, **kwargs):
#         response = super().create(request, *args, **kwargs)
#         return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
        

class UserGetCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        email = request.data.get('email', None)

        # Check if a user with the given email already exists
        if email and User.objects.filter(email=email).exists():
            return Response({'message': 'User with this email already exists'}, status=status.HTTP_400_BAD_REQUEST)

        response = super().create(request, *args, **kwargs)
        
        # Check if the creation was successful
        if response.status_code == status.HTTP_201_CREATED:
            return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
        else:
            # Registration failed, customize the error message
            error_message = {'message': 'User registration failed. Please check the provided data.'}
            response.data = error_message
            return response
        

class UserGetUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'pk'

    def users_update(self, serializer):
        instance = serializer.save()


    def users_destroy(self, instance):
        return super().perform_destroy(instance)

class UserProfileGetUpdate(generics.RetrieveUpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    lookup_field = 'pk'

    def user_update(self, serializer):
        instance = serializer.save()


# =================== News =======================
class MagazineGet(generics.ListAPIView):
    # queryset = Magazine.objects.all()
    pass


class NewsGet(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'intro', 'body']

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        
        # Check if the creation was successful
        if response.status_code == status.HTTP_201_CREATED:
            return Response({'message': 'News created successfully'}, status=status.HTTP_201_CREATED)
        else:
            # Creation failed, customize the error message
            error_message = {'message': 'News creation failed. Please check the provided data.'}
            response.data = error_message
            return response
        


class StoryGet(generics.ListCreateAPIView):

    queryset = Stories.objects.all()
    serializer_class = StorySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'intro', 'body']

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        
        # Check if the creation was successful
        if response.status_code == status.HTTP_201_CREATED:
            return Response({'message': 'Story created successfully'}, status=status.HTTP_201_CREATED)
        else:
            # Creation failed, customize the error message
            error_message = {'message': 'Story creation failed. Please check the provided data.'}
            response.data = error_message
            return response



class NewsLetterView(generics.ListCreateAPIView):
    queryset = NewsLetter.objects.all()
    serializer_class = NewsLetterSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        
        # Check if the creation was successful
        if response.status_code == status.HTTP_201_CREATED:
            return Response({'message': 'Subcription successfull'}, status=status.HTTP_201_CREATED)
        else:
            # Creation failed, customize the error message
            error_message = {'message': 'Subsription creation failed. Please check the provided data.'}
            response.data = error_message
            return response

    



class BasicSubscriptionPlanViewSet(generics.ListCreateAPIView):
    queryset = SubscriptionPlan.objects.filter(category='Basic')
    serializer_class = SubscriptionPlanSerializer

class StandardSubscriptionPlanViewSet(generics.ListCreateAPIView):
    queryset = SubscriptionPlan.objects.filter(category='Standard')
    serializer_class = SubscriptionPlanSerializer

class PremiumSubscriptionPlanViewSet(generics.ListCreateAPIView):
    queryset = SubscriptionPlan.objects.filter(category='Premium')
    serializer_class = SubscriptionPlanSerializer

