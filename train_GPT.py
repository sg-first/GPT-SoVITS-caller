import webui_duplicate

if __name__ == "__main__":
    # Example of how to call the function with parameters
    result = webui_duplicate.open1Bb(
        batch_size=2,
        total_epoch=15,
        exp_name='test',
        if_dpo=False,
        if_save_latest=True,
        if_save_every_weights=True,
        save_every_epoch=15,
        gpu_numbers='0',
        pretrained_s1="GPT_SoVITS/pretrained_models/s1bert25hz-2kh-longer-epoch=68e-step=50232.ckpt"
    )

    print(str(result))
