# Generated by Django 2.1.7 on 2019-11-28 18:50

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(error_messages={'unique': 'El correo ya se encuentra registrado.'}, max_length=254, unique=True, verbose_name='correo electronico')),
                ('gender', models.CharField(choices=[('F', 'Femenino'), ('M', 'Masculino')], max_length=1, verbose_name='Genero')),
                ('birthdate', models.DateField(verbose_name='Fecha de Nacimiento')),
                ('dni_type', models.CharField(blank=True, choices=[('DNI', 'DNI'), ('LE', 'Libreta de Enrolamiento'), ('LC', 'Libreta Cívica')], default='', max_length=100, verbose_name='Tipo Documento')),
                ('dni_number', models.CharField(blank=True, default='', max_length=60, verbose_name='Número Documento')),
                ('street_name', models.CharField(blank=True, default='', max_length=200, verbose_name='Nombre Calle')),
                ('street_number', models.CharField(blank=True, default='', max_length=20, validators=[django.core.validators.RegexValidator('^[0-9]{1,20}$', 'Número calle inválido.')], verbose_name='Número Calle')),
                ('postal_code', models.CharField(blank=True, default='', max_length=12, verbose_name='Código Postal')),
                ('appartment_number', models.CharField(blank=True, default='', max_length=20, verbose_name='Nombre Departamento')),
                ('appartment_floor', models.CharField(blank=True, default='', max_length=20, verbose_name='Piso Departamento')),
                ('phone_number', models.CharField(blank=True, default='', max_length=60, verbose_name='Teléfono Movil')),
                ('email_verified', models.BooleanField(default=False, verbose_name='Email Verificado')),
                ('created_by', models.IntegerField(choices=[(0, 'Mi Argentina')], default=0, verbose_name='Creado Mediante')),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
                'ordering': ['-date_joined'],
                'permissions': (('read_user', 'Can read Usuario'),),
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('code', models.CharField(max_length=3, primary_key=True, serialize=False, verbose_name='Código')),
                ('name', models.CharField(max_length=150, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'País',
                'verbose_name_plural': 'Países',
            },
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Departamento',
                'verbose_name_plural': 'Departamentos',
            },
        ),
        migrations.CreateModel(
            name='EmailActivationToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=150)),
                ('date_sent', models.DateTimeField(auto_now=True, verbose_name='Fecha de Envío')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Token Activación de Email',
                'verbose_name_plural': 'Tokens Activación de Email',
                'ordering': ['-date_sent'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Locality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(choices=[('CAB', 'Ciudad Autónoma de Buenos Aires'), ('BSA', 'Buenos Aires'), ('CAT', 'Catamarca'), ('COR', 'Córdoba'), ('CRR', 'Corrientes'), ('CHA', 'Chaco'), ('CHU', 'Chubut'), ('ENT', 'Entre Ríos'), ('FOR', 'Formosa'), ('JUJ', 'Jujuy'), ('PAM', 'La Pampa'), ('RIO', 'La Rioja'), ('MEN', 'Mendoza'), ('MIS', 'Misiones'), ('NEU', 'Neuquén'), ('RNE', 'Río Negro'), ('SAL', 'Salta'), ('SJU', 'San Juan'), ('SLU', 'San Luis'), ('SCR', 'Santa Cruz'), ('SFE', 'Santa Fe'), ('SDE', 'Santiago del Estero'), ('TDF', 'Tierra del Fuego'), ('TUC', 'Tucumán')], max_length=3, verbose_name='Provincia')),
                ('name', models.CharField(max_length=150, verbose_name='Nombre')),
                ('updated', models.BooleanField(default=False)),
                ('district', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='id.District', verbose_name='Departamento')),
            ],
            options={
                'verbose_name': 'Localidad',
                'verbose_name_plural': 'Localidades',
            },
        ),
        migrations.CreateModel(
            name='PasswordResetToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=150)),
                ('date_sent', models.DateTimeField(auto_now=True, verbose_name='Fecha de Envío')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Token de Contraseña',
                'verbose_name_plural': 'Tokens de Contraseñas',
                'ordering': ['-date_sent'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Provincia',
                'verbose_name_plural': 'Provincias',
            },
        ),
        migrations.CreateModel(
            name='TermAndCondition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140, verbose_name='Term name')),
                ('slug_name', models.SlugField(max_length=100, unique=True)),
                ('is_principal', models.BooleanField(default=True, verbose_name='Principal')),
            ],
            options={
                'verbose_name': 'Términos y Condiciones.',
                'verbose_name_plural': 'Términos y condiciones',
            },
        ),
        migrations.CreateModel(
            name='UserTermAndCondition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=False, help_text='Term and condition acceptance.')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='modified at')),
                ('term', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='id.TermAndCondition')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Términos y Condiciones de Usuario',
                'verbose_name_plural': 'Términos y condiciones de Usuarios',
            },
        ),
        migrations.AddField(
            model_name='termandcondition',
            name='users',
            field=models.ManyToManyField(through='id.UserTermAndCondition', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='district',
            name='province',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='id.Province', verbose_name='Provincia'),
        ),
        migrations.AddField(
            model_name='user',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='current_country', to='id.Country', verbose_name='País'),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='locality',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='id.Locality', verbose_name='Localidad'),
        ),
        migrations.AddField(
            model_name='user',
            name='nationality',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='id.Country', verbose_name='Nacionalidad'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]