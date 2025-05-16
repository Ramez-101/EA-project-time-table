University Timetabling System

Hybrid PSO-GA Optimization for Course Scheduling

📌 Overview
This project implements a hybrid metaheuristic algorithm (PSO + Genetic Algorithm) to solve the university timetabling problem. It generates conflict-free schedules while considering:

Room availability (lecture halls, labs)

Lecturer constraints (availability, course load)

Student enrollments (no overlapping classes)

Equipment requirements (projectors, computers)

 loading screen With music 
![{8F6C931F-BEB1-486F-887F-8B5AF2AA0AC6}](https://github.com/user-attachments/assets/700e68d1-c66d-4ae5-acca-de67111eaccd)


🚀 Key Features:
✅ Hybrid PSO-GA Optimization (combines swarm intelligence + evolutionary algorithms)
✅ Interactive GUI with real-time visualization
✅ Multi-algorithm comparison (PSO vs. GA vs. Hybrid)
✅ Student-specific timetable views
✅ Constraint violation tracking

⚙️ Installation
Prerequisites
Python 3.8+     

Libraries: pygame, pandas, numpy, matplotlib, opencv-python, tkinter

Setup
Clone the repository:

bash
git clone https://github.com/yourusername/university-timetabling.git
cd university-timetabling
Install dependencies:

bash
pip install -r requirements.txt
Run the application:

bash
python main.py
📊 Usage
1. Input Configuration
User can give seed number 
number of courses
number of lectures
number of students
pop size 
number of itrations 
example:

![{7C9B09FE-BA3B-43EB-9411-02B9A2BA7EF0}](https://github.com/user-attachments/assets/3adb2f15-2e07-4aa7-951a-f3a17b30e830)


3. Algorithm Selection
Choose between:

PSO (Particle Swarm Optimization)

Genetic Algorithm (GA)

Hybrid (PSO + GA)

3. Outputs
Timetable Visualization (color-coded conflicts)

![{1D5A967A-6E36-4C70-8C20-5652CCB2D654}](https://github.com/user-attachments/assets/79e798e8-8770-4fcf-8759-bd9d9b2edb4c)

Fitness Progress Graph (convergence analysis)
![{4156438E-777C-4842-844C-100077479A5C}](https://github.com/user-attachments/assets/b51a04e7-8699-4057-ac46-707b4f0c1bb8)

Violation Reports (room/lecturer/student clashes)

![{149AF713-CEFA-4C54-8E0F-AC46B5A148AC}](https://github.com/user-attachments/assets/85ea1bd0-85ba-481d-9d7a-8c89c15bb0f1)

Student-Specific Schedules

![{D16D7955-4791-4A75-8158-978D60673200}](https://github.com/user-attachments/assets/069b96bf-8f42-4f08-a5bf-eb6364562d12)
veiw courses of doctores

![{04B4FD5E-EC13-4682-A14B-C22A39645454}](https://github.com/user-attachments/assets/386e7efe-54a7-4a49-87f4-c165741a63f1)

students and coursess

![{EC377E20-50C3-47DA-876A-C35E432FA43A}](https://github.com/user-attachments/assets/bccfdfef-8a44-4ee9-bd93-b551759cb69c)

menu

![{EB4787B0-707A-46B4-8E27-B9305C90B6DC}](https://github.com/user-attachments/assets/a3d98a9f-bb1e-48e2-9b3b-7593137a5a4b)

Rooms 

![{F2A7F880-60D2-4A99-8C41-180789244B7A}](https://github.com/user-attachments/assets/cdbe4475-7c85-4f7d-ac92-ee01f644870a)

📈 Performance Metrics
Algorithm	   Avg. Fitness	    Speed (iter/sec)	 Best Solution
PSO	          8,200	            45	               9,500
GA	           7,800	            38	               9,200
Hybrid	       8,600	            50	               9,800

![{1003B329-E1BB-4F1E-8C0A-B2449EA6E7E9}](https://github.com/user-attachments/assets/b3ba596a-00cb-4a70-829c-8bb3503eb848)





📜 License
MIT License © 2024

🔗 References
Particle Swarm Optimization (PSO) - Scholarpedia

Genetic Algorithms - GeeksforGeeks

University Timetabling Problem - Springer Paper

🎯 Future Work

⚡ Parallel computing for faster optimization

🐜 New algorithms: Ant Colony Optimization (ACO)

🌐 Web-based GUI (Flask/Django)


Made with ❤️ using Python & Metaheuristics 🚀
