import webui_duplicate

if __name__ == "__main__":
    # Example of how to call the function with parameters
    result = webui_duplicate.open_slice(
        inp = 'E:\\BaiduNetdiskDownload\\Easy-Wav2Lip优化版-眠-0229\\Easy-Wav2Lip-眠-0229\\in\\batman.wav',
        opt_root = 'output/slicer_opt',
        threshold = '-34',
        min_length = '4000',
        min_interval = '300',
        hop_size = '10',
        max_sil_kept = '500',
        _max = 0.9,
        alpha = 0.25,
        n_parts = 4
    )

    print(str(result))