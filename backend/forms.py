from django import forms
from backend.models import Host

class HostForm(forms.ModelForm):
    hostname = forms.CharField(label="主机名")

    class Meta:
         model=Host
         fields=('hostname','ip_addr','asset_id','remark')