import pandas as pd
import numpy as np

# Bước 1: Tải dữ liệu edge list
df = pd.read_csv("D:\Research 2024-1\FIsInGene_PathwayPMID041909.txt", sep="\t")

# Bước 2: Xây dựng ma trận liên kết
genes = sorted(set(df['Start']).union(set(df['End'])))
gene_to_index = {gene: i for i, gene in enumerate(genes)}
n = len(genes)

A_real = np.zeros((n, n), dtype=int)
for _, row in df.iterrows():
    i = gene_to_index[row['Start']]
    j = gene_to_index[row['End']]
    A_real[i, j] = 1
    A_real[j, i] = 1

# Bước 3: Hàm tạo nhiễu
def add_noise_general(A, noise_level=0.5, seed=42):
    np.random.seed(seed)
    n = A.shape[0]
    A_noisy = A.copy()
    current_edges = np.transpose(np.nonzero(np.triu(A_noisy)))
    num_edges = len(current_edges)
    num_add_edges = int(noise_level * num_edges)
    candidate_pairs = [(i, j) for i in range(n) for j in range(i+1, n) if A_noisy[i, j] == 0]

    if len(candidate_pairs) < num_add_edges:
        num_add_edges = len(candidate_pairs)

    selected_pairs = np.random.choice(len(candidate_pairs), size=num_add_edges, replace=False)
    for idx in selected_pairs:
        i, j = candidate_pairs[idx]
        A_noisy[i, j] = 1
        A_noisy[j, i] = 1

    return A_noisy

# Bước 4: Tạo nhiễu và lưu file
A_noisy = add_noise_general(A_real, noise_level=0.5)
adj_df_noisy = pd.DataFrame(A_noisy, index=genes, columns=genes)
adj_df_noisy.to_csv("GRN_adjacency_matrix_noisy_50percent.csv")
