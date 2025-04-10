# NOTE
To use this code upon flower framework you should 
1- add /fixed/local_dp_fixed_mod.py file into flwr/client/mod/localdp_fixed_mod
2- update flwr/common/differential_privacy.py to /fixed/differential_privacy.py

# Differential Privacy-Driven Federated Learning for Large Language Models in HMI Systems

The GLUE dataset learning process is using Transformers library and is adopted from https://github.com/huggingface/transformers/blob/main/examples/pytorch/text-classification/run_glue.py <br>
The Federated learning enviroment is using Flower AI framework. <br>
https://flowerai.net/docs/framework/index.html

## Install dependencies
```
pip install requirement.txt
```
## Experiments
To run the experiments in the paper run:
```
./script.sh
```
## Noise Calculation
We used the project at https://github.com/star-ailab/FSRDP to find the proper noise std deviation for different accountant.
To find the proper std deviation of noise in different accountants:
```
Python ./noise_calculation/get_noise.py
```
target_epsilons and dataset_size_list is configurable in get_noise.py file.

## Single Experiment
```
python federated.py \
  --model_name_or_path google-bert/bert-base-cased \
  --max_seq_length 128 \
  --task_name SST2 \
  --partition_policy Linear \
  --per_device_train_batch_size 550 \
  --learning_rate 2e-5\
  --output_dir /tmp/SST2/
```
Model_name is the based model. <br>
task_name is the dataset which can be (SST2, QNLI, or QQP).<br>
Parition_policy can be (Iid, Linear, Square, or Exp)
## citation
Please cite our papar if you find our repo helpful.

```
@misc{ahmadi2025interactiveframeworkimplementingprivacypreserving,
      title={An Interactive Framework for Implementing Privacy-Preserving Federated Learning: Experiments on Large Language Models}, 
      author={Kasra Ahmadi and Rouzbeh Behnia and Reza Ebrahimi and Mehran Mozaffari Kermani and Jeremiah Birrell and Jason Pacheco and Attila A Yavuz},
      year={2025},
      eprint={2502.08008},
      archivePrefix={arXiv},
      primaryClass={cs.LG},
      url={https://arxiv.org/abs/2502.08008}, 
}
```
