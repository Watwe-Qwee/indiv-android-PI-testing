from agent import Agent
from monitor import interact
import gym
import numpy as n
import sys
sys.path.append("/Users/anon.ong/Documents/02_CP_3_year/INDIV/indiv-android-testing/Lucy/senior/custom_gym/")
import envs

if __name__ == '__main__':
    env = gym.make('CustomEnv-v0')
    agent = Agent()
    avg_rewards, best_avg_reward = interact(env, agent)
