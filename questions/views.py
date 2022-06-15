from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from questions.serializers import QuestionSerializer, QuestionRewardSerializer
from questions.models import Question, QuestionReward
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.db.models import Sum

# Create your views here.

class QuestionViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionRewardListApi(generics.ListAPIView):
    serializer_class = QuestionRewardSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return QuestionReward.objects.filter(user=user)

class QuestionRewardCreateApi(generics.CreateAPIView):
    serializer_class = QuestionRewardSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = self.request.user
        question_id = request.data.get('question')  
        reward = request.data.get('reward')
        if not question_id:
            return Response({'error': 'question is required'})
        if not reward:
            return Response({'error': 'reward is required'})
        question = Question.objects.get(id=question_id)
        QuestionReward.objects.create(user=user, question=question, reward=reward)
        return Response({'status': 'ok'})

class UserRewardGetApi(generics.CreateAPIView):
    serializer_class = QuestionRewardSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = self.request.user
        return Response({'reward': user.questionreward_set.aggregate(Sum('reward'))['reward__sum']})

    

