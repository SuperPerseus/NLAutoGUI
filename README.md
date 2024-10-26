NLAutoGUI: 自然语言驱动的图形用户界面自动化

NLAutoGUI 是一个前沿项目，结合了自然语言处理（NLP）、光学字符识别（OCR）和计算机视觉（CV）技术，实现对图形用户界面（GUI）的自动化操作。用户只需通过自然语言命令即可控制计算机的GUI，无需编写编程或脚本。该工具旨在让复杂的自动化任务变得触手可及，提升工作效率，并简化人机交互。

智谱的大模型还远远处理不了过大的图形文本化数据，几乎用不了，需要编写更多的前端视觉处理和对图片的焦点机制，对输出结果做出更多的预处理，才能让大模型的注意力集中在完成用户交代的任务上面，不然几轮过后就陷入幻觉开始自言自语或者打印不符合返回参数的结果，以至于程序崩溃

可能得使用图片特化型的大模型和文字大模型协同工作，并且需要在模型根源上就做好微调，这一过程又需要海量的模板图片和执行流程来供大模型针对性学习

而且在历史数据堆积过多后，大模型就只会把我的提示词里面包含的范例参数机械地输出，不太能思考OCR返回参数和CV返回参数在时空上的二维关联关系，搞得我头疼，与其用商业常规语言大模型，不如自己重新制作一个能更好理解文字与图片二维关系的新模型

有兴趣继续开发的，可以看看这个我在arxiv找到的这个论文[Xu, J., Li, P., Wang, H., Chen, Z., & Liang, X. (2024). Cross-modal Consistency Learning with Adaptive Loss Weighting for Visual-Language Models. arXiv preprint arXiv:2402.07945. ](https://arxiv.org/abs/2402.07945)

这是该项目的github地址 https://github.com/niuzaisheng/ScreenAgent?tab=readme-ov-file

还得是吉林大学的研究团队专业，比我瞎琢磨的项目更系统更深入。要是早点浏览到这个论文，就不做这个项目了


English Version:

NLAutoGUI: Natural Language Powered GUI Automation

NLAutoGUI is a cutting-edge project that leverages natural language processing (NLP), optical character recognition (OCR), and computer vision (CV) to automate graphical user interface (GUI) operations. By simply using natural language commands, users can control their computer's GUI without the need for programming or script writing. This tool aims to make complex automation accessible to all users, enhancing efficiency and simplifying human-computer interaction.


