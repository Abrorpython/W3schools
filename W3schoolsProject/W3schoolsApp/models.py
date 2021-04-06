from django.db import models

class Coursers(models.Model):
    coursersname = models.CharField(max_length=255, null=False, blank=False)    # kursni namelari haqida

    def __str__(self):
        return "%s - %s" % (self.id - self.name)


class Section(models.Model):
    name  = models.CharField(max_length=255, null=False, blank=False)           # kursning bo'limlari yoziladi
    course = models.ForeignKey(Coursers, blank=True, null=True, on_delete=models.SET_NULL) # bo'lim qaysi kursga tegishligi tanlanadi

    def __str__(self):
        return "%s - %s" % (self.id - self.name)


class Subject(models.Model):
    courserName = models.ForeignKey(Coursers, blank=True, null=True,on_delete=models.SET_NULL) # kurs nomi tanlanadi
    section = models.ForeignKey(Section, blank=True, null=True, on_delete=models.SET_NULL)      # kursdagi bo'lim tanlanadi
    theme = models.CharField(max_length=255,null=False, blank=False)                 # bo'lim ichidagi mavzu yoziladi
    discription = models.TextField(blank=True, null=True)                            # mavzu haqida qisqacha ma'lumot

    def __str__(self):
        return "%s - %s" % (self.id - self.theme)


class ThemeAbout(models.Model):
    subject = models.ForeignKey(Subject, blank=True, null=True, on_delete=models.SET_NULL)     # mavzu tanlanadi
    title = models.CharField(max_length=2048,null=False,blank=False)                                                      # mavzuni titlesi yoziladi
    text= models.TextField()                                                        # mavzuga tegishli ma'lumot
    example = models.TextField(blank=False, null=True)                              # mavzuga oid kodlar kiritiladi
    order = models.IntegerField(blank=False,null=False)                             # berilgan raqamlarga qarab sort qilinadi

    def __str__(self):
        return "%s - %s" % (self.id - self.title)