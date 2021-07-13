from metaworld.envs.mujoco.sawyer_xyz.v2.sawyer_microwave_v2 import SawyerMicrowaveEnvV2
import gym
import matplotlib.pyplot as plt 
env = SawyerMicrowaveEnvV2()
env.reset()
for i in range(10):
    img = env.render(mode="rgb_array")
    plt.imsave('t{}.png'.format(i), img)
    env.step(env.action_space.sample())
