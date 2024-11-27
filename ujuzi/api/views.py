# # from django.contrib.auth import authenticate, login, get_user_model
# # from django.core.exceptions import ValidationError
# # from django.shortcuts import get_object_or_404
# # from rest_framework.response import Response
# # from rest_framework.views import APIView
# # from rest_framework import status
# # from rest_framework.permissions import AllowAny
# # from rest_framework import generics
# # import logging
# # from .serializers import TeacherSerializer
# # from teacher.models import Teacher
# # from markingScheme.models import MarkingScheme
# # from .serializers import MarkingSchemeSerializer
# # from assessment.models import Assessment
# # from .serializers import AssessmentSerializer
# # from module.models import Module
# # from .serializers import ModuleSerializer
# # from facilitator.models import Facilitator
# # from .serializers import FacilitatorSerializer
# # from kicd.models import Kicd
# # from .serializers import KicdSerializer
# # from users.models import Login
# # from .serializers import UserSerializer
# # from api.serializers import RegisterSerializer



# # # Set up logging
# # logger = logging.getLogger(__name__)

# # User = get_user_model()

# # class UserListView(generics.ListCreateAPIView):
# #     """
# #     Handle listing and creating users.
# #     """
# #     queryset = User.objects.all()
# #     serializer_class = UserSerializer

# #     def post(self, request):
# #         """
# #         Create a new user.
# #         """
# #         serializer = self.get_serializer(data=request.data)
# #         if serializer.is_valid():
# #             serializer.save()
# #             logger.info('User created successfully: %s', serializer.data)
# #             return Response(serializer.data, status=status.HTTP_201_CREATED)
# #         else:
# #             logger.error('User creation failed: %s', serializer.errors)
# #             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# # class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
# #     """
# #     Handle user detail retrieval, update, and deletion.
# #     """
# #     queryset = User.objects.all()
# #     serializer_class = UserSerializer

# #     def get(self, request, pk):
# #         """
# #         Retrieve a user by ID.
# #         """
# #         user = self.get_object()
# #         serializer = self.get_serializer(user)
# #         logger.info('User with ID %d retrieved successfully: %s', pk, serializer.data)
# #         return Response(serializer.data)

# #     def patch(self, request, pk):
# #         """
# #         Update a user by ID.
# #         """
# #         user = self.get_object()
# #         serializer = self.get_serializer(user, data=request.data, partial=True)
# #         if serializer.is_valid():
# #             serializer.save()
# #             logger.info('User with ID %d updated successfully: %s', pk, serializer.data)
# #             return Response(serializer.data)
# #         else:
# #             logger.error('User update failed for ID %d: %s', pk, serializer.errors)
# #             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# #     def delete(self, request, pk):
# #         """
# #         Delete a user by ID.
# #         """
# #         user = self.get_object()
# #         user.delete()
# #         logger.info('User with ID %d deleted successfully.', pk)
# #         return Response(status=status.HTTP_204_NO_CONTENT)
    


# # class RegisterView(APIView):
# #     # permission_classes = [AllowAny]  # This allows any user (authenticated or not) to access this view

# #     def post(self, request, *args, **kwargs):
# #         email = request.data.get('email')
# #         registered_via = 'admin'  # Set the registration source to 'admin'

# #         # Check if a user with the provided email already exists
# #         if get_user_model().objects.filter(email=email).exists():
# #             return Response({'error': 'A user with this email already exists.'}, status=status.HTTP_400_BAD_REQUEST)

# #         # Serialize the request data
# #         serializer = RegisterSerializer(data=request.data)
# #         if serializer.is_valid():
# #             # Save the user and set registered_from as 'admin'
# #             user = serializer.save(registered_from=registered_via)

# #             # Prepare response data
# #             response_data = {
# #                 'message': f"{user.role.capitalize()} {user.first_name} {user.last_name} successfully created",
# #                 'user': {
# #                     'first_name': user.first_name,
# #                     'last_name': user.last_name,
# #                     'email': user.email,
# #                     'role': user.role,
# #                 }
# #             }
# #             return Response(response_data, status=status.HTTP_201_CREATED)
        
# #         # If the serializer is invalid, return errors
# #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# # # class RegisterView(APIView):
# # #     permission_classes = [AllowAny]

# # #     def post(self, request, *args, **kwargs):
# # #         email = request.data.get('email')
# # #         registered_via = 'admin'  # Set the registration source to 'admin'

