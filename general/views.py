from general.serializers import ProfileEditConstituentSerializer, CountryCustomisedForEmma
from rest_framework import status
from rest_framework.response import Response
from constituent_operations.models import Message
from constituent_operations.serializers import SendMessageSerializer
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from rest_framework.generics import ListAPIView
from users.models import Country
from rest_framework import  status



User = get_user_model()



class ListCountriesView(ListAPIView):
    permission_classes=()
    serializer_class=CountryCustomisedForEmma
    queryset=Country.objects.all()

    def list(self, request):
        countries = Country.objects.all()

        data = CountryCustomisedForEmma(countries, many=True)

        return Response({
            "status":status.HTTP_200_OK,
            "countries":data.data}, status=status.HTTP_200_OK
        )






class SendMessageMPView(APIView):
    permission_classes = ()
    def post(self, request):
        data = SendMessageSerializer(data= request.data)

        data.is_valid(raise_exception=True)

        sender = data['sender'].value
        receiver = data['receiver'].value
        message = data['message'].value
        attached_file = data['attached_file'].value
        try:
            sender = User.objects.get(system_id_for_user=sender)
            receiver = User.objects.get(id=receiver)

            message = Message.objects.create(
                sender=sender,
                receiver=receiver,
                message=message,
                attached_file=attached_file
            )
            response = {
                "message": "Message has been sent"
                }
        except Exception as e:
            print(e)
            response = {
                "message":"sorry, something went wrong, try again."
            } 

        return Response(response, status=status.HTTP_200_OK)     

class EditProfileView(APIView):
    permission_classes =()
    def post(self, request, id):
        user = User.objects.get(system_id_for_user=id)
        data =ProfileEditConstituentSerializer(data=request.data)

        data.is_valid(raise_exception=True)


        try:

            user.profile_picture = request.data['profile_picture']

            user.save()

            print(request.data['profile_picture'])

            data = {
                "status":status.HTTP_200_OK,
                "message":"Profile has been updated.",
                # "pic":user.profile_picture
            }
            return Response(data, status=status.HTTP_200_OK)

            
        except Exception as e:
            print(e)
            data = {
                "status":status.HTTP_400_BAD_REQUEST,
                "message":"Profile was not updated.",
                # "pic":user.profile_picture
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)



           

