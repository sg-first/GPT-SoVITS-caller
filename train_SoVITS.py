import json
from subprocess import Popen
import os
import sys
from config import python_exec, exp_root, is_half
SoVITS_weight_root="SoVITS_weights"
now_dir = os.getcwd()
sys.path.insert(0, now_dir)
tmp = os.path.join(now_dir, "TEMP")

p_train_SoVITS = None

def open1Ba(batch_size,total_epoch,exp_name,text_low_lr_rate,if_save_latest,if_save_every_weights,save_every_epoch,gpu_numbers1Ba,pretrained_s2G,pretrained_s2D):
    global p_train_SoVITS
    if(p_train_SoVITS==None):
        with open("GPT_SoVITS/configs/s2.json")as f:
            data=f.read()
            data=json.loads(data)
        s2_dir="%s/%s"%(exp_root,exp_name)
        os.makedirs("%s/logs_s2"%(s2_dir),exist_ok=True)
        if(is_half==False):
            data["train"]["fp16_run"]=False
            batch_size=max(1,batch_size//2)
        data["train"]["batch_size"]=batch_size
        data["train"]["epochs"]=total_epoch
        data["train"]["text_low_lr_rate"]=text_low_lr_rate
        data["train"]["pretrained_s2G"]=pretrained_s2G
        data["train"]["pretrained_s2D"]=pretrained_s2D
        data["train"]["if_save_latest"]=if_save_latest
        data["train"]["if_save_every_weights"]=if_save_every_weights
        data["train"]["save_every_epoch"]=save_every_epoch
        data["train"]["gpu_numbers"]=gpu_numbers1Ba
        data["data"]["exp_dir"]=data["s2_ckpt_dir"]=s2_dir
        data["save_weight_dir"]=SoVITS_weight_root
        data["name"]=exp_name
        tmp_config_path="%s/tmp_s2.json"%tmp
        with open(tmp_config_path,"w")as f:f.write(json.dumps(data))

        cmd = '"%s" GPT_SoVITS/s2_train.py --config "%s"'%(python_exec,tmp_config_path)
        print(cmd)
        p_train_SoVITS = Popen(cmd, shell=True)
        p_train_SoVITS.wait()
        p_train_SoVITS=None
        return "SoVITS训练完成",{"__type__":"update","visible":True},{"__type__":"update","visible":False}

if __name__ == "__main__":
    # Example of how to call the function with parameters
    result = open1Ba(
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
