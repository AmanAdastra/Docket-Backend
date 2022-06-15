from rest_framework import serializers
from questions.models import Question,QuestionReward


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ["id", "category","level", "description", "code", "answer"]

class QuestionRewardSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionReward
        fields = ["id", "user", "question", "reward"]