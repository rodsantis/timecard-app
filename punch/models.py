from django.db import models

class Role(models.Model):
    """
        In Role, it will be added the company position of the Employee
        Ex: Agent, Team Manager, Operation Manager, Quality Lead, Team Coordinator, Trainer, etc
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, blank=False, null=False, unique=True)

    def __str__(self):
        return self.name


class Skill(models.Model):
    """
        In Skill, we will have the line in which that Employee will be working.
        Ex: DSS, R2, R1, Trust, Claim, etc..
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=False, null=False, unique=True)

    def __str__(self):
        return self.name


class Market(models.Model):
    """
        In Market, it will have the languages to which the Employee will be working on
        Ex: Italian, English, Spanish, etc.
    """
    id = models.AutoField(primary_key=True)
    language = models.CharField(max_length=100, blank=False, null=False, unique=True)

    def __str__(self):
        return self.language


class Employee(models.Model):
    """
        Here we are creating our employee

        airbnb_id: is a unique value and that is the register that Airbnb Have to our employee
            it should be added as the timesheet will be created with that as referance
    """
    id = models.AutoField(primary_key=True)
    airbnb_id = models.CharField(max_length=10, blank=False, null=False, unique=True)
    first_name = models.CharField(max_length=100, blank=False, null=False)
    last_name = models.CharField(max_length=100, blank=False, null=False)
    role = models.ForeignKey(Role, on_delete=models.PROTECT, related_name="employee_role")
    skill = models.ForeignKey(Skill, on_delete=models.PROTECT, related_name="employee_skill")
    market = models.ForeignKey(Market, on_delete=models.PROTECT, related_name="employee_market")
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
