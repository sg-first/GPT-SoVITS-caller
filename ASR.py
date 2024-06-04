import webui_duplicate

def asr(asr_inp_dir,asr_opt_dir ):
    result = webui_duplicate.open_asr(
        asr_inp_dir=asr_inp_dir,
        asr_opt_dir=asr_opt_dir,
        asr_model='Faster Whisper (多语种)',
        asr_model_size='small',
        asr_lang='auto'
    )

    print(str(result))

    result = webui_duplicate.close_asr()
    print(result)

if __name__ == "__main__":
    asr_inp_dir = 'E:\\BaiduNetdiskDownload\\GPT-SoVITS-beta0306fix2\\output\\slicer_opt'
    asr_opt_dir = 'output/asr_opt'
    asr(asr_inp_dir, asr_opt_dir)