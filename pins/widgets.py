from django.forms.widgets import DateTimeInput
from django.forms import DateTimeField


__all__ = ('DateTimeLocalWidget')

class DateTimeLocalWidget(DateTimeInput):
   input_type = "datetime-local"
   
class DateTimeLocalField(DateTimeField):
   widget=DateTimeLocalWidget
   input_fomats=['%Y-%m-%d %H:%M']
   
   def prepare_value(self, value):
      if value:
         value = value.replace('T', ' ')
      return super(DateTimeLocalField, self).prepare_value(value)
      
   def to_python(self, value):
      if value:
         value = value.replace('T', ' ')
      return super(DateTimeLocalField, self).to_python(value)
      
      