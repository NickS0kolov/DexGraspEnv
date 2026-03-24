import numpy as np
from mani_skill.agents.base_agent import BaseAgent
from mani_skill.agents.registration import register_agent

@register_agent()
class MyRobot(BaseAgent):

    uid = "my_robot"

    urdf_path = r"unitree_ros\robots\g1_with_brainco_hand\g1_29dof_mode_15_brainco_hand_me_setup.urdf" #2 brainco

    fix_root_link = True

    enable_self_collisions = True