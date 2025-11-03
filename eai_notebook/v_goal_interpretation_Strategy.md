# goal_interpretation_Strategy

## Prompts解读

```prompts_model

# 背景介绍：目标、任务、输入、输出、要求

our task is to understand natural language goals for a household robot, reason about the object states and relationships, and turn natural language goals into symbolic goals in the given format. The goals include: node goals describing object states, edge goals describing object relationships and action goals describing must-to-do actions in this goal. The input will be the goal's name, the goal's description, relevant objects as well as their current and all possible states, and all possible relationships between objects. The output should be the symbolic version of the goals.

# 相关物体概念

Relevant objects in the scene indicates those objects involved in the action execution initially. It will include the object name, the object initial states, and the object all possible states. It follows the format: object name, id: ...(object id), states: ...(object states), possible states: ...(all possible states). Your proposed object states should be within the following set: CLOSED, OPEN, ON, OFF, SITTING, DIRTY, CLEAN, LYING, PLUGGED_IN, PLUGGED_OUT.

# 相关物体的初始状态及可能的状态

Relevant objects in the scene are:
<object_in_scene>

# 所有可能的关系和对它们的描述

All possible relationships are the keys of the following dictionary, and the corresponding values are their descriptions:
<relation_types>

# 符号目标格式

Symbolic goals format:
Node goals should be a list indicating the desired ending states of objects. Each goal in the list should be a dictionary with two keys 'name' and 'state'. The value of 'name' is the name of the object, and the value of 'state' is the desired ending state of the target object. For example, [{'name': 'washing_machine', 'state': 'PLUGGED_IN'}, {'name': 'washing_machine', 'state': 'CLOSED'}, {'name': 'washing_machine', 'state': 'ON'}] requires the washing_machine to be PLUGGED_IN, CLOSED, and ON. It can be a valid interpretation of natural language goal: 
Task name: Wash clothes. 
Task description: Washing pants with washing machine
This is because if one wants to wash clothes, the washing machine should be functioning, and thus should be PLUGGED_IN, CLOSED, and ON.

# 边缘目标格式————edge goals

Edge goals is a list of dictionaries indicating the desired relationships between objects. Each goal in the list is a dictionary with three keys 'from_name', and 'relation' and 'to_name'. The value of 'relation' is desired relationship between 'from_name' object to 'to_name' object. The value of 'from_name' and 'to_name' should be an object name. The value of 'relation' should be an relationship. All relations should only be within the following set: ON, INSIDE, BETWEEN, CLOSE, FACING, HOLDS_RH, HOLDS_LH.

# 每种关系可能对应的 “to_name” 目标

Each relation has a fixed set of objects to be its 'to_name' target. Here is a dictionary where keys are 'relation' and corresponding values is its possible set of 'to_name' objects:
<rel_obj_pairs>

# 动作目标————action goals

Action goals is a list of actions that must be completed in the goals. The number of actions is less than three. If node goals and edge goals are not enough to fully describe the goal, add action goals to describe the goal. Below is a dictionary of possible actions, whose keys are all possible actions and values are corresponding descriptions. When output actions goal list, each action goal should be a dictionary with keys 'action' and 'description'.
<action_space>

# 目标名称以及目标描述

Goal name and goal description:
<goal_str>

# 输出说明

Now output the symbolic version of the goal. Output in json format, whose keys are 'node goals', 'edge goals', and 'action goals', and values are your output of symbolic node goals, symbolic edge goals, and symbolic action goals, respectively. That is, {'node goals': SYMBOLIC NODE GOALS, 'edge goals': SYMBOLIC EDGE GOALS, 'action goals': SYMBOLIC ACTION GOALS}. Please strictly follow the symbolic goal format.
```

举例:point_down:：

