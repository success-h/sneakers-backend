from django.contrib.auth import authenticate
from .models import User
import os
import random
from rest_framework.exceptions import AuthenticationFailed
import environ
env = environ.Env()
environ.Env.read_env()

def generate_username(name):

    username = "".join(name.split(' ')).lower()
    if not User.objects.filter(username=username).exists():
        return username
    else:
        random_username = username + str(random.randint(0, 1000))
        return generate_username(random_username)


def register_social_user(provider, user_id, email, name):
    filtered_user_by_email = User.objects.filter(email=email)

    if filtered_user_by_email.exists():
        registered_user = authenticate(
            email=email, password=env('SOCIAL_SECRET'),
            )
            
        if registered_user is not None:
            user = User.objects.get(email=email)
            user.auth_provider = provider
            user.save()

        return {
            'username': registered_user.username,
            'email': registered_user.email,
            'tokens': registered_user.tokens(),
            'auth_provider': registered_user.auth_provider,
            'id': registered_user.id,
            }


    else:
        user = {
            'username': generate_username(name), 'email': email,
            'password': env('SOCIAL_SECRET')}
        user = User.objects.create_user(**user)
        user.is_verified = True
        user.auth_provider = provider
        user.save()

        new_user = authenticate(
            email=email, password=env('SOCIAL_SECRET'))
        return {
            'email': new_user.email,
            'username': new_user.username,
            'tokens': new_user.tokens(),
            'auth_provider': new_user.auth_provider,
            'id': new_user.id,
        }