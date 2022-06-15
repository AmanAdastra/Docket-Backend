from django.contrib import admin
from questions.models import Category, Question, QuestionReward
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'description')
    list_filter = ('name', 'description')
    search_fields = ('name', 'description')

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id','category','description', 'code', 'answer')
    list_filter = ('description', 'code', 'answer')
    search_fields = ('description', 'code', 'answer')

@admin.register(QuestionReward)
class QuestionRewardAdmin(admin.ModelAdmin):
    list_display = ('id','question', 'reward')
    list_filter = ('question', 'reward')
    search_fields = ('question', 'reward')
