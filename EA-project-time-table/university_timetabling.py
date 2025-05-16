# import libraries
import pygame
import pandas as pd
from PIL import Image, ImageTk
import cv2
import threading
import numpy as np
import matplotlib.pyplot as plt
import random
import copy
import tkinter as tk
from tkinter import ttk, messagebox
import time
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import os
import tempfile
import subprocess
##################################################################################################################################################
# variables
############
video_path1 = r"E:\prijects\tenor.gif"
music_path1 = r"E:\prijects\Unwind(MP3_160K).mp3"
students_list = []
df = pd.read_csv(r"E:\prijects\students.csv")
for i in df.index:
    students_list.append( df.loc[i]["Student Name"])
y = 1
NUM_DAYS = 5
NUM_HOURS = 10
random_seed = int(input("please enter the random seed : "))
Doctors_dataset = [
    "Dr. Elena Morales",
    "Dr. Raj Patel",
    "Dr. Sofia Ivanova",
    "Dr. Kwame Adebayo",
    "Dr. Mei Chen}",
    "Dr. Luca Ferrari",
    "Dr. Amina Al-Farsi",
    "Dr. Hiroshi Tanaka",
    "Dr. Nadia Petrov",
    "Dr. Carlos Silva",
    "Dr. Anika Varma",
    "Dr. Youssef Khalid",
    "Dr. Ingrid Bergman",
    "Dr. Javier Ruiz",
    "Dr. Leila Nguyen",
    "Dr. Viktor Novak",
    "Dr. Zara Cohen",
    "Dr. Kenji Nakamura",
    "Dr. Amara Singh",
    "Dr. Matteo Ricci",
    "Dr. Fatima Zahra",
    "Dr. Nikolai Volkov",
    "Dr. Priya Deshpande",
    "Dr. Elias Schmidt",
    "Dr. Yara Hussein",
    "Dr. Marco De Luca",
    "Dr. Anya Kowalski",
    "Dr. Ravi Shankar",
    "Dr. Lina Costa",
    "Dr. Idris Bello",
    "Dr. Clara Moulin",
    "Dr. Omar Farooq",
    "Dr. Saskia Van Dijk",
    "Dr. Arjun Kapoor",
    "Dr. Esra Demir",
    "Dr. Nathan Brooks",
    "Dr. Amirah Hassan",
    "Dr. Pavel Horák",
    "Dr. Linh Tran",
    "Dr. Björn Eriksson",
    "Dr. Catalina Mendez",
    "Dr. Kofi Mensah",
    "Dr. Elin Johansson",
    "Dr. Dante Russo",
    "Dr. Nia Okeke",
    "Dr. Viktor Petrov",
    "Dr. Mariam Abdallah",
    "Dr. Emre Yilmaz",
    "Dr. Parvati Devi",
    "Dr. Alejandro Cruz"
]
courses_dataset = [
    "Python Syntax and Basic Programming",
    "Object-Oriented Programming (OOP) in Python",
    "Functional Programming with Python",
    "Error Handling and Debugging",
    "Python Memory Management",
    "Multithreading and Multiprocessing",
    "Python Generators and Iterators",
    "File Handling and I/O Operations",
    "Regular Expressions in Python",
    "Python Decorators and Context Managers",
    "Arrays, Lists, and Tuples",
    "Linked Lists and Trees in Python",
    "Stacks, Queues, and Deques",
    "Hash Tables and Dictionaries",
    "Graphs and Graph Algorithms (BFS/DFS)",
    "Sorting and Searching Algorithms",
    "Dynamic Programming in Python",
    "Greedy Algorithms and Optimization",
    "Recursion and Backtracking",
    "Big O Notation and Complexity Analysis",
    "Introduction to Machine Learning with Scikit-learn",
    "Supervised Learning (Regression, Classification)",
    "Unsupervised Learning (Clustering, PCA)",
    "Linear and Logistic Regression from Scratch",
    "Decision Trees and Random Forests",
    "Support Vector Machines (SVM)",
    "K-Nearest Neighbors (KNN)",
    "Ensemble Methods (Bagging, Boosting)",
    "Model Evaluation (Accuracy, Precision, ROC-AUC)",
    "Hyperparameter Tuning (Grid Search, Random Search)",
    "Introduction to TensorFlow and Keras",
    "Feedforward Neural Networks",
    "Convolutional Neural Networks (CNNs)",
    "Recurrent Neural Networks (RNNs)",
    "Long Short-Term Memory (LSTM) Networks",
    "Transfer Learning with Pre-trained Models",
    "Autoencoders and Generative Models",
    "Reinforcement Learning Basics (Q-Learning)",
    "Natural Language Processing (NLP) with Transformers",
    "PyTorch Fundamentals",
    "Data Cleaning with Pandas",
    "Exploratory Data Analysis (EDA)",
    "Data Visualization with Matplotlib/Seaborn",
    "Statistical Analysis with SciPy",
    "Time Series Analysis (ARIMA, Prophet)",
    "Feature Engineering and Selection",
    "Handling Missing Data",
    "Dimensionality Reduction (t-SNE, UMAP)",
    "Working with SQL Databases (SQLite, PostgreSQL)",
    "Big Data Tools (PySpark, Dask)",
    "Text Preprocessing (Tokenization, Stemming)",
    "Sentiment Analysis with NLTK",
    "Named Entity Recognition (NER)",
    "Topic Modeling (LDA, LSA)",
    "Word Embeddings (Word2Vec, GloVe)",
    "BERT and Transformer Models",
    "Text Summarization",
    "Chatbot Development with Rasa",
    "Speech Recognition (Speech-to-Text)",
    "Language Translation with Seq2Seq Models",
    "Image Processing with OpenCV",
    "Edge Detection and Filters",
    "Object Detection (YOLO, Faster R-CNN)",
    "Image Segmentation (Mask R-CNN)",
    "Facial Recognition Systems",
    "Optical Character Recognition (OCR)",
    "Video Analysis with FFmpeg",
    "Generative Adversarial Networks (GANs)",
    "Image Captioning",
    "Augmented Reality (AR) with Python",
    "Bayesian Networks and Probabilistic Models",
    "Monte Carlo Methods",
    "Evolutionary Algorithms (Genetic Algorithms)",
    "Swarm Intelligence (Particle Swarm Optimization)",
    "Explainable AI (XAI)",
    "Federated Learning",
    "Quantum Machine Learning",
    "AI for Game Playing (AlphaZero, Minimax)",
    "Meta-Learning and Few-Shot Learning",
    "AI Ethics and Bias Mitigation",
    "Building REST APIs with Flask/Django",
    "Web Scraping with Beautiful Soup and Scrapy",
    "GUI Development (Tkinter, PyQt)",
    "Unit Testing with PyTest",
    "Version Control (Git/GitHub)",
    "Software Design Patterns",
    "Microservices Architecture",
    "DevOps for Python (CI/CD Pipelines)",
    "Packaging and Distributing Python Libraries",
    "Database Design with SQLAlchemy",
    "Robot Simulation with PyBullet",
    "Path Planning Algorithms (A*, Dijkstra)",
    "Control Systems (PID Controllers)",
    "ROS (Robot Operating System) Basics",
    "IoT Automation with Raspberry Pi",
    "Autonomous Drone Programming",
    "Sensor Data Processing",
    "Swarm Robotics",
    "Computer Vision for Robotics",
    "Reinforcement Learning for Robotics",
    "Bioinformatics with Biopython",
    "Financial Modeling and Algorithmic Trading",
    "Healthcare AI (Medical Image Analysis)",
    "Recommendation Systems",
    "Fraud Detection Systems",
    "Climate Modeling with Python",
    "Social Network Analysis",
    "Music Generation with AI",
    "Sports Analytics",
    "Blockchain Development (Smart Contracts)",
    "Dockerizing Python Applications",
    "Cloud Deployment (AWS, Azure, GCP)",
    "Serverless Computing (AWS Lambda)",
    "Model Serving with TensorFlow Serving",
    "Real-Time Inference with FastAPI",
    "Distributed Computing with Celery",
    "Load Testing and Optimization",
    "MLOps (Machine Learning Operations)",
    "Monitoring AI Models in Production",
    "Edge AI (Deploying Models on Devices)",
    "Linear Algebra for Machine Learning",
    "Calculus for Gradient Descent",
    "Probability and Statistics",
    "Discrete Mathematics",
    "Numerical Methods in Python",
    "Optimization Techniques (Gradient Descent)",
    "Graph Theory Applications",
    "Cryptography Basics",
    "Game Theory",
    "Information Theory",
    "AI for Metaverse Development",
    "Low-Code AI Platforms",
    "TinyML (Machine Learning on Microcontrollers)",
    "AI-Driven Cybersecurity",
    "Neural Architecture Search (NAS)",
    "AI in Agriculture",
    "AI for Disaster Response",
    "Synthetic Data Generation",
    "AI in Space Exploration",
    "Ethical Hacking with Python",
    "Building a Self-Driving Car Simulator",
    "COVID-19 Data Analysis and Prediction",
    "Fake News Detection System",
    "Stock Price Prediction with LSTM",
    "Handwritten Digit Recognition (MNIST)",
    "Real-Time Emotion Detection",
    "AI-Powered Chess Engine",
    "Voice Assistant (Like Siri/Alexa)",
    "Predictive Maintenance for IoT Devices",
    "Personalized Learning Recommendation System"
] #150
list_course = []
NUM_LECTURE_HALLS = 10
NUM_LAB_ROOMS = 5
while y == 1 :
                NUM_COURSES = int(input("Enter the number of COURSES (MAX "+str(NUM_HOURS * NUM_DAYS * 2)+") : "))
                if NUM_COURSES < 0 or NUM_COURSES is None :
                    print("Invalid Input")
                    continue
                elif NUM_COURSES > (NUM_HOURS * NUM_DAYS * 2)  :
                    print("too much for the course")
                    continue
                else:
                    NUM_LECTURERS = int(input("Enter the number of LECTURES (Max "+str(int(NUM_COURSES / 2))+") : "))
                    if NUM_LECTURERS < 0 or NUM_LECTURERS is None :
                        print("Invalid Input")
                        continue
                    elif NUM_LECTURERS > len(Doctors_dataset)    :
                        print("too much for the course")
                        continue
                    else:
                        NUM_STUDENTS = int(input("Enter the number of STUDENTS (MAX 10000) : "))
                        if NUM_STUDENTS  < 0 or NUM_STUDENTS > 10000 or NUM_STUDENTS is None:
                            print("Invalid Input")
                            continue
                        else:
                            POPULATION_SIZE = int(input("Enter the population size : "))
                            if POPULATION_SIZE < 0 or POPULATION_SIZE is None:
                                print("Invalid Input")
                                continue
                            elif POPULATION_SIZE > 1000:
                                print("too much for the population size")
                                continue
                            else:
                                MAX_ITERATIONS = int(input("Enter the number of iterations : "))
                                if MAX_ITERATIONS < 0 or MAX_ITERATIONS is None:
                                    print("Invalid Input")
                                    continue
                                else:
                                    break
