from django_filters.filters import DateFromToRangeFilter
from django_filters.rest_framework import filterset
from rest_framework.views import APIView
from .models import Author,Book
from .serializers import AuthorSerializer,BookSerializer
from rest_framework import generics,status
from rest_framework.response import Response
import django_filters.rest_framework
from userapp.permissions import CanUC
class FAuthor(filterset.FilterSet):
    birthday=DateFromToRangeFilter()
    class Meta:
        model=Author
        fields={
                'first_name':["exact"],
                'last_name':["exact"],
                'birthday':["exact","range"],
            }
class AuthorList(generics.ListCreateAPIView):
    queryset=Author.objects.all()
    serializer_class=AuthorSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filter_class=FAuthor
class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Author.objects.all()
    serializer_class=AuthorSerializer
class FBook(filterset.FilterSet):
    class Meta:
        model=Book
        fields={
            "name":["exact","contains"],
            "author":["exact"],
            "genere":["exact"],
            "date_writed":["exact","range"]
            }
class BookList(generics.ListCreateAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer
    filter_backends=[django_filters.rest_framework.DjangoFilterBackend]
    filter_class=FBook
class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer
class BookUCS(APIView):
    permission_classes=[CanUC]
    def post(self,request):
        booksG=request.data.get("books")
        if not booksG:
            return Response({"error":"Please fill all fields"},status=status.HTTP_400_BAD_REQUEST)
        books=[]
        for u in booksG:
            try:
                book=Book(name=u['name'],genere=u['genere'], date_writed=u['date_writed'])
                book.author=Author.objects.get(pk=u['author'])
            except:
                return Response({"error":"Invalid Details"},status=status.HTTP_400_BAD_REQUEST)
            books+=[book]
        Book.objects.bulk_update_or_create(books,['genere','date_writed'],match_field="name")
        return Response({"success":"Successfully Inserts"},status=status.HTTP_200_OK)
