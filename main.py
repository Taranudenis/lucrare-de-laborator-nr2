import murat

clasa Facultatea:
def __init__(self, name, field):
self.name = nume
self.field = câmp
self.students = []

def assign_student(self, student):
self.students.append(student)

def graduate_student(self, student):
dacă student în sine.elevi:
self.students.remove(student)

def enrolled_students(self):
return [student pentru student în sine.studenti dacă nu student.graduate_status]

absolvenți def (auto):
return [student pentru student în sine.studenti dacă student.graduate_status]


elev de clasa:
def __init__(self, name, unic_identifier, email):
self.name = nume
self.unique_identifier = identificator_unic
self.email = email
self.graduate_status = Fals

def absolvent(auto):
self.graduate_status = Adevărat


clasa Universitate:
def __init__(self):
self.facultities = []

def create_faculty(self, name, field):
facultate = Facultate (nume, domeniu)
self.facultities.append(facultate)

def search_faculty(self, unic_identifier):
pentru facultate în sine.facultăți:
pentru student în facultate.studenti:
dacă student.identificator_unic == identificator_unic:
întoarce facultatea
return Niciunul

def display_all_faculties(self):
return [facultate.nume pentru facultate în self.facultities]

def display_faculties_by_field(self, field):
return [faculty.name pentru facultate în self.facultities if faculty.field == câmp]


clasa SaveManager:
@staticmethod
def save_state(universitate, nume de fișier):
încerca:
cu open(filename, 'wb') ca fișier:
pickle.dump(universitate, fișier)
print("Starea programului a fost salvată cu succes.")
cu excepția excepției ca e:
print(f"A apărut o eroare la salvarea stării programului: {e}")

@staticmethod
def load_state(nume fișier):
încerca:
cu open(filename, 'rb') ca fișier:
universitate = pickle.load(file)
print("Starea programului a fost încărcată cu succes.")
întoarce la universitate
cu excepția FileNotFoundError:
print("Nu a fost găsită nicio stare salvată. Începând cu starea goală.")
întoarce la universitate()
cu excepția excepției ca e:
print(f"A apărut o eroare la încărcarea stării programului: {e}")
întoarce la universitate()


nume de fișier = „stat_universitar.pkl”

universitate = SaveManager.load_state(nume fișier)

în timp ce este adevărat:
print("\nMeniu:")
print("1. Operațiuni ale Facultății")
print("2. Operatii generale")
print("3. Ieșire")

choice = input("Introduceți alegerea dvs.: ")

dacă alegere == "1":
print("\nOperațiunile Facultății:")
print("1. Creați și atribuiți un student unei facultăți")
print("2. Absolventa unui student de la o facultate")
print("3. Afișează studenții înscriși în prezent")
print("4. Afișați absolvenți")
print("5. Verificați dacă un student aparține unei facultăți")

faculty_choice = input("Introduceți alegerea dvs.: ")

if faculty_choice == "1":
faculty_name = input("Introduceți numele facultății: ")
faculty_field = input("Introduceți câmpul facultății: ")
student_name = input("Introduceți numele studentului: ")
student_id = input("Introduceți identificatorul unic al studentului: ")
student_email = input("Introduceți adresa de e-mail a studentului: ")

student = Student (student_name, student_id, student_email)
university.create_faculty(faculty_name, faculty_field)
facultate = university.facultities[-1]
faculty.assign_student(student)
print("Student repartizat la facultate.")

elif faculty_choice == „2”:
student_id = input("Introduceți identificatorul unic al studentului: ")
faculty_name = input("Introduceți numele facultății: ")

facultate = university.search_faculty(student_id)

dacă facultate și faculty.name == faculty_name:
pentru student în facultate.studenti:
if student.unique_identifier == student_id:
student.graduate() > Denis: faculty.graduate_student(student)
print("Student a absolvit facultatea.")
pauză
altceva:
print("Studentul nu a fost găsit la facultatea specificată.")
altceva:
print("Studentul nu a fost găsit sau nu este repartizat la facultatea specificată.")

elif faculty_choice == „3”:
faculty_name = input("Introduceți numele facultății: ")

pentru facultatea din universitate.facultăți:
if faculty.name == faculty_name:
enrolled_students = faculty.enrolled_students()
daca elevi_inscrisi:
print("Studenti inscrisi:")
pentru student în enrolled_students:
print(f"- {student.nume}")
altceva:
print("Niciun student înscris la facultatea specificată.")
pauză
altceva:
print("Facultatea nu a fost găsită.")

elif faculty_choice == „4”:
faculty_name = input("Introduceți numele facultății: ")

pentru facultatea din universitate.facultăți:
if faculty.name == faculty_name:
absolventi = faculty.graduates()
dacă absolvenți:
print("Absolvenți:")
pentru studenții absolvenți:
print(f"- {student.nume}")
altceva:
print("Nu există absolvenți în facultatea specificată.")
pauză
altceva:
print("Facultatea nu a fost găsită.")

elif faculty_choice == „5”:
student_id = input("Introduceți identificatorul unic al studentului: ")
faculty_name = input("Introduceți numele facultății: ")

facultate = university.search_faculty(student_id)

dacă facultate și faculty.name == faculty_name:
print(f"Studentul aparține facultății {faculty.name}.")
altceva:
print("Studentul nu a fost găsit sau nu este repartizat la facultatea specificată.")

elif choice == "2":
print("\nOperațiuni generale:")
print("1. Creați o nouă facultate")
print("2. Căutați la ce facultate aparține un student")
print("3. Afișează facultățile universitare")
print("4. Afișează toate facultățile aparținând unui domeniu")

general_choice = input("Introduceți alegerea dvs.: ")

dacă alegere_generală == „1”:
faculty_name = input("Introduceți numele facultății: ")
faculty_field = input("Introduceți câmpul facultății: ")
university.create_faculty(faculty_name, faculty_field)
print("Facultatea creată.")

elif alegere_generală == „2”:
student_id = input("Introduceți identificatorul unic al studentului: ")
facultate = university.search_faculty(student_id)
daca facultate:
print(f"Studentul aparține facultății {faculty.name}.")
altceva:
print("Studentul nu a fost găsit sau nu este repartizat la nicio facultate.")

elif alegere_generală == „3”:
print("Facultăți universitare:")
print(university.display_all_faculties())

elif alegere_generală == „4”:
câmp = input("Introduceți câmp: ")
facultati = university.display_faculties_by_field(field)
daca facultati:
print(f"Facultăți aparținând {domeniului}:")
print(facultati)
altceva:
print("Nu au fost găsite facultăți pentru acest domeniu.")

elif choice == "3":
SaveManager.save_state(universitate, nume de fișier)
print("Se iese din program.")
pauză

altceva:
print("Alegere nevalidă. Vă rugăm să introduceți o opțiune validă.")

