import pandas as pd
import matplotlib.pyplot as plt
import os
import glob
from matplotlib import rcParams

# Set Times New Roman as the default font
def plot_multiple(title,file_names,dataset):
    plt.figure(figsize=(10, 6))

    colors = ['b', 'g', 'orange']  # Define colors for each plot
    for idx, file_name in enumerate(file_names):
        # Read the CSV file
        data = pd.read_csv(file_name)

        # Extract the "Round" and "Accuracy" columns
        rounds = data["Round"]
        accuracy = data["Accuracy"]
        filtered_rounds = [r for r in rounds if r <= 5]
        filtered_accuracy = [accuracy[i] for i, r in enumerate(rounds) if r <= 5]

        # Find the maximum accuracy and its corresponding round
        max_accuracy = accuracy.max()
        max_accuracy_round = rounds[accuracy.idxmax()]

        # Plot the chart
        label = my_map[file_name.split("/")[-1].split(".")[0]]
        plt.plot(filtered_rounds, filtered_accuracy,linewidth=4, marker='o', linestyle='-', color=colors[idx % len(colors)], label=f'{label}')
        plt.gca().spines['bottom'].set_linewidth(4)  # Make x-axis thicker
        plt.gca().spines['left'].set_linewidth(4)  # Make y-axis thicker
        plt.gca().spines['right'].set_linewidth(0)  # Make y-axis thicker
        plt.gca().spines['top'].set_linewidth(0)  # Make y-axis thicker
        # Mark the maximum accuracy
        # plt.scatter(max_accuracy_round, max_accuracy, color=colors[idx % len(colors)], s=100, zorder=5)
        # plt.annotate(
        #     f'({max_accuracy_round}, {max_accuracy:.2f})',
        #     (max_accuracy_round, max_accuracy),
        #     textcoords="offset points",
        #     xytext=(0, 10),
        #     ha='center',
        #     fontsize=10,
        #     color=colors[idx % len(colors)]
        # )

    # Add title, labels, and legend
    rcParams['font.family'] = 'Times New Roman'
    plt.ylim(0.5, 1)
    plt.title(title, fontdict={'family': 'Times New Roman', 'size': 34},weight='bold')
    plt.xlabel("Round", fontdict={'family': 'Times New Roman', 'size': 26},weight='bold')
    plt.ylabel("Accuracy", fontdict={'family': 'Times New Roman', 'size': 26},weight='bold')
    # plt.grid(True, linestyle='--', alpha=0.7)
    plt.xticks(fontsize=26,weight='bold')    # fontsize of the tick labels
    plt.yticks(fontsize=26,weight='bold')    # fontsize of the tick labels
    plt.legend(fontsize=26,loc='lower right')
    plt.xticks(range(1, 6))  # Set x-axis ticks to 1, 2, 3, 4, 5
    plt.tight_layout()

    # Save the plot to a file
    output_file = "./figs/"+dataset+"/"+title+".png"  # Change to your desired file name and format
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f"Plot saved to {output_file}")


title_partition  ={"Exponential":"Exp","Linear":"Linear","Square":"Square","Iid":"Iid"}
datasets = ["qqp","sst2","qnli"]
for dataset in datasets:
    for title in title_partition:
        partition = title_partition[title]
        my_map = {}
        my_map[dataset+"_"+partition+"_10_Our"] = "FSRDP"
        my_map[dataset+"_"+partition+"_10_RDP"] = "RDP"
        my_map[dataset+"_"+partition+"_no_noise"] = "Non_Private"

        # folder_path = "./test_result"  # Replace with the path to your folder
        # csv_files = glob.glob(os.path.join(folder_path, "*.csv"))
        csv_files = ['./pre_calculated_performance_10/'+dataset+"_"+partition+"_10_Our.csv",
                    './pre_calculated_performance_10/'+dataset+"_"+partition+"_10_RDP.csv",
                    './performance/no_noise/'+dataset+"_"+partition+"_no_noise.csv"]
        plot_multiple(title,csv_files,dataset)