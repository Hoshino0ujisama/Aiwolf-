
from openai import OpenAI # type: ignore
import openai # type: ignore
import os

# APIキーを環境変数として設定
openai.api_key = os.environ["OPENAI_API_KEY"]


client = OpenAI()

system = """
You are playing a werewolf game. Write the output appropriately

# output
- English
- python tupple including two elements
- The first element is a python list(elements: contents of the input rewritten into concise contents)
- the second element is a python string for indicator of request and inquiry. 

# rule 
- each element in the list should be less than 12 words
- Representing a person, use Agent[00], Agent[01], Agent[02], Agent[03],or Agent[04]
- Representing the job title, use villager, werewolf, possessed, or seer
- Ignore information that has nothing to do with werewolf game 
- . is unnecessary
- Indicate the subject matter. 
- The second element is "Agent[01]", "Agent[02]", "Agent[03]", "Agent[04]" or None. When the speaker request or inquire something, output the name of the speaker.

# example
Speaker: Agent[00] 
Input: エージェント[03]がずいぶん口をつぐんでるな。なんなんだあいつは。あいつが人狼かもしれん。今夜はエージェント[03]に投票するつもりや。
Output: (["Agent[03] is quiet", "Agent[03] might be a werewolf", "Agent[00] is planning to vote for Agent[03] tonight"], None)
"""

user = """ 
Speaker: Agent[00]
Input: 
皆様、改めてお伝えしますわ。占い師はわたくし以外にいらっしゃいません。
占い師を自称されているAgent[03]、Agent[01]、Agent[04]様たちが嘘をついて
いらっしゃるということになりますわ。
特にAgent[01]とAgent[04]様がお互いを人狼認定する占い結果を出していますが、
役職の配分を見る限りではどちらかが狂人か人狼である可能性が高いですわね。
無論、人狼か狂人が占い師の役割を使用して混乱を招くのは一つの手でございますので、
皆様の推理が不可欠ですわ。
Agent[01]様、わたくし自身がAgent[03]様を占い黒だと結果を出しておりますが、
わたくしは役職としての占い師ですので、
その結果を信用する必要がありますわ。静かに話し合って正しい決定をするためには、
誰が本物の占い師かを見抜くことが重要です。
それには、皆様のご協力が必要ですの。芸術の秋も近いですし、
こういった知的なゲームが心を豊かにしてくれるものですわね。
"""

# 1Mあたり80円/240円
# 入力が400、出力が100トークンの場合、発話1回あたり80/1000 + 240/10000 = 0.1円

user2 = """Agent[00]を占ったら黒だったよ。Agent[01]を占ったら白だったよ。"""

model = "gpt-4o" # gpt-3.5-turbo-0125
completion = client.chat.completions.create(
  model=model,
  messages=[
    {"role": "system", "content": system},
    {"role": "user", "content": user}
  ]
)

with open("output.log", 'a') as f:
    print('入力: ', file=f)
    print(user2, file=f)
    print(f'{model}: ', file=f)
    print(completion.choices[0].message.content, file=f)
    print(file=f)