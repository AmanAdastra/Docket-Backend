from django.db import models
from django_enumfield import enum
from django.contrib.auth.models import User

# Create your models here.

# Base Model for all models
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True



# Model for Category of Question
class Category(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name}"

# EnumType for QuestionLevelType
class QuestionLevelType(enum.Enum):
    EASY = 10
    MEDIUM = 20
    HARD = 30

# Model for Question
class Question(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    level = enum.EnumField(QuestionLevelType, default=QuestionLevelType.EASY)
    description = models.TextField()
    code = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return f"{self.description}"

# Model for QuestionReward
class QuestionReward(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    reward = models.IntegerField()

    def __str__(self):
        return f"{self.reward}"


