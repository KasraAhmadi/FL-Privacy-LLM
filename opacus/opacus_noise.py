from opacus.accountants.utils import get_noise_multiplier
n_train = 20948
batch_size = 550
sample_rate = batch_size/n_train

sigma = get_noise_multiplier(target_epsilon= 6,
    target_delta = 1/n_train,
    sample_rate = batch_size/n_train,
    epochs= 20,
    accountant = "rdp",
    epsilon_tolerance= 0.01)

print(sigma)