MAX_SECTIONS_PER_COURSE = 3
W_MAX = 0.9
W_MIN = 0.4

C1 = 1.49
C2 = 1.49
CROSSOVER_RATE = 0.8
MUTATION_RATE = 0.2
TOURNAMENT_SIZE = 3
random.seed(random_seed)
#################################################################################################################################################################################################################################
# ROOM
############
class Room:
    def __init__(self, id, capacity, room_type, has_projector=False, has_computers=False):
        self.id = id
        self.capacity = capacity
        self.room_type = room_type
        self.has_projector = has_projector
        self.has_computers = has_computers

    def __str__(self):
        return f"Room {self.id} ({self.room_type.capitalize()}, Cap: {self.capacity})"
#################################################################################################################################################################################################################################
# Course
############
class Course:
    def __init__(self, id, name, lecturer_id, student_ids, duration=1, requires_projector=False, requires_computers=False, min_capacity=0, has_lab=False, num_sections=1):
        self.id = id
        self.name = courses_dataset[random.randint(0, len(courses_dataset) - 1)]
        courses_dataset.remove(self.name)
        list_course.append(self.name)
        self.lecturer_id = lecturer_id
        self.student_ids = student_ids
        self.duration = duration
        self.requires_projector = requires_projector
        self.requires_computers = requires_computers
        self.min_capacity = min_capacity
        self.has_lab = has_lab
        self.num_sections = min(num_sections, MAX_SECTIONS_PER_COURSE)

    def __str__(self):
        return f"{self.name} (ID: {self.id}, Sections: {self.num_sections}{', with lab' if self.has_lab else ''})"
#################################################################################################################################################################################################################################
# Lecturer
############
class Lecturer:
    def __init__(self, id, name, availability=None, courses=None):
        self.id = id
        self.name = Doctors_dataset[random.randint(0, len(Doctors_dataset)-1)]
        Doctors_dataset.remove(self.name)
        self.courses = courses if courses is not None else []
        self.courses_name = courses if courses is not None else []
        if availability is None:
            self.availability = np.ones((NUM_DAYS, NUM_HOURS), dtype=bool)
        else:
            self.availability = availability

        i = random.randint(1, 3)
        while i > 0:
            if len(list_course) == 0:
                break
            else:
                course_name = list_course[random.randint(0,(len(list_course)-1))]
                self.courses_name.append(course_name)
                list_course.remove(course_name)
                i -= 1

    def assign_course(self, course_id):
        if course_id not in self.courses:
            self.courses.append(course_id)

    def remove_course(self, course_id):
        if course_id in self.courses:
            self.courses.remove(course_id)

    def __str__(self):
        courses_str = " || ".join(map(str, self.courses_name))
        return f"Lecturer {self.name} (ID: {self.id}, Courses: [{courses_str}])"
#################################################################################################################################################################################################################################
# Student
############
class Student:
    def __init__(self, id, name=None):
        self.id = id
        self.name = students_list[random.randint(0, len(students_list) - 1)]
        students_list.remove(self.name)
        self.courses = []  # List of course IDs the student is enrolled in

    def __str__(self):
        return f"{self.name} (ID: {self.id})"
#################################################################################################################################################################################################################################
# Time
############
class TimeSlot:
    def __init__(self, day, hour):
        self.day = day
        self.hour = hour

    def __str__(self):
        days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"]
        return f"{days[self.day]} at {self.hour + 8}:00"

    def __eq__(self, other):
        if not isinstance(other, TimeSlot):
            return False
        return self.day == other.day and self.hour == other.hour
#################################################################################################################################################################################################################################
# Course Assignment
############
class CourseAssignment:
    def __init__(self, course_id, section_id, room_id, time_slot, is_lab=False):
        self.course_id = course_id
        self.section_id = section_id
        self.room_id = room_id
        self.time_slot = time_slot
        self.is_lab = is_lab

    def __str__(self):
        session_type = "Lab" if self.is_lab else "Lecture"
        return f"Course {self.course_id}-{self.section_id} ({session_type}) in Room {self.room_id} at {self.time_slot}"
#################################################################################################################################################################################################################################
# Time Table
############
class Timetable:
    def __init__(self, assignments=None):
        self.assignments = assignments if assignments else []
        self.fitness = 0
        self.violations = {}

    def add_assignment(self, assignment):
        self.assignments.append(assignment)

    def get_course_assignments(self, course_id, section_id=None):
        if section_id is not None:
            return [a for a in self.assignments if a.course_id == course_id and a.section_id == section_id]
        return [a for a in self.assignments if a.course_id == course_id]

    def __str__(self):
        result = "Timetable:\n"
        for assignment in sorted(self.assignments, key=lambda x: (x.time_slot.day, x.time_slot.hour)):
            result += f"  {assignment}\n"
        return result
#################################################################################################################################################################################################################################
# Particle
############
class Particle:
    def __init__(self, position=None, velocity=None):
        self.position = position if position else Timetable()
        self.velocity = velocity if velocity else []
        self.best_position = copy.deepcopy(self.position)
        self.best_fitness = float('-inf')

    def update_personal_best(self):
        if self.position.fitness > self.best_fitness:
            self.best_position = copy.deepcopy(self.position)
            self.best_fitness = self.position.fitness
