Flappy Bird AI using Deep Reinforcement Learning (DQN)

This project implements an AI agent that learns to play Flappy Bird using Deep Q-Networks (DQN) built with PyTorch. The agent improves over time by interacting with the environment and optimizing its decisions using reinforcement learning techniques such as experience replay and target networks.

📌 Features
Deep Q-Network (DQN) using PyTorch
Experience Replay for stable training
Epsilon-Greedy exploration strategy
Target Network synchronization
Customizable hyperparameters via YAML
Supports CPU / CUDA / MPS acceleration
🧠 How It Works

The agent learns by:

Observing the game state
Taking actions (flap or no flap)
Receiving rewards
Storing experiences in replay memory
Updating Q-values using the Bellman Equation

📂 Project Structure
├── agent.py                # Main training & testing logic
├── dqn.py                  # Neural network model
├── experience_replay.py    # Replay buffer
├── game_flappy_bird.py     # Game environment
├── parameters.yaml         # Hyperparameters
├── runs/                   # Saved models & logs

⚙️ Installation
git clone https://github.com/Ren-Korat-24/FLAPPYBIRD-RL

cd flappy-bird-dqn

pip install torch gymnasium flappy-bird-gymnasium pygame pyyaml

▶️ Usage
Train the model
python agent.py default -train

Run trained model
python agent.py default

⚡ Hyperparameters
You can modify training behavior by editing parameters.yaml:

Learning rate (alpha)
Discount factor (gamma)
Epsilon decay (exploration strategy)
Replay memory size
Mini-batch size

🖥️ Hardware Acceleration
The code automatically selects the best available device:

CUDA (NVIDIA GPU)
MPS (Apple Silicon)
CPU (fallback)

📈 Output
Best model saved in /runs directory
Training logs stored automatically
Reward improvements tracked per episode

🎯 Future Improvements
Double DQN
Dueling Networks
Prioritized Experience Replay
Model performance visualization dashboard
