from util import str2bool


def add_argument(parser):
    parser.set_defaults(max_episode_steps=200)
    parser.set_defaults(object_ob_all=True)
    parser.set_defaults(control_type="impedance")
    parser.set_defaults(furniture_name="table_lack_0825")

    parser.set_defaults(alignment_pos_dist=0.02)
    parser.set_defaults(alignment_rot_dist_up=0.95)
    parser.set_defaults(alignment_rot_dist_forward=0.95)
    parser.set_defaults(alignment_project_dist=0.3)

    parser.add_argument("--pos_threshold", type=float, default=0.015)
    parser.add_argument("--rot_threshold", type=float, default=0.05)
    parser.add_argument("--discrete_grip", type=str2bool, default=True)
    parser.add_argument("--easy_init", type=str2bool, default=False)

    # environment offsets
    parser.add_argument("--above_leg_z", type=float, default=0.05)

    # reward coefficients
    parser.add_argument("--diff_rew", type=str2bool, default=True)
    parser.add_argument("--ctrl_penalty_coef", type=float, default=0.0)
    parser.add_argument("--touch_coef", type=float, default=5)
    parser.add_argument("--gripper_penalty_coef", type=float, default=0.05)
    parser.add_argument("--rot_dist_coef", type=float, default=1)
    parser.add_argument("--pos_dist_coef", type=float, default=50)
    parser.add_argument("--grasp_dist_coef", type=float, default=100)
    parser.add_argument("--lift_dist_coef", type=float, default=100)
    parser.add_argument("--align_pos_dist_coef", type=float, default=100)
    parser.add_argument("--align_rot_dist_coef", type=float, default=50)
    parser.add_argument("--fine_pos_dist_coef", type=float, default=500)
    parser.add_argument("--fine_align_rot_dist_coef", type=float, default=250)

    parser.add_argument("--phase_bonus", type=float, default=1000)
