from django.contrib import admin
# Register your models here.
from .models import Student_Data, Teacher_Data, Student_Performance, Teacher_Performance
# Register your models here.


class studentdata(admin.ModelAdmin):
    list_display = ['Student_Name',
                    'Class',
                    'RollNumber',
                    'DateOfBirth',
                    'Gender',
                    'Address'
                    ]


class studentperform(admin.ModelAdmin):
    list_display = ['Student_Name',
                    'Class',
                    'RollNumber',
                    'Grade',
                    'Remarks'
                    ]


# class teacherdata(admin.ModelAdmin):
#     list_display =['Name',
#                    'TeacherId',
#                    'Qualification',
#                    'DateofJoining',
#                    'Gender',
#                    'Subject'
    # ]

class teacherperform(admin.ModelAdmin):
    list_display = ['Teacher_Name',
                    'TeacherId',
                    'Subject',
                    'Remarks'
                    ]


admin.site.register(Student_Data, studentdata)
# admin.site.register(Teacher_Data,teacherdata)
admin.site.register(Student_Performance, studentperform)
admin.site.register(Teacher_Performance, teacherperform)
# Register your models here.