#################################################################################################################################################################################################################################
# University Timetabling Problem
############
class UniversityTimetablingProblem:
    def __init__(self):
        self.rooms = self.generate_rooms()
        self.lecturers = self.generate_lecturers()
        self.courses = self.generate_courses()  # Generate courses
        self.students = self.generate_students()  # Then generate student if needed
        self.global_best_position = None
        self.global_best_fitness = float('-inf')
        self.avg_fitness_history = []
        self.best_fitness_history = []
        self.violation_history = []

    def generate_rooms(self):
        rooms = []
        for i in range(NUM_LECTURE_HALLS):
            capacity = random.randint(30, 120)
            has_projector = random.random() > 0.1
            has_computers = random.random() > 0.8
            rooms.append(Room(i, capacity, "lecture", has_projector, has_computers))

        for i in range(NUM_LECTURE_HALLS, NUM_LECTURE_HALLS + NUM_LAB_ROOMS):
            capacity = random.randint(15, 30)
            has_projector = random.random() > 0.5
            has_computers = True
            rooms.append(Room(i, capacity, "lab", has_projector, has_computers))
        return rooms

    def generate_lecturers(self):
        lecturers = []
        for i in range(NUM_LECTURERS):
            availability = np.ones((NUM_DAYS, NUM_HOURS), dtype=bool)
            for d in range(NUM_DAYS):
                for h in range(NUM_HOURS):
                    if random.random() < 0.1:
                        availability[d, h] = False
            lecturers.append(Lecturer(i, f"Prof. {i}", availability))
        return lecturers

    def generate_students(self):
        """Generate student data without relying on CSV files."""
        students = []
        print("Creating sample students.")
        start_id = 2022000
        for i in range(NUM_STUDENTS):
            student_id = start_id + i
            student_name = f"Student {student_id}"
            student = Student(student_id, student_name)
            students.append(student)
            num_courses = random.randint(3, 6)
            available_courses = list(range(NUM_COURSES))
            random.shuffle(available_courses)
            student.courses = available_courses[:num_courses]
            for course_id in student.courses:
                self.courses[course_id].student_ids.append(student.id)
        print("\nStudent Enrollment Summary:")
        print(f"Total students: {len(students)}")
        print(f"Total courses: {NUM_COURSES}")
        print("\nSample Student Enrollments (first 5 students):")
        for student in students[:5]:
            course_names = [self.courses[c_id].name[:20] + "..." for c_id in student.courses[:3]]
            print(f"Student {student.id} ({student.name}): {len(student.courses)} courses")
            print(f"  Sample courses: {', '.join(course_names)}")
            if len(student.courses) > 3:
                print(f"  (+ {len(student.courses) - 3} more courses)")
        print("\nCourse Enrollment Counts:")
        for course in self.courses[:10]:  # Print first 10 courses
            print(f"{course.name[:20]}...: {len(course.student_ids)} students")
        if NUM_COURSES > 10:
            print(f"(Showing first 10 of {NUM_COURSES} courses)")

        return students

    def generate_courses(self):
        courses = []
        for i in range(NUM_COURSES):
            lecturer_id = random.randint(0, NUM_LECTURERS - 1)
            student_ids = []

            duration = random.choice([1, 2])
            requires_projector = random.random() > 0.5
            requires_computers = random.random() > 0.7
            has_lab = random.random() < 0.3
            num_sections = random.randint(1, MAX_SECTIONS_PER_COURSE)
            course_name = f"Course-{i}"
            courses.append(Course(
                i, course_name, lecturer_id, student_ids,
                duration, requires_projector, requires_computers,
                0, has_lab, num_sections  # min_capacity set to 0 initially
            ))
        return courses

    def evaluate_timetable(self, timetable):
        violations = {
            'room_conflict': 0,
            'lecturer_conflict': 0,
            'student_conflict': 0,
            'room_capacity': 0,
            'equipment_mismatch': 0,
            'lecturer_unavailable': 0,
            'room_type_mismatch': 0,
            'missing_lab_sessions': 0,
            'missing_lecture_sessions': 0
        }
        if not timetable.assignments:
            for course in self.courses:
                for section in range(course.num_sections):
                    violations['missing_lecture_sessions'] += 1
                    if course.has_lab:
                        violations['missing_lab_sessions'] += 1
            penalties = {
                'room_conflict': 100,
                'lecturer_conflict': 100,
                'student_conflict': 0.1,
                'room_capacity': 50,
                'equipment_mismatch': 30,
                'lecturer_unavailable': 70,
                'room_type_mismatch': 80,
                'missing_lab_sessions': 60,
                'missing_lecture_sessions': 150
            }
            total_penalty = sum(violations[v] * penalties[v] for v in violations)
            fitness = 10000 - total_penalty
            timetable.fitness = fitness
            timetable.violations = violations
            return fitness, violations

        course_sections = {}
        for course in self.courses:
            for section in range(course.num_sections):
                course_sections[(course.id, section)] = {'lecture': False, 'lab': False}
        for i, a1 in enumerate(timetable.assignments):
            course1 = self.courses[a1.course_id]
            room1 = self.rooms[a1.room_id]
            if a1.is_lab:
                course_sections[(a1.course_id, a1.section_id)]['lab'] = True
            else:
                course_sections[(a1.course_id, a1.section_id)]['lecture'] = True
            if a1.is_lab and room1.room_type != "lab":
                violations['room_type_mismatch'] += 1
            elif not a1.is_lab and room1.room_type != "lecture":
                violations['room_type_mismatch'] += 1
            if room1.capacity < course1.min_capacity:
                over_capacity = len(course1.student_ids) - room1.capacity
                violations['room_capacity'] += over_capacity
            if course1.requires_projector and not room1.has_projector:
                violations['equipment_mismatch'] += 1
            if course1.requires_computers and not room1.has_computers:
                violations['equipment_mismatch'] += 1
            lecturer = self.lecturers[course1.lecturer_id]
            if not lecturer.availability[a1.time_slot.day, a1.time_slot.hour]:
                violations['lecturer_unavailable'] += 1
            for j, a2 in enumerate(timetable.assignments):
                if i != j and a1.time_slot.day == a2.time_slot.day and a1.time_slot.hour == a2.time_slot.hour:
                    course2 = self.courses[a2.course_id]
                    if a1.room_id == a2.room_id:
                        violations['room_conflict'] += 1
                    if course1.lecturer_id == course2.lecturer_id:
                        violations['lecturer_conflict'] += 1
                    overlapping_students = set(course1.student_ids) & set(course2.student_ids)
                    if overlapping_students:
                        violations['student_conflict'] += len(overlapping_students)
        for (course_id, section), scheduled in course_sections.items():
            course = self.courses[course_id]
            if course.has_lab and not scheduled['lab']:
                violations['missing_lab_sessions'] += 1
            if not scheduled['lecture']:
                violations['missing_lecture_sessions'] += 1
        penalties = {
            'room_conflict': 100,
            'lecturer_conflict': 100,
            'student_conflict': 0.1,
            'room_capacity': 50,
            'equipment_mismatch': 30,
            'lecturer_unavailable': 70,
            'room_type_mismatch': 80,
            'missing_lab_sessions': 60,
            'missing_lecture_sessions': 150
        }
        total_penalty = sum(violations[v] * penalties[v] for v in violations)
        fitness = 10000 - total_penalty
        timetable.fitness = fitness
        timetable.violations = violations

        return fitness, violations


    def generate_random_timetable(self):
        timetable = Timetable()
        for course in self.courses:
            for section in range(course.num_sections):
                self.assign_random_session(timetable, course, section, is_lab=False)
                if course.has_lab:
                    self.assign_random_session(timetable, course, section, is_lab=True)
        self.evaluate_timetable(timetable)
        return timetable

    def assign_random_session(self, timetable, course, section, is_lab):
        suitable_rooms = [r for r in self.rooms if (r.room_type == "lab" if is_lab else r.room_type == "lecture")]
        if not suitable_rooms:
            return
        room_id = random.choice(suitable_rooms).id
        day = random.randint(0, NUM_DAYS - 1)
        hour = random.randint(0, NUM_HOURS - 1)
        time_slot = TimeSlot(day, hour)
        assignment = CourseAssignment(course.id, section, room_id, time_slot, is_lab)
        timetable.add_assignment(assignment)

    def initialize_pso(self, num_particles):
        particles = []
        for _ in range(num_particles):
            timetable = self.generate_random_timetable()
            particle = Particle(position=timetable)
            particle.best_position = copy.deepcopy(timetable)
            particle.best_fitness = timetable.fitness
            if timetable.fitness > self.global_best_fitness:
                self.global_best_position = copy.deepcopy(timetable)
                self.global_best_fitness = timetable.fitness
            particles.append(particle)
        return particles
    def get_timetable_difference(self, timetable1, timetable2):
        differences = []
        for i, assignment1 in enumerate(timetable1.assignments):
            assignment2 = timetable2.assignments[i]
            if (assignment1.room_id != assignment2.room_id or
                    assignment1.time_slot.day != assignment2.time_slot.day or
                    assignment1.time_slot.hour != assignment2.time_slot.hour):
                diff = (i, assignment2.room_id, assignment2.time_slot.day, assignment2.time_slot.hour)
                differences.append(diff)
        return differences

    def apply_velocity(self, timetable, velocity):
        new_timetable = copy.deepcopy(timetable)
        for course_idx, room_id, day, hour in velocity:
            if 0 <= course_idx < len(new_timetable.assignments):
                    if 0 <= room_id < len(self.rooms):
                        if 0 <= day < NUM_DAYS and 0 <= hour < NUM_HOURS:
                            new_time_slot = TimeSlot(day, hour)
                            new_timetable.assignments[course_idx] = CourseAssignment(new_timetable.assignments[course_idx].course_id,new_timetable.assignments[course_idx].section_id,room_id, new_time_slot,new_timetable.assignments[course_idx].is_lab)
        self.evaluate_timetable(new_timetable)
        return new_timetable

    def update_velocity(self, particle, w, c1, c2):
        inertia = particle.velocity
        cognitive = self.get_timetable_difference(particle.position, particle.best_position)
        social = self.get_timetable_difference(particle.position, self.global_best_position)
        if inertia:
            inertia_sample_size = min(len(inertia), max(0, int(len(inertia) * w)))
            inertia_sample = random.sample(inertia, inertia_sample_size) if inertia_sample_size > 0 else []
        else:
            inertia_sample = []
        if cognitive:
            cognitive_sample_size = min(len(cognitive), max(0, int(len(cognitive) * c1 * random.random())))
            cognitive_sample = random.sample(cognitive, cognitive_sample_size) if cognitive_sample_size > 0 else []
        else:
            cognitive_sample = []
        if social:
            social_sample_size = min(len(social), max(0, int(len(social) * c2 * random.random())))
            social_sample = random.sample(social, social_sample_size) if social_sample_size > 0 else []
        else:
            social_sample = []
        new_velocity = list(set(inertia_sample + cognitive_sample + social_sample))
        return new_velocity

    def mutate_timetable(self, timetable):
        new_timetable = copy.deepcopy(timetable)
        if new_timetable.assignments:
            idx = random.randint(0, len(new_timetable.assignments) - 1)
            assignment = new_timetable.assignments[idx]
            mutation_type = random.choice(['room', 'time', 'both'])
            if mutation_type in ['room', 'both']:
                suitable_rooms = [r for r in self.rooms if (r.room_type == "lab" if assignment.is_lab else r.room_type == "lecture")]
                if suitable_rooms:
                    new_room_id = random.choice(suitable_rooms).id
                    assignment.room_id = new_room_id
            if mutation_type in ['time', 'both']:
                new_day = random.randint(0, NUM_DAYS - 1)
                new_hour = random.randint(0, NUM_HOURS - 1)
                assignment.time_slot = TimeSlot(new_day, new_hour)
        self.evaluate_timetable(new_timetable)
        return new_timetable

    def crossover(self, timetable1, timetable2):
        child = Timetable()
        for i in range(len(timetable1.assignments)):
            if random.random() < 0.5:
                child.add_assignment(copy.deepcopy(timetable1.assignments[i]))
            else:
                child.add_assignment(copy.deepcopy(timetable2.assignments[i]))
        self.evaluate_timetable(child)
        return child

    def tournament_selection(self, population, tournament_size):
        tournament = random.sample(population, tournament_size)
        return max(tournament, key=lambda x: x.fitness)

    def run_pso(self, num_particles=POPULATION_SIZE, max_iterations=MAX_ITERATIONS, c1=C1, c2=C2):
        particles = self.initialize_pso(num_particles)
        self.avg_fitness_history = []
        self.best_fitness_history = []
        self.violation_history = []
        fitness_list = []

        for iteration in range(max_iterations):
            w = W_MAX - ((W_MAX - W_MIN) * (iteration / max_iterations))
            current_fitness_values = [p.position.fitness for p in particles]
            avg_fitness = sum(current_fitness_values) / len(current_fitness_values)
            best_fitness = max(current_fitness_values)
            fitness_list.append(int(self.global_best_fitness))
            if len(fitness_list) >= 31:
                last_four = fitness_list[-30:]
                if all(x == last_four[0] for x in last_four):
                    break

            self.avg_fitness_history.append(avg_fitness)
            self.best_fitness_history.append(self.global_best_fitness)
            total_violations = {violation: 0 for violation in self.global_best_position.violations}

            for p in particles:
                for v_type, v_count in p.position.violations.items():
                    total_violations[v_type] += v_count

            avg_violations = {v_type: count / num_particles for v_type, count in total_violations.items()}
            self.violation_history.append(avg_violations)

            print(
                f"Iteration {iteration}: W={w:.3f}, Avg Fitness = {avg_fitness:.2f}, Best Fitness = {self.global_best_fitness:.2f}")

            for particle in particles:
                new_velocity = self.update_velocity(particle, w, c1, c2)
                particle.velocity = new_velocity
                new_position = self.apply_velocity(particle.position, particle.velocity)
                particle.position = new_position
                particle.update_personal_best()

                if particle.best_fitness > self.global_best_fitness:
                    self.global_best_position = copy.deepcopy(particle.best_position)
                    self.global_best_fitness = particle.best_fitness

        return self.global_best_position
    def run_genetic_algorithm(self, population_size=POPULATION_SIZE, max_iterations=MAX_ITERATIONS,crossover_rate=CROSSOVER_RATE, mutation_rate=MUTATION_RATE,tournament_size=TOURNAMENT_SIZE):
        population = [self.generate_random_timetable() for _ in range(population_size)]
        self.avg_fitness_history = []
        self.best_fitness_history = []
        self.violation_history = []
        best_solution = max(population, key=lambda x: x.fitness)
        best_fitness = best_solution.fitness
        fitnees_list = []
        for generation in range(max_iterations):
            if len(fitnees_list) >= 31:
                last_four = fitnees_list[-30:]
                if all(x == last_four[0] for x in last_four):
                    break
            new_population = []
            current_fitness_values = [p.fitness for p in population]
            avg_fitness = sum(current_fitness_values) / len(current_fitness_values)
            best_fitness_current = max(current_fitness_values)
            self.avg_fitness_history.append(avg_fitness)
            self.best_fitness_history.append(best_fitness)
            total_violations = {violation: 0 for violation in population[0].violations}
            for p in population:
                for v_type, v_count in p.violations.items():
                    total_violations[v_type] += v_count
            avg_violations = {v_type: count / population_size for v_type, count in total_violations.items()}
            self.violation_history.append(avg_violations)
            print(f"Generation {generation}: Avg Fitness = {avg_fitness:.2f}, Best Fitness = {best_fitness:.2f}" )
            new_population.append(copy.deepcopy(best_solution))
            while len(new_population) < population_size:
                parent1 = self.tournament_selection(population, tournament_size)
                parent2 = self.tournament_selection(population, tournament_size)
                if random.random() < crossover_rate:
                    child = self.crossover(parent1, parent2)
                else:
                    child = copy.deepcopy(parent1)
                if random.random() < mutation_rate:
                    child = self.mutate_timetable(child)
                new_population.append(child)
            population = new_population
            current_best = max(population, key=lambda x: x.fitness)
            fitnees_list.append(int(best_fitness))
            if current_best.fitness > best_fitness:
                best_solution = copy.deepcopy(current_best)
                best_fitness = current_best.fitness
        self.global_best_position = best_solution
        self.global_best_fitness = best_fitness
        return best_solution

    def run_hybrid_algorithm(self, population_size=POPULATION_SIZE, max_iterations=MAX_ITERATIONS,
                             w=W_MAX, c1=C1, c2=C2, crossover_rate=CROSSOVER_RATE, mutation_rate=MUTATION_RATE):
        particles = self.initialize_pso(population_size)
        self.avg_fitness_history = []
        self.best_fitness_history = []
        self.violation_history = []
        fitness_list = []
        for iteration in range(max_iterations):
            current_fitness_values = [p.position.fitness for p in particles]
            avg_fitness = sum(current_fitness_values) / len(current_fitness_values)
            self.avg_fitness_history.append(avg_fitness)
            self.best_fitness_history.append(self.global_best_fitness)
            fitness_list.append(int(self.global_best_fitness))
            if len(fitness_list) >= 31:
                last_four = fitness_list[-30:]
                if all(x == last_four[0] for x in last_four):
                    break
            total_violations = {violation: 0 for violation in self.global_best_position.violations}
            for p in particles:
                for v_type, v_count in p.position.violations.items():
                    total_violations[v_type] += v_count
            avg_violations = {v_type: count / population_size for v_type, count in total_violations.items()}
            self.violation_history.append(avg_violations)

            print(
                f"Iteration {iteration}: Avg Fitness = {avg_fitness:.2f}, Best Fitness = {self.global_best_fitness:.2f}")
            for i, particle in enumerate(particles):
                if random.random() < 0.5:
                    new_velocity = self.update_velocity(particle, w, c1, c2)
                    particle.velocity = new_velocity
                    new_position = self.apply_velocity(particle.position, particle.velocity)
                    particle.position = new_position
                else:
                    other_idx = random.randint(0, population_size - 1)
                    while other_idx == i:
                        other_idx = random.randint(0, population_size - 1)
                    other_particle = particles[other_idx]
                    if random.random() < crossover_rate:
                        new_position = self.crossover(particle.position, other_particle.position)
                        particle.position = new_position
                    if random.random() < mutation_rate:
                        particle.position = self.mutate_timetable(particle.position)
                particle.update_personal_best()
                if particle.best_fitness > self.global_best_fitness:
                    self.global_best_position = copy.deepcopy(particle.best_position)
                    self.global_best_fitness = particle.best_fitness
        return self.global_best_position
    def visualize_timetable(self, timetable, title="Optimized Timetable"):
        fig, ax = plt.subplots(figsize=(18, 12))
        days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"]
        hours = [f"{h}:00" for h in range(8, 8 + NUM_HOURS)]
        grid = np.empty((NUM_DAYS, NUM_HOURS), dtype=object)
        for i in range(NUM_DAYS):
            for j in range(NUM_HOURS):
                grid[i, j] = ""

        for assignment in timetable.assignments:
            course = self.courses[assignment.course_id]
            room = self.rooms[assignment.room_id]
            day = assignment.time_slot.day
            hour = assignment.time_slot.hour
            section_id = assignment.section_id
            is_lab = assignment.is_lab
            student_count = len(course.student_ids)
            room_type = "Lab" if room.room_type == "lab" else "Hall"
            room_label = f"{room_type}-{room.id}"
            session_type = "Lecture" if not is_lab else "Lab"

            if 0 <= day < NUM_DAYS and 0 <= hour < NUM_HOURS:
                current_content = grid[day, hour]
                new_entry = (
                    f"{course.name[:15]}...\n"  # Shorten long course names
                    f"Sec-{section_id} ({session_type})\n"
                    f"Room: {room_label}\n"
                    f"Students: {student_count}"
                )

                grid[day, hour] = (
                    f"{current_content}\n\n{new_entry}" if current_content
                    else new_entry
                )

        cell_colors = np.full((NUM_DAYS, NUM_HOURS), "white", dtype=object)

        for day in range(NUM_DAYS):
            for hour in range(NUM_HOURS):
                if "\n\n" in str(grid[day, hour]):
                    cell_colors[day, hour] = "lightyellow"

        table = ax.table(
            cellText=grid,
            rowLabels=days,
            colLabels=hours,
            cellColours=cell_colors,
            loc='center',
            cellLoc='center'
        )

        table.auto_set_font_size(False)
        table.set_fontsize(7)  # Smaller font to fit text
        table.scale(1, 1.5)  # Wider cells
        ax.set_title(f"{title}\nFitness: {timetable.fitness:.2f}", fontsize=14)
        ax.axis('off')

        ax.text(0.01, 0.01,
                "Yellow cells indicate overlapping sessions.",
                transform=ax.transAxes,
                fontsize=9)

        violations_text = "\n".join([f"{k}: {v}" for k, v in timetable.violations.items()])
        ax.text(0.01, 0.05, f"Violations:\n{violations_text}", transform=ax.transAxes)
        plt.tight_layout()
        return fig, ax
    def plot_fitness_progress(self):
        fig, ax = plt.subplots(figsize=(10, 6))
        iterations = range(len(self.avg_fitness_history))
        ax.plot(iterations, self.avg_fitness_history, label='Average Fitness')
        ax.plot(iterations, self.best_fitness_history, label='Best Fitness')
        ax.set_xlabel('Iteration')
        ax.set_ylabel('Fitness')
        ax.set_title('Fitness Progress')
        ax.legend()
        plt.tight_layout()
        return fig, ax

    def plot_violations_progress(self):
        fig, ax = plt.subplots(figsize=(10, 6))
        iterations = range(len(self.violation_history))
        violation_types = list(self.violation_history[0].keys())
        for v_type in violation_types:
            values = [v_dict[v_type] for v_dict in self.violation_history]
            ax.plot(iterations, values, label=v_type)
        ax.set_xlabel('Iteration')
        ax.set_ylabel('Average Violations')
        ax.set_title('Constraint Violations Progress')
        ax.legend()
        plt.tight_layout()
        return fig, ax

    def compare_algorithms(self, population_size=POPULATION_SIZE, max_iterations=MAX_ITERATIONS):
        results = {}
        print("Running PSO...")
        start_time = time.time()
        pso_result = self.run_pso(
            num_particles=population_size,
            max_iterations=max_iterations
        )
        pso_time = time.time() - start_time
        results['PSO'] = {
            'solution': pso_result,
            'time': pso_time,
            'fitness_history': self.best_fitness_history.copy(),
            'violation_history': self.violation_history.copy()
        }
        print("\nRunning Genetic Algorithm...")
        start_time = time.time()
        ga_result = self.run_genetic_algorithm(
            population_size=population_size,
            max_iterations=max_iterations
        )
        ga_time = time.time() - start_time
        results['GA'] = {
            'solution': ga_result,
            'time': ga_time,
            'fitness_history': self.best_fitness_history.copy(),
            'violation_history': self.violation_history.copy()
        }
        print("\nRunning Hybrid Algorithm...")
        start_time = time.time()
        hybrid_result = self.run_hybrid_algorithm(
            population_size=population_size,
            max_iterations=max_iterations
        )
        hybrid_time = time.time() - start_time
        results['Hybrid'] = {
            'solution': hybrid_result,
            'time': hybrid_time,
            'fitness_history': self.best_fitness_history.copy(),
            'violation_history': self.violation_history.copy()
        }

        print("\nAlgorithm Comparison Results:")
        print(f"{'Algorithm':<10} | {'Fitness':<10} | {'Time (s)':<10}")
        print("-" * 35)
        for algo, data in results.items():
            print(f"{algo:<10} | {data['solution'].fitness:<10.2f} | {data['time']:<10.2f}")
        return results
