from teacher.models import Teacher
from rest_framework import serializers
from markingScheme.models import MarkingScheme
from assessment.models import Assessment
from module.models import Module
from facilitator.models import Facilitator
from kicd.models import Kicd
from rest_framework import serializers
from users.models import User


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"


class MarkingSchemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarkingScheme
        fields = "__all__"


class AssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assessment
        fields = "__all__"


class KicdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kicd
        fields = "__all__"


class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = "__all__"



class FacilitatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facilitator
        fields = "__all__"
class UserSerializer(serializers.ModelSerializer):
   
 class Meta:
        model = User
        fields = ['first_name', 'last_name', 'password', 'email', 'role']




class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'password', 'email', 'role']

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            role=validated_data.get('role', User.KICD_OFFICIAL),  # Default role
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
# class LoginSerializer(serializers.Serializer):
#     email = serializers.EmailField(required=True)
#     password = serializers.CharField(required=True)

    



class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if not email or not password:
            raise serializers.ValidationError('Both email and password are required.')
        
        return attrs