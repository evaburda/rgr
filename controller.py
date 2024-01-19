import time
from model import Model
from view import View


class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View()

    def run(self):
        while True:
            choice = self.view.show_menu()

            if choice == '7':
                break
            if choice == '6':
                self.process_search_option()
            elif choice in ['1', '2', '3', '4', '5']:
                self.process_menu_choice(choice)
            else:
                self.view.show_message("Wrong choice. Try again.")

    def process_menu_choice(self, choice):
        while True:
            table = self.view.show_tables()

            if table == '6':
                break

            if choice == '1':
                self.process_add_option(table)
            elif choice == '2':
                self.process_add_random_option(table)
            elif choice == '3':
                self.process_view_option(table)
            elif choice == '4':
                self.process_update_option(table)
            elif choice == '5':
                self.process_delete_option(table)

    def process_add_option(self, table):
        if table == '1':
            self.view.show_message("\nAdding patient:")
            self.add_patient()
        elif table == '2':
            self.view.show_message("\nAdding medicine:")
            self.add_medicine()
        elif table == '3':
            self.view.show_message("\nAdding medical record:")
            self.add_medical_record()
        elif table == '4':
            self.view.show_message("\nAdding medical worker:")
            self.add_medical_worker()
        elif table == '5':
            self.view.show_message("\nAdding worker record:")
            self.add_worker_record()
        else:
            self.view.show_message("Wrong choice. Try again.")

    def process_add_random_option(self, table):
        if table == '1':
            self.view.show_message("\nAdding random patients:")
            self.add_random_fields()
        else:
            self.view.show_message("Wrong choice. Try again.")

    def process_view_option(self, table):
        if table == '1':
            self.view_patients()
        elif table == '2':
            self.view_medicines()
        elif table == '3':
            self.view_medical_records()
        elif table == '4':
            self.view_medical_workers()
        elif table == '5':
            self.view_workers_records()
        elif table == '6':
            self.view.show_menu()
        else:
            self.view.show_message("Wrong choice. Try again.")

    def process_update_option(self, table):
        if table == '1':
            self.view.show_message("\nUpdating patient:")
            self.update_patient()
        elif table == '2':
            self.view.show_message("\nUpdating medicine:")
            self.update_medicine()
        elif table == '3':
            self.view.show_message("\nUpdating medical record:")
            self.update_medical_record()
        elif table == '4':
            self.view.show_message("\nUpdating medical worker:")
            self.update_medical_worker()
        elif table == '5':
            self.view.show_message("\nUpdating worker record:")
            self.update_worker_record()
        else:
            self.view.show_message("Wrong choice. Try again.")

    def process_delete_option(self, table):
        if table == '1':
            self.view.show_message("\nDeleting patient:")
            self.delete_patient()
        elif table == '2':
            self.view.show_message("\nDeleting medicine:")
            self.delete_medicine()
        elif table == '3':
            self.view.show_message("\nDeleting medical record:")
            self.delete_medical_record()
        elif table == '4':
            self.view.show_message("\nDeleting medical worker:")
            self.delete_medical_worker()
        elif table == '5':
            self.view.show_message("\nDeleting worker record:")
            self.delete_worker_record()
        else:
            self.view.show_message("Wrong choice. Try again.")

    def process_search_option(self):
        option = self.view.show_search()

        if option == '1':
            start_time = time.time()
            self.show_patients_diagnosis()
            end_time = time.time()
            elapsed_time = (end_time - start_time) * 1000
            print(f"Час виконання: {elapsed_time:.2f} мс")
        elif option == '2':
            start_time = time.time()
            self.show_workers_patients()
            end_time = time.time()
            elapsed_time = (end_time - start_time) * 1000
            print(f"Час виконання: {elapsed_time:.2f} мс")
        elif option == '3':
            start_time = time.time()
            self.show_patients_with_headache()
            end_time = time.time()
            elapsed_time = (end_time - start_time) * 1000
            print(f"Час виконання: {elapsed_time:.2f} мс")
        else:
            self.view.show_menu()

    def add_patient(self):
        try:
            patient_id, name, birthday, address = self.view.get_patient_input()
            self.model.add_patient(patient_id, name, birthday, address)
            self.view.show_message("Patient added successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def add_medicine(self):
        try:
            medicine_id, patient_id, name, dosage = self.view.get_medicine_input()
            self.model.add_medicine(medicine_id, patient_id, name, dosage)
            self.view.show_message("Medicine added successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def add_medical_record(self):
        try:
            record_id, patient_id, date, symptoms, diagnosis = self.view.get_medical_record_input()
            self.model.add_medical_record(record_id, patient_id, date, symptoms, diagnosis)
            self.view.show_message("Medical record added successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def add_medical_worker(self):
        try:
            worker_id, name, speciality = self.view.get_medical_worker_input()
            self.model.add_medical_worker(worker_id, name, speciality)
            self.view.show_message("Medical worker added successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def add_worker_record(self):
        try:
            tab_id, worker_id, record_id = self.view.get_worker_record_input()
            self.model.add_worker_record(tab_id, worker_id, record_id)
            self.view.show_message("Worker record added successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def view_patients(self):
        try:
            patients = self.model.get_all_patients()
            self.view.show_patients(patients)
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def view_medicines(self):
        try:
            medicines = self.model.get_all_medicines()
            self.view.show_medicines(medicines)
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def view_medical_records(self):
        try:
            medical_records = self.model.get_all_medical_records()
            self.view.show_medical_records(medical_records)
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def view_medical_workers(self):
        try:
            medical_workers = self.model.get_all_medical_workers()
            self.view.show_medical_workers(medical_workers)
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def view_workers_records(self):
        try:
            workers_records = self.model.get_all_workers_records()
            self.view.show_workers_records(workers_records)
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def show_workers_patients(self):
        try:
            rows = self.model.get_workers_patients()
            self.view.show_workers_patients(rows)
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def show_patients_diagnosis(self):
        try:
            rows = self.model.get_patients_diagnosis()
            self.view.show_patients_diagnosis(rows)
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def show_patients_with_headache(self):
        try:
            rows = self.model.get_patients_with_headache()
            self.view.show_patients_with_headache(rows)
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def update_patient(self):
        try:
            patient_id = self.view.get_id()
            name, birthday, address = self.view.get_patient_input()
            self.model.update_patient(name, birthday, address, patient_id)
            self.view.show_message("Patient updated successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def update_medicine(self):
        try:
            medicine_id = self.view.get_id()
            patient_id, name, dosage = self.view.get_medicine_input()
            self.model.update_medicine( patient_id, name, dosage, medicine_id)
            self.view.show_message("Medicine updated successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def update_medical_record(self):
        try:
            record_id = self.view.get_id()
            patient_id, date, symptoms, diagnosis = self.view.get_medical_record_input()
            self.model.update_medical_record(patient_id, date, symptoms, diagnosis, record_id)
            self.view.show_message("Medical record updated successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def update_medical_worker(self):
        try:
            worker_id = self.view.get_id()
            name, speciality = self.view.get_medical_worker_input()
            self.model.update_medical_worker(name, speciality, worker_id)
            self.view.show_message("Medical worker updated successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def update_worker_record(self):
        try:
            tab_id = self.view.get_id()
            worker_id, record_id = self.view.get_worker_record_input()
            self.model.update_worker_record(worker_id, record_id, tab_id)
            self.view.show_message("Worker record updated successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def delete_patient(self):
        try:
            patient_id = self.view.get_id()
            self.model.delete_patient(patient_id)
            self.view.show_message("Patient deleted successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def delete_medicine(self):
        try:
            medicine_id = self.view.get_id()
            self.model.delete_medicine(medicine_id)
            self.view.show_message("Medicine deleted successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def delete_medical_record(self):
        try:
            record_id = self.view.get_id()
            self.model.delete_medical_record(record_id)
            self.view.show_message("Medical record deleted successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def delete_medical_worker(self):
        try:
            worker_id = self.view.get_id()
            self.model.delete_medical_worker(worker_id)
            self.view.show_message("Medical worker deleted successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def delete_worker_record(self):
        try:
            tab_id = self.view.get_id()
            self.model.delete_worker_record(tab_id)
            self.view.show_message("Worker record deleted successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def add_random_fields(self):
        try:
            number = self.view.get_number()
            self.model.add_random_fields(number)
            self.view.show_message("Random fields added successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")