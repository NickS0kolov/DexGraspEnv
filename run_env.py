import gymnasium as gym
import torch
import mani_skill.envs 

# Импорт твоей среды
from clutter_env import TabletopClutterEnv
from my_robot import MyRobot
import numpy as np

env = TabletopClutterEnv(render_mode="human", robot_uids='my_robot')

obs, _ = env.reset()


print(env.action_space.shape)
done = False
while not done:
    action = env.action_space.sample()
    action = np.clip(action, env.action_space.low, env.action_space.high)
    оbs, reward, terminated, truncated, info = env.step(action)
    env.render()

    done = terminated or truncated

env.close()