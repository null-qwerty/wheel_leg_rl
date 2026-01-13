# Wheel-Leg RL

## 简介

基于 Isaac Lab 的五连杆轮腿底盘的强化学习环境，USD 模型：[chassis.usd](https://assets.null-qwerty.work/model/chassis.usd)

> 当前处于**建设初期阶段**，代码和模型均会频繁改动。

## 使用

> 部分翻译自模板原有 README

- 按照 [installation guide](https://isaac-sim.github.io/IsaacLab/main/source/setup/installation/index.html) 安装 Isaac Lab，建议使用虚拟环境。

- 克隆仓库：
    ```bash
    git clone git@github.com:null-qwerty/wheel_leg_rl.git
    cd wheel_leg_rl
    ```

- 使用安装 Isaac Lab 的 Python 解释器，安装 wheel_leg_rl：

    ```bash
    # use 'PATH_TO_isaaclab.sh|bat -p' instead of 'python' if Isaac Lab is not installed in Python venv or conda
    python -m pip install -e source/wheel_leg_rl

- 下载模型文件 chassis.usd，并放置在 `wheel_leg_rl/assets/` 目录下。

- 使用以下方法验证安装是否成功：
    > 请在 wheel_leg_rl 根目录下运行以下命令，因为 config 中写的是相对路径 XD  
    > config 文件位于 `wheel_leg_rl/source/wheel_leg_rl/env_cfg`
    
    > 如果发现不能正常运行，大概率是还没写完 :)
    - 列出可用任务：

        注意任务名有 `Template` 前缀。

        ```bash
        # use 'FULL_PATH_TO_isaaclab.sh|bat -p' instead of 'python' if Isaac Lab is not installed in Python venv or conda
        python scripts/list_envs.py
        ```

    - 运行任务：

        ```bash
        # use 'FULL_PATH_TO_isaaclab.sh|bat -p' instead of 'python' if Isaac Lab is not installed in Python venv or conda
        python scripts/<RL_LIBRARY>/train.py --task=<TASK_NAME>
        ```

    - 运行带有虚拟智能体的任务：

        包括零动作（Zero-action agent）或随机动作（Random-action agent）的虚拟智能体，有助于确保环境配置正确。

        - Zero-action agent

            ```bash
            # use 'FULL_PATH_TO_isaaclab.sh|bat -p' instead of 'python' if Isaac Lab is not installed in Python venv or conda
            python scripts/zero_agent.py --task=<TASK_NAME>
            ```
        - Random-action agent

            ```bash
            # use 'FULL_PATH_TO_isaaclab.sh|bat -p' instead of 'python' if Isaac Lab is not installed in Python venv or conda
            python scripts/random_agent.py --task=<TASK_NAME>
            ```

## 代码格式化

安装 pre-commit：

```bash
pip install pre-commit
```
格式化代码：

```bash
pre-commit run --all-files
```

## VSCode Pylance 设置

### Pylance Missing Indexing of Extensions

如果遇到部分扩展包无法被索引的情况，
请在 `.vscode/settings.json` 中的 `"python.analysis.extraPaths"` 下添加扩展包路径。

```json
{
    "python.analysis.extraPaths": [
        "<path-to-ext-repo>/source/wheel_leg_rl"
    ]
}
```

如果是虚拟环境中安装 Isaac Lab，可能还需要添加 Isaac Lab 路径，例如：
```json
{
    "python.analysis.extraPaths": [
        "~/IsaacLab/source/isaaclab",
        "~/IsaacLab/source/isaaclab_mimic",
        "~/IsaacLab/source/isaaclab_assets",
        "~/IsaacLab/source/isaaclab_rl",
        "~/IsaacLab/source/isaaclab_tasks"
    ]
}
```

### Pylance 崩溃

如果遇到 `pylance` 崩溃，可能是因为索引的文件过多，导致内存不足。
一种可能的解决方案是排除一些在项目中未使用的 omniverse 包。
为此，请修改 `.vscode/settings.json`，并在键 `"python.analysis.extraPaths"` 下注释掉一些包。
以下是一些可能被排除的包的示例：

```json
"<path-to-isaac-sim>/extscache/omni.anim.*"         // Animation packages
"<path-to-isaac-sim>/extscache/omni.kit.*"          // Kit UI tools
"<path-to-isaac-sim>/extscache/omni.graph.*"        // Graph UI tools
"<path-to-isaac-sim>/extscache/omni.services.*"     // Services tools
...
```