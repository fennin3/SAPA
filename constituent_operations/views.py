import json

from django.core.files.base import ContentFile
from mp_operations.serializers import UserSerializer
from users.models import Constituency, Constituent
from mp_operations.serializers import CreateProjectSerializer
<<<<<<< HEAD
from constituent_operations.serializers import ApproveActionPlanSerializer , \
    CommentOnPostSerializer, GetUserInfoSerializer, ListProjectsOfMPs, ProblemForActionPlanSerializer, RNSendIncidentReportSerializer, RetrieveConstituentConstituenciesSerializer, RetrieveMessageSerializer, \
    SendMessageSerializer, RNSendRequestFormSerializer, ConductForAssessmentSerializer, AssessmentSerializer


=======
from constituent_operations.serializers import ApproveActionPlanSerializer, \
    CommentOnPostSerializer, GetUserInfoSerializer, ListProjectsOfMPs, ProblemForActionPlanSerializer, \
    RNSendIncidentReportSerializer, RetrieveConstituentConstituenciesSerializer, RetrieveMessageSerializer, \
    SendMessageSerializer, RNSendRequestFormSerializer, ConductForAssessmentSerializer, AssessmentSerializer

>>>>>>> 4158ec8a7c7e8d1e4390eea4417f5409c35a64c4
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth import get_user_model
from mp_operations.models import ActionPlanAreaSummaryForMp, Comment, Project
from datetime import datetime
import matplotlib.pyplot as plt
import os
<<<<<<< HEAD
from .models import RequestForm, ActionPlanToAssemblyMan, IncidentReport, Message, ProblemsForActionPlan, ApprovedActionPlan, ActionPlanParticipants, Assessment, AssessmentParticipant, ConductAssessment, ConductsForAssessment
from io import BytesIO
from django.db.models import  Sum
import requests





year  = datetime.today().year

=======
from .models import RequestForm, ActionPlanToAssemblyMan, IncidentReport, Message, ProblemsForActionPlan, \
    ApprovedActionPlan, ActionPlanParticipants, Assessment, AssessmentParticipant, ConductAssessment, \
    ConductsForAssessment
from io import BytesIO
from django.db.models import Sum
import requests

year = datetime.today().year
>>>>>>> 4158ec8a7c7e8d1e4390eea4417f5409c35a64c4

User = get_user_model()
# path_ = os.getcwd()

acp_values = {
<<<<<<< HEAD
    "_one":3,
    "_two":2,
    "_three":1
}




class SendMessageConstituentView(APIView):
    permission_classes = ()
    def post(self, request):
        data = SendMessageSerializer(data= request.data)
=======
    "_one": 3,
    "_two": 2,
    "_three": 1
}


class SendMessageConstituentView(APIView):
    permission_classes = ()

    def post(self, request):
        data = SendMessageSerializer(data=request.data)
>>>>>>> 4158ec8a7c7e8d1e4390eea4417f5409c35a64c4

        data.is_valid(raise_exception=True)

        sender = data['sender_id'].value
        message = data['message'].value
        attached_file = data['attached_file'].value

        mp = ""

        try:
            sender = User.objects.get(system_id_for_user=sender)
<<<<<<< HEAD
  
            #Getting MP
=======

            # Getting MP
>>>>>>> 4158ec8a7c7e8d1e4390eea4417f5409c35a64c4
            constituency = sender.constituency.all()
            for const in constituency:
                if const == sender.active_constituency:
                    for member in const.members.all():
<<<<<<< HEAD
                        if member.is_mp==True and member.is_active==True:
                            mp=member
=======
                        if member.is_mp == True and member.is_active == True:
                            mp = member
>>>>>>> 4158ec8a7c7e8d1e4390eea4417f5409c35a64c4
                            break
            receiver = mp
            print(f"MP----{mp}")
            print(f"MP----{receiver}")

            message = Message.objects.create(
                sender=sender,
                receiver=receiver,
                message=message,
                attached_file=attached_file
            )
            response = {
                "message": "Message has been sent"
<<<<<<< HEAD
                }
        except Exception as e:
            print(e)
            response = {
                "message":"sorry, something went wrong, try again."
            } 

        return Response(response, status=status.HTTP_200_OK)     


class RetrieveProjectsView(APIView):
    permission_classes= ()

    def get(self, request, id):
        
        
=======
            }
        except Exception as e:
            print(e)
            response = {
                "message": "sorry, something went wrong, try again."
            }

        return Response(response, status=status.HTTP_200_OK)


class RetrieveProjectsView(APIView):
    permission_classes = ()

    def get(self, request, id):

>>>>>>> 4158ec8a7c7e8d1e4390eea4417f5409c35a64c4
        try:
            user = User.objects.get(system_id_for_user=id)

            const = user.active_constituency
<<<<<<< HEAD
            
=======

>>>>>>> 4158ec8a7c7e8d1e4390eea4417f5409c35a64c4
            mp = ""
            projects = []

            try:
                for user in const.members.all():
                    if user.is_mp == True:
                        mp = user

                print(mp)
<<<<<<< HEAD
                
                

                
=======

>>>>>>> 4158ec8a7c7e8d1e4390eea4417f5409c35a64c4
                for project in mp.projects.all():
                    print("_______________")
                    print(project)
                    projects.append(project)
<<<<<<< HEAD
            

            except Exception as e:
                print(e)
            

            

            
            if len(projects)>0:
=======


            except Exception as e:
                print(e)

            if len(projects) > 0:
>>>>>>> 4158ec8a7c7e8d1e4390eea4417f5409c35a64c4
                projects = list(reversed(projects))
                data = ListProjectsOfMPs(data=projects, many=True)

                data.is_valid(raise_exception=False)

                return Response({
<<<<<<< HEAD
                
                    "status":status.HTTP_200_OK,
                    "data":data.data
                    }, status=status.HTTP_200_OK)
            else:
                data = []
            return Response({
                
                "status":status.HTTP_200_OK,
                "data":data
                }, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({
                "status":status.HTTP_500_INTERNAL_SERVER_ERROR,
                "message":"Sorry something went wrong"})


class RNSendIncidentReportView(APIView):
    permission_classes=()
=======

                    "status": status.HTTP_200_OK,
                    "data": data.data
                }, status=status.HTTP_200_OK)
            else:
                data = []
            return Response({

                "status": status.HTTP_200_OK,
                "data": data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({
                "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
                "message": "Sorry something went wrong"})


class RNSendIncidentReportView(APIView):
    permission_classes = ()

>>>>>>> 4158ec8a7c7e8d1e4390eea4417f5409c35a64c4
    def post(self, request):
        data = RNSendIncidentReportSerializer(data=request.data)
        data.is_valid(raise_exception=True)

        try:
            sender = User.objects.get(system_id_for_user=data['sender'].value)
            # receiver = User.objects.get(id=data['receiver'].value)
            const = sender.active_constituency
            receiver = None

            for user in const.members.all():
                if user.is_mp:
                    receiver = user
                    break

            incident = IncidentReport.objects.create(
                sender=sender,
<<<<<<< HEAD
                receiver = receiver,
                subject=data['subject'].value,
                message=data['message'].value,
                attached_file=data['attached_file'].value 
=======
                receiver=receiver,
                subject=data['subject'].value,
                message=data['message'].value,
                attached_file=data['attached_file'].value
>>>>>>> 4158ec8a7c7e8d1e4390eea4417f5409c35a64c4
            )

            incident.save()
            data = {
<<<<<<< HEAD
                "status":status.HTTP_200_OK,
                "message":"Incident report has been sent."
=======
                "status": status.HTTP_200_OK,
                "message": "Incident report has been sent."
>>>>>>> 4158ec8a7c7e8d1e4390eea4417f5409c35a64c4
            }
            return Response(data, status=status.HTTP_200_OK)

        except Exception as e:
            print(e)
            data = {
<<<<<<< HEAD
                "status":status.HTTP_400_BAD_REQUEST,
                "message":"Incident report was not sent."
=======
                "status": status.HTTP_400_BAD_REQUEST,
                "message": "Incident report was not sent."
>>>>>>> 4158ec8a7c7e8d1e4390eea4417f5409c35a64c4
            }

            return Response(data, status=status.HTTP_400_BAD_REQUEST)


class RNSendRequestFormView(APIView):
<<<<<<< HEAD
    permission_classes=()
=======
    permission_classes = ()

>>>>>>> 4158ec8a7c7e8d1e4390eea4417f5409c35a64c4
    def post(self, request):
        data = RNSendRequestFormSerializer(data=request.data)
        data.is_valid(raise_exception=True)

        try:
            sender = User.objects.get(system_id_for_user=data['sender'].value)
            # receiver = User.objects.get(id=data['receiver'].value)
            const = sender.active_constituency
            receiver = None

            for user in const.members.all():
                if user.is_mp:
                    receiver = user
                    break

            requestform = RequestForm.objects.create(
                sender=sender,
<<<<<<< HEAD
                receiver = receiver,
                subject=data['subject'].value,
                message=data['message'].value,
                attached_file=data['attached_file'].value 
=======
                receiver=receiver,
                subject=data['subject'].value,
                message=data['message'].value,
                attached_file=data['attached_file'].value
>>>>>>> 4158ec8a7c7e8d1e4390eea4417f5409c35a64c4
            )

            requestform.save()
            data = {
<<<<<<< HEAD
                "status":status.HTTP_200_OK,
                "message":"Request Form has been sent."
=======
                "status": status.HTTP_200_OK,
                "message": "Request Form has been sent."
>>>>>>> 4158ec8a7c7e8d1e4390eea4417f5409c35a64c4
            }
        except Exception as e:
            print(e)
            data = {
<<<<<<< HEAD
                "status":status.HTTP_400_BAD_REQUEST,
                "message":"Request Form was not sent."
=======
                "status": status.HTTP_400_BAD_REQUEST,
                "message": "Request Form was not sent."
>>>>>>> 4158ec8a7c7e8d1e4390eea4417f5409c35a64c4
            }

        return Response(data, status=status.HTTP_200_OK)

<<<<<<< HEAD
=======

>>>>>>> 4158ec8a7c7e8d1e4390eea4417f5409c35a64c4
class RetrieveAllConstituencyOfConst(APIView):
    permission_classes = ()

    def get(self, request, id):
        user = User.objects.get(system_id_for_user=id)
        constituencies = user.constituency.all()

        data = RetrieveConstituentConstituenciesSerializer(constituencies, many=True)
        data = {
<<<<<<< HEAD
            "constituencies":data.data
=======
            "constituencies": data.data
>>>>>>> 4158ec8a7c7e8d1e4390eea4417f5409c35a64c4
        }

        return Response(data, status=status.HTTP_200_OK)


class SetActiveConstituencyView(APIView):
    permission_classes = ()

    def post(self, request, user_id, const):
        try:
            constituency = Constituency.objects.get(id=const)
            user = User.objects.get(system_id_for_user=user_id)

            user.active_constituency = constituency
            user.save()

            consts = user.constituency.all()
            towns = Constituent.objects.get(user=user).town.all()
            areas = Constituent.objects.get(user=user).area.all()

            print(towns)
            print(areas)
<<<<<<< HEAD
            
=======
>>>>>>> 4158ec8a7c7e8d1e4390eea4417f5409c35a64c4

            print(consts)

            if len(list(consts)) > 1:

                try:
                    index = list(consts).index(constituency)
<<<<<<< HEAD
                    user.active_town=towns[index]
                    user.active_area=areas[index]
=======
                    user.active_town = towns[index]
                    user.active_area = areas[index]
>>>>>>> 4158ec8a7c7e8d1e4390eea4417f5409c35a64c4

                    user.save()

                    print("__________________ Done ______________------")
<<<<<<< HEAD
                    
                except Exception as e:
                    print(e)

            

            data = {
                "status":status.HTTP_200_OK,
                "message":f"{constituency.name} is active."
=======

                except Exception as e:
                    print(e)

            data = {
                "status": status.HTTP_200_OK,
                "message": f"{constituency.name} is active."
>>>>>>> 4158ec8a7c7e8d1e4390eea4417f5409c35a64c4
            }
            return Response(data, status=status.HTTP_200_OK)

        except Exception as e:
            print(e)
            data = {
<<<<<<< HEAD
                "status":status.HTTP_500_INTERNAL_SERVER_ERROR,
                "message":"Sorry something went wrong, try again."
=======
                "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
                "message": "Sorry something went wrong, try again."
>>>>>>> 4158ec8a7c7e8d1e4390eea4417f5409c35a64c4
            }
            return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class GetUserInfoView(APIView):
<<<<<<< HEAD
    permission_classes=()
=======
    permission_classes = ()

>>>>>>> 4158ec8a7c7e8d1e4390eea4417f5409c35a64c4
    def get(self, request, id):
        user = User.objects.get(system_id_for_user=id)

        data = GetUserInfoSerializer(user)

        print(data.data)

        return Response(data.data)

<<<<<<< HEAD
class CommentOnProjectAndPostView(APIView):
    permission_classes=()
=======

class CommentOnProjectAndPostView(APIView):
    permission_classes = ()

>>>>>>> 4158ec8a7c7e8d1e4390eea4417f5409c35a64c4
    def put(self, request):
        data = CommentOnPostSerializer(data=request.data)

        data.is_valid(raise_exception=True)

        print(data['user_id'].value)

        try:
            user = User.objects.get(system_id_for_user=data['user_id'].value)

<<<<<<< HEAD

=======
>>>>>>> 4158ec8a7c7e8d1e4390eea4417f5409c35a64c4
            comment = Comment.objects.create(
                text=data['comment_body'].value,
                comment_from=user
            )
            comment.save()

            post = Project.objects.get(id=data['project_id'].value)

            post.comments.add(comment)

            post.save()

            data = {
<<<<<<< HEAD
                "status":status.HTTP_200_OK,
                "message":"Comment has been sent."
                }


        
=======
                "status": status.HTTP_200_OK,
                "message": "Comment has been sent."
            }

>>>>>>> 4158ec8a7c7e8d1e4390eea4417f5409c35a64c4
            print(data)

            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            data = {
<<<<<<< HEAD
                "status":status.HTTP_500_INTERNAL_SERVER_ERROR,
                "message":"Comment could not be sent, try again."
                }

            return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class RetriveMessageView(APIView):
    permission_classes = ()
=======
                "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
                "message": "Comment could not be sent, try again."
            }

            return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class RetriveMessageView(APIView):
    permission_classes = ()

>>>>>>> 4158ec8a7c7e8d1e4390eea4417f5409c35a64c4
    def get(self, request, id):
        try:
            user = User.objects.get(system_id_for_user=id)

            const = user.active_constituency

            message = Message.objects.all().order_by("date_sent")

            mp = ""

            for i in const.members.all():
                if i.is_mp:
<<<<<<< HEAD
                    mp=i
=======
                    mp = i
>>>>>>> 4158ec8a7c7e8d1e4390eea4417f5409c35a64c4
                    break
            messages = []

            print(mp)

            for m in message:
                if m.sender == user or m.sender == mp:
                    messages.append(m)

<<<<<<< HEAD


            
=======
>>>>>>> 4158ec8a7c7e8d1e4390eea4417f5409c35a64c4
            data = RetrieveMessageSerializer(messages, many=True)
            # data.is_valid(raise_exception=True)

            data = {
<<<<<<< HEAD
                "status":status.HTTP_200_OK,
                "messages":data.data
=======
                "status": status.HTTP_200_OK,
                "messages": data.data
>>>>>>> 4158ec8a7c7e8d1e4390eea4417f5409c35a64c4
            }

            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)

            return Response()


<<<<<<< HEAD

=======
>>>>>>> 4158ec8a7c7e8d1e4390eea4417f5409c35a64c4
class ProfileEditConstituentView(APIView):
    permission_classes = ()

    def put():
        pass

<<<<<<< HEAD
class LikeProjectView(APIView):
    permission_classes=()
=======

class LikeProjectView(APIView):
    permission_classes = ()
>>>>>>> 4158ec8a7c7e8d1e4390eea4417f5409c35a64c4

    def put(self, request, id, post_id):
        try:
            user = User.objects.get(system_id_for_user=id)
            post = Project.objects.get(id=post_id)

            if user in post.likes.all():
                post.likes.remove(user)
                post.save()
                data = {
<<<<<<< HEAD
                "status":status.HTTP_200_OK,
                "message":"project has been disliked"
=======
                    "status": status.HTTP_200_OK,
                    "message": "project has been disliked"
>>>>>>> 4158ec8a7c7e8d1e4390eea4417f5409c35a64c4
                }
            else:
                post.likes.add(user)
                post.save()
<<<<<<< HEAD
            
                data = {
                    "status":status.HTTP_200_OK,
                    "message":"project has been liked"
=======

                data = {
                    "status": status.HTTP_200_OK,
                    "message": "project has been liked"
>>>>>>> 4158ec8a7c7e8d1e4390eea4417f5409c35a64c4
                }

            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)

            data = {
<<<<<<< HEAD
                "status":status.HTTP_400_BAD_REQUEST,
                "message":"project has been liked"
=======
                "status": status.HTTP_400_BAD_REQUEST,
                "message": "project has been liked"
>>>>>>> 4158ec8a7c7e8d1e4390eea4417f5409c35a64c4
            }

            return Response(data, status=status.HTTP_400_BAD_REQUEST)

<<<<<<< HEAD
class ActionPlanView(APIView):
    permission_classes=()
=======

class ActionPlanView(APIView):
    permission_classes = ()

>>>>>>> 4158ec8a7c7e8d1e4390eea4417f5409c35a64c4
    def post(self, request, id):

        user = User.objects.get(system_id_for_user=id)
        area = user.active_area
        constituency = user.active_constituency

        ap = ProblemsForActionPlan.objects.all()

<<<<<<< HEAD
       


        # for i in ap:
        #     problem_titles.append(i.title)

        


=======
        # for i in ap:
        #     problem_titles.append(i.title)

>>>>>>> 4158ec8a7c7e8d1e4390eea4417f5409c35a64c4
        a = []
        # keys_ = request.data.keys()

        # print(keys_)
<<<<<<< HEAD
        
        try:
            ac_p = ActionPlanParticipants.objects.get(year=year,user=user)


            # if ac_p is not None:
                
            data = {
                "status":status.HTTP_400_BAD_REQUEST,
                "message":"You have already sent your feedback."
            }
        
        except Exception as e:

            keys_ = request.data.keys()
            
            for key_ in keys_:
                print(key_)
                print(str(request.data[key_]))
                act_plan = ActionPlanToAssemblyMan.objects.create(area=area,problem_title=str(request.data[key_]), constituency=constituency)
=======

        try:
            ac_p = ActionPlanParticipants.objects.get(year=year, user=user)

            # if ac_p is not None:

            data = {
                "status": status.HTTP_400_BAD_REQUEST,
                "message": "You have already sent your feedback."
            }

        except Exception as e:

            keys_ = request.data.keys()

            for key_ in keys_:
                print(key_)
                print(str(request.data[key_]))
                act_plan = ActionPlanToAssemblyMan.objects.create(area=area, problem_title=str(request.data[key_]),
                                                                  constituency=constituency)
>>>>>>> 4158ec8a7c7e8d1e4390eea4417f5409c35a64c4
                act_plan.total_participants = int(act_plan.total_participants) + 1
                act_plan.total_rating = act_plan.total_rating + int(acp_values[key_])
                act_plan.save()
                act_plan.participants.add(user)

                a.append(1)

<<<<<<< HEAD
            

            data = {
                "status":status.HTTP_200_OK,
                "message":"Thank you for your feedback."
            }
        if len(a) > 0:
            ac_p = ActionPlanParticipants.objects.create(year=year,user=user)
            ac_p.save()
        return Response(data, status.HTTP_200_OK)

class RetrieveActionPlanStatForAssemblyMan(APIView):
    permission_classes=()
=======
            data = {
                "status": status.HTTP_200_OK,
                "message": "Thank you for your feedback."
            }
        if len(a) > 0:
            ac_p = ActionPlanParticipants.objects.create(year=year, user=user)
            ac_p.save()
        return Response(data, status.HTTP_200_OK)


class RetrieveActionPlanStatForAssemblyMan(APIView):
    permission_classes = ()
>>>>>>> 4158ec8a7c7e8d1e4390eea4417f5409c35a64c4

    def get(self, request, id, date):
        user = User.objects.get(system_id_for_user=id)

        # problems = ProblemsForActionPlan.objects.all()

        # for prob in problems:

        # action_plans = ActionPlanToAssemblyMan.objects.filter(date__year=date, area=user.active_area, constituency=user.active_constituency).annotate(totals=Sum('price'))
        ac = ActionPlanToAssemblyMan.objects.values('problem_title').annotate(total=Sum('total_rating'))

<<<<<<< HEAD
        prob_titles=[]
        stats =[]
=======
        prob_titles = []
        stats = []
>>>>>>> 4158ec8a7c7e8d1e4390eea4417f5409c35a64c4

        for ac in ac:
            prob_titles.append(ac['problem_title'])
            stats.append(ac['total'])
