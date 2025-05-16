University Timetabling System


Hybrid PSO-GA Optimization for Course Scheduling


📌 Overview
This project implements a hybrid metaheuristic algorithm (PSO + Genetic Algorithm) to solve the university timetabling problem. It generates conflict-free schedules while considering:

Room availability (lecture halls, labs)

Lecturer constraints (availability, course load)

Student enrollments (no overlapping classes)

Equipment requirements (projectors, computers)

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
Modify students.csv or adjust parameters in the code:

python
NUM_DAYS = 5      
NUM_HOURS = 10      
NUM_LECTURERS = 20  
NUM_STUDENTS = 500  
NUM_COURSES = 50  
2. Algorithm Selection
Choose between:

PSO (Particle Swarm Optimization)

Genetic Algorithm (GA)

Hybrid (PSO + GA)

3. Outputs
Timetable Visualization (color-coded conflicts)

Fitness Progress Graph (convergence analysis)

Violation Reports (room/lecturer/student clashes)

Student-Specific Schedules

Teacher and students coruses 
Project Gui how it looks :
![{EC377E20-50C3-47DA-876A-C35E432FA43A}](https://github.com/user-attachments/assets/bccfdfef-8a44-4ee9-bd93-b551759cb69c)


📈 Performance Metrics
Algorithm	  Avg. Fitness	Speed (iter/sec)	Best Solution
PSO	          8,200	           45	               9,500
GA	          7,800	           38	               9,200
Hybrid	      8,600	           50	               9,800

📂 Project Structure
├── main.py                 # Entry point (GUI)  
├── requirements.txt        # Dependencies  
├── students.csv            # Sample student data  
├── docs/  
│   ├── algorithm_flow.png  # Workflow diagram  
│   └── results_analysis.md # Performance benchmarks  
└── README.md               # This file  



📜 License
MIT License © 2024

🔗 References
Particle Swarm Optimization (PSO) - Scholarpedia

Genetic Algorithms - GeeksforGeeks

University Timetabling Problem - Springer Paper

🎯 Future Work

Parallel Computing (speed up optimization)

Better Algorithm Ant Colony Optimization (ACO) and Simulated Annealing

Better Gui as it looks white and boring as of right now But if we made it web based it will look better

Made with ❤️ using Python & Metaheuristics 🚀
