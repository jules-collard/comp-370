import pandas as pd
import seaborn as sns
import os

concordia_data = pd.read_csv(os.path.join(os.path.dirname(__file__), "final_labeled_dataset_concordia.tsv"), delimiter="\t")
mcgill_data = pd.read_csv(os.path.join(os.path.dirname(__file__), "final_labeled_dataset_mcgill.tsv"), delimiter="\t")
data = pd.concat([concordia_data, mcgill_data])
counts = data.value_counts("label").reset_index()

sns.barplot(data = counts, y="label", x="count").get_figure().savefig(os.path.join(os.path.dirname(__file__), "results.png"),
                                                                      bbox_inches='tight')
