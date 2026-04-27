import gymnasium
import flappy_bird_gymnasium
import pygame

#creating new env
env = gymnasium.make("FlappyBird-v0", render_mode="human", use_lidar=True)
state,info=env.reset()
done=False

#Initialize PyGame keyword
pygame.init()
screen=pygame.display.get_surface()

while not done:
    action =0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                done=True
        elif event.type == pygame.KEYDOWN:    
            if event.key == pygame.K_SPACE:
                action = 1  # flap

    state, reward, done, truncated, info = env.step(action)
    env.render()

env.close()
pygame.quit()
