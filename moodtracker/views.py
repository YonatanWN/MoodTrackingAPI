from django.http import Http404
from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm
from rest_framework import status, permissions, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from moodtracker.models import MoodInput,MoodForm


# Create your views here.
from moodtracker.permissions import IsOwnerOrReadOnly
from moodtracker.serializers import MoodInputSerializer, UserSerializer

#Adapted and Copied from: https://www.django-rest-framework.org/tutorial/
class UserList(generics.ListAPIView):
    queryset = MoodInput.objects.all()
    serializer_class = UserSerializer

class MoodList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    def get(self, request, format=None):
        if request.user.is_authenticated:

            ls = MoodInput.objects.filter(user=request.user).order_by('-date')
            setStreakValues(ls)
            serializer = MoodInputSerializer(ls, many=True)
            return Response(serializer.data)
        else:
            return redirect("/login/")
    def post(self,request, format=None):
        serializer = MoodInputSerializer(data=request.data)
        if serializer.is_valid():
            setStreakValues(serializer)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED1)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class MoodInputDetail(APIView):
    def get_object(self, pk):
        try:
            return MoodInput.objects.get(pk=pk)
        except MoodInput.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        moodinput = self.get_object(pk)
        serializer = MoodInputSerializer(moodinput)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        moodinput = self.get_object(pk)
        serializer = MoodInputSerializer(moodinput, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        moodinput = self.get_object(pk)
        moodinput.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#Adapted and copied from
def register(response):
    if response.method == "POST":
        form = UserCreationForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect('/moodUserFriendly/')
    else:
        form = UserCreationForm()
    return render(response, 'registration/register.html', context={"form":form})




def home(response):
    ls = []
    if response.method == "POST":
        form = MoodForm(response.POST)
        if form.is_valid():
            form.save(response.user)
        try:
            ls = MoodInput.objects.filter(user=response.user).order_by('-date')
        except:
            pass
    else:
        try:
            ls = MoodInput.objects.filter(user=response.user).order_by('-date')
        except:
            pass
        form = MoodForm()
    setStreakValues(ls)

    return render(response, 'home.html', context={"form":form, "ls":ls})


def setStreakValues(ls):
    lsList = list(ls)
    i = 0
    j = 0
    k = 1
    while k < len(lsList) and j < len(lsList) and i < len(lsList):
        currentStreakModel = lsList[i]

        date0 = lsList[j].date
        date1 = lsList[k].date

        if (date0 - date1).days <= 1:
            currentStreakModel.streak += 1

            j += 1
            k += 1
        else:
            i = k
            j = i
            k = j + 1


def redirecttomood(response):
    return redirect('/moodUserFriendly/')