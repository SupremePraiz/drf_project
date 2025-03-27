from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from watchlist.models import StreamPlatform, Movie, Review
from .serializers import StreamPlatformSerializer, MovieListSerializer, ReviewSerializer


class StreamPlatformView(generics.ListCreateAPIView):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer
    permission_classes = [IsAuthenticated]


class StreamPlatformDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer


class MovieListView(generics.ListCreateAPIView):
    # queryset = WatchList.objects.all()
    serializer_class = MovieListSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Movie.objects.filter(platform=pk)


class MovieDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieListSerializer


class ReviewListView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer




