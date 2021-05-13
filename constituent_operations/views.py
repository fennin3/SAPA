import json

from django.core.files.base import ContentFile
from mp_operations.serializers import UserSerializer
from users.models import Constituency, Constituent
from mp_operations.serializers import CreateProjectSerializer
from constituent_operations.serializers import ApproveActionPlanSerializer ,  CommentOnPostSerializer, GetUserInfoSerializer, ListProjectsOfMPs, ProblemForActionPlanSerializer, RNSendIncidentReportSerializer, RetrieveConstituentConstituenciesSerializer, RetrieveMessageSerializer, SendMessageSerializer, RNSendRequestFormSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth import get_user_model
from mp_operations.models import ActionPlanAreaSummaryForMp, Comment, Project
from datetime import datetime
import matplotlib.pyplot as plt
import os
from .models import RequestForm, ActionPlanToAssemblyMan, IncidentReport, Message, ProblemsForActionPlan, ApprovedActionPlan, ActionPlanParticipants
from io import BytesIO
from django.db.models import  Sum
import requests





year  = datetime.today().year


User = get_user_model()
# path_ = os.getcwd()

acp_values = {
    "_one":3,
    "_two":2,
    "_three":1
}




class SendMessageConstituentView(APIView):
    permission_classes = ()
    def post(self, request):
        data = SendMessageSerializer(data= request.data)

        data.is_valid(raise_exception=True)

        sender = data['sender_id'].value
        message = data['message'].value
        attached_file = data['attached_file'].value

        mp = ""

        try:
            sender = User.objects.get(system_id_for_user=sender)
  
            #Getting MP
            constituency = sender.constituency.all()
            for const in constituency:
                if const == sender.active_constituency:
                    for member in const.members.all():
                        if member.is_mp==True and member.is_active==True:
                            mp=member
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
        
        
        try:
            user = User.objects.get(system_id_for_user=id)

            const = user.active_constituency
            
            mp = ""
            projects = []

            try:
                for user in const.members.all():
                    if user.is_mp == True:
                        mp = user

                print(mp)
                
                

                
                for project in mp.projects.all():
                    print("_______________")
                    print(project)
                    projects.append(project)
            

            except Exception as e:
                print(e)
            

            

            
            if len(projects)>0:
                projects = list(reversed(projects))
                data = ListProjectsOfMPs(data=projects, many=True)

                data.is_valid(raise_exception=False)

                return Response({
                
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
                receiver = receiver,
                subject=data['subject'].value,
                message=data['message'].value,
                attached_file=data['attached_file'].value 
            )

            incident.save()
            data = {
                "status":status.HTTP_200_OK,
                "message":"Incident report has been sent."
            }
            return Response(data, status=status.HTTP_200_OK)

        except Exception as e:
            print(e)
            data = {
                "status":status.HTTP_400_BAD_REQUEST,
                "message":"Incident report was not sent."
            }

            return Response(data, status=status.HTTP_400_BAD_REQUEST)


class RNSendRequestFormView(APIView):
    permission_classes=()
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
                receiver = receiver,
                subject=data['subject'].value,
                message=data['message'].value,
                attached_file=data['attached_file'].value 
            )

            requestform.save()
            data = {
                "status":status.HTTP_200_OK,
                "message":"Request Form has been sent."
            }
        except Exception as e:
            print(e)
            data = {
                "status":status.HTTP_400_BAD_REQUEST,
                "message":"Request Form was not sent."
            }

        return Response(data, status=status.HTTP_200_OK)

class RetrieveAllConstituencyOfConst(APIView):
    permission_classes = ()

    def get(self, request, id):
        user = User.objects.get(system_id_for_user=id)
        constituencies = user.constituency.all()

        data = RetrieveConstituentConstituenciesSerializer(constituencies, many=True)
        data = {
            "constituencies":data.data
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
            

            print(consts)

            if len(list(consts)) > 1:

                try:
                    index = list(consts).index(constituency)
                    user.active_town=towns[index]
                    user.active_area=areas[index]

                    user.save()

                    print("__________________ Done ______________------")
                    
                except Exception as e:
                    print(e)

            

            data = {
                "status":status.HTTP_200_OK,
                "message":f"{constituency.name} is active."
            }
            return Response(data, status=status.HTTP_200_OK)

        except Exception as e:
            print(e)
            data = {
                "status":status.HTTP_500_INTERNAL_SERVER_ERROR,
                "message":"Sorry something went wrong, try again."
            }
            return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class GetUserInfoView(APIView):
    permission_classes=()
    def get(self, request, id):
        user = User.objects.get(system_id_for_user=id)

        data = GetUserInfoSerializer(user)

        print(data.data)

        return Response(data.data)

class CommentOnProjectAndPostView(APIView):
    permission_classes=()
    def put(self, request):
        data = CommentOnPostSerializer(data=request.data)

        data.is_valid(raise_exception=True)

        print(data['user_id'].value)

        try:
            user = User.objects.get(system_id_for_user=data['user_id'].value)


            comment = Comment.objects.create(
                text=data['comment_body'].value,
                comment_from=user
            )
            comment.save()

            post = Project.objects.get(id=data['project_id'].value)

            post.comments.add(comment)

            post.save()

            data = {
                "status":status.HTTP_200_OK,
                "message":"Comment has been sent."
                }


        
            print(data)

            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            data = {
                "status":status.HTTP_500_INTERNAL_SERVER_ERROR,
                "message":"Comment could not be sent, try again."
                }

            return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class RetriveMessageView(APIView):
    permission_classes = ()
    def get(self, request, id):
        try:
            user = User.objects.get(system_id_for_user=id)

            const = user.active_constituency

            message = Message.objects.all().order_by("date_sent")

            mp = ""

            for i in const.members.all():
                if i.is_mp:
                    mp=i
                    break
            messages = []

            print(mp)

            for m in message:
                if m.sender == user or m.sender == mp:
                    messages.append(m)



            
            data = RetrieveMessageSerializer(messages, many=True)
            # data.is_valid(raise_exception=True)

            data = {
                "status":status.HTTP_200_OK,
                "messages":data.data
            }

            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)

            return Response()



class ProfileEditConstituentView(APIView):
    permission_classes = ()

    def put():
        pass

class LikeProjectView(APIView):
    permission_classes=()

    def put(self, request, id, post_id):
        try:
            user = User.objects.get(system_id_for_user=id)
            post = Project.objects.get(id=post_id)

            if user in post.likes.all():
                post.likes.remove(user)
                post.save()
                data = {
                "status":status.HTTP_200_OK,
                "message":"project has been disliked"
                }
            else:
                post.likes.add(user)
                post.save()
            
                data = {
                    "status":status.HTTP_200_OK,
                    "message":"project has been liked"
                }

            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)

            data = {
                "status":status.HTTP_400_BAD_REQUEST,
                "message":"project has been liked"
            }

            return Response(data, status=status.HTTP_400_BAD_REQUEST)

class ActionPlanView(APIView):
    permission_classes=()
    def post(self, request, id):

        print(request.data)
        user = User.objects.get(system_id_for_user=id)
        area = user.active_area
        constituency = user.active_constituency

        ap = ProblemsForActionPlan.objects.all()

        problem_titles = []

        # for a in request.data.keys():
        #     print(a)


        for title_ in request.data.keys():
            problem_titles.append(title_)


        # for i in ap:
        #     problem_titles.append(i.title)

        


        a = []
        for prob in problem_titles:
            try:
                ac_p = ActionPlanParticipants.objects.get(year=year,user=user)


                # if ac_p is not None:
                    
                data = {
                    "status":status.HTTP_400_BAD_REQUEST,
                    "message":"You have already sent your feedback."
                }
                # else:
                #     act_plan.participants.add(user)
                #     act_plan.total_participants = int(act_plan.total_participants) + 1
                #     act_plan.total_rating = act_plan.total_rating + int(request.data[prob][0])
                #     act_plan.save()
                #     data = {
                #         "status":status.HTTP_200_OK,
                #         "message":"Thank you for your feedback."
                #     }
            except Exception as e:

                keys_ = request.data.keys()
                
                for key_ in keys_:
                    
                    act_plan = ActionPlanToAssemblyMan.objects.create(area=area,problem_title=str(request.data[key_]), constituency=constituency)
                    act_plan.total_participants = int(act_plan.total_participants) + 1
                    act_plan.total_rating = act_plan.total_rating + int(acp_values[key_])
                    act_plan.save()
                    act_plan.participants.add(user)

                    a.append(1)

                

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

    def get(self, request, id, date):
        user = User.objects.get(system_id_for_user=id)

        # problems = ProblemsForActionPlan.objects.all()

        # for prob in problems:

        # action_plans = ActionPlanToAssemblyMan.objects.filter(date__year=date, area=user.active_area, constituency=user.active_constituency).annotate(totals=Sum('price'))
        ac = ActionPlanToAssemblyMan.objects.values('problem_title').annotate(total=Sum('total_rating'))

        prob_titles=[]
        stats =[]

        for ac in ac:
            prob_titles.append(ac['problem_title'])
            stats.append(ac['total'])
        
        data = {
            "status":status.HTTP_200_OK,
            "problem_titles": prob_titles,
            "stats":stats
        }

        return Response(data, status.HTTP_200_OK)

class ApproveActionPlanView(APIView):
    permission_classes = ()
    def post(self, request, id):
        user = User.objects.get(system_id_for_user=id)
        data = ApproveActionPlanSerializer(data = request.data)
        data.is_valid(raise_exception=True)

        x = data['problem_titles'].value
        y = data['stats'].value

        # def addlabels(x,y):
        #     for i in range(len(x)):
        #     plt.text(i,y[i],y[i])

        def addlabels(x,y):
            for i in range(len(x)):
                plt.text(i,y[i], y[i])


        try:
            figure = BytesIO()
            
            plt.bar(x, y)
            addlabels(x,y)
            plt.savefig(figure)
            

            content_file = ContentFile(figure.getvalue())


            ap = ActionPlanAreaSummaryForMp.objects.create(
                constituency = user.active_constituency,
                area = user.active_area,
                comment = data['comment'].value
            )

            ap.image.save("stats_image.jpg", content_file)

            ap.save()

            data = {
                "status":status.HTTP_200_OK,
                "message":f"Action plan summary of {user.active_area.name} has been approved."
            }

            return Response(data, status.HTTP_200_OK)
        except Exception as e:
            print(e)
            data = {
                "status":status.HTTP_400_BAD_REQUEST,
                "message":f"Action plan summary of {user.active_area.name} was not approved, try again."
            }

            return Response(data, status.HTTP_400_BAD_REQUEST)


class RetrieveProblemTitlesView(APIView):
    permission_classes = ()

    def get(self, request):

        data = ProblemsForActionPlan.objects.all()

        data = ProblemForActionPlanSerializer(data, many=True)

        data = {
            "status":status.HTTP_200_OK,
            "data":data.data
        }

        return Response(data, status=status.HTTP_200_OK)


class RetrieveYearsView(APIView):
    permission_classes=()

    def get(self, request):
        ap = ActionPlanToAssemblyMan.objects.all()

        years = []
        for i in ap:
            years.append(i.date.year)


        years = list(set(years))

        print(years)

        return Response({
            "status":status.HTTP_200_OK,
            "years":years
        })


class GetActionPlanApprovedStatusView(APIView):
    permission_classes=()

    def post(self, request, id, year):
        user = User.objects.get(system_id_for_user=id)
        try:
            approved = ApprovedActionPlan.objects.get(system_id_for_user=id, year=year)
            return Response(
                {
                    "status":status.HTTP_400_BAD_REQUEST,
                    "message":"Action Plan has already been Approved."
                }
            )

        except Exception:
            approved = ApprovedActionPlan.objects.create(
                user = user,
                year = year
            )

            approved.save()

            return Response(
                {
                    "status":status.HTTP_200_OK,
                    "message":"Action Plan has been Approved."
                }
            )

    def get(self, request, id, year):
        user = User.objects.get(system_id_for_user=id)

        try:
            approved = ApprovedActionPlan.objects.get(user=user, year=year)
            return Response(
                {
                    "status":status.HTTP_200_OK,
                    "status":True
                }
            )

        except Exception:
        

            return Response(
                {
                    "status":status.HTTP_200_OK,
                    "status":False
                }
            )

class CreateProjectForMP(APIView):
    permission_classes=()

    def post(self, request):
        user_id = request.data['user_id']

        user = User.objects.get(system_id_for_user=user_id)

        user_info = user.more_info

        mp = user_info.subadmin_for

        project = Project.objects.create(
            mp=mp,
            place= request.data['place'],
            description=request.data['description'],
            name=request.data['name'],
            media=request.data['media'],
        )
        project.save()

        data = {
            "status":status.HTTP_200_OK,
            "message":"Project has been created."
        }

        return Response(data, status=status.HTTP_200_OK)


class ReplyNotification(APIView):
    permission_classes = ()

    def post(self, request,id):
        user = User.objects.get(system_id_for_user=id)

        mp = user.more_info.subadmin_for
        receiver = User.objects.get(system_id_for_user=request.data['receiver'])


        message = Message.objects.create(
            sender=mp,
            receiver=receiver,
            attached_file=request.data['attached_file'],
            message=request.data['message']
        )


        message.save()

        return Response(
            {
                "status":status.HTTP_200_OK,
                "message":"message has been sent."
            }
        )










