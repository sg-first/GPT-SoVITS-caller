import webui_duplicate

def train_gpt(exp_name, gpu_numbers, GPT_weight_root):
    result = webui_duplicate.open1Bb(
        batch_size=2,
        total_epoch=15,
        exp_name=exp_name,
        if_dpo=False,
        if_save_latest=True,
        if_save_every_weights=True,
        save_every_epoch=15,
        gpu_numbers=gpu_numbers,
        pretrained_s1="GPT_SoVITS/pretrained_models/s1bert25hz-2kh-longer-epoch=68e-step=50232.ckpt",
        GPT_weight_root = GPT_weight_root
    )
    print(str(result))

    result = webui_duplicate.close1Bb()
    print(result)


if __name__ == "__main__":
    # Example of how to call the function with parameters
    exp_name = 'batman'
    gpu_numbers = '0'
    GPT_weight_root = 'C:\\Users\\Bruce Wayne\\Desktop\\storage\\batman'
    train_gpt(exp_name, gpu_numbers, GPT_weight_root)
