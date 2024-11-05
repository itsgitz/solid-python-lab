class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class EmailSender:
    def send_email(self, person: Person, message):
        print(f"Sending email to {person.name}: {message}")

class Profile:
    def get_profile(self, person: Person):
        print(f"Profile: {person.name} - {person.age}")

person = Person('Anggit M Ginanjar', 26)
email = EmailSender()
email.send_email(person, 'Hello!')