import json
from zhipuai import ZhipuAI
from get_hwnd import WindowEnumerator


class NLP:
    def __init__(self,mission):
        self.mission=mission
        with open("H:\Project_Warehouse\API令牌.txt", 'r', encoding='utf-8') as f:
            self.api_token = f.read()

        prompt_path = "prompt.json"
        with open(prompt_path, 'r', encoding='utf-8') as f:
            self.prompt = f.read()

    def NLP_find_mission(self):
        client = ZhipuAI(api_key=self.api_token)
        user_input = self.mission
        enumerator = WindowEnumerator()
        json_data = json.dumps(enumerator.windows, ensure_ascii=False)
        print(json_data)
        response = client.chat.completions.create(
            model="glm-4-0520",
            messages=[
                {"role": "system",
                 "content": "你需要根据传入的句柄和进程名，再结合用户自然语言中想操作的具体进程给出句柄号。"
                            "注意，你只用打印你觉得最匹配的句柄号(例如：133304，yyyy。只准返回句柄号)，如果你有发现有多个你觉得符合条件的结果，就返回-1"},
                {"role": "user",
                 "content": f"当前系统为windows11，系统分辨率为2560*1440，当前系统的句柄和标题如下{json_data}，你的任务是{user_input}"},
            ],
            stream=False,
        )
        full_response_content = response.choices[0].message.content
        print(full_response_content)
        return full_response_content

    def NLP_do_mission(self):
        mission=self.mission
        client = ZhipuAI(api_key=self.api_token)
        while True:
            response = client.chat.completions.create(
                model="glm-4-0520",
                messages=[
                    {"role": "system",
                     "content": self.prompt},
                    {"role": "user",
                     "content": "当前系统为windows11，系统分辨率为2560*1440，当前需要执行的任务是‘清除桌面QQ的‘缓存数据’,请在输出第一条指令后保持阻断状态，等待OCR返回数据"},
                ],
                stream=False,
            )
            full_response_content = response.choices[0].message.content
            print(full_response_content)

            # 流式传输
            # for chunk in response:
            #    print(chunk.choices[0].delta)
            while True:
                # ocr_data = wait_for_ocr_data()  # 等待OCR模块返回数据的模拟函数
                ocr_data = 123465
                if ocr_data:
                    print(f"OCR模块返回的数据: {ocr_data}")
                    # next_response_content = next_response.choices[0].message.content
                    # print(f"GPT生成的下一条指令: {next_response_content}")

                # 问用户是否继续对话
                keep_talking = input("是否继续对话？(yes/no): ")
                if keep_talking.lower() != 'yes':
                    break