```prompts_examples

# 背景介绍：目标、任务、输入、输出、要求

Your task is to understand natural language goals for a household robot, reason about the object states and relationships, and turn natural language goals into symbolic goals in the given format. The goals include: node goals describing object states, edge goals describing object relationships and action goals describing must-to-do actions in this goal. The input will be the goal's name, the goal's description, relevant objects as well as their current and all possible states, and all possible relationships between objects. The output should be the symbolic version of the goals.

# 相关物体概念

Relevant objects in the scene indicates those objects involved in the action execution initially. It will include the object name, the object initial states, and the object all possible states. It follows the format: object name, id: ...(object id), states: ...(object states), possible states: ...(all possible states). Your proposed object states should be within the following set: CLOSED, OPEN, ON, OFF, SITTING, DIRTY, CLEAN, LYING, PLUGGED_IN, PLUGGED_OUT.

# 物体的初始状态及可能的状态

Relevant objects in the scene are:\nfloor_lamp, initial states: ['OFF', 'CLEAN'], possible states: ['CLEAN', 'OFF', 'ON', 'BROKEN', 'OFF', 'ON']\ncharacter, initial states: [], possible states: ['LYING', 'SITTING']\nbedroom, initial states: ['CLEAN'], possible states: ['CLEAN']\ndining_room, initial states: ['CLEAN'], possible states: ['CLEAN']

# 相关物体的可能的边缘状态

All possible relationships are the keys of the following dictionary, and the corresponding values are their descriptions:\n{'ON': 'An object rests atop another, like a book on a table.', 'FACING': 'One object is oriented towards another, as in a person facing a wall.', 'HOLDS_LH': 'An object is held or supported by the left hand, like a left hand holding a ball.', 'INSIDE': 'An object is contained within another, like coins inside a jar.', 'BETWEEN': 'An object is situated spatially between two entities, like a park between two buildings.', 'HOLDS_RH': 'An object is grasped or carried by the right hand, such as a right hand holding a pen.', 'CLOSE': 'Objects are near each other without touching, like two close-standing trees.'}

# 符号目标格式

Symbolic goals format:\nNode goals should be a list indicating the desired ending states of objects. Each goal in the list should be a dictionary with two keys 'name' and 'state'. The value of 'name' is the name of the object, and the value of 'state' is the desired ending state of the target object. For example, [{'name': 'washing_machine', 'state': 'PLUGGED_IN'}, {'name': 'washing_machine', 'state': 'CLOSED'}, {'name': 'washing_machine', 'state': 'ON'}] requires the washing_machine to be PLUGGED_IN, CLOSED, and ON. It can be a valid interpretation of natural language goal: \nTask name: Wash clothes. \nTask description: Washing pants with washing machine\nThis is because if one wants to wash clothes, the washing machine should be functioning, and thus should be PLUGGED_IN, CLOSED, and ON.

# 边缘目标格式————edge goals

Edge goals is a list of dictionaries indicating the desired relationships between objects. Each goal in the list is a dictionary with three keys 'from_name', and 'relation' and 'to_name'. The value of 'relation' is desired relationship between 'from_name' object to 'to_name' object. The value of 'from_name' and 'to_name' should be an object name. The value of 'relation' should be an relationship. All relations should only be within the following set: ON, INSIDE, BETWEEN, CLOSE, FACING, HOLDS_RH, HOLDS_LH.

# 每种关系可能对应的 “to_name” 目标

Each relation has a fixed set of objects to be its 'to_name' target. Here is a dictionary where keys are 'relation' and corresponding values is its possible set of 'to_name' objects:\n{'ON': {'oven', 'bed', 'dishwasher', 'washing_machine', 'toilet', 'coffe_maker', 'table', 'couch', 'character'}, 'HOLDS_LH': {'keyboard', 'novel', 'tooth_paste', 'spectacles', 'water_glass', 'toothbrush'}, 'HOLDS_RH': {'address_book', 'phone', 'novel', 'tooth_paste', 'cup', 'remote_control', 'drinking_glass', 'mouse', 'water_glass', 'toothbrush'}, 'INSIDE': {'hands_both', 'dining_room', 'bathroom', 'home_office', 'freezer'}, 'FACING': {'computer', 'laptop', 'phone', 'television', 'toilet', 'remote_control'}, 'CLOSE': {'shower', 'cat'}}

# 动作目标————action goals

Action goals is a list of actions that must be completed in the goals. The number of actions is less than three. If node goals and edge goals are not enough to fully describe the goal, add action goals to describe the goal. Below is a dictionary of possible actions, whose keys are all possible actions and values are corresponding descriptions. When output actions goal list, each action goal should be a dictionary with keys 'action' and 'description'.\n{'CLOSE': 'as opposed to open sth, CLOSE sth means changing the state from OPEN to CLOSE, not get close to!', 'DRINK': 'drink up sth', 'FIND': 'find and get near to sth', 'WALK': 'walk towards sth, get near to sth', 'GRAB': 'graph sth', 'LOOKAT': 'look at sth, face sth', 'LOOKAT_SHORT': 'shortly look at sth', 'LOOKAT_LONG': 'look at sth for long', 'OPEN': 'open sth, as opposed to close sth', 'POINTAT': 'point at sth', 'PUTBACK': 'put object A back to object B', 'PUTIN': 'put object A into object B', 'PUTOBJBACK': 'put object back to its original place', 'RUN': 'run towards sth, get close to sth', 'SIT': 'sit on sth', 'STANDUP': 'stand up', 'SWITCHOFF': 'switch sth off (normally lamp/light)', 'SWITCHON': 'switch sth on (normally lamp/light)', 'TOUCH': 'touch sth', 'TURNTO': 'turn and face sth', 'WATCH': 'watch sth', 'WIPE': 'wipe sth out', 'PUTON': 'put on clothes, need to hold the clothes first', 'PUTOFF': 'put off clothes', 'GREET': 'greet to somebody', 'DROP': \"drop something in robot's current room, need to hold the thing first\", 'READ': 'read something, need to hold the thing first', 'LIE': 'lie on something, need to get close the thing first', 'POUR': 'pour object A into object B', 'TYPE': 'type on keyboard', 'PUSH': 'move sth', 'PULL': 'move sth', 'MOVE': 'move sth', 'WASH': 'wash sth', 'RINSE': 'rinse sth', 'SCRUB': 'scrub sth', 'SQUEEZE': 'squeeze the clothes', 'PLUGIN': 'plug in the plug', 'PLUGOUT': 'plug out the plug', 'CUT': 'cut some food', 'EAT': 'eat some food', 'RELEASE': 'drop sth inside the current room'}

# 目标名称以及目标描述

Goal name and goal description:
Goal name: Turn on light

Goal description: I go to bedroom and locate a lamp. This lamp can be turned on by touch, as it has capacitive sensing. So I do it.

# 输出说明

Now output the symbolic version of the goal. Output in json format, whose keys are 'node goals', 'edge goals', and 'action goals', and values are your output of symbolic node goals, symbolic edge goals, and symbolic action goals, respectively. That is, {'node goals': SYMBOLIC NODE GOALS, 'edge goals': SYMBOLIC EDGE GOALS, 'action goals': SYMBOLIC ACTION GOALS}. Please strictly follow the symbolic goal format.\n"
```

