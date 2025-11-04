from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import get_user_model

User = get_user_model()

async def index(request):
    user = await User.objects.afirst()
    return HttpResponse(f"Hello, {user.username}!")
