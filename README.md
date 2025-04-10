

# Differential Privacy-Driven Federated Learning for Large Language Models in HMI Systems

The GLUE dataset learning process is using Transformers library and is adopted from [run_glue](https://github.com/huggingface/transformers/blob/main/examples/pytorch/text-classification/run_glue.py). <br>
The Federated learning enviroment is using [Flower](https://flowerai.net/docs/framework/index.html). <br>


## NOTE
Because of an existing problem with flwr[simulation]==1.12.0 when using local DP, following steps should be done:

- copy [localdp_fixed_mod.py](fixed/localdp_fixed_mod.py) in flwr/client/mod

- use [differential_privacy.py](fixed/differential_privacy.py) instead of /fixed/differential_privacy.py

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
To calculate required noise for target Epsilon, we used our previous work [FSRDP Accountant](https://github.com/star-ailab/FSRDP).
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
- Model_name is the based model. <br>
- task_name is the dataset which can be (SST2, QNLI, or QQP).<br>
- Parition_policy can be (Iid, Linear, Square, or Exp).
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
