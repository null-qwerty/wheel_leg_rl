import isaaclab.sim as sim_utils
from isaaclab.actuators import ImplicitActuatorCfg
from isaaclab.assets import ArticulationCfg

WHEELLEG_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path="assets/chassis.usd",
        rigid_props=sim_utils.RigidBodyPropertiesCfg(
            rigid_body_enabled=True,
            max_linear_velocity=1000.0,
            max_angular_velocity=1000.0,
            max_depenetration_velocity=100.0,
            enable_gyroscopic_forces=True,
        ),
        articulation_props=sim_utils.ArticulationRootPropertiesCfg(
            enabled_self_collisions=True,
            solver_position_iteration_count=32,
            solver_velocity_iteration_count=4,
            sleep_threshold=0.005,
            stabilization_threshold=0.001,
        ),
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.5),
        joint_pos={
            "LeftFrontMotor": 0.0,
            "LeftBackMotor": 0.0,
            "RightFrontMotor": 0.0,
            "RightBackMotor": 0.0,
            "LeftWheelMotor": 0.0,
            "RightWheelMotor": 0.0,
        },
    ),
    actuators={
        "LegMotors": ImplicitActuatorCfg(
            joint_names_expr=[
                "LeftFrontMotor",
                "LeftBackMotor",
                "RightFrontMotor",
                "RightBackMotor",
            ],
            effort_limit=18.0,
            velocity_limit=1203.2113,
            stiffness=25.0,
            damping=0.01,
        ),
        "WheelMotors": ImplicitActuatorCfg(
            joint_names_expr=["LeftWheelMotor", "RightWheelMotor"],
            effort_limit=2.462823726,
            velocity_limit=545.547,
            stiffness=0.0,
            damping=10.0,
        ),
    },
    soft_joint_pos_limit_factor=0.95,
)
