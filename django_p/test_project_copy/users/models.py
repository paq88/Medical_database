from django.db import models
# def create_placeholder_employee():
#     # Create a placeholder employee with generic information
#     # Example:
#     placeholder_employee = employes.objects.create(first_name='Placeholder Admin', email='admin@example.com')
#     return placeholder_employee.id



# tworzenie klasy w nawiasie pisze że dziedziczy po Model

class laboratory(models.Model):
    name = models.CharField('Name of the laboratory', max_length=45)
    address = models.CharField('Address of the laboratory', max_length=45)


class patients(models.Model):
    name = models.CharField('Name of the patient', max_length=45)
    last_name = models.CharField('Last Name of the patient', max_length=45)
    sex = models.CharField('Sex of the patient', max_length=1)
    DOB = models.DateField('Date of birth')
    pesel = models.IntegerField('Pesel of the patient')
    phone_number = models.IntegerField('Phone number of the patient')
    email = models.EmailField('Email of the patient')
    group = models.CharField('Group of the patient', max_length=45)
    address = models.CharField('Address of the patient', max_length=45)

class employes(models.Model):
    # teraz sobie robimy kolumny
    first_name = models.CharField('First Name', max_length=45)
    last_name = models.CharField('Last Name', max_length=45)
    login = models.CharField('Login', max_length=45)
    password = models.CharField('Password', max_length=45)
    email = models.EmailField('Email', max_length=45)
    pesel = models.IntegerField('Pesel')
    phone_number = models.IntegerField('Phone Number')

    # tworzenie klucza obcego
    # definiujemy też działanie co się dzieje przy usunięciu cascade znaczy
    # że usuwając pracowników usuwamy wszystkich
    # to jest jednocześnie relacja wiele do jednego i umieszczamy go tam gdzie wiele
    id_lab = models.ForeignKey(laboratory, on_delete=models.CASCADE)


    #tworzenie relacji wiele do wielu tabela przejściowa sama sie robi
    #nie ma znaczenia czy umieścimy ją w jednej czy w drugiej
    #relacja jeden do jednego to one to one


    #id_employes = models.ManyToManyField(project,blank=True)


class project(models.Model):
    name_of_project = models.CharField('Name of the project', max_length=45)
    description = models.CharField('Description of the project', max_length=45)
    start_date = models.DateField('Start')
    end_date = models.DateField('End')
    id_project = models.ManyToManyField(employes)

    #admin_employee = models.ForeignKey(employes, on_delete=models.CASCADE, related_name='administered_projects',  default=create_placeholder_employee)


class experiments(models.Model):
    name_of_experiment = models.CharField('Name of the experiment', max_length=45)
    start_date = models.DateField('Start')
    end_date = models.DateField('End')
    status = models.CharField('Status of the experiment', max_length=45)
    description_of_results = models.CharField('Description results', max_length=45)
    id_project = models.ForeignKey(project, on_delete=models.CASCADE)
    id_experiments = models.ManyToManyField(employes)

class keywords(models.Model):
    key_word = models.CharField('Key word', max_length=45)
    id_experiment = models.ForeignKey(experiments, on_delete=models.CASCADE)
    id_project = models.ForeignKey(project, on_delete=models.CASCADE)

class results(models.Model):
    filename = models.CharField('Filename', max_length=45)
    id_experiment = models.ForeignKey(experiments, on_delete=models.CASCADE)

class protocols(models.Model):
    protocol_name = models.CharField('Name of the protocol', max_length=45)
    id_experiment = models.ForeignKey(experiments, on_delete=models.CASCADE)
