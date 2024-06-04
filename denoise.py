import webui_duplicate

def denoise(denoise_inp_dir, denoise_opt_dir):

    result = webui_duplicate.open_denoise(
        denoise_inp_dir=denoise_inp_dir,
        denoise_opt_dir=denoise_opt_dir
    )

    print(str(result))

    result = webui_duplicate.close_denoise()
    print(result)

if __name__ == "__main__":
    denoise_inp_dir = 'E:\\BaiduNetdiskDownload\\GPT-SoVITS-beta0306fix2\\output\\slicer_opt'
    denoise_opt_dir = 'E:\\BaiduNetdiskDownload\\GPT-SoVITS-beta0306fix2\\output\\denoise_opt'
    denoise(denoise_inp_dir, denoise_opt_dir)