# # #         # Check if a user with the provided email already exists
# # #         if get_user_model().objects.filter(email=email).exists():
# # #             return Response({'error': 'A user with this email already exists.'}, status=status.HTTP_400_BAD_REQUEST)

   

# # #         # Serialize the request data
# # #         serializer = RegisterSerializer(data=request.data)
# # #         if serializer.is_valid():
# # #             # Save the user and set registered_from as 'admin'
# # #             user = serializer.save(registered_from=registered_via)
            
        

# # #             # Prepare response data
# # #             response_data = {
# # #                 'message': f"{user.role.capitalize()} {user.first_name} {user.last_name} successfully created",
# # #                 'user': {
# # #                     'first_name': user.first_name,
# # #                     'last_name': user.last_name,
# # #                     'email': user.email,
# # #                     'role': user.role,
                   
# # #                 }
# # #             }
# # #             return Response(response_data, status=status.HTTP_201_CREATED)
# # #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





# # # User = get_user_model()
# # # logger = logging.getLogger(__name__)


# # class LoginUser(APIView):
# #     # permission_classes = [AllowAny]
# #     # authentication_classes = []  # Disable authentication for login

# #     def create_new_user(self, email, password):
# #         """Create a new user with the given email and password"""
# #         try:
# #             user = User.objects.create_user(
# #                 email=email,
# #                 password=password,
# #                 first_name="New",
# #                 last_name="User",
# #                 role="user",
# #                 is_active=True  # Ensure the user is active
# #             )
# #             return user
# #         except Exception as e:
# #             logger.error(f"Error creating new user: {str(e)}")
# #             raise

# #     def post(self, request, *args, **kwargs):
# #         try:
# #             # Extract credentials
# #             email = request.data.get('email')
# #             password = request.data.get('password')

# #             # Input validation
# #             if not email or not password:
# #                 return Response(
# #                     {'detail': 'Email and password are required.'},
# #                     status=status.HTTP_400_BAD_REQUEST
# #                 )

# #             # Log authentication attempt
# #             logger.info(f"Login/Registration attempt for email: {email}")

# #             # Check if user exists
# #             existing_user = User.objects.filter(email=email).first()
            
# #             if existing_user:
# #                 # Try to authenticate existing user
# #                 user = authenticate(request, email=email, password=password)
# #                 if not user:
# #                     return Response(
# #                         {'detail': 'Invalid password.'},
# #                         status=status.HTTP_401_UNAUTHORIZED
# #                     )
# #             else:
# #                 # Create new user
# #                 try:
# #                     user = self.create_new_user(email, password)
# #                     # Authenticate the new user
# #                     user = authenticate(request, email=email, password=password)
# #                     logger.info(f"New user created with email: {email}")
# #                 except Exception as e:
# #                     logger.error(f"Failed to create new user: {str(e)}")
# #                     return Response(
# #                         {'detail': 'Failed to create new user.'},
# #                         status=status.HTTP_400_BAD_REQUEST
# #                     )

# #             if not user.is_active:
# #                 logger.warning(f"Inactive user attempted login: {email}")
# #                 return Response(
# #                     {'detail': 'This account is inactive.'},
# #                     status=status.HTTP_403_FORBIDDEN
# #                 )

# #             # Login user
# #             login(request, user)

# #             # Log successful login
# #             Login.objects.create(user=user)
# #             logger.info(f"Successful login for user: {email}")

# #             # Prepare response
# #             response_data = {
# #                 'message': 'Login successful',
# #                 'is_new_user': not existing_user,
# #                 'user': {
# #                     'id': user.id,
# #                     'first_name': user.first_name,
# #                     'last_name': user.last_name,
# #                     'email': user.email,
# #                     'role': user.role,
# #                 }
# #             }

# #             return Response(response_data, status=status.HTTP_200_OK)

# #         except ValidationError as e:
# #             logger.error(f"Validation error during login: {str(e)}")
# #             return Response(
# #                 {'detail': str(e)},
# #                 status=status.HTTP_400_BAD_REQUEST
# #             )
# #         except Exception as e:
# #             logger.error(f"Unexpected error during login: {str(e)}")
# #             return Response(
# #                 {'detail': 'An unexpected error occurred. Please try again.'},
# #                 status=status.HTTP_500_INTERNAL_SERVER_ERROR
# #             )













# # # Create your views here.


