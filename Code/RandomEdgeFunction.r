A1 <- as.matrix(read.csv("", header = TRUE, row.names = 1))
n <- nrow(A1)
missing_edges <- which(A1 == 1, arr.ind = TRUE)
set.seed(42)
num_edges_to_add <- floor(0.8 * length(missing_edges) / 2)
selected_edges <- sample(1:nrow(missing_edges), num_edges_to_add)
A2 <- A1
for (i in selected_edges) {
  row <- missing_edges[i, 1]
  col <- missing_edges[i, 2]
  A2[row, col] <- 1
  A2[col, row] <- 1
}
write.csv(A2, "", row.names = TRUE)
