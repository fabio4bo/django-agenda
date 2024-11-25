
### helpful commands
```
# is responsible for creating new migrations based on the changes you made to your MODELS:
python manage.py makemigrations

# is responsible for applying and unapplying migrations:
python manage.py migrate

python manage.py runserver

python manage.py createsuperuser

python manage.py changepassword USERNAME

python manage.py shell

```

### Django Shell
```
from contact.modes import Contact
c = Contact(first_name='Antonio')
c.save()

# QuerySet 
c = Contact.objects.all()

c = Contact.objects.filter(last_name='Souza')

c = Contact.objects.all().order_by('-id')

# Create without .save()

c = Contact.objects.create(first_name='José', last_name='Bonifácio')

```