# # class TeacherListView(APIView):
# #     def get(self, request):
# #         teachers = Teacher.objects.all()
# #         serializer = TeacherSerializer(teachers, many=True)
# #         return Response(serializer.data)
    
# #     def post(self, request):
# #         serializer = TeacherSerializer(data=request.data)
# #         if serializer.is_valid():
# #             serializer.save()
# #             return Response(serializer.data, status=status.HTTP_201_CREATED)
# #         else:
# #             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





# class TeacherDetailView(APIView):
#     def get(self, request, id):
#         teacher = Teacher.objects.get(id=id) 
#         serializer = TeacherSerializer(teacher)
#         return Response(serializer.data)
    
#     def put(self, request, id):
#         teacher = Teacher.objects.get(id=id)
#         serializer = TeacherSerializer(teacher, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)  
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

    

# class MarkingSchemeListView(APIView):
#     def get(self, request):
#         markingschemes = MarkingScheme.objects.all()
#         serializer = MarkingSchemeSerializer(markingschemes, many=True)
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = MarkingSchemeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class MarkingSchemeDetailView(APIView):
#     def get(self, request, id):
#         markingschemes = MarkingScheme.objects.get(id=id) 
#         serializer = MarkingSchemeSerializer(markingschemes)
#         return Response(serializer.data)
    
#     def put(self, request, id):
#         markingschemes = MarkingScheme.objects.get(id=id)
#         serializer = MarkingSchemeSerializer(markingschemes, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)  
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#     def delete(self, request, id):
#         markingscheme = MarkingScheme.objects.get(id=id)
#         markingscheme.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
# class AssessmentListView(APIView):
#     def get(self, request):
#         assessments = Assessment.objects.all()
#         serializer = AssessmentSerializer(assessments, many=True)
#         return Response(serializer.data)
#     def post(self, request):
#         serializer = AssessmentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# class AssessmentDetailView(APIView):
#     def get(self, request, pk):
#         try:
#             assessment = Assessment.objects.get(pk=pk)
#         except Assessment.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         serializer = AssessmentSerializer(assessment)
#         return Response(serializer.data)
#     def put(self, request, pk):
#         try:
#             assessment = Assessment.objects.get(pk=pk)
#         except Assessment.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         serializer = AssessmentSerializer(assessment, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     def delete(self, request, pk):
#         try:
#             assessment = Assessment.objects.get(pk=pk)
#         except Assessment.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         assessment.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)   
    


# class FacilitatorListView(APIView):
#     def get(self, request):
#         facilitators = Facilitator.objects.all()
#         serializer = FacilitatorSerializer(facilitators, many=True)
#         return Response(serializer.data)
#     def post(self, request):
#         serializer = FacilitatorSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# class FacilitatorDetailView(APIView):
#     def get(self, request, id):
#        facilitators = Facilitator.objects.get(id=id)
#        serializer = FacilitatorSerializer(facilitators)
#        return Response(serializer.data)
#     def put(self, request, id):
#         facilitators = Facilitator.objects.get(id=id)
#         serializer = FacilitatorSerializer(facilitators, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from django.contrib.auth import authenticate, login, get_user_model
from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.middleware.csrf import get_token

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import generics
import logging

from .serializers import (
    TeacherSerializer, MarkingSchemeSerializer, 
    AssessmentSerializer, ModuleSerializer, 
    FacilitatorSerializer, KicdSerializer, 
    UserSerializer, RegisterSerializer
)

from teacher.models import Teacher
from markingScheme.models import MarkingScheme
from assessment.models import Assessment
from module.models import Module
from facilitator.models import Facilitator
from kicd.models import Kicd
from users.models import Login

# Set up logging
logger = logging.getLogger(__name__)

User = get_user_model()

# CSRF Handling Decorator
def csrf_exempt_if_development(view_func):
    def wrapped_view(request, *args, **kwargs):
        # Check if in development mode or some other condition
        if request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            request.csrf_processing_done = True
        return view_func(request, *args, **kwargs)
    return wrapped_view

# Base View with CSRF Handling
class CSRFExemptAPIView(APIView):
    """
    Base API View that can be exempted from CSRF for specific scenarios
    """
    @method_decorator(csrf_exempt_if_development)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

# CSRF Token View
class GetCSRFToken(APIView):
    """
    View to get CSRF token for frontend
    """
    permission_classes = [AllowAny]

    def get(self, request):
        csrf_token = get_token(request)
        return Response({'csrfToken': csrf_token})

