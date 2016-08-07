from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager


class MyUserManager(BaseUserManager):
    def create_user(self, username, real_name, password=None, fav_present=""):
        if not username:
            raise ValueError('Users must have username')
        if not real_name:
            raise ValueError('Please enter your real name')

        user = self.model(
            username=username,
            real_name=real_name,
            fav_present=fav_present,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, real_name, password):
        user = self.create_user(
            username,
            password=password,
            real_name=real_name,
        )
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    username = models.CharField(max_length=100, unique=True, verbose_name='Имя пользователя')
    password = models.CharField(max_length=100, verbose_name="Пароль")
    real_name = models.CharField(max_length=100, verbose_name="Имя, которое будет отображаться твоему Санте")

    fav_present = models.TextField(default="", blank=True, verbose_name="Лучший подарок, который тебе дарили")
    fav_film = models.TextField(default="", blank=True, verbose_name="Любимый фильм")
    fav_game = models.TextField(default="", blank=True, verbose_name="Любимая игра")
    fav_color = models.TextField(default="", blank=True, verbose_name="Любимый цвет")
    hobbies = models.TextField(default="", blank=True, verbose_name="Хобби")
    key_words = models.TextField(default="", blank=True, verbose_name="Слова, которые помогут твоему Санте :) ")

    santa_for = models.OneToOneField('self', null=True, blank=True)
    is_taken = models.BooleanField(default=False)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['real_name']

    def get_full_name(self):
        # The user is identified by their email address
        return self.real_name

    def get_short_name(self):
        # The user is identified by their email address
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        if self.is_admin:
            return True
        return False

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    def __str__(self):
        return self.real_name