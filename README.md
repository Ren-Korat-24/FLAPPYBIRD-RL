# 🐦 Flappy Bird AI (Deep Reinforcement Learning - DQN)

A Deep Reinforcement Learning project where an AI agent learns to play **Flappy Bird** using **Deep Q-Networks (DQN)** with PyTorch.

The agent improves its gameplay by interacting with the environment, collecting rewards, and learning optimal actions over time through reinforcement learning techniques.

---

## 📌 Features

- Deep Q-Network (DQN) implementation  
- Experience Replay for stable learning  
- Epsilon-Greedy exploration strategy  
- Target Network synchronization  
- Customizable hyperparameters using YAML  
- Supports CPU / CUDA / Apple MPS  
- Train and test AI agent  
- Automatic model saving and logging  

---

## 🛠 Technologies Used

- Python  
- PyTorch  
- Gymnasium  
- Flappy Bird Gymnasium Environment  
- Pygame  
- YAML  

---

## 📂 Project Structure

```txt
FLAPPYBIRD_RL/
├── runs/
│   ├── trained_models/
│   └── logs/
│
├── agent.py
├── dqn.py
├── experience_replay.py
├── game_flappy_bird.py
├── parameters.yaml
├── README.md
└── requirements.txt

⚙️ How It Works
The Flappy Bird environment is created using Gymnasium
The AI agent observes the game state
The DQN model predicts the best possible action
Experience Replay stores previous experiences for stable training
The Target Network improves learning consistency
The agent gradually learns to survive longer and score higher

🚀 Getting Started
1. Clone Repository
git clone https://github.com/your-username/flappy-bird-dqn.git
cd flappy-bird-dqn
2. Create Virtual Environment
python -m venv venv
For Windows
venv\Scripts\activate
3. Install Dependencies
pip install torch gymnasium flappy-bird-gymnasium pygame pyyaml

Or install from requirements file:

pip install -r requirements.txt
▶️ Train The Model
python agent.py FLAPPYBIRD_RL -train

The AI agent will start training and improve over multiple episodes.

🎮 Run The Trained Model
python agent.py FLAPPYBIRD_RL

The trained AI agent will automatically play Flappy Bird.

📈 Output
Trained model saved inside runs/
Training logs generated automatically
Performance improves over episodes
AI learns better obstacle avoidance over time
🧠 Reinforcement Learning Concepts Used
Deep Q-Learning (DQN)
Bellman Equation
Experience Replay Memory
Exploration vs Exploitation
Target Network Updates
Reward-Based Learning

🎯 Purpose

This project is created to understand and implement Deep Reinforcement Learning concepts by training an AI agent to play Flappy Bird autonomously.

⚠️ Important GitHub Note

Avoid uploading unnecessary files and folders:

venv/
__pycache__/
.ipynb_checkpoints/
runs/

Large trained model files can also be managed using Git LFS if needed.

🔮 Future Improvements
Add Double DQN implementation
Add Dueling DQN architecture
Add TensorBoard visualization
Add real-time training graphs
Improve reward engineering
Add multiplayer AI comparison
Deploy as a playable web application