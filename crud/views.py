from crud import serializer
from crud.models import DetailsModel
from crud.serializer import DetailsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class DetailsTable(APIView):
    def get(self, request):
        detailsObj = DetailsModel.objects.all()
        detailSerializeObj = DetailsSerializer(detailsObj, many=True)
        return Response(detailSerializeObj.data)
    def post(self, request):
        serializObj = DetailsSerializer(data=request.data)
        if serializObj.is_valid():
            serializObj.save()
            return Response("Successfully Submitted")
        return Response(serializObj.errors)       
class DetailsUpdate(APIView):
     def post(self, request, pk):
        try:
            detailObj = DetailsModel.objects.get(pk=pk)
        except:
            return Response("Not Found in Database")
        serializObj = DetailsSerializer(detailObj, data=request.data)
        if serializObj.is_valid():
            serializObj.save()
            return Response("Successfully Updated") 
        return Response(serializObj.errors)    
class DetailsDelete(APIView):
     def post(self, request, pk):
        try:
            detailObj = DetailsModel.objects.get(pk=pk)
        except:
            return Response("Not Found in Database")
        detailObj.delete() 
        return Response("Successfully Deleted")    
