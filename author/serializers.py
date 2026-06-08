from rest_framework import serializers

from author.models import Author


class AuthorSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=64)
    last_name = serializers.CharField(max_length=64)
    pseudonym = serializers.CharField(
        max_length=64,
        allow_null=True,
        required=False,
    )
    age = serializers.IntegerField()
    retired = serializers.BooleanField()

    class Meta:
        model = Author
        fields = (
            "first_name",
            "last_name",
            "pseudonym",
            "age",
            "retired",
        )
