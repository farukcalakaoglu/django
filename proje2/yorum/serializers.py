from .models import Yorum
from rest_framework import serializers
import re
class YorumListSerializers(serializers.ModelSerializer):
     class   Meta:
       model=Yorum
       fields=["id","user","baslik","yorumu","slug"]
       
#------------------------------------------------------------------------------------------------
class YorumDetailsSerializers(serializers.ModelSerializer):
    class Meta:
        model=Yorum
        fields=["id","user","baslik","yorum","slug"]


#------------------------------------------------------------------------------------------------

class YorumSerializers(serializers.ModelSerializer):
    user = serializers.CharField()
    baslik = serializers.CharField()
    yorum = serializers.CharField()
    slug = serializers.SlugField()

    default_error_messages = {
        "does_not_exist": "Seçtiğiniz nesne yok."
    }