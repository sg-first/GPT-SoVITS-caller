import inference_webui_duplicate
import wave



def save_audio_to_wav(sampling_rate, audio_data, output_path):
    # 创建一个 WAV 文件
    with wave.open(output_path, 'wb') as wf:
        # 设置 WAV 文件的参数
        wf.setnchannels(1)  # 单声道
        wf.setsampwidth(2)  # 16位音频，每样本2字节
        wf.setframerate(sampling_rate)  # 采样率

        # 将音频数据写入 WAV 文件
        wf.writeframes(audio_data.tobytes())


if __name__ == "__main__":
    # 指定模型位置
    inference_webui_duplicate.change_gpt_weights('GPT_weights/test-e15.ckpt')
    inference_webui_duplicate.change_sovits_weights('SoVITS_weights/test_e8_s368.pth')


    # Example of how to call the function with parameters
    generator = inference_webui_duplicate.get_tts_wav(
        how_to_cut='Cut per 50 characters',
        prompt_language='多语种混合',
        prompt_text='',
        ref_free=True,
        ref_wav_path='C:\\Users\\BRUCEW~1\\AppData\\Local\\Temp\\batmany9tjec4p.wav_0000171840_0000328960.wav',
        temperature=1,
        text="hello, i'. mark zuckerberg and i'm here at your orders. 另外，我的中文水平目前还不是很好，请多担待。",
        text_language='多语种混合',
        top_k=50,
        top_p=1
    )

    sampling_rate, audio_data = next(generator)

    # 保存音频数据到本地指定路径
    output_path = 'C:\\Users\\Bruce Wayne\\Desktop\\test\\output_audio.wav'
    save_audio_to_wav(sampling_rate, audio_data, output_path)

    print(f"音频已保存到 {output_path}")
