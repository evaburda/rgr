import psycopg2


class Model:
    def __init__(self):
        self.conn = psycopg2.connect(
            dbname='patients',
            user='postgres',
            password='1111',
            host='localhost',
            port=3000
        )

    def add_patient(self, patient_id, name, birthday, address):
        c = self.conn.cursor()
        c.execute('INSERT INTO "Patients" ("Patient_ID", "Name", "Birthday", "Address") VALUES (%s, %s, %s, %s)', (patient_id, name, birthday, address))
        self.conn.commit()

    def add_medicine(self, medicine_id, patient_id, name, dosage):
        c = self.conn.cursor()
        c.execute('INSERT INTO "Medicine" ("Medicine_ID", "Patient_ID", "Name", "Dosage") VALUES (%s, %s, %s, %s)', (medicine_id, patient_id, name, dosage))
        self.conn.commit()

    def add_medical_record(self, record_id, patient_id, date, symptoms, diagnosis):
        c = self.conn.cursor()
        c.execute('INSERT INTO "Medical_Record" ("Record_ID", "Patient_ID", "Date", "Symptoms", "Diagnosis") VALUES (%s, %s, %s, %s, %s)', (record_id, patient_id, date, symptoms, diagnosis))
        self.conn.commit()

    def add_medical_worker(self, worker_id, name, speciality):
        c = self.conn.cursor()
        c.execute('INSERT INTO "Medical_Worker" ("Worker_ID", "Name", "Speciality") VALUES (%s, %s, %s)', (worker_id, name, speciality))
        self.conn.commit()

    def add_worker_record(self, tab_id, worker_id, record_id):
        c = self.conn.cursor()
        c.execute('INSERT INTO "Worker_Record" ("Tab_ID", "Worker_ID", "Record_ID") VALUES (%s, %s, %s)', (tab_id, worker_id, record_id))
        self.conn.commit()

    def get_all_patients(self):
        c = self.conn.cursor()
        c.execute('SELECT * FROM "Patient"')
        return c.fetchall()

    def get_all_medicines(self):
        c = self.conn.cursor()
        c.execute('SELECT * FROM "Medicine"')
        return c.fetchall()

    def get_all_medical_records(self):
        c = self.conn.cursor()
        c.execute('SELECT * FROM "Medical_Record"')
        return c.fetchall()

    def get_all_medical_workers(self):
        c = self.conn.cursor()
        c.execute('SELECT * FROM "Medical_Worker"')
        return c.fetchall()

    def get_all_workers_records(self):
        c = self.conn.cursor()
        c.execute('SELECT * FROM "Worker_Record"')
        return c.fetchall()

    def update_patient(self, name, birthday, address, id):
        c = self.conn.cursor()
        c.execute('UPDATE "Patient" SET "Name"=%s, "Birthday"=%s, "Address"=%s WHERE "Patient_ID"=%s', (name, birthday, address, id))
        self.conn.commit()

    def update_medicine(self, patient_id, name, dosage, id):
        c = self.conn.cursor()
        c.execute('UPDATE "Medicine" SET "Patient_ID"=%s, "Name"=%s, "Dosage"=%s WHERE "Medicine_ID"=%s', (patient_id, name, dosage, id))
        self.conn.commit()

    def update_medical_record(self, patient_id, date, symptoms, diagnosis, id):
        c = self.conn.cursor()
        c.execute('UPDATE "Medical_Record" SET "Patient_ID"=%s, "Date"=%s, "Symptoms"=%s, "Diagnosis"=%s WHERE "Record_ID"=%s', (patient_id, date, symptoms, diagnosis, id))
        self.conn.commit()

    def update_medical_worker(self, name, speciality, id):
        c = self.conn.cursor()
        c.execute('UPDATE "Medical_Worker" SET "Name"=%s, "Speciality"=%s WHERE "Worker_ID"=%s', (name, speciality, id))
        self.conn.commit()

    def update_worker_record(self, worker_id, record_id, id):
        c = self.conn.cursor()
        c.execute('UPDATE "Worker_Record" SET "Worker_ID"=%s, "Record_ID"=%s WHERE "Tab_ID"=%s', (worker_id, record_id, id))
        self.conn.commit()

    def delete_patient(self, patient_id):
        c = self.conn.cursor()
        c.execute('DELETE FROM "Patient" WHERE "Patient_ID"=%s', (patient_id,))
        self.conn.commit()

    def delete_medicine(self, medicine_id):
        c = self.conn.cursor()
        c.execute('DELETE FROM "Medicine" WHERE "Medicine_ID"=%s', (medicine_id,))
        self.conn.commit()

    def delete_medical_record(self, record_id):
        c = self.conn.cursor()
        c.execute('DELETE FROM "Medical_Record" WHERE "Record_ID"=%s', (record_id,))
        self.conn.commit()

    def delete_medical_worker(self, worker_id):
        c = self.conn.cursor()
        c.execute('DELETE FROM "Medical_Worker" WHERE "Worker_ID"=%s', (worker_id,))
        self.conn.commit()

    def delete_worker_record(self, tab_id):
        c = self.conn.cursor()
        c.execute('DELETE FROM "Worker_Record" WHERE "Tab_ID"=%s', (tab_id,))
        self.conn.commit()

    def get_patients_diagnosis(self):
         c = self.conn.cursor()
         c.execute('SELECT "Patient"."Name", "Medical_Record"."Diagnosis" FROM "Patient" JOIN "Medical_Record" ON "Patient"."Patient_ID" = "Medical_Record"."Patient_ID";')
         return c.fetchall()

    def get_workers_patients(self):
        c = self.conn.cursor()
        c.execute(
            'SELECT "Medical_Worker"."Name", COUNT("Patient"."Patient_ID") AS "Patient_Count" FROM "Medical_Worker" LEFT JOIN "Worker_Record" ON "Medical_Worker"."Worker_ID" = "Worker_Record"."Worker_ID" LEFT JOIN "Medical_Record" ON "Worker_Record"."Record_ID" = "Medical_Record"."Record_ID" LEFT JOIN "Patient" ON "Medical_Record"."Patient_ID" = "Patient"."Patient_ID"GROUP BY "Medical_Worker"."Name";')
        return c.fetchall()

    def get_patients_with_headache(self):
        c = self.conn.cursor()
        c.execute(
            '''SELECT "Medical_Worker"."Name", "Patient"."Address" FROM "Medical_Worker" JOIN "Worker_Record" ON "Medical_Worker"."Worker_ID" = "Worker_Record"."Worker_ID" JOIN "Medical_Record" ON "Worker_Record"."Record_ID" = "Medical_Record"."Record_ID" JOIN "Patient" ON "Medical_Record"."Patient_ID" = "Patient"."Patient_ID" WHERE "Medical_Record"."Symptoms" = 'headache';''')
        return c.fetchall()

    def add_random_fields(self, number):
        c = self.conn.cursor()
        c.execute('''
        WITH max_id AS (SELECT COALESCE(MAX("Patient_ID"), 0) FROM public."Patient")
        INSERT INTO public."Patient" ("Patient_ID", "Name", "Birthday", "Address")
        SELECT (SELECT * FROM max_id) + row_number() OVER () as "Patient_id",
            chr(trunc(65 + random() * 25)::int) || chr(trunc(65 + random() * 25)::int),
            current_date + (random() * 30)::integer * '1 day'::interval,
            chr(trunc(65 + random() * 25)::int) || chr(trunc(65 + random() * 25)::int)
        FROM generate_series(1, %s);
    ''',(number,))
        self.conn.commit()


