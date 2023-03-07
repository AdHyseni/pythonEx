class Individ:
    emer = ''
    mbiemer = ''

    def __init__(self,emer, mbiemer):
        self.emer = emer
        self.mbiemer = mbiemer

    def ecen(self):
        print('Une eci')

    def prezantohu(self):
        print(f'Une jame {self.emer} {self.mbiemer}')


individ_1 = Individ('emri_1','mbiemri_1')
individ_2 = Individ('emri_2','mbiemri_2')
individ_3 = Individ('emri_3','mbiemri_3')
individ_4 = Individ('emri_4','mbiemri_4')
individ_5 = Individ('emri_5','mbiemri_5')
individ_1.prezantohu()
individ_2.prezantohu()
individ_3.prezantohu()
individ_4.prezantohu()
individ_5.prezantohu()


class Student(Individ):
    shkolla = ''
    def __init__(self, emer, mbiemer,shkolla):
        super().__init__(emer, mbiemer)
        self.shkolla = shkolla
    
    def _shkolla(self):
        print(f'Une studioj ne shkollen {self.shkolla}')

stud_1 = Student('individ_6', 'mbiemer_6','shkolla_1')
stud_1._shkolla()
stud_1.prezantohu()