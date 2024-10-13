from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Review
from .serializers import ReviewSerializer

from rest_framework import generics
from .serializers import UserSerializer
from django.contrib.auth import get_user_model

from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all().order_by('-created_at')
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        # Set the user to the currently logged-in user
        serializer.save(user=self.request.user)

#views for registration

User = get_user_model()

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

#filtering and searching
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all().order_by('-created_at')
    serializer_class = ReviewSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['movie_title', 'rating']