from django.forms import widgets
from django.contrib.auth.models import User
from rest_framework import serializers
from quickstart.models import Quickstart, LANGUAGE_CHOICES, STYLE_CHOICES


class QuickstartSerializer(serializers.ModelSerializer):
  owner = serializers.ReadOnlyField(source='owner.username')
  highlight = serializers.HyperlinkedIdentityField(view_name='quickstart-highlight', format='html')

  class Meta:
    model = Quickstart
    fields = ('url', 'highlight', 'owner', 'title', 'code', 'linenos', 'language', 'style')


class UserSerializer(serializers.ModelSerializer):
  quickstart = serializers.PrimaryKeyRelatedField(many=True, queryset= Quickstart.objects.all())
  quickstart = serializers.HyperlinkedRelatedField(many=True, view_name='quickstart-detail', read_only=True)

  class Meta:
    model = User
    fields = ('url', 'username', 'quickstart')




"""
  pk = serializers.IntegerField(read_only=True)
  title = serializers.CharField(required=False, allow_blank=True, max_length=100)
  code = serializers.CharField(style={'base_template': 'textarea.html'})
  linenos = serializers.BooleanField(required=False)
  language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
  style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')


  def create(self, validated_data):
      #create and return a new quickstart instance given the validated data
      return Quickstart.objects.create(**validated_data)

  def update(self, instance, validated_data):
    #update and retun an existing quickstart instance given to validate
      instance.title = validated_data.get('title', instance.title)
      instance.code = validated_data.get('code', instance.code)
      instance.linenos = validated_data.get('linenos', instance.linenos)
      instance.language = validated_data.get('language', instance.language)
      instance.style = validated_data.get('style', instance.style)
      instance.save()
      return instance
"""
