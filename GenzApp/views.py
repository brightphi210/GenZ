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

from supabase_client import supabase
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


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

class UserGetCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)


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
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Save image to Supabase Storage
        file = request.data['image']
        file_name = file.name
        file_data = file.read()

        response = supabase.storage.from_bucket("images").upload(file_name, file_data)

        if response["error"]:
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        # Save image details to your Django model
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]



class StoryGet(generics.ListCreateAPIView):

    queryset = Stories.objects.all()
    serializer_class = StorySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'intro', 'body']



class NewsLetterView(generics.ListCreateAPIView):
    queryset = NewsLetter.objects.all()
    serializer_class = NewsLetterSerializer



class BasicSubscriptionPlanViewSet(generics.ListCreateAPIView):
    queryset = SubscriptionPlan.objects.filter(category='Basic')
    serializer_class = SubscriptionPlanSerializer

class StandardSubscriptionPlanViewSet(generics.ListCreateAPIView):
    queryset = SubscriptionPlan.objects.filter(category='Standard')
    serializer_class = SubscriptionPlanSerializer

class PremiumSubscriptionPlanViewSet(generics.ListCreateAPIView):
    queryset = SubscriptionPlan.objects.filter(category='Premium')
    serializer_class = SubscriptionPlanSerializer

