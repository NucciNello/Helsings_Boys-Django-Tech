from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, password=None):
        if not username:
            raise ValueError('The given username must be set')
        user = self.model(
            username=self.normalize_email(username) 
        )
        user.is_superuser = False
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password=None):
        return self._create_user(username, password)


    def create_superuser(self, username, password):
        user = self.create_user(username=username, password = password)
        user.is_staff = True
        user.is_superuser = True
        user.is_admin = True
        user.save(using=self._db)
        return user