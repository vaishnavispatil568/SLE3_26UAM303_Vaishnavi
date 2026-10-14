# SLE-3: Architectural Design using Full C4 Model
Course: 02AML204 – Introduction to Artificial Intelligence  
PRN: 26UAM303  
Name: Vaishnavi Satish Patil  
Division: A  

## 📌 Project Overview
This repository contains the deliverables for **SLE-3 (Architectural Design using Full C4 Model)**. The project models the architecture of a **Maze Solving System** that utilizes **Breadth-First Search (BFS)** and **Depth-First Search (DFS)** algorithms to find the optimal path in a grid-based maze.

## 📂 Repository Contents
* **`SLE03_26UAM303_Vaishnavi_Satish_Patil.docx`** (or `.pdf`): Complete architectural report featuring all 4 levels of the C4 Model (Context, Container, Component, and Code).
* **`maze_search_26UAM303.py`**: Python implementation containing the core classes and search algorithms (BFS and DFS).

## 🏗️ C4 Model Architecture Summary
1. **Level 1 (Context Diagram):** Shows the user interacting with the Maze Solving System.
2. **Level 2 (Container Diagram):** Breaks the system down into modules (Input Module, Search Engine, Memory/Visited Set, Path Reconstructor, Output Module).
3. **Level 3 (Component Diagram):** Dives into the internal components of the *Search Engine* (Frontier/Open List, Explored/Closed Set, Goal Test Component, Successor Generator).
4. **Level 4 (Code Level Overview):** Key classes (`Node`, `MazeProblem`) and methods (`bfs_search`, `dfs_search`).

## 🚀 How to Run the Code
Make sure you have Python installed, then run the search script using:
```bash
python maze_search_26UAM303.py


