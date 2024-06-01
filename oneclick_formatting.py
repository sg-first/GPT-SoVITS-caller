import webui_duplicate


def main():
    inp_text = "E:\\BaiduNetdiskDownload\\GPT-SoVITS-beta0306fix2\\output\\asr_opt\\test.list"  # 必须是这种文件路径，双反斜杠的
    inp_wav_dir = "E:\\BaiduNetdiskDownload\\GPT-SoVITS-beta0306fix2\\output\\slicer_opt\\test"
    exp_name = ("test")
    gpu_numbers1a = "0"  # 0	NVIDIA GeForce RTX 3050 Ti Laptop GPU
    gpu_numbers1Ba = "0"
    gpu_numbers1c = "0"
    bert_pretrained_dir = "GPT_SoVITS/pretrained_models/chinese-roberta-wwm-ext-large"
    ssl_pretrained_dir = "GPT_SoVITS/pretrained_models/chinese-hubert-base"
    pretrained_s2G_path = "GPT_SoVITS/pretrained_models/s2G488k.pth"

    for status in webui_duplicate.open1abc(
            inp_text,
            inp_wav_dir,
            exp_name,
            gpu_numbers1a,
            gpu_numbers1Ba,
            gpu_numbers1c,
            bert_pretrained_dir,
            ssl_pretrained_dir,
            pretrained_s2G_path
    ):
        print(status[0])  # Print the progress message
        # Optionally, handle the dictionaries if needed
        # update_visibility(status[1], status[2])


if __name__ == "__main__":
    main()
