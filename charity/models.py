from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

class Category(models.Model):
    """[summary]
    Category model
    """
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Institution(models.Model):
    """[summary]
    Institution model
    """
    TYPE_CHOICES = (
        ('fundacja', 'Fundacja'),
        ('organizacja pozarządowa', 'Organizacja Pozarządowa'),
        ('zbiórka lokalna', 'Zbiórka Lokalna'),
    )


    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    type_institution = models.CharField(max_length=100,default='fundacja', choices=TYPE_CHOICES)
    categories = models.ManyToManyField(Category, related_name='categories')

    class Meta:
        verbose_name = _('Institution')
        verbose_name_plural = _('Institutions')


    def __str__(self):
        return self.name


class Dotation(models.Model):
    """[summary]
    Dodation model
    """
    quantity = models.PositiveIntegerField(
        verbose_name=_('Ilość'), 
        help_text=_('Wymagany'), 
        default=1, 
        validators=[MinValueValidator(1), MaxValueValidator(100)])
    categories = models.ManyToManyField(Category, related_name='category_selection', verbose_name=_('Category'), help_text=_('Wymagany'))
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    # Dilvery Dotation
    address = models.CharField(verbose_name=_('Data'), help_text=_('Wymagany'), max_length=255)
    phone_number = models.CharField(verbose_name=_('Data'), help_text=_('Wymagany'), max_length=50)
    city = models.CharField(verbose_name=_('Data'), help_text=_('Wymagany'), max_length=150)
    postcode = models.CharField(verbose_name=_('Kod Pocztowy'), help_text=_('Wymagany'), max_length=50)
    pick_up_date = models.DateField(verbose_name=_('Data'), help_text=_('Wymagany'), auto_now_add=True)
    pick_up_time = models.DateTimeField(verbose_name=_('Czas'), help_text=_('Wymagany'), auto_now_add=True)
    pick_up_comment = models.TextField(verbose_name=_('Komentarz'), help_text=_('Wymagany'), max_length=500, blank=True)
    user = models.ForeignKey(User, help_text=_('Użytkownik'), null=True, on_delete=models.CASCADE)


    class Meta:
        verbose_name = _('Dotation')
        verbose_name_plural = _('Dotations')

    

    




