import webui_duplicate

if __name__ == "__main__":
    # Example of how to call the function with parameters
    result = webui_duplicate.open_denoise(
        denoise_inp_dir = 'E:\\BaiduNetdiskDownload\\GPT-SoVITS-beta0306fix2\\output\\slicer_opt',
        denoise_opt_dir = 'E:\\BaiduNetdiskDownload\\GPT-SoVITS-beta0306fix2\\output\\denoise_opt'
    )

    print(str(result))
