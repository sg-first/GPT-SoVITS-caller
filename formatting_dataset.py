# import os
# import sys
#
# # 设置工作目录为脚本所在目录
# script_dir = os.path.dirname(os.path.abspath(__file__))
# os.chdir(script_dir)
#
# # 确保脚本所在目录在 sys.path 中
# sys.path.append(script_dir)

import webui_duplicate


def oneclick_formatting(inp_text,inp_wav_dir,exp_name,gpu_numbers1a,gpu_numbers1Ba,gpu_numbers1c,bert_pretrained_dir,
                        ssl_pretrained_dir,pretrained_s2G_path):
    # inp_text = "E:\\BaiduNetdiskDownload\\GPT-SoVITS-beta0306fix2\\output\\asr_opt\\slicer_opt.list"  # 必须是这种文件路径，双反斜杠的
    # inp_wav_dir = "E:\\BaiduNetdiskDownload\\GPT-SoVITS-beta0306fix2\\output\\slicer_opt"
    # exp_name = ("test")
    # gpu_numbers1a = "0"  # 0	NVIDIA GeForce RTX 3050 Ti Laptop GPU
    # gpu_numbers1Ba = "0"
    # gpu_numbers1c = "0"
    # bert_pretrained_dir = "GPT_SoVITS/pretrained_models/chinese-roberta-wwm-ext-large"
    # ssl_pretrained_dir = "GPT_SoVITS/pretrained_models/chinese-hubert-base"
    # pretrained_s2G_path = "GPT_SoVITS/pretrained_models/s2G488k.pth"

    result = webui_duplicate.open1abc(
            inp_text,
            inp_wav_dir,
            exp_name,
            gpu_numbers1a,
            gpu_numbers1Ba,
            gpu_numbers1c,
            bert_pretrained_dir,
            ssl_pretrained_dir,
            pretrained_s2G_path
    )
    print(result)

    result = webui_duplicate.close1abc()
    print(result)



if __name__ == "__main__":
    oneclick_formatting("E:\\BaiduNetdiskDownload\\GPT-SoVITS-beta0306fix2\\output\\asr_opt\\slicer_opt.list",
                        "E:\\BaiduNetdiskDownload\\GPT-SoVITS-beta0306fix2\\output\\slicer_opt",
                        "test",
                        "0",
                        "0",
                        "0",
                        "GPT_SoVITS/pretrained_models/chinese-roberta-wwm-ext-large",
                        "GPT_SoVITS/pretrained_models/chinese-hubert-base",
                        "GPT_SoVITS/pretrained_models/s2G488k.pth")