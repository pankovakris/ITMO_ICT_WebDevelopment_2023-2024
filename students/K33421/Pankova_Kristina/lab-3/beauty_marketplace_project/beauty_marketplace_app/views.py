from django.shortcuts import render
from django.utils import timezone
from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers, generics

from .models import *

class SalonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salon
        fields = "__all__"

class SalonServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalonService
        fields = "__all__"

class SalonCommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalonComments
        fields = "__all__"

class SalonServiceCommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalonServiceComments
        fields = "__all__"

class SalonAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalonAppointment
        fields = "__all__"

class SalonOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalonOwner
        fields = "__all__"

# Create serializers

class SalonCreateSerializer(serializers.Serializer):
    owner = PrimaryKeyRelatedField(queryset=SalonOwner.objects.all())
    name = serializers.CharField(max_length=150)
    type = serializers.CharField()
    date_registered = serializers.DateField()
    city = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=500)

    def create(self, validated_data):
        salon = Salon.objects.create(**validated_data)
        return salon

class SalonServiceCreateSerializer(serializers.Serializer):
    salon = PrimaryKeyRelatedField(queryset=Salon.objects.all())
    name = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=500)
    price = serializers.IntegerField()

    def create(self, validated_data):
        service = SalonService.objects.create(**validated_data)
        return service


class SalonAppointmentCreateSerializer(serializers.Serializer):
    salon = PrimaryKeyRelatedField(queryset=Salon.objects.all())
    customer = PrimaryKeyRelatedField(queryset=Customer.objects.all())
    service = PrimaryKeyRelatedField(queryset=SalonService.objects.all())
    datetime = serializers.DateField()

    def validate_datetime(self, value):
        if value < timezone.now().date():
            raise serializers.ValidationError("The appointment date must be in the future or today.")
        return value
    def create(self, validated_data):
        appointment = SalonAppointment.objects.create(**validated_data)
        return appointment

class SalonCommentsCreateSerializer(serializers.Serializer):
    customer = PrimaryKeyRelatedField(queryset=Customer.objects.all())
    salon = PrimaryKeyRelatedField(queryset=Salon.objects.all())
    text = serializers.CharField(max_length=555)
    rating = serializers.IntegerField()

    def create(self, validated_data):
        comment = SalonComments.objects.create(**validated_data)
        return comment

class SalonServiceCommentsCreateSerializer(serializers.Serializer):
    customer = PrimaryKeyRelatedField(queryset=Customer.objects.all())
    salon_service = PrimaryKeyRelatedField(queryset=SalonService.objects.all())
    text = serializers.CharField(max_length=555)
    rating = serializers.IntegerField()

    def create(self, validated_data):
        comment = SalonServiceComments.objects.create(**validated_data)
        return comment


class SalonOwnerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalonOwner
        fields = ['password', 'username', 'first_name', 'last_name', 'email', 'phone_number']

    def create(self, validated_data):
        owner = SalonOwner.objects.create(**validated_data)
        owner.save()
        return owner

class CustomerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['password', 'username', 'first_name', 'last_name', 'email', 'phone_number']

    def create(self, validated_data):
        customer = Customer.objects.create(**validated_data)
        customer.save()
        return customer


class SalonAPIView(APIView):
    def get(self, request):
        salons = Salon.objects.all()
        serializer = SalonSerializer(salons, many=True)
        return Response({"Salons": serializer.data})


class SalonCommentsListAPIView(generics.ListAPIView):
   serializer_class = SalonCommentsSerializer
   queryset = SalonComments.objects.all()

class SalonAppointmentListAPIView(generics.ListAPIView):
   serializer_class = SalonAppointmentSerializer
   queryset = SalonAppointment.objects.all()

class SalonServiceListAPIView(generics.ListAPIView):
   serializer_class = SalonServiceSerializer
   queryset = SalonService.objects.all()

class SalonServiceCommentsListAPIView(generics.ListAPIView):
   serializer_class = SalonServiceCommentsSerializer
   queryset = SalonServiceComments.objects.all()

class SalonOwnerListAPIView(generics.ListAPIView):
   serializer_class = SalonOwnerSerializer
   queryset = SalonOwner.objects.all()


class SalonListAPIView(generics.ListAPIView):
   serializer_class = SalonSerializer
   queryset = Salon.objects.all()


class SalonCreateAPIView(generics.CreateAPIView):
   serializer_class = SalonCreateSerializer
   queryset = Salon.objects.all()

   def perform_create(self, serializer):
        serializer.save()

class SalonOwnerCreateAPIView(generics.CreateAPIView):
    serializer_class = SalonOwnerCreateSerializer
    queryset = SalonOwner.objects.all()

class CustomerCreateAPIView(generics.CreateAPIView):
    serializer_class = CustomerCreateSerializer
    queryset = Customer.objects.all()

class SalonAppointmentCreateAPIView(generics.CreateAPIView):
    serializer_class = SalonAppointmentCreateSerializer
    queryset = Customer.objects.all()

class SalonServiceCreateAPIView(generics.CreateAPIView):
    serializer_class = SalonServiceCreateSerializer
    queryset = SalonService.objects.all()

class SalonServiceCommentsCreateAPIView(generics.CreateAPIView):
    serializer_class = SalonServiceCommentsCreateSerializer
    queryset = SalonServiceComments.objects.all()

class SalonCommentsCreateAPIView(generics.CreateAPIView):
    serializer_class = SalonCommentsCreateSerializer
    queryset = SalonComments.objects.all()

class SalonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = SalonSerializer
    queryset = Salon.objects.all()

class SalonAppointmentRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = SalonAppointmentSerializer
    queryset = SalonAppointment.objects.all()

class SalonServiceRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = SalonServiceSerializer
    queryset = SalonService.objects.all()

class SalonCommentsRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = SalonCommentsSerializer
    queryset = SalonComments.objects.all()

class SalonServiceCommentsRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = SalonServiceCommentsSerializer
    queryset = SalonServiceComments.objects.all()

