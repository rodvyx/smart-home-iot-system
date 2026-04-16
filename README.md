# Smart Home IoT System

Intelligent IoT system for energy monitoring and optimization using design patterns.

## Features
- Device management (Factory + Prototype)
- Energy optimization (Strategy)
- Automation (Command)
- Rule engine (Interpreter)
- State recovery (Memento)
- External integration (Adapter)
- Dynamic features (Decorator)


---

## 🧠 Design Patterns Implementation

---

### 🏭 Factory Pattern
**Location:** `patterns/factory/`  

**Purpose:**  
Handles creation of different smart devices (e.g., meter, thermostat, solar panel).

**Problem Solved:**  
- Eliminates direct object instantiation  
- Makes system easily extendable  

---

### 🧬 Prototype Pattern
**Location:** `patterns/prototype/`  

**Purpose:**  
Creates new devices by cloning existing ones.

**Problem Solved:**  
- Reduces object creation cost  
- Reuses pre-configured objects  

---

### 🧠 Strategy Pattern
**Location:** `patterns/strategy/`  

**Purpose:**  
Implements multiple energy optimization strategies:
- Cost-saving  
- Eco-friendly  
- Performance-based  

**Problem Solved:**  
- Enables dynamic behavior switching  
- Avoids complex conditional logic  

---

### 🎮 Command Pattern
**Location:**  
- `patterns/command/`  
- `services/command_service.py`  

**Purpose:**  
Encapsulates actions such as:
- Turning off devices  
- Executing automation workflows  

**Problem Solved:**  
- Decouples request from execution  
- Supports automation sequences  

---

### 🔁 Iterator Pattern
**Location:**  
- `patterns/iterator/`  
- `core/devices/device_collection.py`  

**Purpose:**  
Provides a standard way to traverse device collections.

**Problem Solved:**  
- Hides internal data structure  
- Improves flexibility  

---

### 🧾 Interpreter Pattern
**Location:** `patterns/interpreter/`  

**Purpose:**  
Implements rule-based logic:
- Example: IF energy > threshold THEN turn off devices  

**Problem Solved:**  
- Enables intelligent decision-making  
- Supports dynamic rule evaluation  

---

### 💾 Memento Pattern
**Location:**  
- `patterns/memento/`  
- `services/device_service.py`  

**Purpose:**  
Saves and restores system state.

**Problem Solved:**  
- Enables undo functionality  
- Improves system reliability  

---

### 🎭 Decorator Pattern
**Location:** `patterns/decorator/`  

**Purpose:**  
Adds dynamic features such as:
- Logging  
- Alerts  

**Problem Solved:**  
- Extends functionality without modifying base classes  

---

### 🔌 Adapter Pattern
**Location:** `patterns/adapter/`  

**Purpose:**  
Integrates external systems (e.g., energy API).

**Problem Solved:**  
- Converts incompatible interfaces  
- Enables third-party integration  

---

## ⚙️ Core Components

---

### Device Service
`services/device_service.py`  
- Manages devices  
- Uses Factory, Prototype, and Memento  

---

### Energy Service
`services/energy_service.py`  
- Applies Strategy pattern for optimization  

---

### Command Service
`services/command_service.py`  
- Executes commands  

---

### Automation Controller
`controllers/automation_controller.py`  
- Coordinates all system operations  

---

## 🚀 System Functionality

The system demonstrates:

- Creation and cloning of devices  
- Dynamic energy optimization  
- Execution of automation commands  
- Rule-based decision making  
- State saving and restoration  
- External API integration  
- Dynamic feature extension  

---

## ▶️ How to Run

```bash
python app.py