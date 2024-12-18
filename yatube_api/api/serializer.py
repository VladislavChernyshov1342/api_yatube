from rest_framework import serializers

from posts.models import Comment, Group, Post


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class BaseSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        abstract = True


class PostSerializer(BaseSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class CommentSerializer(BaseSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('post',)
