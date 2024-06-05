import webui_duplicate

def train_so_vits(exp_name, gpu_numbers1Ba, SoVITS_weight_root):
    # Example of how to call the function with parameters
    result = webui_duplicate.open1Ba(
        batch_size = 2,
        total_epoch = 8,
        exp_name = exp_name,
        text_low_lr_rate = 0.4,
        if_save_latest = True,
        if_save_every_weights = True,
        save_every_epoch = 8,
        gpu_numbers1Ba = gpu_numbers1Ba,
        pretrained_s2G = "GPT_SoVITS/pretrained_models/s2G488k.pth",
        pretrained_s2D = "GPT_SoVITS/pretrained_models/s2D488k.pth",
        SoVITS_weight_root = SoVITS_weight_root
    )
    print(str(result))

    result = webui_duplicate.close1Ba()
    print(result)

if __name__ == "__main__":

    exp_name = 'batman'
    gpu_numbers1Ba = '0'
    SoVITS_weight_root = 'C:\\Users\\Bruce Wayne\\Desktop\\storage\\batman'
    train_so_vits(exp_name, gpu_numbers1Ba, SoVITS_weight_root)