## llm输出部分样例（DeepSeekV3 :whale:）

```llm_outputs
{
    {
        "identifier": "11_1",
        "llm_output": "{\n  \"node goals\": [\n    {\"name\": \"floor_lamp\", \"state\": \"ON\"}\n  ],\n  \"edge goals\": [],\n  \"action goals\": []\n}"
    },
    {
        "identifier": "120_1",
        "llm_output": "{\n  \"node goals\": [\n    {\"name\": \"light\", \"state\": \"ON\"},\n    {\"name\": \"light\", \"state\": \"ON\"}\n  ],\n  \"edge goals\": [],\n  \"action goals\": [\"SWITCHON\"]\n}"
    },
    {
        "identifier": "125_2",
        "llm_output": "{\n  \"node goals\": [\n    {\"name\": \"light\", \"state\": \"ON\"}\n  ],\n  \"edge goals\": [],\n  \"action goals\": [\"SWITCHON\"]\n}"
    },
    {
        "identifier": "150_2",
        "llm_output": "{\n  \"node goals\": [\n    {\n      \"name\": \"light\",\n      \"state\": \"ON\"\n    }\n  ],\n  \"edge goals\": [],\n  \"action goals\": [\n    \"SWITCHON\"\n  ]\n}"
    }
}
```

:sparkles: 由此可知,输出形式应为:

```output_format
    {
        "identifier": "task_id",
        "llm_output": "{"node goals": [{"name": "object_name","state": "object_state"}],"edge goals": [{"from_name": "object_name or character", "relation": "relation_name", "to_name": "object_name or character"}],"action goals": [{"action":"action_name"}]}"
    }
```

## Strategy

### :star: 底层思想：语言理解+逻辑翻译

### :v: 两个思路

```
1. Strong llm + Prompt Engineering + Few shot
2. Little llm + Fine Tune
```

### :one: 确定ground_truth

#### 从init_and_final_graphs.json中提取node goals 和 edge goals改变的部分，如下：