<<<<<<< HEAD
        
        data = {
            "status":status.HTTP_200_OK,
            "problem_titles": prob_titles,
            "stats":stats
=======

        data = {
            "status": status.HTTP_200_OK,
            "problem_titles": prob_titles,
            "stats": stats
>>>>>>> 4158ec8a7c7e8d1e4390eea4417f5409c35a64c4
        }

        return Response(data, status.HTTP_200_OK)

<<<<<<< HEAD
class ApproveActionPlanView(APIView):
    permission_classes = ()
    def post(self, request, id):
        user = User.objects.get(system_id_for_user=id)
        data = ApproveActionPlanSerializer(data = request.data)
=======

class ApproveActionPlanView(APIView):
    permission_classes = ()

    def post(self, request, id):
        user = User.objects.get(system_id_for_user=id)
        data = ApproveActionPlanSerializer(data=request.data)
>>>>>>> 4158ec8a7c7e8d1e4390eea4417f5409c35a64c4
        data.is_valid(raise_exception=True)

        x = data['problem_titles'].value
        y = data['stats'].value

        # def addlabels(x,y):
        #     for i in range(len(x)):
        #     plt.text(i,y[i],y[i])

<<<<<<< HEAD
        def addlabels(x,y):
            for i in range(len(x)):
                plt.text(i,y[i], y[i])


=======
        def addlabels(x, y):
            for i in range(len(x)):
                plt.text(i, y[i], y[i])
>>>>>>> 4158ec8a7c7e8d1e4390eea4417f5409c35a64c4

        try:

            app_ = ApprovedActionPlan.objects.create(year=year, user=user)

            app_.save()
            figure = BytesIO()
<<<<<<< HEAD
            
            plt.bar(x, y)
            addlabels(x,y)
            plt.savefig(figure)
            

            content_file = ContentFile(figure.getvalue())


            ap = ActionPlanAreaSummaryForMp.objects.create(
                constituency = user.active_constituency,
                area = user.active_area,
                comment = data['comment'].value
=======

            plt.bar(x, y)
            addlabels(x, y)
            plt.savefig(figure)

            content_file = ContentFile(figure.getvalue())

            ap = ActionPlanAreaSummaryForMp.objects.create(
                constituency=user.active_constituency,
                area=user.active_area,
                comment=data['comment'].value
>>>>>>> 4158ec8a7c7e8d1e4390eea4417f5409c35a64c4
            )

            ap.image.save("stats_image.jpg", content_file)

            ap.save()

            data = {
<<<<<<< HEAD
                "status":status.HTTP_200_OK,
                "message":f"Action plan summary of {user.active_area.name} has been approved."
=======
                "status": status.HTTP_200_OK,
                "message": f"Action plan summary of {user.active_area.name} has been approved."
>>>>>>> 4158ec8a7c7e8d1e4390eea4417f5409c35a64c4
            }

            return Response(data, status.HTTP_200_OK)
        except Exception as e:
            print(e)
            data = {
<<<<<<< HEAD
                "status":status.HTTP_400_BAD_REQUEST,
                "message":f"Action plan summary of {user.active_area.name} was not approved, try again."
=======
                "status": status.HTTP_400_BAD_REQUEST,
                "message": f"Action plan summary of {user.active_area.name} was not approved, try again."
>>>>>>> 4158ec8a7c7e8d1e4390eea4417f5409c35a64c4
            }

            return Response(data, status.HTTP_400_BAD_REQUEST)


class RetrieveProblemTitlesView(APIView):
    permission_classes = ()

    def get(self, request):
<<<<<<< HEAD

=======
>>>>>>> 4158ec8a7c7e8d1e4390eea4417f5409c35a64c4
        data = ProblemsForActionPlan.objects.all()

        data = ProblemForActionPlanSerializer(data, many=True)

        data = {
<<<<<<< HEAD
            "status":status.HTTP_200_OK,
            "data":data.data
=======
            "status": status.HTTP_200_OK,
            "data": data.data
>>>>>>> 4158ec8a7c7e8d1e4390eea4417f5409c35a64c4
        }

        return Response(data, status=status.HTTP_200_OK)


class RetrieveYearsView(APIView):
<<<<<<< HEAD
    permission_classes=()
=======
    permission_classes = ()
>>>>>>> 4158ec8a7c7e8d1e4390eea4417f5409c35a64c4

    def get(self, request):
        ap = ActionPlanToAssemblyMan.objects.all()

        years = []
        for i in ap:
            years.append(i.date.year)

<<<<<<< HEAD

=======
>>>>>>> 4158ec8a7c7e8d1e4390eea4417f5409c35a64c4
        years = list(set(years))

        print(years)

        return Response({
<<<<<<< HEAD
            "status":status.HTTP_200_OK,
            "years":years
=======
            "status": status.HTTP_200_OK,
            "years": years
>>>>>>> 4158ec8a7c7e8d1e4390eea4417f5409c35a64c4
        })


class GetActionPlanApprovedStatusView(APIView):
<<<<<<< HEAD
    permission_classes=()
=======
    permission_classes = ()
>>>>>>> 4158ec8a7c7e8d1e4390eea4417f5409c35a64c4

    def post(self, request, id, year):
        user = User.objects.get(system_id_for_user=id)
        try:
            approved = ApprovedActionPlan.objects.get(system_id_for_user=id, year=year)
            return Response(
                {
<<<<<<< HEAD
                    "status":status.HTTP_400_BAD_REQUEST,
                    "message":"Action Plan has already been Approved."
=======
                    "status": status.HTTP_400_BAD_REQUEST,
                    "message": "Action Plan has already been Approved."
>>>>>>> 4158ec8a7c7e8d1e4390eea4417f5409c35a64c4
                }
            )

        except Exception:
            approved = ApprovedActionPlan.objects.create(
<<<<<<< HEAD
                user = user,
                year = year
=======
                user=user,
                year=year
>>>>>>> 4158ec8a7c7e8d1e4390eea4417f5409c35a64c4
            )

            approved.save()

            return Response(
                {
<<<<<<< HEAD
                    "status":status.HTTP_200_OK,
                    "message":"Action Plan has been Approved."
=======
                    "status": status.HTTP_200_OK,
                    "message": "Action Plan has been Approved."
>>>>>>> 4158ec8a7c7e8d1e4390eea4417f5409c35a64c4
                }
            )

    def get(self, request, id, year):
        user = User.objects.get(system_id_for_user=id)

        try:
            approved = ApprovedActionPlan.objects.get(user=user, year=year)
            return Response(
                {
<<<<<<< HEAD
                    "status":status.HTTP_200_OK,
                    "status":True
=======
                    "status": status.HTTP_200_OK,
                    "status": True
>>>>>>> 4158ec8a7c7e8d1e4390eea4417f5409c35a64c4
                }
            )

        except Exception:
<<<<<<< HEAD
        

            return Response(
                {
                    "status":status.HTTP_200_OK,
                    "status":False
                }
            )

class CreateProjectForMP(APIView):
    permission_classes=()
=======

            return Response(
                {
                    "status": status.HTTP_200_OK,
                    "status": False
                }
            )


class CreateProjectForMP(APIView):
    permission_classes = ()
>>>>>>> 4158ec8a7c7e8d1e4390eea4417f5409c35a64c4

    def post(self, request):
        user_id = request.data['user_id']

        user = User.objects.get(system_id_for_user=user_id)

        user_info = user.more_info

        mp = user_info.subadmin_for

        project = Project.objects.create(
            mp=mp,
<<<<<<< HEAD
            place= request.data['place'],
=======
            place=request.data['place'],
>>>>>>> 4158ec8a7c7e8d1e4390eea4417f5409c35a64c4
            description=request.data['description'],
            name=request.data['name'],
            media=request.data['media'],
        )
        project.save()

        data = {
<<<<<<< HEAD
            "status":status.HTTP_200_OK,
            "message":"Project has been created."
=======
            "status": status.HTTP_200_OK,
            "message": "Project has been created."
>>>>>>> 4158ec8a7c7e8d1e4390eea4417f5409c35a64c4
        }

        return Response(data, status=status.HTTP_200_OK)


class ReplyNotification(APIView):
    permission_classes = ()

<<<<<<< HEAD
    def post(self, request,id):
=======
    def post(self, request, id):
>>>>>>> 4158ec8a7c7e8d1e4390eea4417f5409c35a64c4
        user = User.objects.get(system_id_for_user=id)

        mp = user.more_info.subadmin_for
        receiver = User.objects.get(system_id_for_user=request.data['receiver'])

<<<<<<< HEAD

=======
>>>>>>> 4158ec8a7c7e8d1e4390eea4417f5409c35a64c4
        message = Message.objects.create(
            sender=mp,
            receiver=receiver,
            attached_file=request.data['attached_file'],
            message=request.data['message']
        )

<<<<<<< HEAD

=======
>>>>>>> 4158ec8a7c7e8d1e4390eea4417f5409c35a64c4
        message.save()

        return Response(
            {
<<<<<<< HEAD
                "status":status.HTTP_200_OK,
                "message":"message has been sent."
=======
                "status": status.HTTP_200_OK,
                "message": "message has been sent."
>>>>>>> 4158ec8a7c7e8d1e4390eea4417f5409c35a64c4
            }
        )


# Untested Endpoints
# New features

class RetrieveProjectsForAssessmentView(APIView):
<<<<<<< HEAD
    permission_classes=()
    def get(self, request,id, year):
        user =  User.objects.get(system_id_for_user=id)
=======
    permission_classes = ()

    def get(self, request, id, year):
        user = User.objects.get(system_id_for_user=id)
>>>>>>> 4158ec8a7c7e8d1e4390eea4417f5409c35a64c4
        const = user.active_constituency
        area = user.active_area
        mp = user

        for mem in const.members.all():
            if mem.is_mp == True:
                mp = mem

<<<<<<< HEAD


=======
>>>>>>> 4158ec8a7c7e8d1e4390eea4417f5409c35a64c4
        projects = Project.objects.filter(mp=mp, date_posted__year=year, is_post=False)
        cond = ConductsForAssessment.objects.all()

        projects = ListProjectsOfMPs(projects, many=True)
<<<<<<< HEAD
        cond = ConductForAssessmentSerializer(cond,many=True)


        return Response(
            {
            "status":status.HTTP_200_OK,
            "projects":projects.data,
            "conducts":cond.data
            })



# class RetrieveConductForAssessment(APIView):



class RetrieveConductsForAssessmentView(APIView):
    permission_classes=()

    def get(self, request):

=======
        cond = ConductForAssessmentSerializer(cond, many=True)

        return Response(
            {
                "status": status.HTTP_200_OK,
                "projects": projects.data,
                "conducts": cond.data
            })


# class RetrieveConductForAssessment(APIView):


class RetrieveConductsForAssessmentView(APIView):
    permission_classes = ()

    def get(self, request):
>>>>>>> 4158ec8a7c7e8d1e4390eea4417f5409c35a64c4
        cond = ConductsForAssessment.objects.all()

        data = ConductForAssessmentSerializer(cond, many=True)

        return Response(
            {
<<<<<<< HEAD
                "data":data.data
=======
                "data": data.data
>>>>>>> 4158ec8a7c7e8d1e4390eea4417f5409c35a64c4
            }
        )


class SendAssessmentView(APIView):
<<<<<<< HEAD
    permission_classes=()
=======
    permission_classes = ()
>>>>>>> 4158ec8a7c7e8d1e4390eea4417f5409c35a64c4

    def post(self, request, id):
        user = User.objects.get(system_id_for_user=id)
        const = user.active_constituency

        data_ = AssessmentSerializer(request.data)

<<<<<<< HEAD
        

=======
        print('------------------------------')
        print(data_)
        print('------------------------------')
>>>>>>> 4158ec8a7c7e8d1e4390eea4417f5409c35a64c4

        try:
            ass_part = AssessmentParticipant.objects.get(user=user)

            data = {
<<<<<<< HEAD
            "status":status.HTTP_400_BAD_REQUEST,
            "message":"Sorry, you have already sent your feedback."
=======
                "status": status.HTTP_400_BAD_REQUEST,
                "message": "Sorry, you have already sent your feedback."
>>>>>>> 4158ec8a7c7e8d1e4390eea4417f5409c35a64c4
            }

            return Response(data, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            print(e)

            # Creating Projects assessment objects

<<<<<<< HEAD
            print("------------4444444%%%%%%%%%%%%_______________________--")

            
=======
>>>>>>> 4158ec8a7c7e8d1e4390eea4417f5409c35a64c4
            for project in data_['projects_assessment'].value.keys():
                project_ = Project.objects.get(id=int(project))

                assessment = Assessment.objects.create(
                    user=user,
                    project=project_,
                    constituency=const,
                    assessment=data_["projects_assessment"].value[project]
                )

                assessment.save()

            ass_p = AssessmentParticipant.objects.create(
                user=user,
                year=year,
            )

            ass_p.save()

<<<<<<< HEAD
            

            
            for i in data_['conduct_assessment'].value.keys():
                cond = ConductAssessment.objects.create(
                    conduct=i,
                    user =user,
=======
            for i in data_['conduct_assessment'].value.keys():
                cond = ConductAssessment.objects.create(
                    conduct=i,
                    user=user,
>>>>>>> 4158ec8a7c7e8d1e4390eea4417f5409c35a64c4
                    constituency=const,
                    assessment=data_['conduct_assessment'].value[i]
                )

                cond.save()

<<<<<<< HEAD


            
            
            data = {
                "status":status.HTTP_200_OK,
                "message":"Thank you for your Feedback."
=======
            data = {
                "status": status.HTTP_200_OK,
                "message": "Thank you for your Feedback."
>>>>>>> 4158ec8a7c7e8d1e4390eea4417f5409c35a64c4
            }

            return Response(data, status=status.HTTP_200_OK)






<<<<<<< HEAD

=======
>>>>>>> 4158ec8a7c7e8d1e4390eea4417f5409c35a64c4