#################################################################################################################################################################################################################################
# Gui \ loading screen
############
class VideoLoadingScreen:
    def __init__(self, root, video_path=None, audio_path=None):
        self.stop_flag = False
        self.video_path = video_path
        self.audio_path = audio_path
        self.temp_audio_file = None
        self.loop_count = 0
        self.is_looping = True
        self.audio_loaded = False
        self.loading_window = tk.Toplevel(root)
        self.loading_window.title("Loading")
        self.loading_window.geometry("800x650")
        self.loading_window.resizable(False, False)
        self.video_label = tk.Label(self.loading_window)
        self.video_label.pack(pady=10)
        self.progress = ttk.Progressbar(self.loading_window, mode='indeterminate', length=600)
        self.progress.pack(pady=10)
        self.status_var = tk.StringVar(value="Initializing...")
        ttk.Label(self.loading_window, textvariable=self.status_var, font=('Helvetica', 12)).pack()
        self.loop_var = tk.BooleanVar(value=True)
        self.loop_checkbox = ttk.Checkbutton(
            self.loading_window,
            text="Loop Video & Audio",
            variable=self.loop_var,
            command=self.toggle_loop
        )
        self.loop_checkbox.pack(pady=5)
        pygame.init()
        pygame.mixer.init(frequency=48000, size=-16, channels=2, buffer=1024)

        self.MUSIC_END_EVENT = pygame.USEREVENT + 1
        pygame.mixer.music.set_endevent(self.MUSIC_END_EVENT)

        self.setup_audio()

    def toggle_loop(self):
        """Toggle the looping state"""
        self.is_looping = self.loop_var.get()
        print(f"Video and audio looping {'enabled' if self.is_looping else 'disabled'}")

    def setup_audio(self):
        """Setup audio for the video playback"""
        self.audio_loaded = False

        if self.audio_path and os.path.exists(self.audio_path):
            print(f"Using provided audio file: {self.audio_path}")
            try:
                pygame.mixer.music.load(self.audio_path)
                print("Audio loaded successfully from direct path")
                self.audio_loaded = True
            except Exception as e:
                print(f"Error loading provided audio: {e}")
        elif self.video_path:
            self.extract_audio()
        else:
            print("No video or audio path provided, skipping audio setup")

    def extract_audio(self):
        try:

            temp_fd, temp_path = tempfile.mkstemp(suffix='.mp3')
            os.close(temp_fd)
            self.temp_audio_file = temp_path

            if not os.path.exists(self.video_path):
                print(f"Video file not found: {self.video_path}")
                return

            try:

                cmd = [
                    "ffmpeg",
                    "-i", self.video_path,
                    "-q:a", "0",
                    "-map", "a",
                    "-f", "mp3",
                    self.temp_audio_file
                ]
                subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                print(f"Audio extracted with ffmpeg to: {self.temp_audio_file}")
            except (subprocess.SubprocessError, FileNotFoundError) as e:
                print(f"FFmpeg extraction failed: {e}, trying alternate method...")

                ffmpeg_paths = [
                    r"C:\ffmpeg\bin\ffmpeg.exe",
                    r"C:\Program Files\ffmpeg\bin\ffmpeg.exe",
                    r"ffmpeg"  # Check if in PATH
                ]

                success = False
                for ffpath in ffmpeg_paths:
                    try:
                        cmd[0] = ffpath
                        subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        print(f"Audio extracted with {ffpath} to: {self.temp_audio_file}")
                        success = True
                        break
                    except:
                        continue

                if not success:
                    print("All FFmpeg extraction methods failed, audio may not play")
                    return

            try:
                pygame.mixer.music.load(self.temp_audio_file)
                print("Audio loaded successfully")
                self.audio_loaded = True
            except Exception as e:
                print(f"Error loading extracted audio: {e}")
                self.audio_loaded = False

        except Exception as e:
            print(f"Error extracting audio: {e}")
            import traceback
            traceback.print_exc()

    def play_video(self):
        try:
            cap = cv2.VideoCapture(self.video_path)
            if not cap.isOpened():
                print(f"Error: Could not open video file {self.video_path}")
                return

            original_fps = cap.get(cv2.CAP_PROP_FPS)
            total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

            print(f"Video stats - FPS: {original_fps}, Total frames: {total_frames}")

            target_fps = 60.0
            frame_time = 1.0 / target_fps
            if self.audio_loaded:
                try:
                    pygame.mixer.music.play()
                    print("Started audio playback")
                except Exception as e:
                    print(f"Error playing audio: {e}")
            else:
                print("No audio loaded, playing video without sound")
            next_frame_time = time.time()
            frame_number = 0
            while cap.isOpened() and not self.stop_flag:
                if self.audio_loaded:
                    try:
                        for event in pygame.event.get():
                            if event.type == self.MUSIC_END_EVENT:
                                print("Music playback finished")
                                if self.is_looping:
                                    print("Restarting audio playback (looping)")
                                    pygame.mixer.music.play()
                    except Exception as e:
                        print(f"Error handling pygame events: {e}")
                        if self.is_looping and not pygame.mixer.music.get_busy():
                            try:
                                print("Music not playing - restarting (fallback method)")
                                pygame.mixer.music.play()
                            except Exception as e:
                                print(f"Error restarting audio: {e}")
                try:
                    if not self.loading_window.winfo_exists():
                        print("Loading window no longer exists, stopping video")
                        break
                except:
                    print("Error checking window existence, stopping video")
                    break

                current_time = time.time()
                if current_time >= next_frame_time:
                    ret, frame = cap.read()
                    if ret:
                        try:
                            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                            frame = cv2.resize(frame, (760, 540))
                            img = Image.fromarray(frame)
                            imgtk = ImageTk.PhotoImage(image=img)
                            if self.video_label.winfo_exists():
                                self.video_label.config(image=imgtk)
                                self.video_label.image = imgtk
                        except Exception as e:
                            break
                        next_frame_time = current_time + frame_time
                        frame_number += 1
                    else:
                        self.loop_count += 1
                        if self.is_looping:
                            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
                            if self.audio_loaded:
                                if pygame.mixer.music.get_busy():
                                    music_pos = pygame.mixer.music.get_pos() / 1000
                                    if music_pos > 0.5:
                                        continue
                                    else:
                                        try:
                                            pygame.mixer.music.play()
                                        except Exception as e:
                                            print(f"Error restarting audio: {e}")
                                else:
                                    try:
                                        pygame.mixer.music.play()
                                    except Exception as e:
                                        print(f"Error restarting audio: {e}")

                try:
                    if self.loading_window.winfo_exists():
                        self.loading_window.update_idletasks()
                        self.loading_window.update()
                except Exception as e:
                    print(f"Error updating window: {e}")
                    break

                sleep_time = next_frame_time - time.time()
                if sleep_time > 0:
                    time.sleep(sleep_time)

            cap.release()
        except Exception as e:
            print(f"Error in video playback thread: {e}")
            import traceback
            traceback.print_exc()

    def fallback_play_without_audio(self, root, video_path):
        """A simple alternative player if audio extraction fails"""
        self.status_var.set("Playing video without audio")
        print("Using fallback player without audio")

        try:
            cap = cv2.VideoCapture(video_path)
            if not cap.isOpened():
                print("Error: Could not open video file using fallback method")
                return

            target_fps = 30.0
            frame_time = 1.0 / target_fps

            next_frame_time = time.time()

            while cap.isOpened() and not self.stop_flag:
                try:
                    if not self.loading_window.winfo_exists():
                        break
                except:
                    break

                current_time = time.time()

                if current_time >= next_frame_time:
                    ret, frame = cap.read()

                    if ret:
                        try:
                            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                            frame = cv2.resize(frame, (760, 540))

                            img = Image.fromarray(frame)
                            imgtk = ImageTk.PhotoImage(image=img)

                            if self.video_label.winfo_exists():
                                self.video_label.config(image=imgtk)
                                self.video_label.image = imgtk
                        except Exception as e:
                            print(f"Error in fallback player: {e}")
                            break

                        next_frame_time = current_time + frame_time
                    else:
                        if self.is_looping:
                            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
                        else:
                            break

                try:
                    if self.loading_window.winfo_exists():
                        self.loading_window.update_idletasks()
                        self.loading_window.update()
                except:
                    break

                sleep_time = next_frame_time - time.time()
                if sleep_time > 0:
                    time.sleep(sleep_time)

            cap.release()
        except Exception as e:
            print(f"Error in fallback player: {e}")

    def start(self, message="Processing..."):
        self.status_var.set(message)
        self.progress.start()
        if not self.audio_loaded and self.video_path:
            self.video_thread = threading.Thread(
                target=self.fallback_play_without_audio,
                args=(self.loading_window, self.video_path),
                daemon=True
            )
        else:
            self.video_thread = threading.Thread(target=self.play_video, daemon=True)

        self.video_thread.start()
        self.loading_window.grab_set()

    def stop(self):
        self.stop_flag = True
        try:
            pygame.mixer.music.stop()
        except:
            pass
        if hasattr(self, 'video_thread'):
            self.video_thread.join(timeout=0.5)

        try:
            if self.loading_window.winfo_exists():
                self.progress.stop()
                self.loading_window.grab_release()
                self.loading_window.destroy()
        except Exception as e:
            print(f"Error closing loading window: {e}")

        self.cleanup_temp_files()
        try:
            pygame.mixer.quit()
            pygame.quit()
        except Exception as e:
            print(f"Error quitting pygame: {e}")

    def cleanup_temp_files(self):
        try:
            if self.temp_audio_file and os.path.exists(self.temp_audio_file):
                os.remove(self.temp_audio_file)
                print(f"Removed temporary audio file: {self.temp_audio_file}")
        except Exception as e:
            print(f"Error removing temporary file: {e}")

    def __del__(self):
        self.stop()

class TimetablingGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("University Timetabling System")
        self.root.geometry("1400x900")
        self.problem = UniversityTimetablingProblem()
        self.current_solution = None
        self.loading_screen = None
        self.style = ttk.Style()
        self.style.configure('TNotebook.Tab', font=('Helvetica', 10, 'bold'), padding=[10, 5])
        self.style.configure('Title.TLabel', font=('Helvetica', 12, 'bold'))
        self.style.configure('Header.TLabel', font=('Helvetica', 10, 'bold'))
        self.style.configure('Highlight.TFrame', background='#f0f0f0')
        self.main_frame = ttk.Frame(root)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.left_panel = ttk.Frame(self.main_frame, width=300)
        self.left_panel.pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=5)
        self.right_panel = ttk.Frame(self.main_frame)
        self.right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        self.create_problem_info()
        self.create_algorithm_controls()
        self.create_stats_panel()
        self.create_solution_display()

        self.status_var = tk.StringVar()
        self.status_bar = ttk.Label(root, textvariable=self.status_var, relief=tk.SUNKEN, anchor=tk.W)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        self.status_var.set("Ready")


    def show_loading_screen(self, message):
        self.loading_screen = VideoLoadingScreen(self.root, video_path1, music_path1)
        self.loading_screen.start(message)

    def hide_loading_screen(self):
        if self.loading_screen:
            self.loading_screen.stop()
            self.loading_screen = None

    def create_problem_info(self):
        info_frame = ttk.LabelFrame(self.left_panel, text="Problem Information", padding=10)
        info_frame.pack(fill=tk.X, padx=5, pady=5)

        params = [
            ("Courses", NUM_COURSES),
            ("Lecturers", NUM_LECTURERS),
            ("Students", NUM_STUDENTS),
            ("Days", NUM_DAYS),
            ("Hours per Day", NUM_HOURS),
            ("Lecture Halls", NUM_LECTURE_HALLS),
            ("Lab Rooms", NUM_LAB_ROOMS),
            ("Max Sections/Course", MAX_SECTIONS_PER_COURSE)
        ]

        for i, (label, value) in enumerate(params):
            ttk.Label(info_frame, text=f"{label}:").grid(row=i, column=0, sticky=tk.W, padx=5, pady=2)
            ttk.Label(info_frame, text=str(value), font=('Helvetica', 10, 'bold')).grid(row=i, column=1, sticky=tk.E,
                                                                                        padx=5, pady=2)

        btn_frame = ttk.Frame(info_frame)
        btn_frame.grid(row=len(params), columnspan=2, pady=10)

        ttk.Button(btn_frame, text="View Rooms", command=self.show_rooms, width=15).pack(side=tk.LEFT, padx=2)
        ttk.Button(btn_frame, text="View Courses", command=self.show_courses, width=15).pack(side=tk.LEFT, padx=2)
        ttk.Button(btn_frame, text="View students", command=self.show_students(), width=15).pack(side=tk.TOP, pady=5)

    def show_students(self):
        window = tk.Toplevel(self.root)
        window.title("Students Information")
        window.geometry("800x600")

        tree = ttk.Treeview(window, columns=("ID", "Name", "Courses"), show="headings")
        tree.heading("ID", text="ID")
        tree.heading("Name", text="Name")
        tree.heading("Courses", text="Courses")
        tree.column("ID", width=100, anchor=tk.CENTER)
        tree.column("Name", width=150)
        tree.column("Courses", width=400)

        for student in self.problem.students:
            course_names = ", ".join([self.problem.courses[c_id].name[:20] for c_id in student.courses[:3]])
            if len(student.courses) > 3:
                course_names += f" (+{len(student.courses) - 3} more)"
            tree.insert("", tk.END, values=(student.id, student.name, course_names))

        scrollbar = ttk.Scrollbar(window, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        tree.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

    def show_student_timetable(self, student_id):
        if not self.current_solution:
            messagebox.showinfo("No Solution", "No timetable has been generated yet")
            return

        window = tk.Toplevel(self.root)
        window.title(f"Timetable for Student {student_id}")
        window.geometry("1000x700")

        text = tk.Text(window, wrap=tk.NONE, font=('Courier New', 10))
        scroll_y = ttk.Scrollbar(window, orient="vertical", command=text.yview)
        scroll_x = ttk.Scrollbar(window, orient="horizontal", command=text.xview)
        text.configure(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)

        scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
        scroll_x.pack(side=tk.BOTTOM, fill=tk.X)
        text.pack(fill=tk.BOTH, expand=True)

        header_format = "{:<8}{:<8}{:<30}{:<15}{:<15}{:<10}\n"
        text.insert(tk.END, header_format.format("Day", "Time", "Course", "Lecturer", "Room", "Type"))
        text.insert(tk.END, "=" * 96 + "\n")

        days = ["Sun", "Mon", "Tue", "Wed", "Thu"]
        row_format = "{:<8}{:<8}{:<30}{:<15}{:<15}{:<10}\n"

        student_assignments = []
        for assignment in self.current_solution.assignments:
            course = self.problem.courses[assignment.course_id]
            if student_id in course.student_ids:
                student_assignments.append(assignment)

        student_assignments.sort(key=lambda x: (x.time_slot.day, x.time_slot.hour))

        for assignment in student_assignments:
            course = self.problem.courses[assignment.course_id]
            room = self.problem.rooms[assignment.room_id]
            lecturer = self.problem.lecturers[course.lecturer_id]
            session_type = "Lab" if assignment.is_lab else "Lecture"
            course_name = course.name[:27] + "..." if len(course.name) > 27 else course.name
            room_str = f"Room {room.room_type[:3]}-{room.id}"

            line = row_format.format(
                days[assignment.time_slot.day],
                f"{assignment.time_slot.hour + 8}:00",
                course_name,
                lecturer.name.split(".")[1].strip()[:12] + "...",
                room_str,
                session_type
            )

            text.insert(tk.END, line)

        text.configure(state=tk.DISABLED)

    def generate_all_student_timetables(self):
        if not self.current_solution:
            messagebox.showinfo("No Solution", "No timetable has been generated yet")
            return
        window = tk.Toplevel(self.root)
        window.title("Student Timetables Browser")
        window.geometry("1200x800")
        window.minsize(800, 600)
        style = ttk.Style()
        style.configure('TNotebook.Tab', font=('Helvetica', 9, 'bold'))
        style.configure('TFrame', background='white')
        style.configure('TButton', font=('Helvetica', 9))
        main_frame = ttk.Frame(window)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        control_frame = ttk.Frame(main_frame)
        control_frame.pack(fill=tk.X, pady=(0, 10))

        ttk.Label(control_frame, text="Select Student:").pack(side=tk.LEFT, padx=5)

        self.student_var = tk.StringVar()
        student_combo = ttk.Combobox(control_frame, textvariable=self.student_var,
                                     state="readonly", width=40)
        student_combo.pack(side=tk.LEFT, padx=5)
        student_list = [f"{s.id} - {s.name}" for s in self.problem.students]
        student_combo['values'] = student_list
        if student_list:
            student_combo.current(0)
        search_frame = ttk.Frame(control_frame)
        search_frame.pack(side=tk.RIGHT, padx=10)

        ttk.Label(search_frame, text="Search:").pack(side=tk.LEFT)
        self.search_var = tk.StringVar()
        search_entry = ttk.Entry(search_frame, textvariable=self.search_var, width=20)
        search_entry.pack(side=tk.LEFT, padx=5)
        ttk.Button(search_frame, text="Find", command=self.search_student).pack(side=tk.LEFT)
        self.timetable_notebook = ttk.Notebook(main_frame)
        self.timetable_notebook.pack(fill=tk.BOTH, expand=True)
        if student_list:
            self.display_student_timetable(0)
        student_combo.bind('<<ComboboxSelected>>',
                           lambda e: self.display_student_timetable(student_combo.current()))

    def show_courses(self):
        window = tk.Toplevel(self.root)
        window.title("Courses Information")
        window.geometry("1200x700")

        columns = ("ID", "Name", "Lecturer", "Lecturer Name", "student", "Duration", "Sections", "Requirements")
        tree = ttk.Treeview(window, columns=columns, show="headings")

        tree.column("ID", width=50, anchor=tk.CENTER)
        tree.column("Name", width=200)
        tree.column("Lecturer", width=80, anchor=tk.CENTER)
        tree.column("Lecturer Name", width=150)
        tree.column("student", width=120, anchor=tk.CENTER)
        tree.column("Duration", width=80, anchor=tk.CENTER)
        tree.column("Sections", width=80, anchor=tk.CENTER)
        tree.column("Requirements", width=150)

        for col in columns:
            tree.heading(col, text=col)

        for course in self.problem.courses:
            student = ", ".join(f"G{g}" for g in course.student_ids)
            requirements = []
            if course.requires_projector:
                requirements.append("Projector")
            if course.requires_computers:
                requirements.append("Computers")
            req_str = ", ".join(requirements) if requirements else "None"
            lecturer = self.problem.lecturers[course.lecturer_id]
            lecturer_name = lecturer.name

            tree.insert("", tk.END, values=(
                course.id,
                course.name,
                f"L-{course.lecturer_id}",
                lecturer_name,
                student,
                f"{course.duration} hr",
                course.num_sections,
                req_str
            ))
        scroll_y = ttk.Scrollbar(window, orient=tk.VERTICAL, command=tree.yview)
        scroll_x = ttk.Scrollbar(window, orient=tk.HORIZONTAL, command=tree.xview)
        tree.configure(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
        scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
        scroll_x.pack(side=tk.BOTTOM, fill=tk.X)
        tree.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        def view_lecturer_details():
            selected = tree.focus()
            if not selected:
                messagebox.showwarning("No Selection", "Please select a course first")
                return
            lecturer_id = int(tree.item(selected)['values'][2].split("-")[1])
            self.show_lecturer_details(lecturer_id)

        ttk.Button(window, text="View Lecturer Details", command=view_lecturer_details).pack(pady=5)

    def show_lecturer_details(self, lecturer_id):
        lecturer = self.problem.lecturers[lecturer_id]
        window = tk.Toplevel(self.root)
        window.title(f"Lecturer Details: {lecturer.name}")
        window.geometry("600x400")
        main_frame = ttk.Frame(window, padding=10)
        main_frame.pack(fill=tk.BOTH, expand=True)
        ttk.Label(main_frame, text=f"Name: {lecturer.name}", font=('Helvetica', 12, 'bold')).pack(anchor=tk.W, pady=5)
        ttk.Label(main_frame, text=f"ID: {lecturer.id}").pack(anchor=tk.W)
        ttk.Label(main_frame, text="Courses Taught:", font=('Helvetica', 10, 'bold')).pack(anchor=tk.W, pady=(10, 0))
        courses_frame = ttk.Frame(main_frame)
        courses_frame.pack(fill=tk.X, padx=5, pady=5)

        if lecturer.courses_name:
            for course in lecturer.courses_name:
                ttk.Label(courses_frame, text=f"- {course}").pack(anchor=tk.W)
        else:
            ttk.Label(courses_frame, text="No courses assigned").pack(anchor=tk.W)

        ttk.Label(main_frame, text="Availability Schedule:", font=('Helvetica', 10, 'bold')).pack(anchor=tk.W,pady=(10, 0))
        avail_frame = ttk.Frame(main_frame)
        avail_frame.pack(fill=tk.X, padx=5, pady=5)
        days = ["Sun", "Mon", "Tue", "Wed", "Thu"]
        hours = [f"{h}:00" for h in range(8, 8 + NUM_HOURS)]

        for col, day in enumerate(days):
            ttk.Label(avail_frame, text=day, width=8).grid(row=0, column=col + 1, padx=2, pady=2)

        for row, hour in enumerate(hours):
            ttk.Label(avail_frame, text=hour).grid(row=row + 1, column=0, padx=2, pady=2)
            for col in range(len(days)):
                available = lecturer.availability[col, row]
                color = "green" if available else "red"
                lbl = ttk.Label(avail_frame, text="✓" if available else "✗", foreground=color, width=8)
                lbl.grid(row=row + 1, column=col + 1, padx=2, pady=2)

    def show_rooms(self):
        window = tk.Toplevel(self.root)
        window.title("Rooms Information")
        window.geometry("600x400")

        columns = ("ID", "Type", "Capacity", "Projector", "Computers")
        tree = ttk.Treeview(window, columns=columns, show="headings")

        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=100, anchor=tk.CENTER)

        for room in self.problem.rooms:
            tree.insert("", tk.END, values=(
                room.id,
                room.room_type.capitalize(),
                room.capacity,
                "Yes" if room.has_projector else "No",
                "Yes" if room.has_computers else "No"
            ))

        scrollbar = ttk.Scrollbar(window, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        tree.pack(fill=tk.BOTH, expand=True)

    def create_algorithm_controls(self):
        control_frame = ttk.LabelFrame(self.left_panel, text="Algorithm Controls", padding=10)
        control_frame.pack(fill=tk.X, padx=5, pady=5)

        ttk.Label(control_frame, text="Algorithm:").pack(anchor=tk.W, pady=2)
        self.algorithm_var = tk.StringVar(value="Hybrid")
        algo_menu = ttk.OptionMenu(control_frame, self.algorithm_var, "Hybrid", "PSO", "GA", "Hybrid")
        algo_menu.pack(fill=tk.X, pady=5)

        self.run_btn = ttk.Button(control_frame, text="Run Optimization", command=self.run_optimization)
        self.run_btn.pack(fill=tk.X, pady=5)

        ttk.Button(control_frame, text="Compare Algorithms", command=self.run_comparison).pack(fill=tk.X, pady=5)
        ttk.Button(control_frame, text="View All student Timetables", command=self.generate_all_student_timetables).pack(
            fill=tk.X, pady=5)

    def create_stats_panel(self):
        stats_frame = ttk.LabelFrame(self.left_panel, text="Solution Statistics", padding=10)
        stats_frame.pack(fill=tk.X, padx=5, pady=5)

        ttk.Label(stats_frame, text="Fitness:", style='Header.TLabel').pack(anchor=tk.W, pady=2)
        self.fitness_var = tk.StringVar(value="N/A")
        ttk.Label(stats_frame, textvariable=self.fitness_var, font=('Helvetica', 12, 'bold')).pack(anchor=tk.W)

        ttk.Label(stats_frame, text="Violations:", style='Header.TLabel').pack(anchor=tk.W, pady=(10, 2))

        self.violations_frame = ttk.Frame(stats_frame)
        self.violations_frame.pack(fill=tk.X)

        self.violation_vars = {}
        violations = [
            'room_conflict', 'lecturer_conflict', 'student_conflict',
            'room_capacity', 'equipment_mismatch', 'lecturer_unavailable',
            'room_type_mismatch', 'missing_lab_sessions', 'missing_lecture_sessions'
        ]

        for i, violation in enumerate(violations):
            ttk.Label(self.violations_frame, text=violation.replace('_', ' ').title() + ":").grid(row=i, column=0,  sticky=tk.W, padx=5, pady=1)
            self.violation_vars[violation] = tk.StringVar(value="0")
            ttk.Label(self.violations_frame, textvariable=self.violation_vars[violation]).grid(row=i, column=1,sticky=tk.E, padx=5, pady=1)

    def create_solution_display(self):
        self.solution_notebook = ttk.Notebook(self.right_panel)
        self.solution_notebook.pack(fill=tk.BOTH, expand=True)

        self.timetable_tab = ttk.Frame(self.solution_notebook)
        self.solution_notebook.add(self.timetable_tab, text="Timetable")

        self.progress_tab = ttk.Frame(self.solution_notebook)
        self.solution_notebook.add(self.progress_tab, text="Progress")

        self.conflicts_tab = ttk.Frame(self.solution_notebook)
        self.solution_notebook.add(self.conflicts_tab, text="Conflicts")

        self.init_timetable_display()
        self.init_progress_display()
        self.init_conflicts_display()

    def init_timetable_display(self):
        for widget in self.timetable_tab.winfo_children():
            widget.destroy()

        self.timetable_text = tk.Text(self.timetable_tab, wrap=tk.NONE, font=('Courier New', 10), state=tk.DISABLED)
        scroll_y = ttk.Scrollbar(self.timetable_tab, orient="vertical", command=self.timetable_text.yview)
        scroll_x = ttk.Scrollbar(self.timetable_tab, orient="horizontal", command=self.timetable_text.xview)
        self.timetable_text.configure(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)

        scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
        scroll_x.pack(side=tk.BOTTOM, fill=tk.X)
        self.timetable_text.pack(fill=tk.BOTH, expand=True)

        self.timetable_text.configure(state=tk.NORMAL)
        self.timetable_text.insert(tk.END, "No timetable generated yet. Run an optimization algorithm to see results.")
        self.timetable_text.configure(state=tk.DISABLED)

    def init_progress_display(self):
        for widget in self.progress_tab.winfo_children():
            widget.destroy()

        self.progress_canvas_frame = ttk.Frame(self.progress_tab)
        self.progress_canvas_frame.pack(fill=tk.BOTH, expand=True)

        ttk.Label(self.progress_tab, text="Algorithm progress will be shown here after running").pack(expand=True)

    def init_conflicts_display(self):
        for widget in self.conflicts_tab.winfo_children():
            widget.destroy()

        self.conflicts_text = tk.Text(self.conflicts_tab, wrap=tk.WORD, font=('Helvetica', 10), state=tk.DISABLED)
        scroll_y = ttk.Scrollbar(self.conflicts_tab, orient="vertical", command=self.conflicts_text.yview)
        self.conflicts_text.configure(yscrollcommand=scroll_y.set)

        scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
        self.conflicts_text.pack(fill=tk.BOTH, expand=True)

        self.conflicts_text.configure(state=tk.NORMAL)
        self.conflicts_text.insert(tk.END,
                                   "No conflict data available yet. Run an optimization algorithm to see results.")
        self.conflicts_text.configure(state=tk.DISABLED)

    def run_optimization(self):
        algorithm = self.algorithm_var.get()
        self.show_loading_screen(f"Running {algorithm} optimization...")
        self.run_btn.config(state=tk.DISABLED)

        def optimization_thread():
            try:
                if algorithm == "PSO":
                    solution = self.problem.run_pso()
                elif algorithm == "GA":
                    solution = self.problem.run_genetic_algorithm()
                else:
                    solution = self.problem.run_hybrid_algorithm()

                self.current_solution = solution
                self.root.after(0, lambda: self.display_solution(solution))
                self.root.after(0, self.generate_all_student_timetables)
            except Exception as e:
                self.root.after(0, lambda: messagebox.showerror("Error", f"An error occurred during optimization:\n{str(e)}"))
            finally:
                self.root.after(0, self.hide_loading_screen)
                self.root.after(0, lambda: self.run_btn.config(state=tk.NORMAL))
                self.root.after(0, lambda: self.status_var.set("Ready"))

        threading.Thread(target=optimization_thread, daemon=True).start()

    def run_comparison(self):
        self.show_loading_screen("Comparing algorithms...")

        def comparison_thread():
            try:
                results = {}
                algorithms = ["PSO", "GA", "Hybrid"]

                for algo in algorithms:
                    self.root.after(0, lambda: self.status_var.set(f"Running {algo}..."))

                    start_time = time.time()
                    if algo == "PSO":
                        solution = self.problem.run_pso()
                    elif algo == "GA":
                        solution = self.problem.run_genetic_algorithm()
                    else:
                        solution = self.problem.run_hybrid_algorithm()

                    elapsed = time.time() - start_time
                    results[algo] = {
                        'solution': solution,
                        'time': elapsed,
                        'fitness': solution.fitness,
                        'violations': solution.violations,
                        'fitness_history': self.problem.best_fitness_history.copy()
                    }

                self.root.after(0, lambda: self.show_comparison_results(results))
                self.root.after(0, lambda: self.status_var.set("Algorithm comparison completed"))
            except Exception as e:
                self.root.after(0, lambda: messagebox.showerror("Error",
                                                                f"An error occurred during comparison:\n{str(e)}"))
                self.root.after(0, lambda: self.status_var.set("Error during comparison"))
            finally:
                self.root.after(0, self.hide_loading_screen)

        threading.Thread(target=comparison_thread, daemon=True).start()

    def display_timetable(self, solution):
        self.timetable_text.configure(state=tk.NORMAL)
        self.timetable_text.delete(1.0, tk.END)

        header_format = "{:<8}{:<8}{:<30}{:<12}{:<15}{:<15}{:<10}\n"
        self.timetable_text.insert(tk.END,
                                   header_format.format("Day", "Time", "Course", "Section", "Students", "Room", "Type"))
        self.timetable_text.insert(tk.END, "=" * 111 + "\n")

        days = ["Sun", "Mon", "Tue", "Wed", "Thu"]
        row_format = "{:<8}{:<8}{:<30}{:<12}{:<15}{:<15}{:<10}\n"

        sorted_assignments = sorted(solution.assignments, key=lambda x: (x.time_slot.day, x.time_slot.hour))

        for assignment in sorted_assignments:
            course = self.problem.courses[assignment.course_id]
            room = self.problem.rooms[assignment.room_id]
            session_type = "Lab" if assignment.is_lab else "Lecture"
            course_name = course.name[:27] + "..." if len(course.name) > 27 else course.name
            student_count = len(course.student_ids)
            room_str = f"Room {room.room_type[:3]}-{room.id}"

            line = row_format.format(
                days[assignment.time_slot.day],
                f"{assignment.time_slot.hour + 8}:00",
                course_name,
                f"Sec {assignment.section_id + 1}/{course.num_sections}",
                student_count,
                room_str,
                session_type
            )

            start_pos = self.timetable_text.index(tk.END)
            self.timetable_text.insert(tk.END, line)
            end_pos = self.timetable_text.index(tk.END)

            if assignment.is_lab:
                self.timetable_text.tag_add("lab", start_pos, end_pos)
            if self.is_conflict(assignment, solution):
                self.timetable_text.tag_add("conflict", start_pos, end_pos)

        self.timetable_text.tag_config("lab", background="lightblue")
        self.timetable_text.tag_config("conflict", background="lightcoral", foreground="white")
        self.timetable_text.configure(state=tk.DISABLED)

    def update_stats(self, solution):
        self.fitness_var.set(f"{solution.fitness:.2f}")
        for violation, count in solution.violations.items():
            self.violation_vars[violation].set(str(count))

    def is_conflict(self, assignment, solution):
        course = self.problem.courses[assignment.course_id]
        room = self.problem.rooms[assignment.room_id]
        lecturer = self.problem.lecturers[course.lecturer_id]

        if room.capacity < course.min_capacity:
            return True
        if course.requires_projector and not room.has_projector:
            return True
        if course.requires_computers and not room.has_computers:
            return True
        if not lecturer.availability[assignment.time_slot.day, assignment.time_slot.hour]:
            return True
        if assignment.is_lab and room.room_type != "lab":
            return True
        if not assignment.is_lab and room.room_type != "lecture":
            return True

        for other in solution.assignments:
            if other == assignment:
                continue
            if (other.time_slot.day == assignment.time_slot.day and
                    other.time_slot.hour == assignment.time_slot.hour):
                if other.room_id == assignment.room_id:
                    return True
                other_course = self.problem.courses[other.course_id]
                if course.lecturer_id == other_course.lecturer_id:
                    return True
                if any(g in course.student_ids for g in other_course.student_ids):
                    return True

        return False

    def display_progress(self):
        for widget in self.progress_canvas_frame.winfo_children():
            widget.destroy()

        if not hasattr(self.problem, 'avg_fitness_history') or not self.problem.avg_fitness_history:
            return

        fig = Figure(figsize=(8, 6))
        ax1 = fig.add_subplot(211)
        iterations = range(len(self.problem.avg_fitness_history))
        ax1.plot(iterations, self.problem.avg_fitness_history, label='Average Fitness')
        ax1.plot(iterations, self.problem.best_fitness_history, label='Best Fitness')
        ax1.set_xlabel('Iteration')
        ax1.set_ylabel('Fitness')
        ax1.set_title('Fitness Progress')
        ax1.legend()
        ax1.grid(True, linestyle='--', alpha=0.7)

        ax2 = fig.add_subplot(212)
        if self.problem.violation_history:
            violation_types = list(self.problem.violation_history[0].keys())
            for v_type in violation_types:
                values = [v_dict[v_type] for v_dict in self.problem.violation_history]
                ax2.plot(iterations, values, label=v_type.replace('_', ' ').title())
            ax2.set_xlabel('Iteration')
            ax2.set_ylabel('Average Violations')
            ax2.set_title('Constraint Violations Progress')
            ax2.legend()
            ax2.grid(True, linestyle='--', alpha=0.7)

        fig.tight_layout()
        canvas = FigureCanvasTkAgg(fig, master=self.progress_canvas_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        toolbar = NavigationToolbar2Tk(canvas, self.progress_canvas_frame)
        toolbar.update()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def display_conflicts(self, solution):
        self.conflicts_text.configure(state=tk.NORMAL)
        self.conflicts_text.delete(1.0, tk.END)

        if not solution.assignments:
            self.conflicts_text.insert(tk.END, "No assignments to analyze for conflicts.")
            self.conflicts_text.configure(state=tk.DISABLED)
            return

        conflict_count = 0
        for i, assignment in enumerate(solution.assignments):
            course = self.problem.courses[assignment.course_id]
            room = self.problem.rooms[assignment.room_id]
            lecturer = self.problem.lecturers[course.lecturer_id]
            conflicts = []

            if room.capacity < course.min_capacity:
                conflicts.append(f"Room capacity {room.capacity} < required {course.min_capacity}")
            if course.requires_projector and not room.has_projector:
                conflicts.append("Missing projector")
            if course.requires_computers and not room.has_computers:
                conflicts.append("Missing computers")
            if not lecturer.availability[assignment.time_slot.day, assignment.time_slot.hour]:
                conflicts.append("Lecturer unavailable")
            if assignment.is_lab and room.room_type != "lab":
                conflicts.append("Lab session in non-lab room")
            if not assignment.is_lab and room.room_type != "lecture":
                conflicts.append("Lecture in non-lecture room")

            for other in solution.assignments[i + 1:]:
                if (other.time_slot.day == assignment.time_slot.day and
                        other.time_slot.hour == assignment.time_slot.hour):
                    if other.room_id == assignment.room_id:
                        other_course = self.problem.courses[other.course_id]
                        conflicts.append(f"Room conflict with {other_course.name} (Sec {other.section_id})")
                    other_course = self.problem.courses[other.course_id]
                    if course.lecturer_id == other_course.lecturer_id:
                        conflicts.append(f"Lecturer conflict with {other_course.name} (Sec {other.section_id})")
                    if any(g in course.student_ids for g in other_course.student_ids):
                        conflicts.append(f"Student group conflict with {other_course.name} (Sec {other.section_id})")

            if conflicts:
                conflict_count += 1
                self.conflicts_text.insert(tk.END,
                                           f"Conflict #{conflict_count}: {course.name} (Sec {assignment.section_id}) at {assignment.time_slot}\n")
                for conflict in conflicts:
                    self.conflicts_text.insert(tk.END, f"  - {conflict}\n")
                self.conflicts_text.insert(tk.END, "\n")

        if conflict_count == 0:
            self.conflicts_text.insert(tk.END, "No conflicts detected in the timetable!")

        self.conflicts_text.configure(state=tk.DISABLED)

    def show_comparison_results(self, results):
        window = tk.Toplevel(self.root)
        window.title("Algorithm Comparison Results")
        window.geometry("1000x700")

        algorithms = ["PSO", "GA", "Hybrid"]
        notebook = ttk.Notebook(window)
        notebook.pack(fill=tk.BOTH, expand=True)

        summary_tab = ttk.Frame(notebook)
        notebook.add(summary_tab, text="Summary")
        columns = ("Algorithm", "Fitness", "Time (s)", "Violations")
        tree = ttk.Treeview(summary_tab, columns=columns, show="headings")

        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=150, anchor=tk.CENTER)

        for algo, data in results.items():
            total_violations = sum(data['violations'].values())
            tree.insert("", tk.END, values=(
                algo,
                f"{data['fitness']:.2f}",
                f"{data['time']:.2f}",
                total_violations
            ))

        scrollbar = ttk.Scrollbar(summary_tab, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        tree.pack(fill=tk.BOTH, expand=True)

        violations_tab = ttk.Frame(notebook)
        notebook.add(violations_tab, text="Detailed Violations")
        violation_types = list(results["PSO"]['violations'].keys())
        columns = ["Algorithm"] + [v.replace('_', ' ').title() for v in violation_types]
        violations_tree = ttk.Treeview(violations_tab, columns=columns, show="headings")

        for col in columns:
            violations_tree.heading(col, text=col)
            violations_tree.column(col, width=120, anchor=tk.CENTER)

        for algo, data in results.items():
            row = [algo] + [str(data['violations'][v]) for v in violation_types]
            violations_tree.insert("", tk.END, values=row)

        scrollbar = ttk.Scrollbar(violations_tab, orient=tk.VERTICAL, command=violations_tree.yview)
        violations_tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        violations_tree.pack(fill=tk.BOTH, expand=True)

        progress_tab = ttk.Frame(notebook)
        notebook.add(progress_tab, text="Fitness Progress")
        fig = Figure(figsize=(8, 4))
        ax = fig.add_subplot(111)

        for algo in algorithms:
            if 'fitness_history' in results[algo]:
                iterations = range(len(results[algo]['fitness_history']))
                ax.plot(iterations, results[algo]['fitness_history'], label=algo)

        ax.set_xlabel('Iteration')
        ax.set_ylabel('Fitness')
        ax.set_title('Algorithm Comparison - Fitness Progress')
        ax.legend()
        ax.grid(True, linestyle='--', alpha=0.7)

        canvas = FigureCanvasTkAgg(fig, master=progress_tab)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        toolbar = NavigationToolbar2Tk(canvas, progress_tab)
        toolbar.update()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
    def display_solution(self, solution):
        self.update_stats(solution)
        self.display_timetable(solution)
        self.display_progress()
        self.display_conflicts(solution)
    def display_student_timetable(self, student_index):
        for tab in self.timetable_notebook.tabs():
            self.timetable_notebook.forget(tab)
        student = self.problem.students[student_index]
        tab_frame = ttk.Frame(self.timetable_notebook)
        self.timetable_notebook.add(tab_frame, text=f"Student {student.id}")
        header_frame = ttk.Frame(tab_frame, relief=tk.RIDGE, borderwidth=2)
        header_frame.pack(fill=tk.X, pady=(0, 10))
        ttk.Label(header_frame,
                  text=f"Timetable for {student.name} (ID: {student.id})",
                  font=('Helvetica', 12, 'bold')).pack(side=tk.LEFT, padx=10, pady=5)

        grid_frame = ttk.Frame(tab_frame)
        grid_frame.pack(fill=tk.BOTH, expand=True)
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        hours = [f"{h}:00" for h in range(8, 8 + NUM_HOURS)]
        for i in range(len(days) + 1):
            grid_frame.grid_columnconfigure(i, weight=1)
        for j in range(len(hours) + 1):
            grid_frame.grid_rowconfigure(j, weight=1)
        for i, day in enumerate(days):
            ttk.Label(grid_frame, text=day, font=('Helvetica', 10, 'bold'),
                      relief=tk.RIDGE).grid(row=0, column=i + 1, sticky='nsew', padx=1, pady=1)

        for j, hour in enumerate(hours):
            ttk.Label(grid_frame, text=hour, font=('Helvetica', 9),
                      relief=tk.RIDGE).grid(row=j + 1, column=0, sticky='nsew', padx=1, pady=1)

        student_assignments = []
        for assignment in self.current_solution.assignments:
            course = self.problem.courses[assignment.course_id]
            if student.id in course.student_ids:
                student_assignments.append(assignment)
        for assignment in student_assignments:
            course = self.problem.courses[assignment.course_id]
            room = self.problem.rooms[assignment.room_id]
            lecturer = self.problem.lecturers[course.lecturer_id]
            day_idx = assignment.time_slot.day
            hour_idx = assignment.time_slot.hour
            cell = tk.Frame(grid_frame, borderwidth=1, relief=tk.RIDGE)
            cell.grid(row=hour_idx + 1, column=day_idx + 1, sticky='nsew', padx=1, pady=1)
            bg_color = "#E6F3FF" if assignment.is_lab else "#FFE6E6"
            cell.config(bg=bg_color)
            info_frame = tk.Frame(cell, bg=bg_color)
            info_frame.pack(fill=tk.BOTH, expand=True, padx=3, pady=3)
            name_label = tk.Label(info_frame, text=course.name[:12] + ("..." if len(course.name) > 12 else ""),
                                  bg=bg_color, font=('Helvetica', 9, 'bold'))
            name_label.pack(anchor=tk.W)
            type_label = tk.Label(info_frame, text="LAB" if assignment.is_lab else "LEC",
                                  bg=bg_color, font=('Helvetica', 8))
            type_label.pack(anchor=tk.W)
            lect_label = tk.Label(info_frame, text=f"Dr. {lecturer.name.split()[-1]}",
                                  bg=bg_color, font=('Helvetica', 8))
            lect_label.pack(anchor=tk.W)
            room_label = tk.Label(info_frame, text=f"Rm {room.id}",
                                  bg=bg_color, font=('Helvetica', 8))
            room_label.pack(anchor=tk.W)

    def search_student(self):
        search_term = self.search_var.get().lower()
        if not search_term:
            return

        for i, student in enumerate(self.problem.students):
            if (search_term in str(student.id).lower() or
                    search_term in student.name.lower()):
                self.student_var.set(f"{student.id} - {student.name}")
                self.display_student_timetable(i)
                return

        messagebox.showinfo("Not Found", f"No student matching '{search_term}' found")

if __name__ == "__main__":
    root = tk.Tk()
    app = TimetablingGUI(root)
    root.mainloop()