# User List and Registration Views
class UserListView(CSRFExemptAPIView):
    """
    Handle listing and creating users with flexible CSRF protection.
    """
    permission_classes = [AllowAny]

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Create a new user with flexible CSRF handling.
        """
        try:
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                logger.info('User created successfully: %s', serializer.data)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                logger.error('User creation failed: %s', serializer.errors)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(f'Unexpected error in user creation: {str(e)}')
            return Response({'detail': 'An unexpected error occurred'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# User Detail View
class UserDetailView(CSRFExemptAPIView):
    """
    Handle user detail retrieval, update, and deletion.
    """
    permission_classes = [AllowAny]

    def get(self, request, pk):
        """
        Retrieve a user by ID.
        """
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user)
        logger.info('User with ID %d retrieved successfully: %s', pk, serializer.data)
        return Response(serializer.data)

    def patch(self, request, pk):
        """
        Update a user by ID.
        """
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            logger.info('User with ID %d updated successfully: %s', pk, serializer.data)
            return Response(serializer.data)
        else:
            logger.error('User update failed for ID %d: %s', pk, serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """
        Delete a user by ID.
        """
        user = get_object_or_404(User, pk=pk)
        user.delete()
        logger.info('User with ID %d deleted successfully.', pk)
        return Response(status=status.HTTP_204_NO_CONTENT)

# Registration View
class RegisterView(CSRFExemptAPIView):
    """
    User registration view with flexible CSRF protection.
    """
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        try:
            email = request.data.get('email')
            registered_via = 'admin'  # Set the registration source to 'admin'

            # Check if a user with the provided email already exists
            if get_user_model().objects.filter(email=email).exists():
                return Response({'error': 'A user with this email already exists.'}, status=status.HTTP_400_BAD_REQUEST)

            # Serialize the request data
            serializer = RegisterSerializer(data=request.data)
            if serializer.is_valid():
                # Save the user and set registered_from as 'admin'
                user = serializer.save(registered_from=registered_via)

                # Prepare response data
                response_data = {
                    'message': f"{user.role.capitalize()} {user.first_name} {user.last_name} successfully created",
                    'user': {
                        'first_name': user.first_name,
                        'last_name': user.last_name,
                        'email': user.email,
                        'role': user.role,
                    }
                }
                return Response(response_data, status=status.HTTP_201_CREATED)
            
            # If the serializer is invalid, return errors
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            logger.error(f'Registration error: {str(e)}')
            return Response({'detail': 'Registration failed'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Login View
class LoginUser(CSRFExemptAPIView):
    """
    Login view with flexible CSRF protection and error handling.
    """
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        try:
            # Extract credentials
            email = request.data.get('email')
            password = request.data.get('password')

            # Input validation
            if not email or not password:
                return Response(
                    {'detail': 'Email and password are required.'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            # Log authentication attempt
            logger.info(f"Login/Registration attempt for email: {email}")

            # Check if user exists
            existing_user = User.objects.filter(email=email).first()
            
            if existing_user:
                # Try to authenticate existing user
                user = authenticate(request, email=email, password=password)
                if not user:
                    return Response(
                        {'detail': 'Invalid password.'},
                        status=status.HTTP_401_UNAUTHORIZED
                    )
            else:
                # Create new user logic
                try:
                    user = User.objects.create_user(
                        email=email,
                        password=password,
                        first_name="New",
                        last_name="User",
                        role="user",
                        is_active=True
                    )
                    user = authenticate(request, email=email, password=password)
                    logger.info(f"New user created with email: {email}")
                except Exception as e:
                    logger.error(f"Failed to create new user: {str(e)}")
                    return Response(
                        {'detail': 'Failed to create new user.'},
                        status=status.HTTP_400_BAD_REQUEST
                    )

            if not user.is_active:
                logger.warning(f"Inactive user attempted login: {email}")
                return Response(
                    {'detail': 'This account is inactive.'},
                    status=status.HTTP_403_FORBIDDEN
                )

            # Login user
            login(request, user)

            # Log successful login
            Login.objects.create(user=user)
            logger.info(f"Successful login for user: {email}")

            # Prepare response
            response_data = {
                'message': 'Login successful',
                'is_new_user': not existing_user,
                'user': {
                    'id': user.id,
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'email': user.email,
                    'role': user.role,
                }
            }

            return Response(response_data, status=status.HTTP_200_OK)

        except ValidationError as e:
            logger.error(f"Validation error during login: {str(e)}")
            return Response(
                {'detail': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            logger.error(f"Unexpected error during login: {str(e)}")
            return Response(
                {'detail': 'An unexpected error occurred. Please try again.'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

# Teacher Views
class TeacherListView(CSRFExemptAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TeacherDetailView(CSRFExemptAPIView):
    def get(self, request, id):
        teacher = get_object_or_404(Teacher, id=id)
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data)
    
    def put(self, request, id):
        teacher = get_object_or_404(Teacher, id=id)
        serializer = TeacherSerializer(teacher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)  
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Marking Scheme Views
class MarkingSchemeListView(CSRFExemptAPIView):
    def get(self, request):
        markingschemes = MarkingScheme.objects.all()
        serializer = MarkingSchemeSerializer(markingschemes, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = MarkingSchemeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MarkingSchemeDetailView(CSRFExemptAPIView):
    def get(self, request, id):
        markingschemes = get_object_or_404(MarkingScheme, id=id)
        serializer = MarkingSchemeSerializer(markingschemes)
        return Response(serializer.data)
    
    def put(self, request, id):
        markingschemes = get_object_or_404(MarkingScheme, id=id)
        serializer = MarkingSchemeSerializer(markingschemes, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)  
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, id):
        markingscheme = get_object_or_404(MarkingScheme, id=id)
        markingscheme.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Assessment Views
class AssessmentListView(CSRFExemptAPIView):
    def get(self, request):
        assessments = Assessment.objects.all()
        serializer = AssessmentSerializer(assessments, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = AssessmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AssessmentDetailView(CSRFExemptAPIView):
    def get(self, request, pk):
        assessment = get_object_or_404(Assessment, pk=pk)
        serializer = AssessmentSerializer(assessment)
        return Response(serializer.data)
    
    def put(self, request, pk):
        assessment = get_object_or_404(Assessment, pk=pk)
        serializer = AssessmentSerializer(assessment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        assessment = get_object_or_404(Assessment, pk=pk)
        assessment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Facilitator Views
class FacilitatorListView(CSRFExemptAPIView):
    def get(self, request):
        facilitators = Facilitator.objects.all()
        serializer = FacilitatorSerializer(facilitators, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = FacilitatorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FacilitatorDetailView(CSRFExemptAPIView):
    def get(self, request, id):
       facilitators = get_object_or_404(Facilitator, id=id)
       serializer = FacilitatorSerializer(facilitators)
       return Response(serializer.data)
    
    def put(self, request, id):
        facilitators = get_object_or_404(Facilitator, id=id)
        serializer = FacilitatorSerializer(facilitators, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, id):
        facilitator = Facilitator.objects.get(id=id)
        facilitator.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




class ModuleListView(APIView):
    def get(self, request):
        modules = Module.objects.all()
        serializer = ModuleSerializer(modules, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ModuleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ModuleDetailView(APIView):
    def get(self, request, id):
        module = get_object_or_404(Module, id=id)
        serializer = ModuleSerializer(module)
        return Response(serializer.data)

    def put(self, request, id):
        module = get_object_or_404(Module, id=id)
        serializer = ModuleSerializer(module, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        module = get_object_or_404(Module, id=id)
        module.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


        
    
# @method_decorator(csrf_exempt, name='dispatch')
# class KicdListView(APIView):
#     def get(self, request):
#         kicds = Kicd.objects.all()
#         serializer = KicdSerializer(kicds, many=True)
#         return Response(serializer.data)
    

#     def post(self, request):
#         serializer = KicdSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    



class KicdListView(generics.ListCreateAPIView):
    queryset = Kicd.objects.all()
    serializer_class = KicdSerializer

    def get(self, request, *args, **kwargs):
        kicds = self.get_queryset()
        serializer = self.get_serializer(kicds, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class KicdDetailView(APIView):
    def get(self, request, id):
        kicd = get_object_or_404(Kicd, id=id)
        serializer = KicdSerializer(kicd)
        return Response(serializer.data)
    def put(self, request, id):
        kicd = get_object_or_404(Kicd, id=id)
        serializer = KicdSerializer(kicd, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id):
        kicd = get_object_or_404(Kicd, id=id)
        kicd.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    