```python
import json

file_path = '/data/xjq/embodied-agent-interface/src/virtualhome_eval/dataset/programs_processed_precond_nograb_morepreconds/init_and_final_graphs/TrimmedTestScene1_graph/results_intentions_march-13-18/file120_1.json'

with open(file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

init_nodes = data.get('init_graph', {}).get('nodes', [])
final_nodes = data.get('final_graph', {}).get('nodes', [])
init_edges = data.get('init_graph', {}).get('edges', [])
final_edges = data.get('final_graph', {}).get('edges', [])

init_nodes_dict = {node['id']: node for node in init_nodes}
final_nodes_dict = {node['id']: node for node in final_nodes}

state_changes = []

for node_id, init_node in init_nodes_dict.items():
    final_node = final_nodes_dict.get(node_id)
    if final_node:
        init_states = set(init_node.get('states', []))
        final_states = set(final_node.get('states', []))
        if init_states != final_states:
            added_states = final_states - init_states
            removed_states = init_states - final_states
            change_info = {
                'id': node_id,
                'class_name': init_node['class_name'],
                'added_states': list(added_states),
                'removed_states': list(removed_states)
            }
            state_changes.append(change_info)

def edge_to_tuple(edge):
    return (edge['from_id'], edge['relation_type'], edge['to_id'])

init_edges_set = {edge_to_tuple(edge) for edge in init_edges}
final_edges_set = {edge_to_tuple(edge) for edge in final_edges}

added_edges = final_edges_set - init_edges_set
removed_edges = init_edges_set - final_edges_set

if state_changes:
    print("节点状态变化:")
    for change in state_changes:
        print(f"ID: {change['id']}, 类名: {change['class_name']}")
        if change['added_states']:
            print(f"  添加的状态: {', '.join(change['added_states'])}")
        if change['removed_states']:
            print(f"  移除的状态: {', '.join(change['removed_states'])}")
        print("-" * 40)
else:
    print("没有发现节点状态变化。")

print("\n边关系变化:")
if added_edges:
    print("添加的边:")
    for edge in added_edges:
        print(f"form_id:{edge[0]} relation_type:({edge[1]}) to_name:{edge[2]}")
if removed_edges:
    print("移除的边:")
    for edge in removed_edges:
        print(f"form_id:{edge[0]} relation_type:({edge[1]}) to_name:{edge[2]}")
if not added_edges and not removed_edges:
    print("没有发现边关系变化。")
```

#### 如任务11_1的结果如下：

```outputs
节点状态变化:
ID: 1000, 类名: floor_lamp
  添加的状态: ON
  移除的状态: OFF
----------------------------------------

边关系变化:
添加的边:
form_id:1000 relation_type:(CLOSE) to_name:65
form_id:65 relation_type:(INSIDE) to_name:67
form_id:65 relation_type:(CLOSE) to_name:1000
移除的边:
form_id:65 relation_type:(INSIDE) to_name:201
```

#### 然而，`eai_eval`评测时并不是按照`virtual home`的标准来评测的，添加了很多制约条件，因此edge_goals需要按实际情况选择：

```constraint
Here is a dictionary where keys are 'relation' and corresponding values is its possible set of 'to_name' objects:
{
    'ON': {'oven', 'bed', 'dishwasher', 'washing_machine', 'toilet', 'coffe_maker', 'table', 'couch', 'character'}, 
    'HOLDS_LH': {'keyboard', 'novel', 'tooth_paste', 'spectacles', 'water_glass', 'toothbrush'}, 
    'HOLDS_RH': {'address_book', 'phone', 'novel', 'tooth_paste', 'cup', 'remote_control', 'drinking_glass', 'mouse', 'water_glass', 'toothbrush'}, 
    'INSIDE': {'hands_both', 'dining_room', 'bathroom', 'home_office', 'freezer'}, 
    'FACING': {'computer', 'laptop', 'phone', 'television', 'toilet', 'remote_control'}, 
    'CLOSE': {'shower', 'cat'}
}
```

#### 所以，上述例子11_1中的edge goals就都不能选择，置空

:negative_squared_cross_mark::
```
"{\"node goals\": [{\"name\": \"floor_lamp\", \"state\": \"ON\"}], \"edge goals\": [{\"from_name\": \"floor_lamp\", \"relation\": \"CLOSE\", \"to_name\":\"character\"},\n{\"from_name\": \"character\", \"relation\": \"INSIDE\", \"to_name\":\"bedroom\"},\n{\"from_name\": \"character\", \"relation\": \"CLOSE\", \"to_name\":\"floor_lamp\"},\n], \"action goals\": []}"
```

