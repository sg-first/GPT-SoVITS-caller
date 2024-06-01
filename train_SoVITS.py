import webui_duplicate

if __name__ == "__main__":
    # Example of how to call the function with parameters
    result = webui_duplicate.open1Ba(
        batch_size=2,
        total_epoch=8,
        exp_name='test',
        text_low_lr_rate=0.4,
        if_save_latest=True,
        if_save_every_weights=True,
        save_every_epoch=8,
        gpu_numbers1Ba='0',
        pretrained_s2G="GPT_SoVITS/pretrained_models/s2G488k.pth",
        pretrained_s2D="GPT_SoVITS/pretrained_models/s2D488k.pth"
    )

    print(str(result))
