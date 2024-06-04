import webui_duplicate

if __name__ == "__main__":
    # Example of how to call the function with parameters
    result = webui_duplicate.open_asr(
        asr_inp_dir = 'E:\\BaiduNetdiskDownload\\GPT-SoVITS-beta0306fix2\\output\\slicer_opt',
        asr_opt_dir = 'output/asr_opt',
        asr_model = 'Faster Whisper (多语种)',
        asr_model_size = 'small',
        asr_lang = 'auto'
    )

    print(str(result))

    result = webui_duplicate.close_asr()
    print(result)