:white_check_mark:
```
"{\"node goals\": [{\"name\": \"floor_lamp\", \"state\": \"ON\"}], \"edge goals\": [], \"action goals\": []}"
```
#### 这里还有一个问题，就是init_and_final_graphs.json中的状态变化很有可能会更多，例如file120_1：
```example
节点状态变化:
ID: 245, 类名: light
  添加的状态: ON
  移除的状态: OFF
----------------------------------------
ID: 411, 类名: light
  添加的状态: ON
  移除的状态: OFF
----------------------------------------
ID: 1000, 类名: floor_lamp
  添加的状态: ON
  移除的状态: OFF
----------------------------------------

边关系变化:
添加的边:
form_id:65 relation_type:(CLOSE) to_name:1000
form_id:65 relation_type:(CLOSE) to_name:411
form_id:1000 relation_type:(CLOSE) to_name:65
form_id:411 relation_type:(CLOSE) to_name:65
```

#### 图中状态变化的有三个，light（245）、light（411）、floor_lamp（1000），但是问题中只有两个light发生变化

### Little llm + Fine Tune

#### 第一次尝试(失败 :disappointed:)
```
Little llm: Qwen-2.5-7B-Instruct
Fine Tune Dataset: 自建数据集
Dataset format: input&output
```
本次的思路是，将`prompts`喂给超大参数量的模型（如DeepSeekv3 :whale:），得到输出，通过这些输出中正确的部分作为`groundtruth`，错误的部分作为对比学习的数据来源，以此进行微调。

:star: 微调参数如下：
|  Parameter                   | Value       |
| ---------------------------  | ----------- |
| r                            | 64          |
| lora_alpha                   | 16          |
| lora_dropout                 | 0.05        |
| epoch                        | 10          |
| per_device_train_batch_size  | 1           |
|gradient_accumulation_steps   | 8           |
|learning_rate                 | 2e-4        |
|weight_decay                  | 0.0         |
|max_grad_norm                 | 1.0         |
|logging_steps                 | 10          |
|save_total_limit              | 2           |
|max_seq_length                | 1024        |

微调之后，本地测试发现效果不好，我觉得原因可能有以下几点：
:heavy_exclamation_mark: 数据量太少，对于微调而言不痛不痒
:heavy_exclamation_mark: 数据格式不恰当 

#### 第二次尝试（有效果，学到了格式，但是precise过低 :confused:）

```
Little llm: Qwen-2.5-7B-Instruct
Fine Tune Dataset: 自建数据集(Final_graph-Init_graph)
Dataset format: ChatML
```

```ChatML format
{
    "messages": [
        {
           "role": "system", 
           "content": "·······"
        }, 
        {
            "role": "user", 
            "content": "······"
        }, 
        {
            "role": "assistant", 
            "content": "······"
        }
                ]
}

```

#### 第三次尝试（激进策略，强制过拟合 :smiling_imp:）

```
Little llm: Qwen-2.5-7B-Instruct
Fine Tune Dataset: 自建数据集(Final_graph-Init_graph)
Dataset format: ChatML
train points: high learninig rate & low batch_size & high epoch
```

```参数
output_dir=OUTPUT_DIR,
per_device_train_batch_size=PER_DEV_BS,
gradient_accumulation_steps=GR_ACC,
num_train_epochs=EPOCHS,
learning_rate=LR,
weight_decay=0.0,
lr_scheduler_type="cosine",
warmup_ratio=0.03,
logging_steps=10,
save_steps=500,
save_total_limit=2,
bf16=True,
optim="paged_adamw_32bit",
dataloader_num_workers=2,
report_to="none",
deepspeed=ds_cfg
```

```Effect_train_example 
task_11_1:
Expected_output
--------------------------
{
    "node goals": [
        {
            "name": "floor_lamp",
            "state": "ON"
        }
                  ],
    "edge goals": [],
    "action goals": []
}
gold_output
--------------------------
{
    "node goals": [
        {
            "name": "floor_lamp",
            "state": "ON"
        }
                  ],
    "edge goals": [],
    "action goals": []
}
✅
```

```Unseen_example
task_make_coffee:
Expected_output
--------------------------
{
    "node goals": [
        {
            "name": "cup",
            "state": "FULL"
        }
                  ],
    "edge goals": [from_name: "cup", relation: "HOLDS_LH",to_name: "character"],
    "action goals": []
}
gold_output
--------------------------
{
    "node goals": [],
    "edge goals": [from_name: "cup", relation: "HOLDS_LH",to_name: "character"],
    "action goals": []
}
❌
```