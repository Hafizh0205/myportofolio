from rest_framework import serializers
from django.utils.html import strip_tags
from main.models import Project, Experience


class ProjectSerializer(serializers.ModelSerializer):
    star_count = serializers.IntegerField(source="starred_by.count", read_only=True)
    is_starred = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = [
            "id",
            "title",
            "description",
            "tech_stack",
            "project_url",
            "project_image_url",
            "star_count",
            "is_starred",
        ]
        read_only_fields = ["id", "star_count", "is_starred"]

    def get_is_starred(self, obj):
        request = self.context.get("request")
        if request is None or not request.user.is_authenticated:
            return False
        return obj.starred_by.filter(id=request.user.id).exists()

    def validate_title(self, value):
        value = strip_tags(value).strip()
        if not value:
            raise serializers.ValidationError("Title cannot be empty.")
        return value

    def validate_description(self, value):
        return strip_tags(value).strip()

    def validate_tech_stack(self, value):
        return strip_tags(value).strip()


class ExperienceSerializer(serializers.ModelSerializer):
    stars_count = serializers.IntegerField(source="starred_by.count", read_only=True)
    is_starred = serializers.SerializerMethodField()

    class Meta:
        model = Experience
        fields = [
            "id",
            "title",
            "description",
            "category",
            "ended_at",
            "stars_count",
            "is_starred",
        ]
        read_only_fields = ["id", "stars_count", "is_starred"]

    def get_is_starred(self, obj):
        request = self.context.get("request")
        if request is None or not request.user.is_authenticated:
            return False
        return obj.starred_by.filter(id=request.user.id).exists()

    def validate_title(self, value):
        value = strip_tags(value).strip()
        if not value:
            raise serializers.ValidationError("Title cannot be empty.")
        return value

    def validate_description(self, value):
        return strip_tags(value).strip()

    def validate_category(self, value):
        return strip_tags(value).strip()