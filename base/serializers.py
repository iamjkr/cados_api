from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Advocate, Company


class CompanySerializer(ModelSerializer):
    employee_count = SerializerMethodField(read_only=True) # for counting how may employee works in specific cmpny
    class Meta:
        model =Company
        fields = '__all__'

    def get_employee_count(self,obj): #name shoud be same after get_ refer upper

        count = obj.advocate_set.count()
        return count


class AdvocateSerializer(ModelSerializer):
    company = CompanySerializer() # to view compay name insted of comay id like 1 or 2
    class Meta:
        model =Advocate
        fields = '__all__'


