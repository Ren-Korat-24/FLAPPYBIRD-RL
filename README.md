# 🐦 Flappy Bird AI (Deep Reinforcement Learning - DQN)

This repository contains a Flappy Bird AI agent built using **Deep Q-Learning (DQN)** with PyTorch.  
The agent learns to play the game by interacting with the environment and improving its decisions over time using reinforcement learning techniques.

---

## 📌 Features
- Deep Q-Network (DQN) implementation  
- Experience Replay for stable learning  
- Epsilon-Greedy exploration strategy  
- Target Network synchronization  
- Customizable hyperparameters (YAML)  
- Supports CPU / CUDA / MPS  

---

## 🛠 Technologies Used
- Python  
- PyTorch  
- Gymnasium  
- Flappy Bird Gym Environment  
- Pygame  
- YAML  

---

## 📂 Project Structure
- `agent.py` → Training & testing logic  
- `dqn.py` → Neural network model  
- `experience_replay.py` → Replay memory buffer  
- `game_flappy_bird.py` → Game environment  
- `parameters.yaml` → Hyperparameters  
- `runs/` → Saved models & logs  

---

## 🎯 Purpose
This project is created to understand and implement **Deep Reinforcement Learning** concepts by training an AI agent to play Flappy Bird.

---

## 🚀 Getting Started

### 1. Clone Repository
```bash
git clone https://github.com/your-username/flappy-bird-dqn.git
cd flappy-bird-dqn

### 2. Install  Dependencies
pip install torch gymnasium flappy-bird-gymnasium pygame pyyaml

### 3. Train the model
python agent.py FLAPPBIRD_RL -train

### 4. Run the model
python agent.py FLAPPBIRD_RL

## 📈 Output
Trained model saved in runs/
Training logs generated automatically
Performance improves over episode
